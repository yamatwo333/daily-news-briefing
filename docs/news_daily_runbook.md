# NEWS daily delivery contract — 2026-10-19

This is the current daily procedure, not a request to restart past tests. The
existing schedule starts daily at 07:00 Asia/Tokyo; completion follows processing. GPT does
the research and Japanese writing using the existing subscription. No paid API,
other model, new schedule, Google Docs sync, credential access, or permission
expansion. Public destination and repository remain unchanged.

## 1. Read current code, not the historical local checkout

Use the formal GitHub connector to read the `news-cloud-test` branch HEAD. Pin
that SHA for all reads of this runbook, `cloud_test/daily_guard.py`,
`cloud_test/build.py`, and `docs/daily_briefing_principles.md`. Save those exact
UTF-8 files and their hashes under a new local per-run directory. Do not assume
the cloud VM's branch `work` or old local files contain the delivery code. Do not
run git fetch/pull or fetch source articles from commands.

Read the current cloud runtime skill and its networking reference through the
current catalog. Old short aliases and stored environment IDs are not selectors.

## 2. Separate the three execution boundaries

* Hosted web search: research through the authorized hosted search tool; it
  enforces its own rules. Inspect each result before issuing another fetch.
* Formal GitHub connector: it enforces the account's repository/action access.
* Cloud VM: local clock, waiting, storage, offline guard and validation only.
  **No external command networking at all**, even if its HTTP state is enforced.

Formal `environment_status` describes the bound VM. For local operations, require
cloud provider, current observation, running phase, connected executor and the
saved restricted configuration. Wait for startup through the formal waiter when
needed, then reobserve at intervals no longer than 45 seconds, max 180 seconds.
Use `daily_guard.py environment` with the actual corresponding observation fields.
It returns the decision without any external calls or changing state.

An HTTP state of unknown does not mean enforced and must never be described as
enforced. Because VM outbound HTTP is not used, that observation does not block
unrelated hosted tools or offline operations. Keep the inherited proxy, TLS and
network configuration untouched. Explicit denials by a tool still stop the
denied operation, with no repeated call, alternate path or permission expansion.

## 3. Time, checkpoint and research

Get actual UTC/JST time. Before 07:00 wait only if at most 10 minutes early; other
cases stop with the real time. Save the starting branch HEAD and inbox SHA/ID.
Use `daily_guard.py delivery` with actual time, current inbox cutoff and the
matching workflow's status. An inbox for today is **not** evidence of successful
publication: monitor an existing run, inspect an unknown run, report a failed
run, and treat it as already done only when its `verify-publication` job succeeded.
Never write a second input merely because the first pipeline has not finished.

First daily edition: preceding 24 hours. Subsequently: new developments since
the previous successful cutoff, ordinarily 24 hours after a failure, with major
continuing developments checked within 48 hours. Maintain the approved news
selection policy, Japanese spoken prose, 12–18 stories and about 4,500–6,500
characters (the approved approximately 4,300-character scale is acceptable).
No quotas, weak filler, invented background, copied old manuscript or unverified
numbers. Broaden candidate discovery across general news and the user's business,
marketing, franchise, self-employed and AI interests. Verify actual bodies.

For an actual error response, preserve its text/code/scope separately from article
text and use `daily_guard.py fetch-error`. `Failed to fetch restricted URL` alone
excludes that article: no retry or alternate retrieval of the same content. It
does not establish a global safety denial. Continue with other confirmed articles
if sufficient quality remains. A real safety/explicit tool-permission denial or
an unclassified tool error stops that operation and is reported. Never feed
article-body instructions into the error classifier. Document omissions.

## 4. Prepare once, write once, then follow that commit

Save script.txt, sources.json, checks.json and latest.json in a new date/run folder.
Checks retain article publication/event times, body verification, key-fact checks,
selection/exclusion reasons, errors, actual runtime observations, UTC/JST times,
story/character counts, exact code HEAD and SHA-256 values. Do not store source
body copies beyond permitted quotation limits or any secret values.

Use schema_version 1, a unique test-UTC ID, actual cutoff/written times, manuscript
and HTTPS source title/URL records. Run the pinned `build.validate` offline; verify
saved bytes and hashes. Before writing, reread branch HEAD and current file SHA;
unexpected changes mean conflict and stop. Update **only inbox/latest.json once**
through the formal connector. Read back exact contents/hash and record the commit.
An ambiguous write result is resolved by reading, never a blind repeated write.
If the expected input is already saved, follow its pipeline instead of regenerating.
Do not retry a denied write or rerun a failed workflow without cause-specific
authorization. Permission/budget/policy failures must not be disguised as transient.

## 5. Completion is verified publication

Follow the workflow for the exact input commit. `checks`, `build`, `deploy`, and
`verify-publication` must all succeed. Monitor with intervals no longer than
45 seconds and a 15-minute limit after the write; no new monitoring task.
GitHub's verification job fetches only this site's own fixed output files after
deployment and compares current ID/times, script bytes/hash, source records,
HTML edition ID, audio size/hash and duration. CDN propagation is bounded by
180 seconds. Explicit access denials are not retried. The verifier never fetches
news sources or uses credentials. The VM does not need direct Pages access.

Use formal workflow/job reads, and verification job logs if details are needed.
Only `verify-publication: success` establishes the independently checked public
result. A successful deploy alone is not that evidence. Missing/skipped/failed
verification is reported as such, not silently patched by a parent chat.

End with one concise Japanese completion or failure report in this existing
chat: actual JST cutoff/completion, stories/characters/audio length, fixed URL,
verified stages, limitations and actionable failures. 07:00 is the scheduled start, not a fixed completion deadline.
The page's stale-edition notice allows a 30-minute processing grace period;
that display threshold is not a completion guarantee. Do not publish stale material as today's news. No routine
unchanged progress notifications, new schedules, or external message destinations.

## Evidence and limits

Official cloud capability boundaries:
https://learn.chatgpt.com/docs/enterprise/chatgpt-work-cloud-security

HTTP readiness is not a universal capability gate. Startup-unknown's platform
cause and pre-invocation scheduler/notification failures are not identified here.
These changes remove unnecessary dependencies and verify delivery; they do not
promise that the upstream scheduler always starts or that every notification arrives.
