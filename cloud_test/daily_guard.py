"""Offline decisions for the hosted-tools-only NEWS daily run.

No networking, connectors, credentials, scheduler mutations, or file writes.
Pass actual tool error metadata, never article text, to classify_fetch_error.
"""
import argparse
from datetime import datetime, time, timedelta, timezone
import json
import re
import sys
from urllib.parse import urlsplit

JST = timezone(timedelta(hours=9))
RESEARCH_BUDGET_SECONDS = 1800
NORMAL_MIN_CHARACTERS = 3200
MAX_MANUSCRIPT_CHARACTERS = 4200


def coverage_decision(candidates, elapsed_seconds=0, discovery_complete=False,
                      coverage_gaps=None, manuscript_characters=None,
                      research_passes=0, publisher_origins=None,
                      examined_candidates=0, exhaustion_reason="",
                      expansion_attempted=False):
    """Prioritize normal volume; compact is allowed only after real exhaustion."""
    if (not isinstance(candidates, list) or
            not isinstance(elapsed_seconds, (int, float)) or elapsed_seconds < 0):
        raise ValueError("Actual candidates and nonnegative research time are required")
    coverage_gaps = coverage_gaps or []
    if not isinstance(coverage_gaps, list) or any(not isinstance(x, str) for x in coverage_gaps):
        raise ValueError("coverage_gaps must list actual unconfirmed topics")
    if (manuscript_characters is not None and
            (type(manuscript_characters) is not int or manuscript_characters < 0)):
        raise ValueError("manuscript_characters must be the actual saved length")
    if (type(research_passes) is not int or research_passes < 0 or
            type(examined_candidates) is not int or examined_candidates < 0 or
            not isinstance(exhaustion_reason, str) or type(expansion_attempted) is not bool):
        raise ValueError("Actual research and manuscript expansion evidence is required")
    publisher_origins = publisher_origins or []
    if (not isinstance(publisher_origins, list) or
            any(not isinstance(x, str) or not x.strip() for x in publisher_origins)):
        raise ValueError("publisher_origins must name independent editorial origins")
    verified, seen = [], set()
    for story in candidates:
        story_id = story.get("id")
        if not isinstance(story_id, str) or not story_id or story_id in seen:
            raise ValueError("Candidate IDs must be unique nonempty strings")
        seen.add(story_id)
        urls = story.get("source_urls")
        valid_sources = isinstance(urls, list) and bool(urls)
        if valid_sources:
            for url in urls:
                if not isinstance(url, str):
                    valid_sources = False
                    break
                parsed = urlsplit(url)
                if (parsed.scheme != "https" or not parsed.hostname or
                        parsed.username or parsed.password):
                    valid_sources = False
                    break
        if (all(story.get(k) is True for k in
                ("body_verified", "facts_verified", "in_window", "newsworthy"))
                and valid_sources):
            verified.append(story_id)
    result = dict(verified_ids=verified, verified_count=len(verified),
                  coverage_gaps=coverage_gaps, max_research_seconds=RESEARCH_BUDGET_SECONDS,
                  manuscript_characters=manuscript_characters,
                  listening_policy="eight-minute-v1",
                  target_manuscript_characters=[3600, 3900],
                  normal_min_characters=NORMAL_MIN_CHARACTERS,
                  max_audio_seconds=600,
                  research_passes=research_passes, examined_candidates=examined_candidates,
                  independent_publishers=len(set(x.strip() for x in publisher_origins)))
    # Length is a listening budget, not a reason to pad or accelerate speech.
    if manuscript_characters is not None and manuscript_characters > MAX_MANUSCRIPT_CHARACTERS:
        return dict(result, action="shorten_manuscript", write_input=False,
                    max_manuscript_characters=MAX_MANUSCRIPT_CHARACTERS,
                    instruction="11月5日の利用者変更：旧4300字下限は撤廃。3600〜3900字を目標に、出来事と必要な意味の説明を残して重複・細部を削り再検査してください。")
    if len(verified) >= 12:
        if manuscript_characters is None:
            return dict(result, action="draft_normal", write_input=False)
        if manuscript_characters >= NORMAL_MIN_CHARACTERS:
            return dict(result, action="prepare_normal", edition_kind="normal",
                        write_input="after_fact_structure_and_conflict_checks")
        if not expansion_attempted:
            return dict(result, action="expand_verified_manuscript", write_input=False)
    exhausted = (discovery_complete is True and elapsed_seconds >= 900 and
                 research_passes >= 3 and result["independent_publishers"] >= 5 and
                 examined_candidates >= 24 and bool(exhaustion_reason.strip()))
    deadline = elapsed_seconds >= RESEARCH_BUDGET_SECONDS
    if not exhausted and not deadline:
        return dict(result, action="continue_research", write_input=False)
    if not verified:
        return dict(result, action="stop_no_verified_news", write_input=False)
    reason = "documented_source_exhaustion" if exhausted else "research_deadline_reached"
    if manuscript_characters is None:
        return dict(result, action="draft_compact", fallback_reason=reason, write_input=False)
    return dict(result, action="prepare_compact", edition_kind="compact", fallback_reason=reason,
                write_input="after_fact_structure_and_conflict_checks")


def environment_decision(observation, elapsed_seconds=0):
    """The unused shell HTTP route is not a prerequisite for hosted tools."""
    if observation.get("provider") != "cloud":
        return {"action": "stop", "reason": "cloud_binding_required"}
    if (observation.get("observations_current") is not True or
            observation.get("observed_phase") != "running" or
            observation.get("connectivity") != "connected"):
        return {"action": "wait_local_runtime" if elapsed_seconds < 180 else "stop",
                "reason": "local_runtime_not_ready", "max_wait_seconds": 180}
    network = observation.get("network_policy") or {}
    if network.get("mode") != "restricted":
        return {"action": "stop", "reason": "unexpected_network_configuration"}
    return {"action": "continue_hosted_tools_and_local_only",
            "shell_external_network_allowed": False,
            "http_state_observed": network.get("state", "unknown"),
            "http_enforcement_confirmed": network.get("state") == "enforced",
            "hosted_permissions": "checked_by_each_hosted_tool"}


def classify_fetch_error(error):
    """Classify a fetch *error envelope*, not a successful article response."""
    text = error.get("message", "")
    if not isinstance(text, str):
        raise ValueError("error.message must contain the actual tool error text")
    code = str(error.get("code") or "").upper()
    denied = {"SAFETY_BLOCKED", "SAFETY_CHECK_BLOCKED", "POLICY_DENIED",
              "PERMISSION_DENIED", "ACCESS_DENIED", "UNAUTHORIZED_TOOL"}
    explicit = (code in denied or error.get("tool_authorization") == "denied" or
                "this tool call was blocked by openai's safety checks" in text.lower())
    if explicit:
        return {"action": "stop_operation", "retry_url": False,
                "alternate_route": False, "reason": "explicit_tool_or_policy_denial"}
    url_unavailable = re.search(
        r"(?:^|\n)URL https://\S+ is not accessible via this tool\.\s*$", text) is not None
    if (url_unavailable or "Failed to fetch restricted URL" in text or
            error.get("http_status") in {400, 401, 403, 404, 410, 429, 500, 502, 503, 504} or
            error.get("kind") in {"url_unavailable", "paywall", "body_missing", "robots"}):
        return {"action": "exclude_article", "retry_url": False,
                "alternate_route": False, "continue_unrelated_confirmed_articles": True}
    return {"action": "stop_operation", "retry_url": False,
            "alternate_route": False, "reason": "unclassified_tool_error"}


def delivery_decision(now, current_cutoff=None, pipeline=None):
    """An existing daily input is a checkpoint, never an automatic success."""
    now = datetime.fromisoformat(now.replace("Z", "+00:00"))
    if now.tzinfo is None:
        raise ValueError("now requires timezone")
    target = datetime.combine(now.astimezone(JST).date(), time(7, 0), JST)
    if now < target:
        seconds = (target - now).total_seconds()
        return {"action": "wait_until_schedule" if seconds <= 600 else "stop",
                "wait_seconds": seconds}
    if current_cutoff:
        cutoff = datetime.fromisoformat(current_cutoff.replace("Z", "+00:00"))
        if cutoff.tzinfo is None:
            raise ValueError("current_cutoff requires timezone")
        if cutoff > now + timedelta(minutes=5):
            return {"action": "stop", "reason": "future_input"}
        if cutoff >= target:
            pipeline = pipeline or {}
            if pipeline.get("status") in {"queued", "waiting", "in_progress", "pending"}:
                return {"action": "monitor_existing_pipeline", "write_input": False}
            if (pipeline.get("conclusion") == "success" and
                    pipeline.get("verify_publication") == "success"):
                return {"action": "already_verified", "write_input": False}
            if pipeline.get("status") == "completed" and pipeline.get("conclusion") != "success":
                return {"action": "report_pipeline_failure", "write_input": False}
            return {"action": "inspect_existing_pipeline", "write_input": False}
    return {"action": "prepare_new_edition", "write_input": "after_quality_and_conflict_checks"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("decision", choices=["environment", "fetch-error", "delivery", "coverage"])
    args = parser.parse_args()
    data = json.load(sys.stdin)
    if args.decision == "environment":
        result = environment_decision(data["observation"], data.get("elapsed_seconds", 0))
    elif args.decision == "fetch-error":
        result = classify_fetch_error(data)
    elif args.decision == "coverage":
        result = coverage_decision(data["candidates"], data.get("elapsed_seconds", 0),
                                   data.get("discovery_complete", False), data.get("coverage_gaps"),
                                   **{k: data[k] for k in ("manuscript_characters", "research_passes",
                                       "publisher_origins", "examined_candidates", "exhaustion_reason",
                                       "expansion_attempted") if k in data})
    else:
        result = delivery_decision(data["now"], data.get("current_cutoff"), data.get("pipeline"))
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
