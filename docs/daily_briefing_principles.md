# Daily Briefing Principles

## Core Model

The foundational learning document remains the map:

- `docs/news_foundation_2026_ja.pdf`
- `docs/news_foundation_2026_ja.docx`
- `docs/news_foundation_2026_ja.md`

The daily brief is the daily application layer built on top of that map.

It is a morning news digest meant to be easy to follow by ear. It should feel
like a serious radio flash-news program with short explanation, not like a
worksheet, a policy briefing, an analyst memo, or an official-release roundup.

The quality target is a near-100-point daily result:

- real newsworthiness
- public salience
- strong story selection
- radio-style section flow
- compact main stories
- flexible social and daily-life coverage
- no official-release filler
- no editorial leakage in the read-aloud script

The listener should quickly understand what kind of news they are hearing,
what changed today, why it matters, how it may affect Japan or daily life, and
what to watch next.

## Newsworthiness-First Agenda

The briefing must behave like a radio flash-news editor, not like an
official-document collector.

Do not start from ministry releases, white papers, regular statistics,
councils, forums, scheduled meetings, or official update queues.

First identify the actual public news agenda of the day from major news
sources and socially salient coverage.

Scan and compare major coverage across:

- NHK major news
- Reuters Japan
- Nikkei
- Kyodo or Jiji when available
- major national newspapers
- major TV or radio-style news agendas when available
- reputable specialist sources for health, cybersecurity, finance,
  technology, law, science, and public safety
- credible reports of socially salient incidents that affect health, safety,
  privacy, money, work, trust, or daily behavior
- official sources only after candidate stories are identified

Official documents should be used for verification and detail, not as the
primary agenda-setting mechanism.

Use official sources after candidate stories are identified, mainly for:

- factual confirmation
- numbers
- dates
- legal or policy wording
- implementation detail
- agency, company, or institutional position

If an item is visible mainly because an official body published it, but it is
not meaningfully part of the broader public news agenda, it should usually not
lead a main section.

## Public-Agenda And Social-Salience Scan

Before final story selection, explicitly scan for socially salient stories
even if they are not classic politics, economy, or hard-news stories.

Check for:

- public health and infectious disease
- travel and quarantine risks
- consumer safety
- corporate scandals or misconduct
- information leaks and privacy incidents
- SNS-origin incidents with real-world institutional impact
- workplace, school, hospital, bank, local-government, transport, or
  infrastructure incidents
- platform and digital-behavior issues
- cyber incidents, ransomware, data breaches, and non-cyber information leaks
- product recalls, service outages, fraud, scams, and account abuse
- stories widely covered by TV, radio, or web news
- stories strongly circulating in public conversation because they affect
  trust, safety, privacy, health, money, institutions, or daily behavior

Do not dismiss these stories as soft news when they affect trust, safety,
privacy, health, money, institutions, or daily behavior.

A bank employee posting workplace footage that exposes customer information is
a financial-institution trust and information-management story, not mere
social-media gossip.

A cruise-ship or travel-related infectious-disease cluster may be a
public-health, travel, quarantine, and risk-communication story, not just
overseas health trivia.

Do not force public-health, SNS, privacy, cyber, culture, or consumer-safety
stories every day.

Do not overlook them when they would plausibly appear in mainstream radio or
TV flash news.

## SNS-Origin Source Handling

SNS trends, viral posts, or platform discussion may be used as discovery
signals, but never as the sole source for final factual claims.

For SNS-origin or viral stories:

- verify with reputable media, official statements, company statements,
  agency releases, or primary documents
- avoid repeating unverified claims
- if a claim remains uncertain, phrase cautiously or omit the contested detail
- focus on confirmed institutional impact, not gossip

If a viral claim is unverified but socially salient, the read-aloud script
should frame only what is confirmed or omit the contested detail.

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

## Importance-First, Not Forced Variety

The daily brief should select the most important public news in each run.

Do not avoid a topic merely because it appeared yesterday.

If the topic is still one of the most important public news items today, it is
acceptable and correct to include it again.

Do not repeat yesterday's explanation mechanically.

When a continuing story remains important, explain at least one of:

- what is newly confirmed today
- what is newly uncertain today
- what decision, negotiation, number, deadline, or reaction moved today
- why it still deserves a main slot today

The goal is not forced variety.

The goal is correct editorial priority.

Do not replace an important continuing story with a weaker story just to create
variety.

Do not over-prioritize novelty. A new but minor story should not displace a
continuing story that remains more important.

## Recurring Stories And Anti-Staleness

A topic may appear as a main story on consecutive days if it remains one of the
most important news items today.

This is allowed for:

- major political stories
- judicial and legal reform
- international crises
- economic and market-moving events
- disaster and accident follow-up
- public-health and infection stories
- social-risk and trust-related stories
- major corporate or technology stories with public impact

For a recurring story to remain in a main section, the script must show at
least one of:

- a new decision
- a new negotiation step
- a new deadline
- a new official position
- a new confirmed fact
- a new market or household impact
- a new legal or procedural stage
- a new reaction from key actors
- a meaningful clarification of uncertainty
- a reason why the issue still dominates today's agenda

Do not keep using the same major story as a main story out of habit.

A recurring story is acceptable only if it is still one of the strongest
stories today.

If a recurring story has only weak movement, move it to short secondary
tracking.

If another story has become more important, promote the new story even if the
previous story was important yesterday.

When a recurring story stays in the main lineup, give only the minimum
refresher needed for first-time listeners.

## Flexible Section Rule

The section model is a guide, not a prison.

The system should not mechanically fill categories with weak items.

The five core agenda lanes are:

- `政治・行政・司法`
- `国際・安全保障`
- `経済・家計`
- `社会・暮らし・インフラ`
- `産業・企業・テクノロジー`

The rotating sixth section may be one of:

- `文化・地域`
- `科学`
- `環境・資源`
- `国際協力`
- `メディア・情報空間`

Use the rotating sixth section only when it is meaningful. If the rotating
sixth section is weak, skip it rather than forcing a low-value story.

`政治・行政・司法` is the highest-priority domestic section.

`経済・家計` should be household-oriented, not market-only.

`社会・暮らし・インフラ` is a core section, not an optional bucket.

`産業・企業・テクノロジー` remains important, but it should require
substantive updates.

If `社会・暮らし・インフラ` has multiple genuinely strong stories on the same
day, such as an accident, infectious-disease story, privacy or SNS
information-leak story, or consumer-safety story, it may use 2 main stories.

If `政治・行政・司法` has two genuinely major and distinct stories, it may use
2 main stories, but only if both are main-news level.

If `国際・安全保障` and `国際協力` overlap through the same supply-chain,
energy, or geopolitical crisis, compress one into short secondary tracking.

If a core lane has no main-worthy update, do not fill it with official-release
filler. Use short secondary tracking or omit the weak item.

The final lineup should feel like a serious radio news editor chose it, not
like every category was filled mechanically.

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

Use `最後は...` for the final included main section.

After the main sections, add:

`そのほか、短く確認します。`

End with:

`今日ここだけ覚える`

That closing section must contain exactly 3 short points and then end cleanly.

## Length And Density Targets

The final read-aloud script should target roughly 3,600 to 4,800 Japanese
characters.

Keep it short enough to finish comfortably and dense enough to be useful.

If 7 main stories are selected, shorten each story further rather than
exceeding the listening comfort target.

Each main story should usually stay within 6 to 8 sentences total.

Strict cap: do not exceed 8 sentences for a main story unless absolutely
necessary for accuracy.

After the sentence beginning with `次に見るべき点は`, do not add more
explanation for that story.

Prefer slightly incomplete detail over overpacked density.

The listener should understand the story on first listen without being
overloaded.

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
- it directly affects household burden, wages, employment, rights, safety,
  health, privacy, or daily life
- it represents an actual policy decision, law change, enforcement action,
  court decision, budget change, or regulatory change
- it is strongly connected to a major political, judicial, social,
  public-health, digital-safety, or international issue already in the public
  agenda
- it would plausibly be covered in a mainstream radio or TV flash-news segment
- it has exceptional explanatory value for the user

If none of those conditions is met, move the item to short secondary tracking
or omit it.

### Radio Agenda Alignment

Before finalizing the main stories, ask:

`Would a serious morning radio flash-news program plausibly include this as one of its main items today?`

If the answer is no, the story should usually not be a main story unless it
has exceptional explanatory value for the user.

### Main-Story Strength Test

Each main story must pass at least two of these tests:

- important to many people
- new today or still one of the most important continuing stories today
- changes policy, rights, money, safety, health, privacy, work, or social
  systems
- likely to appear in mainstream news broadcasts
- strongly discussed in public because it affects trust, daily behavior, or
  institutional credibility
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
- whether the story remains one of the most important topics today even if it
  appeared recently
- likelihood of being covered in a serious radio or TV flash-news segment
- domestic relevance for Japan
- effect on daily life, rights, money, work, security, health, safety,
  privacy, trust, or social systems
- political, judicial, institutional, or social weight
- explanatory value
- public salience
- section balance when it does not override importance
- broadcast plausibility
- whether recent coverage makes the story stale or still clearly dominant
- source reliability

Do not over-prioritize novelty.

A new but minor story should not displace a continuing story that remains more
important.

Penalize candidates when:

- they are only `a meeting was held` with little decision or substance
- they are only market noise without broader household or real-economy
  relevance
- they duplicate another story in the same causal chain
- they were already main stories recently and today adds little
- they are official but minor
- they are easy to write about but not actually one of the day's more
  important stories

If there is a meaningful domestic politics, justice, institutional,
public-health, privacy, safety, or trust-related story, it should usually
outrank a minor market-data story, routine statistic, narrow administrative
enforcement story, procedural international agreement, or routine ministry
update.

## Mandatory Candidate Checks

Before final story selection, explicitly check whether there are material
updates in:

- constitutional revision / `憲法改正`
- retrial system / `再審制度`
- major Diet deliberations
- cabinet decisions with broad impact
- party negotiations
- tax, budget, social security
- healthcare, education, labor, childcare, pensions
- major justice or court developments
- criminal justice reform
- scandals or accountability issues with institutional importance
- national security policy decisions
- disaster response
- public health and infectious disease
- travel, quarantine, and international movement risks
- consumer safety
- corporate scandals, misconduct, and privacy incidents
- SNS-origin incidents with institutional impact
- cyber or digital safety
- major international/security developments
- wages, prices, employment, consumption, rates
- important business / technology / industry developments
- culture, regional policy, science, environment, international cooperation,
  or media / information-space issues

Record these checks in the reference daily briefing when they materially affect
selection or omission. Do not leak these checks into the final read-aloud
script.

## Section-Specific Selection Rules

### Politics / Administration / Justice

Prioritize:

- constitutional revision
- retrial system reform
- criminal justice
- major bills
- Diet developments
- cabinet decisions with broad impact
- party negotiations
- tax / budget / social security
- healthcare / education / labor / childcare / pensions
- administrative reform
- court decisions or judicial-system changes
- rights, governance, transparency, accountability
- scandals or accountability issues with institutional importance
- national security policy decisions

Do not let this section be displaced by minor market stories when meaningful
political, administrative, or judicial updates exist.

A narrow administrative enforcement item should not become the main politics
story if a broader political, judicial, or institutional story has meaningful
movement.

### International / Security

Prioritize:

- wars / ceasefires / negotiations
- sanctions
- alliances
- sea lanes
- hostage / evacuation / citizen protection
- major diplomatic talks
- defense and security frameworks
- international legal or institutional changes
- public-health events with cross-border travel, quarantine, or
  international-agency relevance

Do not split one international causal chain into too many separate main
stories.

If a supply-chain, energy, or geopolitical crisis also fits another section,
choose the strongest main angle and compress the weaker overlapping angle into
short secondary tracking.

### Economy / Household

Prioritize:

- wages
- prices
- employment
- consumption
- household burden
- interest rates
- housing / loans
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

### Society / Daily Life / Infrastructure

Prioritize:

- disasters
- healthcare safety
- infectious disease and public health
- education
- cyber incidents or official cyber statistics
- non-cyber information leaks and privacy incidents
- SNS-origin incidents with real-world institutional impact
- public safety
- infrastructure
- transport
- local operational issues
- environment and public health
- consumer safety
- school, hospital, bank, local government, or essential service disruptions
- scams, fraud, and digital-behavior risks that affect ordinary people

Cyber belongs here when strong, but it is not mandatory every day.

Information leaks caused by human behavior, workplace filming, SNS posts, or
misdirected communications may be main-worthy even if they are not
cyberattacks.

On strong days, this section may use more than one main slot when distinct
stories separately affect health, safety, privacy, money, schools, hospitals,
banks, local government, infrastructure, consumer protection, or daily
behavior.

### Industry / Business / Technology

Prioritize:

- earnings with meaningful numbers
- M&A
- factory / capex announcements
- semiconductors / AI with concrete numbers or deals
- supply-chain changes
- energy / infrastructure investment
- policy-linked industrial developments
- major product, safety, or platform changes
- business decisions with employment, investment, consumer, regional, privacy,
  or trust impact
- corporate misconduct or governance issues when they affect customers or
  public trust

Do not promote scheduled events without substantive new information.

Do not use `meeting held` or `forum held` as a main story unless there is a
concrete decision, project, investment, agreement, number, or implementation
step.

### Rotating Sixth Section

Use only when meaningful.

Good candidates:

- culture policy
- regional revitalization
- cultural heritage
- tourism with regional or economic significance
- ODA / international cooperation
- science policy
- environment / resource policy
- media / information-space policy
- misinformation / platform governance / speech regulation

Culture should not be celebrity gossip.

Use the rotating section only when it helps explain society, policy, values,
region, identity, diplomacy, or economic change.

If the rotating sixth section overlaps with an already selected international,
energy, supply-chain, or technology story, compress it or skip it.

## Repetition, Recurring-Story, And Cluster Control

Apply the importance-first recurring-story rule before rejecting a topic as
repetitive.

Do not avoid a topic only because it appeared recently.

Do not reuse the same major story as a main story out of habit.

A recurring story may remain a main story only when it is still one of the
strongest stories today and the script shows fresh movement, fresh uncertainty,
or a clear reason why it still dominates the day's agenda.

If a story remains important but has only weak movement, move it to short
secondary tracking or omit it.

If a stronger new story has emerged, promote the new story even if yesterday's
story was important.

If a topic appeared recently, do not re-explain the same background at full
length. Give only the minimum refresher needed for first-time listeners.

Do not use more than 2 main stories from the same broad causal cluster across
the whole digest.

Examples of one broad causal cluster include:

- Middle East conflict -> sea lanes -> oil -> inflation -> IMF forecast
- AI boom -> semiconductors -> suppliers -> capex
- fiscal strain -> bonds -> budget debate
- cyber incident -> outage -> cyber regulation
- domestic fiscal policy -> market rates -> bond auction
- wages -> price pass-through -> small-business profitability
- SNS incident -> information leak -> corporate apology -> privacy regulation
- critical minerals -> G7 coordination -> ASEAN supply chain -> energy prices

If a third candidate from the same cluster is strong but overlapping, merge it
into the stronger story or move it to short secondary tracking.

## Per-Story Spoken Flow

Within each section, each main story should follow this natural spoken flow:

- headline
- one short natural sentence that tells the listener what kind of news this is
- concrete new fact
- short background or reason why this issue surfaced now
- why it matters
- Japan / daily-life impact
- what to watch next

Per-story rules:

- The title should sound like a real news heading
- The sentence immediately after the title is crucial
- It must tell the listener what kind of story this is
- Never let the listener enter detailed facts without understanding the
  premise
- Explain the concrete fact in 2 to 3 short sentences
- If numbers matter, show the numbers early
- Explain background / reason-for-occurrence in 1 to 2 short sentences when
  needed
- Use at most one short plain comparison or example when helpful
- Explain why it matters in 1 to 2 short sentences
- Explain Japan / daily-life impact briefly and concretely
- End with 1 short sentence about what to watch next
- Each main story should usually stay within 6 to 8 sentences total
- Strict cap: do not exceed 8 sentences unless absolutely necessary for
  accuracy
- After the sentence beginning with `次に見るべき点は`, do not add more
  explanation for that story

Prefer short sentences and one main idea per sentence.

Prefer slightly incomplete detail over overpacked density.

The writing should sound natural by ear and remain calm, plain, and
beginner-friendly.

The final script should sound like a radio flash-news explainer, not a policy
briefing.

## Short Secondary Tracking

After the main sections, add:

`そのほか、短く確認します。`

Use 2 to 4 brief items.

Each item should be one short breath, not merely one grammatical sentence.

Target each secondary item at roughly 60 to 90 Japanese characters.

If an item needs more than that, either promote it to a main story or omit
details.

Use this section for:

- important themes with weak updates
- worthy but non-leading stories
- stories pushed out because of cluster overlap

Keep secondary tracking truly short.

Do not include analysis, teaching comments, listening advice, or
editorial-process notes.

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
- `きょうも分野ごとに要点だけ短く整理します`
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
- for SNS-origin or viral stories, verify with reliable media, official
  statements, company statements, or primary documents before treating them as
  factual
- if a viral claim is unverified but socially salient, frame it cautiously or
  omit the contested detail

## Reference Artifacts

The reference daily briefing may be more structured and source-oriented than
the read-aloud version.

It may use markdown when useful.

It should record:

- the effective coverage window
- the major-news-agenda comparison when it materially affected selection
- why each main section was selected today
- what materially changed inside the coverage window
- the public-agenda and social-salience scan when it affected selection
- recurring-story evaluation when a recent topic was kept, demoted, or
  replaced
- when a continuing story was demoted because there was no material update
- any cluster-overlap judgment
- whether recent coverage was stale or still justified as recurring
- source reliability or uncertainty when that matters
- when a routine official item was demoted because it did not clear the
  newsworthiness-first tests
- the distinction between fact, background, and inference when that matters

The final read-aloud script and Google Doc body should present only the news
itself and should not leak the internal newsroom process.
