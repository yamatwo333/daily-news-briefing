import copy
import hashlib
import json
import unittest
from cloud_test.daily_guard import environment_decision, classify_fetch_error, delivery_decision
from cloud_test.verify_publication import check_once, verify, PublicationPending, AccessDenied


class GuardTests(unittest.TestCase):
    def test_unknown_unused_shell_network_does_not_stop_hosted_tools(self):
        result = environment_decision(dict(provider="cloud", observed_phase="running",
            connectivity="connected", observations_current=True,
            network_policy=dict(mode="restricted", state="unknown")))
        self.assertEqual(result["action"], "continue_hosted_tools_and_local_only")
        self.assertFalse(result["shell_external_network_allowed"])
        self.assertFalse(result["http_enforcement_confirmed"])

    def test_local_runtime_must_be_current_and_ready_with_bounded_wait(self):
        observation = dict(provider="cloud", observed_phase="starting", observations_current=False)
        self.assertEqual(environment_decision(observation, 0)["action"], "wait_local_runtime")
        self.assertEqual(environment_decision(observation, 180)["action"], "stop")

    def test_unrestricted_configuration_is_not_silently_accepted(self):
        observation = dict(provider="cloud", observed_phase="running", connectivity="connected",
                           observations_current=True, network_policy=dict(mode="unrestricted"))
        self.assertEqual(environment_decision(observation)["action"], "stop")

    def test_article_url_failure_excludes_only_that_article(self):
        result = classify_fetch_error({"message": "Failed to fetch restricted URL"})
        self.assertEqual(result["action"], "exclude_article")
        self.assertFalse(result["retry_url"])
        self.assertFalse(result["alternate_route"])

    def test_explicit_safety_denial_wins_over_article_failure_text(self):
        for error in [dict(message="This tool call was blocked by OpenAI's safety checks."),
                      dict(message="Failed to fetch restricted URL", code="POLICY_DENIED")]:
            self.assertEqual(classify_fetch_error(error)["action"], "stop_operation")

    def test_unknown_tool_error_is_not_assumed_safe(self):
        self.assertEqual(classify_fetch_error(dict(message="unknown error"))["action"], "stop_operation")

    def test_existing_input_is_not_success_without_pipeline_verification(self):
        now, cutoff = "2026-10-19T07:01:00+09:00", "2026-10-19T06:35:00+09:00"
        for pipeline, expected in [({}, "inspect_existing_pipeline"),
            ({"status": "in_progress"}, "monitor_existing_pipeline"),
            ({"status": "completed", "conclusion": "failure"}, "report_pipeline_failure"),
            ({"status": "completed", "conclusion": "success"}, "inspect_existing_pipeline"),
            ({"status": "completed", "conclusion": "success", "verify_publication": "success"}, "already_verified")]:
            result = delivery_decision(now, cutoff, pipeline)
            self.assertEqual(result["action"], expected)
            self.assertFalse(result["write_input"])

    def test_jst_day_and_early_start_are_not_confused_with_utc(self):
        self.assertEqual(delivery_decision("2026-10-18T21:27:00Z")["action"], "wait_until_schedule")
        self.assertEqual(delivery_decision("2026-10-18T20:00:00Z")["action"], "stop")
        self.assertEqual(delivery_decision("2026-10-18T21:35:00Z", "2026-10-18T19:00:00+09:00")["action"], "prepare_new_edition")


class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.data = dict(id="test-20261019T010613Z", cutoff_at="2026-10-19T09:55:46+09:00",
                         written_at="2026-10-19T10:06:13+09:00", manuscript="確認した原稿です。\n", sources=[])
        self.audio = b"one exact audio file"
        self.manifest = {k:self.data[k] for k in ["id", "cutoff_at", "written_at"]}
        self.manifest.update(manuscript_sha256=hashlib.sha256(self.data["manuscript"].encode()).hexdigest(),
            audio_sha256=hashlib.sha256(self.audio).hexdigest(), mp3_bytes=len(self.audio), duration_seconds=12)
        self.files = {"manifest.json": json.dumps(self.manifest).encode(), "script.txt": self.data["manuscript"].encode(),
            "sources.json": b"[]", "index.html": self.data["id"].encode(), "audio.mp3": self.audio}

    def test_exact_publication_is_verified(self):
        self.assertEqual(check_once(self.data, self.files.__getitem__)["result"], "verified")

    def test_stale_manifest_changed_script_sources_and_audio_are_detected(self):
        for name, content in [("manifest.json", b'{"id":"old"}'), ("script.txt", b"old script"),
                              ("sources.json", b'[{}]'), ("index.html", b"old"), ("audio.mp3", b"old audio")]:
            files = copy.deepcopy(self.files); files[name] = content
            with self.subTest(name=name), self.assertRaises(PublicationPending):
                check_once(self.data, files.__getitem__)

    def test_cdn_propagation_is_bounded_and_rechecked(self):
        ticks=[0]; calls=[0]
        def fetch(name):
            calls[0] += 1
            if calls[0] == 1: raise PublicationPending("not propagated")
            return self.files[name]
        def sleep(seconds): ticks[0] += seconds
        result=verify(self.data, fetch=fetch, clock=lambda:ticks[0], sleep=sleep)
        self.assertEqual(result["result"], "verified")
        self.assertEqual(ticks[0], 10)
        def missing(name): raise PublicationPending("always stale")
        with self.assertRaises(PublicationPending):
            verify(self.data, budget_seconds=20, fetch=missing, clock=lambda:ticks[0], sleep=sleep)

    def test_access_denial_is_never_retried(self):
        calls=[]
        def denied(name): calls.append(name); raise AccessDenied("HTTP 403")
        with self.assertRaises(AccessDenied): verify(self.data, fetch=denied)
        self.assertEqual(calls,["manifest.json"])


if __name__ == "__main__":
    unittest.main()
