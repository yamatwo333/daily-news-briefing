"""Verify only the NEWS Pages files against this workflow's exact input.

Run by GitHub Actions after deploy; not by the NEWS cloud VM. Source article
URLs are never fetched. No credentials, API keys, redirects, or remote code.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import time
import urllib.error
import urllib.parse
import urllib.request

PUBLIC_BASE = "https://yamatwo333.github.io/daily-news-briefing/"
LIMITS = {"manifest.json": 100_000, "script.txt": 120_000,
          "sources.json": 120_000, "index.html": 1_000_000, "audio.mp3": 25_000_000}


class PublicationPending(RuntimeError):
    """The expected revision is not yet served consistently."""


class AccessDenied(RuntimeError):
    """Never retry an explicit access denial or redirect."""


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise AccessDenied("Unexpected redirect from the fixed NEWS publication URL")


def fetch_file(name, edition_id, deadline):
    if name not in LIMITS:
        raise ValueError("Only the fixed NEWS output files may be verified")
    remaining = deadline - time.monotonic()
    if remaining <= 0:
        raise PublicationPending("Publication verification deadline exceeded")
    query = urllib.parse.urlencode({"edition": edition_id, "check": time.time_ns()})
    req = urllib.request.Request(PUBLIC_BASE + name + "?" + query,
                                 headers={"Cache-Control": "no-cache"})
    try:
        with urllib.request.build_opener(NoRedirect).open(req, timeout=min(15, remaining)) as response:
            body = response.read(LIMITS[name] + 1)
    except urllib.error.HTTPError as exc:
        if exc.code in {401, 403}:
            raise AccessDenied(f"HTTP {exc.code}: verification access denied") from exc
        if exc.code in {404, 408, 429, 500, 502, 503, 504}:
            raise PublicationPending(f"HTTP {exc.code}: publication not ready") from exc
        raise
    except (urllib.error.URLError, TimeoutError) as exc:
        raise PublicationPending("Publication transport not ready") from exc
    if len(body) > LIMITS[name]:
        raise ValueError(f"Published {name} exceeds the size limit")
    return body


def check_once(data, fetch):
    manifest = json.loads(fetch("manifest.json"))
    for field in ["id", "cutoff_at", "written_at"]:
        if manifest.get(field) != data[field]:
            raise PublicationPending(f"Published {field} differs from this input")
    manuscript = data["manuscript"].encode("utf-8")
    script = fetch("script.txt")
    if script != manuscript or hashlib.sha256(script).hexdigest() != manifest.get("manuscript_sha256"):
        raise PublicationPending("Published manuscript or its hash differs")
    if json.loads(fetch("sources.json")) != data["sources"]:
        raise PublicationPending("Published sources differ")
    if data["id"] not in fetch("index.html").decode("utf-8"):
        raise PublicationPending("Published HTML belongs to another edition")
    audio = fetch("audio.mp3")
    if (len(audio) != manifest.get("mp3_bytes") or
            hashlib.sha256(audio).hexdigest() != manifest.get("audio_sha256")):
        raise PublicationPending("Published audio or its hash differs")
    duration = manifest.get("duration_seconds")
    if not isinstance(duration, (int, float)) or not 1 <= duration <= 1800:
        raise ValueError("Published audio duration is invalid")
    return {"result": "verified", "id": data["id"],
            "verified_at": datetime.now(timezone.utc).isoformat(),
            "manuscript_sha256": manifest["manuscript_sha256"],
            "audio_sha256": manifest["audio_sha256"], "audio_bytes": len(audio),
            "duration_seconds": duration, "public_url": PUBLIC_BASE}


def verify(data, *, budget_seconds=180, interval_seconds=10, fetch=None,
           clock=time.monotonic, sleep=time.sleep):
    if not 0 < budget_seconds <= 180 or not 0 < interval_seconds <= 10:
        raise ValueError("Verification budget must remain bounded")
    deadline = clock() + budget_seconds
    fetch = fetch or (lambda name: fetch_file(name, data["id"], deadline))
    while True:
        try:
            return check_once(data, fetch)
        except (PublicationPending, json.JSONDecodeError, UnicodeDecodeError) as exc:
            remaining = deadline - clock()
            if remaining <= 0:
                raise PublicationPending("Verification failed before deadline: " + str(exc)) from exc
            sleep(min(interval_seconds, remaining))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, default=Path("publication-check.json"))
    args = parser.parse_args()
    data = json.loads(args.input.read_text(encoding="utf-8"))
    try:
        result = verify(data)
    except Exception as exc:
        result = {"result": "failed", "id": data.get("id"),
                  "reason": str(exc), "public_url": PUBLIC_BASE}
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        raise
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
