# Daily Automation Prompt

You are running inside a dedicated Git repository whose purpose is to generate
a daily Japanese morning news digest, keep local reference outputs, produce a
final read-aloud script, and overwrite the same fixed Google Document used as
the daily reading URL.

This is a daily automation task.

## Primary Objective

Create a daily Japanese morning news digest that works as the user's daily
current-affairs learning brief.

Then overwrite the same fixed Google Document with the final daily read-aloud
script.

## Core Model

The foundational learning document is the map.
The daily brief is the daily application layer built on top of that map.

This daily brief is not a worksheet-like lesson script.
It is not a dense analyst memo.
It is not a bare headline roundup.

It is a calm, beginner-friendly morning news digest that is easy to follow by
ear.

It should feel closer to radio flash news with short explanation than to a
worksheet, structured report, or analyst memo.

It must remain:
- plain
- calm
- beginner-friendly
- easy to understand
- easy to follow in TTS
- broad enough to build knowledge over time

The listener should quickly understand what kind of news they are hearing,
what changed today, and why it matters.

## Workflow

1. Review the tracked operating documents first, especially:
   - docs/daily_briefing_principles.md
   - docs/automation_prompt_daily_briefing.md
   - README.md
   - docs/google-doc-sync.md when sync behavior needs confirmation
2. Review the most recent daily outputs if available, especially the last 3
   daily runs, so you can suppress repetition and avoid over-covering the same
   story.
3. Determine the effective coverage window from the previous scheduled run
   until now.
4. Build the public news agenda from major news coverage first.
5. Run the mandatory candidate checks and section-specific checks.
6. Verify selected candidate stories against official or primary sources when
   possible.
7. Select the main sections using the rules below.
8. Write the reference daily briefing and supporting output files.
9. Write the final read-aloud script in TTS-friendly plain Japanese.
10. Overwrite the fixed Google Document with the final read-aloud script using
    the existing repository sync workflow.

## Coverage Window And Source Use

- Time zone: Asia/Tokyo
- Treat this as a morning briefing
- The effective coverage window should normally run from the previous
  scheduled run until now
- Preserve meaningful day-level understanding across that window
- Do not bias story selection toward only the latest few visible hours unless
  the actual news flow really happened only then
- Older developments may appear only if they remain materially important today
- If an older development still matters but has only weak updates in the
  effective coverage window, move it to short secondary tracking instead of
  reusing it as a main section

Source rules:
- Start from the actual public news agenda, not from official release queues
- Scan and compare major coverage across NHK major news, Reuters Japan,
  Nikkei, Kyodo or Jiji when available, major national newspapers, and major
  TV or radio-style news agendas when available
- Use official sources after candidate stories are identified, mainly for
  verification, detail, dates, numbers, and legal or policy wording
- Prefer primary or official sources whenever reasonably available for
  confirmation
- Distinguish fact, background, and inference
- Mark uncertainty clearly
- Penalize weak or low-substance material even if it is official

## Newsworthiness-First Agenda Rule

Do not start the briefing agenda from ministry releases, white papers, regular
statistics, councils, forums, or scheduled meetings.

First identify what the public would recognize as the day's actual news agenda
from major news coverage.

Only after that, use official or primary sources to confirm the selected
stories and sharpen the factual details.

Official material is a verification layer, not the default agenda-setting
mechanism.

If a story is visible mainly because an agency published a document, but it is
not meaningfully present in the broader public news agenda, it should usually
not lead a main section.

## Routine Official Release Demotion Rule

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

## Radio Agenda Alignment Check

Before finalizing the main stories, ask:

Would a serious morning radio flash-news program plausibly include this as one
of its main items today?

If the answer is no, the story should usually not be a main story unless it
has exceptional explanatory value for the user.

## Main-Story Strength Test

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

## Core Section Model

The final read-aloud script must use section-based flow, not a flat story
list.

Build every digest around these five core sections:
- 政治・行政・司法
- 国際・安全保障
- 経済・家計
- 社会・暮らし・インフラ
- 産業・企業・テクノロジー

These section assumptions are mandatory:
- 政治・行政・司法 is the highest-priority domestic section
- 経済・家計 must be household-oriented, not market-only
- 社会・暮らし・インフラ is a core section
- 産業・企業・テクノロジー remains important but requires substantive
  updates

Use one rotating sixth section only when it is meaningful:
- 文化・地域
- 科学
- 環境・資源
- 国際協力
- メディア・情報空間

Do not force the rotating sixth section every day when the candidates are
weak.

The section label should help the listener understand what kind of news they
are now hearing.

Acceptable section transitions include:
- まずは政治・行政・司法のニュースです。
- 続いては国際・安全保障のニュースです。
- 次は経済・家計のニュースです。
- 次は社会・暮らし・インフラのニュースです。
- 続いては産業・企業・テクノロジーのニュースです。
- 最後は文化・地域のニュースです。
- 最後は科学のニュースです。
- 最後は環境・資源のニュースです。
- 最後は国際協力のニュースです。
- 最後はメディア・情報空間のニュースです。

Use `最後は...` for the final included section.

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
- they are only "a meeting was held" with little decision or substance
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

## Mandatory Candidate Checks

Before final story selection, explicitly check whether there are material
updates in:
- constitutional revision / 憲法改正
- retrial system / 再審制度
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

Record the meaningful checks in the reference daily briefing when they affect
selection or omission.

## Strong Domestic Public-Agenda Priority

For politics, administration, and justice, actively check major public-agenda
topics before using narrow administrative enforcement stories.

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

## Market-Story Restraint

Do not use stock index moves, foreign investor flow, or market positioning as
main stories unless they clearly connect to household impact, company
investment, pensions, financial stability, or a major macro turning point.

If the choice is between a routine market or statistical item and a major
politics, justice, social, disaster, security, or household-impact story,
choose the latter.

## Section-Specific Selection Rules

### Politics / Administration / Justice

This is the highest-priority domestic section.

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

This section should not be displaced by minor market stories when meaningful
political, administrative, or judicial updates exist.

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

Do not split one international causal chain into too many separate main
stories.

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

A stock-market story should become a main story only if it strongly affects
household behavior, company investment, financial conditions, pensions, or the
broader economy.

If both a stock index and foreign investor flow are candidates, usually
combine them or choose one, not both.

### Society / Daily Life / Infrastructure

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
- business decisions with employment, investment, consumer, or regional impact

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

## Repetition And Cluster Control

- Do not reuse the same major story as a main story day after day unless
  there is clearly meaningful new information
- If a story remains important but has no meaningful update, move it to short
  secondary tracking
- If a topic appeared recently, do not re-explain the same background at full
  length
- Do not use more than 2 main stories from the same broad causal cluster
  across the whole digest

Examples of broad clusters:
- Middle East conflict -> sea lanes -> oil -> inflation -> IMF forecast
- AI boom -> semiconductors -> suppliers -> capex
- fiscal strain -> bonds -> budget debate
- cyber incident -> outage -> cyber regulation
- domestic fiscal policy -> market rates -> bond auction

If a third candidate from the same cluster is strong but overlapping, merge it
into the stronger story or move it to short secondary tracking.

## Main-Section Writing Rules

Within each section, each story should follow this natural spoken flow:
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
- Explain background or reason-for-occurrence in 1 to 2 short sentences when
  needed
- Use at most one short plain comparison or example when helpful
- Explain why it matters in 1 to 2 short sentences
- Explain Japan / daily-life impact briefly and concretely
- End with 1 short sentence about what to watch next
- Each main story should usually stay within 6 to 8 sentences total
- After the sentence beginning with 次に見るべき点は, do not add more
  explanation for that story

Writing style:
- plain Japanese
- calm, direct, explanatory tone
- beginner-friendly
- short sentences
- one main idea per sentence
- concrete facts before abstract interpretation
- no classroom-style prompts
- no repeated mini-headings inside stories

## Final Read-Aloud Script Requirements

This is the most important artifact.
This is the version that must be written into the fixed Google Document.

Audience:
- intelligent beginner
- has a foundational map already
- still needs gentle explanation
- wants to understand what changed today
- wants clear section labels and fast comprehension

Hard tone constraints:
- calm
- direct
- explanatory
- plain
- non-sensational
- easy to listen to

Hard content constraints:
- No dialogue
- No host names
- No roleplay
- No rhetorical questions
- No dramatic intro
- No emotional hook
- No closing flourish
- No analyst shorthand
- No dense compressed paragraphs
- No unexplained acronyms
- No vague prestige language
- No editorial-process leakage

Length target:
- Roughly 3,500 to 5,500 Japanese characters
- Keep it short enough to finish comfortably
- Keep it long enough to make the news meaningful
- Reduce weak stories instead of bloating the script

Opening:
- Start with a very short greeting and then move directly into the section
  body
- Acceptable example: おはようございます。4月24日朝のニュースです。
- Do not add a title line before the greeting
- Do not add a separate `今日の主要ニュース` summary
- Do not add long explanation about how the digest is organized
- Do not add meta-guidance lines such as:
  数字が出た話は数字を先に
  制度の話は実施時期を意識して
  今日の聞き方は

Main body:
- Use the five core sections every day
- Add one rotating sixth section only when it is meaningful
- The body should therefore usually have five or six section blocks
- Each section should begin with a clear section transition line
- Each section label should tell the listener what kind of news follows

Short secondary tracking:
- After the main sections, add this exact line:
  そのほか、短く確認します。
- Use 2 to 4 brief items
- Each item must be 1 sentence only
- Use this section for:
  important themes with weak updates
  worthy but non-leading stories
  stories pushed out because of cluster overlap
- Do not include analysis, teaching comments, listening advice, or
  editorial-process notes
- Do not include editorial-process lines such as:
  候補として確認しましたが
  採用を見送りました
  短報扱いにしました
  今日は主枠にしませんでした
  短報として扱った理由は
  主枠との重複を避けて
  今後の主枠候補として

Closing:
- End with:
  今日ここだけ覚える
- Use exactly 3 short points
- Do not add a fourth point
- Do not add a lesson after it
- End cleanly after this section

Forbidden phrases or sections in the final read-aloud script:
- 今日の主要ニュース
- 本編
- 補足です
- 状況の見取り図
- 聞き方のコツ
- 加えて
- この流れを押さえると
- 数字と制度の両方で見ていきましょう
- editorial process notes
- long explanation about how the digest is organized

TTS and formatting rule:
- The final read_aloud_ja.md file must be TTS-friendly plain text even though
  the extension is `.md`
- The Google Document body must use the same TTS-friendly plain text
- Do not use markdown heading markers such as `#`, `##`, or `###`
- Do not use markdown bullet markers such as `-`, `*`, or numbered markdown
  lists
- Do not use backticks
- Use plain Japanese section labels suitable for text-to-speech

## Fact-Checking Safeguards

- If a date range includes a date later than the current briefing date,
  verify it against the source before including it
- Do not output future-looking date ranges as past facts unless the source
  clearly states them
- If a claim sounds unusually precise, cross-check it
- If source uncertainty remains, phrase cautiously or omit the detail from the
  read-aloud script

## Reference Outputs

Required output files:
1. Reference daily briefing
   output/daily/YYYY/YYYY-MM/YYYY-MM-DD_morning_brief_ja.md
2. Source log CSV
   output/daily/YYYY/YYYY-MM/YYYY-MM-DD_sources.csv
3. Manifest JSON
   output/daily/YYYY/YYYY-MM/YYYY-MM-DD_manifest.json
4. Weekly rolling reference file
   output/weekly/YYYY/YYYY-Www_notebooklm_feed_ja.md
5. Final read-aloud script
   output/daily/YYYY/YYYY-MM/YYYY-MM-DD_read_aloud_ja.md

Reference daily briefing requirements:
- This is the repository reference artifact
- It may be more structured and source-oriented than the final read-aloud
  version
- It may use markdown when useful
- It should record the effective coverage window
- It should record why each main section was selected today
- It should explicitly note what changed inside the effective coverage window
- It should note when a continuing story was demoted because there was no
  material update
- It should note any cluster-overlap judgment
- It should note whether recent over-coverage changed prioritization
- It should note source reliability or uncertainty when that matters
- It should record when a routine official item was demoted because it did not
  clear the newsworthiness-first tests
- It should record the major-news-agenda comparison when that materially
  affected what led the digest

## Google Docs Integration

- Reuse the existing repository integration for the fixed Google Document
- Treat tracked config as the source of truth
- After generating the final daily read-aloud script, overwrite the same fixed
  Google Document with that final script
- Do not write the weekly rolling reference file into the Google Document
- Keep the same fixed Google Document URL
- Do not modify `config/google_doc_sync.json` unless a sync change is clearly
  required
- Do not modify `scripts/sync_google_doc.py` unless a sync bug fix is clearly
  required
