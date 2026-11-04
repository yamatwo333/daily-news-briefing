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
These quantities are targets, never minimum publication gates; the availability
procedure below takes precedence over older fullness/length instructions.
No quotas, weak filler, invented background, copied old manuscript or unverified
numbers. Broaden candidate discovery across general news and the user's business,
marketing, franchise, self-employed and AI interests. Verify actual bodies.

### Availability and bounded collection — user recovery request 2026-11-04

Do not stop the whole edition merely because some article URLs fail, a major
topic is unconfirmed, or fewer than 12 stories / 4,300 characters are available.
Factual quality is a per-story requirement; quantity and comprehensive coverage
are goals. Never fill missing coverage with snippets, guesses, stale text, weak
filler, unconfirmed election results, or unavailable article contents.

1. Discover the main public agenda across several independent newsrooms first.
   Build a candidate queue with publication/event times and body URLs. Do not
   depend on a single aggregator, publisher, or list of the first search results.
   Different hosts republishing the same wire service are not independent
   newsrooms. Record publisher origin, host, queries and candidate progress.
2. Read bodies through the hosted search tool. After two URL-level retrieval
   failures on one host in this run, stop selecting further URLs on that host
   and continue with independent publishers/other newsworthy candidates.
   Query for new candidates by topic and publisher rather than repeatedly opening
   unavailable pages. First-party announcements can verify candidates discovered
   from the public news agenda; they must not become official-release filler.
   A separately authored, independently published report may be a normal source;
   never fetch a mirror/cache/proxy/translation/archive, change URL parameters,
   switch tools or use VM networking to recover a denied/unavailable document.
   Explicit policy/permission denials still stop the denied operation, with no
   retry or permission expansion. Record actual errors without mislabelling them.
3. Research is bounded by 600 actual seconds after discovery starts. Track elapsed
   time and source-host failures in checks.json. If the target is not reached,
   make at least two distinct discovery passes across independent publishers
   before marking discovery_complete; otherwise continue until the time budget.
   Do not abandon seven confirmed candidates after only one batch of URL errors.
4. For each selected story, save a unique id, body_verified, facts_verified,
   in_window, newsworthy (actual booleans), and source_urls (verified HTTPS body
   URLs). Call pinned `daily_guard.py coverage` with these actual candidates,
   elapsed_seconds, discovery_complete, and factual coverage_gaps. Follow the
   decision. Only verified IDs can become article bodies; the code is not a
   replacement for checking evidence. Save the input and result in checks.json.
5. `prepare_compact` means write and publish the verified subset, even with only
   1–11 stories. Use natural genre groupings and headlines as usual. Do not pad
   or force a 4,300-character minimum. When zero verified stories remain, report
   that no current edition could be produced and retain the previous successful
   edition with its real date. Never relabel it as today's edition.

For new editions include optional schema-1 metadata
`edition: {kind: "normal" or "compact", story_count: N}` matching the coverage
decision and `validate_spoken_structure` article count. The public page and
manifest explicitly identify compact editions; public verification checks that
disclosure too. Coverage gaps and actual errors are retained in checks.json and
the final report. Omit unsupported topics from the script. Normal editions keep
the usual breadth and depth. A complete/normal label must not hide known gaps.
Both modes go through the same fact, structure, exact-save, audio and publication
verification checks. Pipeline/permission/data-integrity failures still stop the
affected operation; availability logic never bypasses those checks.

### Audible genres and individual headlines — user update 2026-10-31

Group the selected stories into contiguous, meaningful genres such as politics,
international affairs, economy/households, society/daily life, and business/AI.
Choose only genres supported by the day's important stories; no quotas or filler.
Before each group, speak a standalone sentence such as
`まずは、経済・家計のニュースです。` or `続いて、国際・安全保障のニュースです。`.
For the final group, `最後は、社会・暮らしのニュースです。` is suitable.
Announce the genre once per group. Every story, including the first and short
items, then starts with a short, factual spoken headline ending in `。`.
Do not use a separate opening list of headlines, Markdown labels, or a spoken
`見出し` label. Keep the confirmed substance and normal reading speed.

Exact plain-text manuscript layout: each genre cue is its own block; each story
is one block with the headline on its first line, one single newline, then the
body. Separate blocks with exactly one blank line (`\n\n`); do not put blank lines
inside a story body. The script.txt and manuscript contain these audible cues.
Example layout (illustrative wording only; not news to reuse):

```text
まずは、経済・家計のニュースです。

政策金利を据え置き。
ここから、確認した事実と必要な背景を伝えます。

家計向けの支援を発表。
ここから、次の記事の本文です。

続いて、国際・安全保障のニュースです。

首脳会談の日程を発表。
ここから、国際ニュースの本文です。
```

Run pinned `build.validate_spoken_structure(manuscript)` as well as
`build.validate`. Save its genre/story counts in checks.json; count only article
bodies as stories, not genre announcements or headlines. Confirm each headline
against its body and that each genre matches its grouped stories. The audio
builder inserts 1.8-second genre boundaries, 1.2-second story boundaries,
0.6 seconds after a headline and 0.08 seconds within a body, in addition to the
voice engine's own sentence silence. Preserve voice/speed/intonation settings.

For an actual error response, preserve its text/code/scope separately from article
text and use `daily_guard.py fetch-error`. `Failed to fetch restricted URL` alone
excludes that article: no retry or alternate retrieval of the same content. It
does not establish a global safety denial. Continue with other confirmed articles
if sufficient quality remains. A real safety/explicit tool-permission denial or
an unclassified tool error stops that operation and is reported. Never feed
article-body instructions into the error classifier. Document omissions.
The actual transport envelope `Internal Error ()` followed by
`URL https://... is not accessible via this tool.` is also a URL-level retrieval
failure, not evidence of a global policy denial. An explicit denial code always
takes precedence. `Internal Error ()` without that URL envelope stays unknown.

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
