# Daily Briefing Principles

## Core Model

The foundational learning document is the map:

- `docs/news_foundation_2026_ja.pdf`
- `docs/news_foundation_2026_ja.docx`
- `docs/news_foundation_2026_ja.md`

The daily brief is the guided daily practice layer built on top of that map. It should help the reader place today’s events into the larger structure, without re-teaching the whole foundation from zero.

Assume the reader is still a beginner. Writing must remain calm, plain, beginner-friendly, and non-dense.

Daily story selection must balance:

- importance
- freshness
- learning value
- Japan relevance
- diversity across fields
- non-repetition across consecutive days
- non-repetition of yesterday’s explanation

## Daily Reading Questions

Use these five reading questions in every daily brief:

1. これは何の話か
2. なぜニュースになるのか
3. 誰が得して、誰が困るのか
4. 日本や自分の生活とどう関係するのか
5. 一時的な話か、構造的な話か

## Coverage Window

The effective coverage window should normally run from the previous scheduled run until now.

The brief should preserve meaningful day-level understanding. It should not become biased toward only the most recent few morning hours unless the relevant news flow truly happened only then.

If execution timing is manual or shifted, story selection should still cover the meaningful developments across the day-level window, not just the latest visible headlines.

Record the effective coverage window in the run summary.

Older developments may be included only if they remain clearly dominant and materially relevant today. When an older development remains important but has no material update, prefer `継続監視` over a full repeated main story.

## Story Count And Composition

Use 5 stories by default.

Use 6 stories if one extra story is clearly useful for learning breadth or for understanding the day.

Use 4 stories only on genuinely light days.

The base composition is:

- international politics / geopolitics / security
- economy / prices / interest rates / macro
- Japan domestic politics / policy / institution / social system
- business / industry / technology
- one rotating lens
- optional second rotating lens

Rotating lenses:

- law / regulation / judiciary
- society / population / labor / education / healthcare
- energy / resources / food / environment / logistics
- media / information space / misinformation / narrative
- disaster / public health / infrastructure / resilience
- history / background relevance when especially useful

Do not include weak stories just to fill a category. If one base bucket is weak that day, replace it with a more important and fresher story from another bucket while preserving breadth as much as possible.

## Japan Domestic Slot

The Japan domestic slot should preferably be a true Japan domestic politics / policy / institution / social system story.

Actively prioritize:

- government decision-making
- policy design
- 制度変更
- budget / taxation / social security
- education / healthcare / labor / regulation
- domestic governance or administrative change

Do not let the Japan domestic slot drift too often into only Japanese market data unless that is truly the strongest Japan-relevant development.

## Business And Technology Freshness

Do not promote a business or technology topic to a main story only because:

- a scheduled earnings date has arrived
- an event is today
- a company may announce something later

A business or technology story should generally require meaningful new substance such as:

- released earnings numbers
- guidance changes
- official investment announcements
- production / order / demand changes
- signed agreements
- policy-linked industrial developments
- materially new documents or results

Weak-update business stories should be moved to `継続監視` or excluded.

## Freshness And Non-Repetition

Every main story must explicitly state what changed since yesterday or since the previous scheduled run. If there is no meaningful update, the story probably should not be a main story.

The same major story should not be reused as a main story on consecutive days unless there is clearly meaningful new information.

A story may reappear as a main story only if there is a material update such as:

- a new official statement
- a new number or forecast
- a new negotiation or ruling step
- a meaningful Japan-side response
- movement into a new phase
- a materially different interpretation today

Otherwise, move it to a short `継続監視` section instead of repeating the full explanation.

## Explanation Repetition Suppression

Even if a topic reappears, do not re-explain the same background at full length.

Do not reuse near-identical wording across consecutive days. Compress refresher background for recurring topics and focus on what changed today.

The reader should feel:

- 「今日、何が変わったかが分かった」

not:

- 「昨日と同じ説明をもう一度聞いた」

If a topic appeared as a main story within the last 3 days, then unless there is a major phase change:

- background should usually be limited to one short refresher sentence
- key term explanation should be shorter than usual
- the value should come mainly from the delta

## 継続監視

Important continuing themes with limited updates should appear as short monitoring bullets rather than full repeated stories.

Use `継続監視` for topics that remain important but do not have enough new information to justify a main story today.

Monitoring bullets should be short and should explain:

- what is being watched
- why it still matters
- what kind of change would make it a main story again

## Final Study Script Structure

The final read-aloud study script must use this structure:

1. `今日の全体像`
2. `昨日から新しく分かったこと`
3. `まずこれだけ知っておくと分かりやすいこと`
4. `今日のニュースはこの順番で考えると分かりやすい`
5. Main stories, 5 by default, with the required per-story fields
6. `継続監視`
7. `今日のつながり`
8. `今日わかったこと`
9. `ことばのやさしい説明`
10. `明日以降の見方`

Each main story must use the five reading questions and must also clearly state what changed today.

## Sync Boundary

Keep the Google Docs sync workflow unchanged unless there is a specific sync requirement.

Do not modify `config/google_doc_sync.json` unless necessary.

Do not regress `scripts/sync_google_doc.py`.
