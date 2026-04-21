# Daily Briefing Principles

## Core Model

The foundational learning document remains the map:

- `docs/news_foundation_2026_ja.pdf`
- `docs/news_foundation_2026_ja.docx`
- `docs/news_foundation_2026_ja.md`

The daily brief is the daily application layer built on top of that map.

It is no longer a heavily scaffolded learning worksheet.

It is now a daily morning news digest.

It must still remain:

- plain
- calm
- beginner-friendly
- easy to understand by ear
- broad enough to build knowledge over time

The foundation still guides judgment, but the final output should not feel like
a classroom handout or a repeated lesson script.

## User Preference Shift

The brief should now clearly optimize for:

- news titles first
- faster understanding of what happened
- less repeated explanation
- less rigid sectioning
- more variety across topics
- concrete before abstract
- background or reason-for-occurrence explained when needed
- short plain examples or comparisons only when they truly help
- TTS-friendly final output
- short opening and short ending sections

## Coverage Window

The effective coverage window should normally run from the previous scheduled
run until now.

Story selection should preserve meaningful day-level understanding even if the
actual execution timing shifts.

Do not let a delayed or manual run collapse into only the last few visible
hours unless the relevant news flow truly happened only then.

Older developments may still appear if they remain materially important today.
But if an older story has only weak updates inside the effective coverage
window, move it to the short secondary section instead of reusing it as a main
story.

## Story Count And Breadth

Use 6 main stories by default.

Use 7 only when the extra story is clearly useful.

Use 5 only on genuinely light days.

The daily selection should actively broaden the reader's knowledge across
fields over time.

## Topic Pools

The daily brief should rotate across these important pools as the news allows:

- international politics / geopolitics / security
- economy / prices / rates / macro
- Japan domestic politics / policy / institution / social system
- business / industry / technology
- society / justice / healthcare / education / labor
- cyber security / ransomware / breaches / infrastructure cyber risk
- art / culture / cultural policy / heritage / content industries
- energy / resources / environment / logistics
- disaster / public health / infrastructure / resilience
- media / information space / misinformation / narrative

These are editorial pools, not rigid quotas.

Do not force weak stories just to fill a bucket.

Cyber is not mandatory every day, and art or culture is not mandatory every
day, but neither category should be systematically overlooked.

## Main Story Selection Rules

Choose stories by balancing all of the following:

- importance
- freshness
- learning value
- Japan relevance
- breadth across fields
- diversity across broad causal clusters
- non-repetition across consecutive days
- clarity for a beginner listener

Headline-first clarity matters.

The reader should understand what the story is before hearing a long
interpretation of it.

## Anti-Repetition Rule

The same major story should not be reused as a main story on consecutive days
unless there is clearly meaningful new information.

Meaningful update criteria should remain explicit.

A continuing story should return as a main story only when there is substance
such as:

- a new official statement
- a newly disclosed number, forecast, or document
- a meaningful policy, legal, or negotiation step
- a new phase in the situation
- a meaningful Japan-side response
- infrastructure disruption, operational change, or security consequence
- a materially different interpretation today because the facts changed

If updates are weak, move the story to the short secondary section instead of
reusing it as a full main story.

## Explanation Repetition Suppression

Even if a topic reappears, do not re-explain the same background at full
length.

Do not reuse near-identical wording across consecutive days.

Compress recurring background sharply.

Focus on what changed today.

Keep any refresher background to one short sentence at most.

The intended feeling is:

- 「今日、何が変わったかが分かった」

not:

- 「昨日の説明をまた聞いた」

For topics that appeared as main stories within the last 3 daily runs,
background should usually be reduced to a brief refresher unless the story has
moved into a clearly new phase.

## Japan Domestic Rule

The Japan domestic slot should preferably remain a true Japan domestic policy,
institution, or social-system story.

Actively prioritize:

- laws and bills
- policy design
- regulation
- justice
- healthcare
- labor
- education
- tax
- budget
- social security
- administrative or institutional change

Do not let this slot drift too often into only market data unless market data
is truly the strongest Japan domestic development that day.

## Business And Technology Freshness Rule

Do not elevate a business or technology story only because:

- a date arrived
- an event is expected later
- a company may announce something soon

Require real substantive information such as:

- released earnings
- guidance changes
- official investment decisions
- production, demand, or supply changes
- signed agreements
- policy-linked industrial developments
- materially new results or documents

Weak-update business stories should be pushed out of the main lineup and moved
to the short secondary section or excluded.

## Cyber Rule

Cyber security, ransomware, breaches, and infrastructure cyber risk should be
treated as real candidate categories for the main lineup.

They should not be systematically overlooked.

Raise cyber priority when there is:

- official disclosure
- infrastructure disruption
- government, regulatory, or policy response
- operational interruption
- geopolitical linkage

Do not force cyber every day.

## Art And Culture Rule

Art and culture remain valid main-story categories when they help explain
society, values, policy, diplomacy, identity, or structural change.

Celebrity gossip remains excluded.

Qualifying angles can include cultural policy, heritage, arts institutions,
content industries, diplomacy, or broader social change.

Do not force culture every day.

But do not let it disappear for long stretches if meaningful candidates exist.

## Cluster Diversity Rule

Avoid overloading the main lineup with too many stories from the same broad
causal cluster.

Prefer not to use more than 2 main stories from the same broad cluster.

Additional stories from the same cluster should usually move to the short
secondary section.

The goal is broader understanding, not hearing the same crisis three different
ways.

## Concrete-Before-Abstract Writing Rule

Within each story:

- say what happened before abstract interpretation
- place important numbers early when they matter
- explain why the story surfaced when that background is needed
- use one short plain example or comparison only if it truly helps the listener
  imagine the issue
- simplify abstract policy language into plain meaning whenever possible

The brief should move from concrete facts to explanation, not the other way
around.

## Secondary Section Rule

Use the short secondary section for important follow-up items that still matter
but do not justify full treatment today.

Use it when:

- a major continuing story has weak updates
- a candidate is meaningful but loses the freshness test
- a candidate would create excessive cluster concentration
- a recurring story still matters, but today's value is mainly "still ongoing"

Keep these items concise and focused on what is being watched next.

## Final Read-Aloud And Google Docs Formatting

The final `read_aloud_ja.md` file and Google Doc body must be TTS-friendly.

Do not use:

- markdown heading markers such as `#`, `##`, `###`
- markdown bullet markers such as `-` or `*`
- numbered markdown lists
- backticks

Use plain Japanese section labels suitable for text-to-speech.

Repository reference artifacts may still use markdown when useful.

## Final Content Structure

The tracked automation prompt should use this final read-aloud structure:

1. title
2. `今日の主要ニュース`
3. 6 default main stories, or 7 when clearly useful, or 5 on genuinely light
   days
4. `短く追うニュース`
5. `今日ここだけ覚える`

The opening section should be very short and should not become a lesson-style
introduction.

Each main story should use this order:

- `ニュースタイトル`
- `一言でいうと`
- `何が起きたか`
- `なんでこの話が出てきたのか`
- `なぜ重要か`
- `日本への影響`
- `次の焦点`

The closing section should contain only 3 short points.

The ending should not become a long lesson or essay.

## Reference Outputs And Sync Boundary

The repository should continue to generate:

- a reference daily briefing
- a source log CSV
- a manifest JSON
- a weekly rolling reference file
- a final read-aloud study script

Keep the Google Docs sync workflow unchanged unless a sync-specific change is
explicitly required.

Do not modify `config/google_doc_sync.json` unless necessary.

Do not regress `scripts/sync_google_doc.py`.
