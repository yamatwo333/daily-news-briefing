# Daily Briefing Principles

## Core Model

The foundational learning document remains the map:

- `docs/news_foundation_2026_ja.pdf`
- `docs/news_foundation_2026_ja.docx`
- `docs/news_foundation_2026_ja.md`

The daily brief is the daily application layer built on top of that map.

It is a morning news digest meant to be easy to follow by ear.

It should feel closer to radio flash news with short explanation than to a
worksheet, structured report, or analyst memo.

The quality target remains:

- plain
- calm
- beginner-friendly
- easy to understand
- easy to follow in TTS
- broad enough to build knowledge over time

The listener should quickly understand what kind of news they are hearing,
what changed today, and why it matters.

## Newsworthiness-First Agenda

The briefing must behave like a radio flash-news editor, not like an
official-document collector.

Do not start from ministry releases, white papers, regular statistics,
councils, forums, or scheduled meetings.

First identify the actual public news agenda of the day from major news
coverage.

Scan and compare major coverage across:

- NHK major news
- Reuters Japan
- Nikkei
- Kyodo or Jiji when available
- major national newspapers
- major TV or radio-style news agendas when available

Only after candidate stories are identified should official sources be used
for verification, numbers, dates, legal wording, and implementation detail.

Official documents should support selection, not define it by default.

If an item is visible mainly because an official body published it, but it is
not meaningfully part of the broader public news agenda, it should usually not
lead a main section.

## Coverage Window And Sync Boundary

The effective coverage window should normally run from the previous scheduled
run until now.

Story selection should preserve meaningful day-level understanding even if the
actual execution timing shifts.

Do not let a delayed or manual run collapse into only the last few visible
hours unless the relevant news flow truly happened only then.

Older developments may still appear if they remain materially important today.

If an older story has only weak updates inside the effective coverage window,
move it to short secondary tracking instead of reusing it as a main section.

Keep the existing Google Docs sync workflow intact.

Do not modify `config/google_doc_sync.json` unless a sync change is clearly
required.

Do not modify `scripts/sync_google_doc.py` unless an actual sync bug fix is
required.

## Final Read-Aloud Structure

The final `read_aloud_ja.md` file and Google Doc body should begin with a very
short greeting and then move directly into the section-based body.

Acceptable opening example:

`おはようございます。4月24日朝のニュースです。`

Do not add a separate `今日の主要ニュース` headline list.

Do not add a title line before the greeting in the read-aloud body.

Do not add long introductory framing or explanation about how the digest is
organized.

Do not add meta-guidance lines such as:

- `数字が出た話は数字を先に`
- `制度の話は実施時期を意識して`
- `今日の聞き方は`

The final script should use section-based flow, not a flat story list.

The section label should help the listener understand what kind of news they
are now hearing.

Acceptable section transitions include:

- `まずは政治・行政・司法のニュースです。`
- `続いては国際・安全保障のニュースです。`
- `次は経済・家計のニュースです。`
- `次は社会・暮らし・インフラのニュースです。`
- `続いては産業・企業・テクノロジーのニュースです。`
- `最後は文化・地域のニュースです。`
- `最後は科学のニュースです。`
- `最後は環境・資源のニュースです。`
- `最後は国際協力のニュースです。`
- `最後はメディア・情報空間のニュースです。`

After the main sections, add:

`そのほか、短く確認します。`

End with:

`今日ここだけ覚える`

That closing section must contain exactly 3 short points and then end cleanly.

## Core Section Model

Build the digest around these five core sections:

1. `政治・行政・司法`
2. `国際・安全保障`
3. `経済・家計`
4. `社会・暮らし・インフラ`
5. `産業・企業・テクノロジー`

`政治・行政・司法` is the highest-priority domestic section.

`経済・家計` should be household-oriented, not market-only.

`社会・暮らし・インフラ` is a core section, not an optional bucket.

`産業・企業・テクノロジー` remains important, but it should require
substantive updates.

Use one rotating sixth section only when it is meaningful:

- `文化・地域`
- `科学`
- `環境・資源`
- `国際協力`
- `メディア・情報空間`

Do not force the rotating sixth section every day when the candidates are
weak.

## Main-Story Gate

Before a story becomes a main story, apply all of the following checks.

### Routine Official Release Demotion

The following should not become main stories by default:

- regular monthly statistics
- white papers
- routine ministry meetings
- advisory council meetings
- ministerial press conferences
- forums or symposiums
- routine adoption or grant selections
- JIS updates
- routine diplomatic agreements
- weekly investment flow statistics
- regularly scheduled reports

These may become main stories only if at least one of the following is true:

- the number is a major surprise, record, sharp reversal, or changes the
  interpretation of the economy or society
- it directly affects household burden, wages, employment, rights, safety, or
  daily life
- it represents an actual policy decision, law change, enforcement action,
  court decision, budget change, or regulatory change
- it is strongly connected to a major political, judicial, social, or
  international issue already in the public agenda
- it would plausibly be covered in a mainstream radio or TV flash-news segment
- it has exceptional explanatory value for the user

If none of those conditions is met, move the item to short secondary tracking
or omit it.

### Radio Agenda Alignment

Ask:

`Would a serious morning radio flash-news program plausibly include this as one of its main items today?`

If the answer is no, the story should usually not be a main story unless it
has exceptional explanatory value for the user.

### Main-Story Strength Test

Each main story must pass at least two of these tests:

- important to many people
- new today
- changes policy, rights, money, safety, work, or social systems
- likely to appear in mainstream news broadcasts
- helps explain a major ongoing issue
- has strong Japan relevance
- has a reliable factual basis
- is not merely a routine official update

If a story passes only because it has an official source, reject it as a main
story.

## Story Selection Priorities

Story selection must explicitly prioritize:

- public importance
- genuine freshness today
- domestic relevance for Japan
- effect on daily life, rights, money, work, security, or social systems
- political or institutional weight
- explanatory value
- topic diversity
- whether the story was already over-covered in recent outputs
- source reliability

Penalize candidates when:

- they are only `a meeting was held` with little decision or substance
- they are only market noise without broader household or real-economy
  relevance
- they duplicate another story in the same causal chain
- they were already main stories recently and today adds little
- they are official but minor
- they are easy to write about but not actually one of the day's more
  important stories

If there is a meaningful domestic politics, justice, or institutional story,
it should usually outrank a minor market-data story or a procedural
international agreement.

## Domestic Public-Agenda Priority

For `政治・行政・司法`, actively check major public-agenda topics before
using narrow administrative enforcement stories.

Give priority to:

- constitutional revision
- retrial system reform
- criminal justice
- major Diet deliberations
- major bills
- party negotiations
- cabinet decisions with broad impact
- tax, pension, healthcare, education, childcare, labor
- major court rulings
- criminal justice reform
- scandals or accountability issues with institutional importance
- national security policy decisions

A narrow administrative enforcement item should not be the main politics story
if a broader political, judicial, or institutional story has meaningful
movement.

## Mandatory Candidate Checks

Before final story selection, explicitly check whether there are material
updates in:

- constitutional revision / `憲法改正`
- retrial system / `再審制度`
- major Diet deliberations
- cabinet decisions
- tax, budget, social security
- education, healthcare, labor, childcare, pensions
- major justice or court developments
- disaster response
- cyber or digital safety
- major international or security developments
- wages, prices, employment, consumption, rates
- important business, technology, or industry developments
- culture, regional policy, science, environment, or international cooperation

Record these checks in the reference daily briefing when they materially affect
selection.

## Section-Specific Rules

### Politics, Administration, And Justice

This is the highest-priority domestic section.

Prioritize:

- constitutional revision
- retrial system reform
- criminal justice
- major bills
- Diet developments
- cabinet decisions
- tax, budget, or social security
- healthcare, education, or labor
- administrative reform
- court decisions or judicial-system changes
- rights, governance, transparency, and accountability
- scandals or accountability issues with institutional importance
- national security policy decisions

Do not let this section be displaced by minor market stories when meaningful
political, administrative, or judicial updates exist.

### International And Security

Prioritize:

- wars, ceasefires, or negotiations
- sanctions
- alliances
- sea lanes
- hostage, evacuation, or citizen protection
- major diplomatic talks
- defense and security frameworks
- international legal or institutional changes

Do not split one international causal chain into too many separate main
stories.

### Economy And Household

Prioritize:

- wages
- prices
- employment
- consumption
- household burden
- interest rates
- housing or loans
- key macro indicators
- government measures affecting living costs
- small-business profitability when it affects local employment or price
  pass-through

Do not overuse stock-market-only stories.

Do not use stock index moves, foreign investor flow, or market positioning as
main stories unless they clearly connect to household impact, company
investment, pensions, financial stability, or a major macro turning point.

If the choice is between a routine market or statistical item and a major
politics, justice, social, disaster, security, or household-impact story,
choose the latter.

A stock-market story should become a main story only if it strongly affects
household behavior, company investment, financial conditions, pensions, or the
broader economy.

If both a stock index and foreign investor flow are candidates, usually
combine them or choose one, not both.

### Society, Daily Life, And Infrastructure

Prioritize:

- disasters
- healthcare safety
- education
- cyber incidents or official cyber statistics
- public safety
- infrastructure
- transport
- local operational issues
- environment and public health
- consumer safety
- school, hospital, local government, or essential service disruptions

Cyber belongs here when it is strong, but it is not mandatory every day.

### Industry, Business, And Technology

Prioritize:

- earnings with meaningful numbers
- M&A
- factory or capex announcements
- semiconductors or AI with concrete numbers or deals
- supply-chain changes
- energy or infrastructure investment
- policy-linked industrial developments
- major product, safety, or platform changes
- business decisions with employment, investment, consumer, or regional impact

Do not promote scheduled events without substantive new information.

Do not use `meeting held` or `forum held` as a main story unless there is a
concrete decision, project, investment, agreement, number, or implementation
step.

### Rotating Sixth Section

Use the rotating sixth section only when it is meaningful.

Good candidates include:

- culture policy
- regional revitalization
- cultural heritage
- tourism with regional or economic significance
- ODA or international cooperation
- science policy
- environment or resource policy
- media or information-space policy
- misinformation, platform governance, or speech regulation

Culture should not be celebrity gossip.

The rotating section should help explain society, policy, values, region,
identity, diplomacy, or economic change.

## Repetition And Cluster Control

Do not reuse the same major story as a main story day after day unless there
is clearly meaningful new information.

If a story remains important but has no meaningful update, move it to short
secondary tracking.

If a topic appeared recently, do not re-explain the same background at full
length.

Do not use more than 2 main stories from the same broad causal cluster across
the whole digest.

Examples of broad clusters include:

- Middle East conflict -> sea lanes -> oil -> inflation -> IMF forecast
- AI boom -> semiconductors -> suppliers -> capex
- fiscal strain -> bonds -> budget debate
- cyber incident -> outage -> cyber regulation
- domestic fiscal policy -> market rates -> bond auction

If a third candidate from the same cluster is strong but overlapping, merge it
into the stronger story or move it to short secondary tracking.

## Per-Story Spoken Flow

Within each main section, the lead story should follow this natural spoken
flow:

- headline
- one short natural sentence that tells the listener what kind of news this is
- concrete new fact
- short background or reason why this issue surfaced now
- why it matters
- Japan or daily-life impact
- what to watch next

Per-story rules:

- The title should sound like a real news heading
- The sentence immediately after the title is crucial
- It must tell the listener what kind of story this is
- Never let the listener enter detailed facts without understanding the
  premise
- Explain the concrete fact in 2 to 3 short sentences
- If numbers matter, show the numbers early
- Explain background or reason-for-occurrence in 1 to 2 short sentences when
  needed
- Use at most one short plain comparison or example when helpful
- Explain why it matters in 1 to 2 short sentences
- Explain Japan or daily-life impact briefly and concretely
- End with 1 short sentence about what to watch next
- Each main story should usually stay within 6 to 8 sentences total
- After the sentence beginning with `次に見るべき点は`, do not add more
  explanation for that story

Prefer short sentences and one main idea per sentence.

The writing should sound natural by ear and remain calm, plain, and
beginner-friendly.

## Short Secondary Tracking

After the main sections, add:

`そのほか、短く確認します。`

Use 2 to 4 brief items.

Each item should be 1 sentence only.

Use this section for:

- important themes with weak updates
- worthy but non-leading stories
- stories pushed out because of cluster overlap

Do not include editorial-process notes.

Do not write lines such as:

- `候補として確認しましたが`
- `採用を見送りました`
- `短報扱いにしました`
- `今日は主枠にしませんでした`
- `短報として扱った理由は`
- `主枠との重複を避けて`
- `今後の主枠候補として`

## Closing

Finish with:

`今日ここだけ覚える`

Use exactly 3 short points.

Do not add a fourth point.

Do not add a lesson after it.

End cleanly after this section.

## TTS And Hard Constraints

The final `read_aloud_ja.md` file and Google Doc body should avoid noisy
markdown syntax.

Do not use:

- markdown heading markers such as `#`, `##`, or `###`
- markdown bullet markers such as `-`, `*`, or numbered markdown lists
- backticks

Use plain Japanese section labels suitable for text-to-speech.

The final read-aloud script must not contain:

- `今日の主要ニュース`
- `本編`
- `補足です`
- `状況の見取り図`
- `聞き方のコツ`
- `加えて`
- `この流れを押さえると`
- `数字と制度の両方で見ていきましょう`
- editorial process notes
- long explanation about how the digest is organized

## Fact-Checking Safeguards

Before the final read-aloud script is written:

- if a date range includes a date later than the current briefing date,
  verify it against the source before including it
- do not output future-looking date ranges as past facts unless the source
  clearly states them
- if a claim sounds unusually precise, cross-check it
- if source uncertainty remains, phrase cautiously or omit the detail from the
  read-aloud script

## Reference Artifacts

The reference daily briefing may be more structured and source-oriented than
the read-aloud version.

It may use markdown when useful.

It should record:

- the effective coverage window
- why each main section was selected today
- what materially changed inside the coverage window
- when a continuing story was demoted because there was no material update
- any cluster-overlap judgment
- whether recent over-coverage affected selection
- source reliability or uncertainty when that matters

The final read-aloud script and Google Doc body should present only the news
itself and should not leak the internal newsroom process.
