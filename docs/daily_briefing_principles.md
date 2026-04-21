# Daily Briefing Principles

## Core Model

The foundational learning document remains the map:

- `docs/news_foundation_2026_ja.pdf`
- `docs/news_foundation_2026_ja.docx`
- `docs/news_foundation_2026_ja.md`

The daily brief is the daily application layer built on top of that map.

It is no longer a heavily scaffolded beginner worksheet. It is now a broader,
headline-first daily digest with enough explanation to make the news meaningful.

The foundational map still matters. The daily brief should help the reader place
today's events onto that map without re-teaching the whole map every morning.

The five learning questions from the foundation still guide editorial judgment,
story ordering, and explanation depth, but they should not force a rigid
worksheet-style final script every day.

## Reader And Tone

Assume the reader is still a beginner.

Writing must remain:

- plain
- calm
- beginner-friendly
- clear enough for listening
- non-dense

The brief should feel broader, fresher, and more listenable than before.

## Coverage Window

The effective coverage window should normally run from the previous scheduled run
until now.

Story selection should preserve meaningful day-level understanding even if the
actual execution timing shifts.

Do not let a manual or delayed run collapse into only the latest few visible
hours of headlines unless the relevant news flow truly happened only then.

Older developments may still appear when they remain materially important today.
But if an older story has little meaningful new information inside the effective
coverage window, move it to the short secondary section instead of reusing it as
a full main story.

Record the effective coverage window in the reference briefing and in the run
summary.

## Story Count And Breadth

Use 6 main stories by default.

Use 7 only when the extra story is clearly useful for breadth or day-level
understanding.

Use 5 only on genuinely light days.

The daily selection should actively broaden the reader's knowledge across fields
over time, not just mirror whichever topic dominated yesterday.

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

These are editorial pools, not rigid quotas. Do not force weak stories just to
fill a bucket. But do use them to maintain breadth over time.

## Headline-First Presentation

The final brief should present stories headline first.

Each main story should begin with a clear news title, then explain the story in
a way that makes the day's change meaningful.

The output should feel like a daily digest, not like a worksheet.

## Anti-Repetition Rule

The same major story should not be reused as a main story on consecutive days
unless there is clearly meaningful new information.

Meaningful update criteria should remain explicit. A story may return as a main
story only when there is substance such as:

- a new official statement
- a new disclosed number, forecast, or document
- a meaningful policy, legal, or negotiation step
- a new phase in the situation
- a meaningful Japan-side response
- infrastructure disruption, operational change, or security consequence
- a materially different interpretation today because facts changed

If updates are weak, move the story to the short secondary section instead of
reusing it as a full main story.

## Explanation Repetition Suppression

Even if a topic reappears, do not re-explain the same background at full
length.

Do not reuse near-identical wording across consecutive days.

Compress recurring background sharply.

Focus on what changed today.

The intended feeling is:

- 「今日、何が変わったかが分かった」

not:

- 「昨日の説明をまた聞いた」

For topics that were main stories within the last 3 daily runs, background
should usually be reduced to a very short refresher unless the story has moved
into a clearly new phase.

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

Do not let this slot drift too often into only market data unless market data is
truly the strongest Japan domestic development that day.

## Business And Technology Freshness Rule

Do not elevate a business or technology story only because:

- a date arrived
- an event is scheduled later
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
treated as a real rotating main-story category.

They should not be systematically overlooked.

Raise cyber priority when there is:

- official disclosure
- infrastructure disruption
- government or regulatory response
- operational interruption
- geopolitical linkage

## Art And Culture Rule

Art and culture remain valid rotating categories when they help explain society,
values, policy, diplomacy, identity, or structural change.

Celebrity gossip remains excluded.

Possible qualifying angles include:

- cultural policy
- heritage and preservation with public significance
- censorship or free-expression issues
- arts institutions and funding
- content industries with structural relevance
- international cultural diplomacy
- major cultural developments that illuminate broader social change

Art and culture are not mandatory every day.

But the category should not silently disappear for long stretches. If art or
culture has been absent as a main story for 7 daily runs, raise its priority
meaningfully on the next eligible day without forcing weak content.

## Cluster Diversity Rule

Avoid overloading the main lineup with too many stories from the same broad
causal cluster.

Prefer not to use more than 2 main stories from the same broad cluster.

Additional stories from the same cluster should usually move to the short
secondary section.

The goal is broader understanding, not hearing the same crisis three different
ways.

## Secondary Section Rule

The short secondary section is for important follow-up items that still matter
but do not justify full treatment today.

Use it when:

- a major continuing story has weak updates
- a candidate is meaningful but loses the freshness test
- a candidate would create excessive cluster concentration
- a recurring story matters, but today's value is mainly "still ongoing"

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
3. 6 default main stories, or 7 when clearly useful, or 5 on genuinely light days
4. `短く追うニュース`
5. `最後に押さえるポイント`

Each main story should use this headline-first order:

- `ニュースタイトル`
- `要点`
- `なぜ重要か`
- `日本への影響`
- `次の焦点`

The final script should sound smooth when read aloud and should avoid rigid
worksheet-style repetition.

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
