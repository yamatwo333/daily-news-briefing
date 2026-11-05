# NEWS daily delivery contract — 2026-10-19

This is the current daily procedure, not a request to restart past tests. The
existing schedule starts daily at 07:00 Asia/Tokyo; completion follows processing. GPT does
the research and Japanese writing using the existing subscription. No paid API,
other model, new schedule, Google Docs sync, credential access, or permission
expansion. Public destination and repository remain unchanged.

## Listening length and clarity — user update 2026-11-05

Target about 8 minutes (normally 7–9); the finished audio must not exceed 600
seconds, including genre cues, headlines and pauses. Keep the approved voice,
speed 1.3, intonation 0.8 and audible boundaries. Never accelerate, cut off the
recording, or remove the explanatory sentence just to fit. This supersedes older
4,300-character minimums, 4,500–6,500-character targets and 6–8-sentence templates.

Keep the praised news selection and broad research effort. Normally select
12–16 substantive stories; up to 18 only when they fit without crowding out
understanding. Aim for 3,600–3,900 total Japanese characters, including headlines
and cues. New normal editions require at least 12 stories and 3,200 characters;
all new editions have a 4,200-character editorial ceiling. These are planning
bounds, not a guarantee of speaking time or permission to pad. Check actual audio.
An eight-minute normal edition is not a source-shortage compact edition.

For each story use a brief factual headline, then usually 3–5 short sentences:
what happened and who is affected, then ONE necessary background/meaning/impact
explanation. Usually 180–280 characters including the headline; give an unusually
important story up to about 350 while saving space elsewhere. Allocate a total
budget before drafting. Explain one level more clearly than the old script,
without treating the listener as a child or repeating basic lessons every day.

Use everyday words and introduce unfamiliar acronyms with a short natural gloss.
Keep subjects explicit and one main idea per sentence. Prefer one or two essential
numbers with a useful comparison over lists of amounts, dates or organization
names. Integrate uncertainty precisely as 'proposed', 'scheduled', or 'according
to X'. Do not append repetitive 'this does not mean...' corrections or generic
'we need to watch...' endings. Preserve a caveat when it actually changes the
meaning. Do not invent personal consequences or causal links to make a story easy.

Read the draft as something heard once: can a listener say what happened and why
it matters without seeing the text? Remove duplicate detail before removing the
useful explanation. Keep source detail in the source list, not spoken URLs.
Record this editorial review and actual character/story counts in checks.json.

New inboxes should include listening_policy="eight-minute-v1". For compatibility
with existing scheduled JSON, the new-input CLI adds that build metadata when
omitted, without changing the manuscript, sources, ID or dates. It validates the
4,200-character ceiling, and the audio builder
checks the measured final MP3 duration before rendering/uploading. If over 600
seconds, no overlong audio is published: report that the manuscript needs editing,
without automatic truncation, faster speech, or a second unapproved inbox write.
The public verifier checks the policy and 600-second ceiling. Historical inputs
without the policy remain readable and verifiable; do not relabel old long audio.

The November 5 user change supersedes the older length instructions embedded in
the existing daily schedule. Always use these current repository editing rules
and the current coverage guard results after fetching the pinned HEAD. An old
4,300-character floor must not be used to pad a new script or reject prepare_normal.
The schedule itself remains at 07:00; no schedule mutation is required for this
repository policy to apply. The prepared replacement prompt is saved separately
for eventual schedule-text alignment, not an instruction to create another task.

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
selection policy and Japanese spoken prose under the current eight-minute
listening budget above (normally 12–16 stories and 3,600–3,900 characters).
These are normal-edition targets, not grounds for discarding all verified news.
The normal-first collection and last-resort procedure below controls the decision.
No quotas, weak filler, invented background, copied old manuscript or unverified
numbers. Broaden candidate discovery across general news and the user's business,
marketing, franchise, self-employed and AI interests. Verify actual bodies.

### Normal volume first; compact only as a last resort — 2026-11-04 clarification

The primary output is a substantive normal edition within the listening budget
above. The November 5 listening limit supersedes the former longer word target.
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
- shorten_manuscript: more than 4,200 actual characters; remove redundant detail
  and secondary specifics, preserve meaning, then revalidate. No public write.
- prepare_normal: at least 12 verified selected stories AND 3,200–4,200 actual
  saved characters. Aim for 3,600–3,900 with one useful explanation per article.
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
matching the final guard result and spoken structure count, plus
listening_policy="eight-minute-v1" for every new input. The public page,
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
