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
RESEARCH_BUDGET_SECONDS = 600


def coverage_decision(candidates, elapsed_seconds=0, discovery_complete=False,
                      coverage_gaps=None):
    """Quantity/coverage gaps never discard independently verified news."""
    if (not isinstance(candidates, list) or
            not isinstance(elapsed_seconds, (int, float)) or elapsed_seconds < 0):
        raise ValueError("Actual candidates and nonnegative research time are required")
    coverage_gaps = coverage_gaps or []
    if not isinstance(coverage_gaps, list) or any(not isinstance(x, str) for x in coverage_gaps):
        raise ValueError("coverage_gaps must list actual unconfirmed topics")
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
                  coverage_gaps=coverage_gaps, max_research_seconds=RESEARCH_BUDGET_SECONDS)
    if (not discovery_complete and elapsed_seconds < RESEARCH_BUDGET_SECONDS
            and (len(verified) < 12 or coverage_gaps)):
        return dict(result, action="continue_research", write_input=False)
    if not verified:
        return dict(result, action="stop_no_verified_news", write_input=False)
    compact = len(verified) < 12 or bool(coverage_gaps)
    return dict(result, action="prepare_compact" if compact else "prepare_normal",
                edition_kind="compact" if compact else "normal",
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
                                   data.get("discovery_complete", False), data.get("coverage_gaps"))
    else:
        result = delivery_decision(data["now"], data.get("current_cutoff"), data.get("pipeline"))
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
