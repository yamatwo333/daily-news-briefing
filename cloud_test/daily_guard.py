"""Offline decisions for the hosted-tools-only NEWS daily run.

No networking, connectors, credentials, scheduler mutations, or file writes.
Pass actual tool error metadata, never article text, to classify_fetch_error.
"""
import argparse
from datetime import datetime, time, timedelta, timezone
import json
import sys

JST = timezone(timedelta(hours=9))


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
    if ("Failed to fetch restricted URL" in text or
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
    target = datetime.combine(now.astimezone(JST).date(), time(6, 30), JST)
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
    parser.add_argument("decision", choices=["environment", "fetch-error", "delivery"])
    args = parser.parse_args()
    data = json.load(sys.stdin)
    if args.decision == "environment":
        result = environment_decision(data["observation"], data.get("elapsed_seconds", 0))
    elif args.decision == "fetch-error":
        result = classify_fetch_error(data)
    else:
        result = delivery_decision(data["now"], data.get("current_cutoff"), data.get("pipeline"))
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
