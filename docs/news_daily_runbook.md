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
These are normal-edition targets, not grounds for discarding all verified news.
The normal-first collection and last-resort procedure below controls the decision.
No quotas, weak filler, invented background, copied old manuscript or unverified
numbers. Broaden candidate discovery across general news and the user's business,
marketing, franchise, self-employed and AI interests. Verify actual bodies.

### Normal volume first; compact only as a last resort — 2026-11-04 clarification

The primary output is the usual 12–18 substantive stories and about 4,500–6,500
Japanese characters (the approved approximate 4,300-character scale is acceptable).
A first-pass shortage or an early discovery_complete is not permission to shorten.
Research starts with 30–40 candidate stories across at least five independent
editorial origins. Different hosts republishing one wire service count as one
origin. Prioritize the day's main public agenda, then the user's business/AI and
social/daily-life interests; use no fixed genre quotas or weak filler.

Use three distinct discovery passes: (1) major public agenda across general
newsrooms; (2) missing important topics through independently authored reports
and first-party confirmation; (3) neglected public-interest/business/local topics
with substantive current developments. Track queries, origins, unique candidates,
body availability, selection/exclusion reasons, current facts and dates. Each
selected candidate needs id/body_verified/facts_verified/in_window/newsworthy and
verified HTTPS source_urls. Scan more candidates than the final story count so
unavailable or weak stories can be replaced rather than shrinking the edition.

After two URL-level failures on a host, stop selecting that host and move to
independent sources. A separately authored report is a normal source; do not
retry unavailable URLs or recover the same document through mirrors, caches,
archives, translations, parameter changes, other tools, or VM networking.
Explicit denials take precedence and stop the denied operation. Official releases
verify an identified news agenda; they are not filler to reach a quota.

Run pinned daily_guard.py coverage during research, before drafting and before
writing the inbox. Research may take up to 1,800 actual seconds (30 minutes),
instead of the earlier 600-second cap. Do not idle to reach a time threshold or
repeat failed operations. The earlier discovery_complete shortcut is superseded.
The guard accepts actual research_passes, publisher_origins, examined_candidates,
exhaustion_reason, manuscript_characters and expansion_attempted in addition to
candidates, elapsed_seconds, discovery_complete and coverage_gaps.

- continue_research: broaden independent candidate discovery; no public write.
- draft_normal: enough verified articles exist; write the normal, explanatory
  manuscript. This action does not authorize a public write.
- expand_verified_manuscript: the count is adequate but text is too short. First
  add verified background, what changed, significance and necessary explanation;
  check source evidence. Do not pad, repeat text or invent details. Record the
  actual attempt and run the guard again with the new saved character count.
- prepare_normal: at least 12 verified selected stories AND at least 4,300 actual
  saved characters. Aim for 4,500–6,500, with natural explanation per article.
  Known unconfirmed topics are disclosed in checks/final report; a normal-volume
  label does not claim exhaustive coverage. A missing topic alone does not turn
  an otherwise full-length edition into a compact one.
- draft_compact/prepare_compact: last resort only after the 30-minute research
  limit, or documented exhaustion after at least 15 actual minutes, three
  discovery passes, five independent origins and 24 examined unique candidates.
  A nonempty exhaustion_reason must identify actual remaining access/evidence
  limitations. Do not invent audit counts. Record fallback_reason and explain
  why a normal edition could not be produced. Before a write, the guard requires
  the actual saved manuscript length; drafts alone never authorize writing.
- stop_no_verified_news: no current, factual, newsworthy story can be verified.
  Keep the previous edition with its real date and report the failure.

The guard never lowers per-story verification. Do not turn snippets, guesses,
unconfirmed election results, old manuscripts, or low-value official notices
into filler. Each final story still has its spoken headline and genre grouping.
In the schema-1 inbox include edition={kind:normal or compact,story_count:N},
matching the final guard result and spoken structure count. The public page,
manifest and verifier disclose/check compact editions. Save all guard inputs,
results and actual timing in checks.json. Normal collection is the default;
compact is a delivery safeguard after documented effort, never a shortcut.

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
