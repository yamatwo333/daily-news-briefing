You are running inside a dedicated Git repository whose purpose is to generate a
daily Japanese morning news digest, keep local reference outputs, produce a
final read-aloud study script, and overwrite the same fixed Google Document
used as the daily reading URL.

This is a daily automation task.

Primary objective:
Create a daily Japanese morning news digest that works as the user's daily
current-affairs learning brief.
Then overwrite the same fixed Google Document with the final daily read-aloud
script.

Core model:
The foundational learning document is the map.
The daily brief is the daily application layer built on top of that map.

This daily brief is NOT a worksheet-like lesson script.
It is NOT a dense analyst memo.
It is NOT a bare headline roundup.

It is a calm, beginner-friendly morning news digest that is easy to follow by
ear, puts news titles first, explains concrete facts before abstract meaning,
and broadens the user's knowledge across fields over time.

The foundational map still matters.
The brief should help the user place today's events on that map without
re-teaching the whole map every morning.

The final result should feel closer to a good radio or TV news explainer than
to a structured handout.

Internal editorial lens:
The foundational map's big learning questions still matter, but they are now
internal editorial checks.
Use them to guide story selection, ordering, and explanation depth.
Do not turn them into repeated visible classroom-style prompts in the final
script.

Audience assumptions:
- The user is still a beginner
- The user has a foundational document about how politics, economics, society,
  technology, law, history, and world affairs connect
- The user wants news titles first
- The user wants a very short opening
- The user wants faster understanding of what happened
- The user wants concrete explanation before abstract interpretation
- The user wants fewer repeated labels
- The user wants fewer repeated explanation patterns
- The user wants more variety across topics
- The user wants broader coverage across days
- The user wants a TTS-friendly final output
- The user wants a very short ending
- The user wants background or reason-for-occurrence explained clearly when
  needed
- The user does not want repeated mini-headings to become annoying

Therefore:
- Write for a smart beginner
- Assume some basic orientation exists, but do not assume fluency
- Keep the wording plain, calm, and easy to hear
- Avoid jargon unless truly necessary
- If a technical term appears, explain it immediately in simple Japanese
- Prefer headline-first clarity, concrete-before-abstract writing, and natural
  listenability over sophistication
- Keep only the minimum required section labels in the final script
- Avoid extra worksheet-like headings, repeated cue phrases, repeated
  explanation patterns, and near-identical wording across days

Coverage window:
- Time zone: Asia/Tokyo
- Treat this as a morning briefing
- The effective coverage window should normally run from the previous scheduled
  run until now
- Preserve meaningful day-level understanding across that window
- Do not bias story selection toward only the latest few visible hours unless
  the actual news flow really happened only then
- If execution timing is manual or shifted, still select stories to preserve a
  day-level understanding of what changed
- Older developments may appear only if they remain materially important today
- If an older development still matters but has only weak updates in the
  effective coverage window, move it to the short secondary section instead of
  reusing it as a full main story
- Record the effective coverage window in the reference briefing and in the run
  summary

Before selecting stories:
- Review the most recent daily output files if available
- Check recent main stories, especially the last 3 daily runs
- Note recurring topics where background should be compressed today
- Note continuing topics that should probably move to the short secondary
  section unless there is a material update
- Note whether cyber has recently been underused despite meaningful candidates
- Note whether art or culture has been absent for a long stretch despite
  meaningful candidates

Daily story selection framework:
Balance all of these:
- importance
- freshness
- learning value
- Japan relevance
- diversity across fields
- diversity across broad causal clusters
- non-repetition across consecutive days
- non-repetition of yesterday's explanation
- meaningful day-level coverage
- clarity for a beginner listener
- natural listenability by ear

Story count:
- Use 6 main stories by default
- Use 7 only when the extra story is clearly useful for breadth or day-level
  understanding
- Use 5 only on genuinely light days

The daily selection should actively broaden the user's knowledge across fields
over time.

Important topic pools:
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
Do not force a weak story just to fill a bucket.
But do use these pools to preserve breadth over time.

Cyber is not mandatory every day.
Art or culture is not mandatory every day.
But neither category should be systematically overlooked.

Japan domestic rule:
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

Do not let the Japan domestic slot drift too often into only market data unless
market data is truly the strongest Japan domestic development that day.

Business / industry / technology freshness rule:
Do not promote a business or technology story to the main lineup only because:
- a scheduled date arrived
- an event is expected later
- a company may announce something later

Require substantive new information such as:
- released earnings
- guidance changes
- official investment decisions
- production, demand, or supply changes
- signed agreements
- policy-linked industrial developments
- materially new results or documents

Weak-update business stories should be pushed out of the main lineup and moved
to the short secondary section or excluded.

Cyber rule:
Cyber security, ransomware, breaches, and infrastructure cyber risk are real
candidate categories for the main lineup.

Do not systematically overlook them.

Raise cyber priority when there is:
- official disclosure
- infrastructure disruption
- government, regulatory, or policy response
- operational interruption
- geopolitical linkage

Do not force cyber every day.

Art / culture rule:
Art and culture remain valid main-story categories when they help explain
society, values, policy, diplomacy, identity, or structural change.

Do not use celebrity gossip or low-value entertainment updates.

Examples that may qualify:
- cultural policy
- heritage and preservation with public significance
- censorship or free-expression issues
- arts institutions and funding
- content industries with structural relevance
- international cultural diplomacy
- major cultural developments that illuminate broader social change

Do not force culture every day.
But do not let it disappear for long stretches if meaningful candidates exist.

Cluster diversity rule:
- Avoid overloading the main lineup with too many stories from the same broad
  causal cluster
- Prefer not to use more than 2 main stories from the same broad cluster
- Additional stories from that cluster should usually move to the short
  secondary section
- A broad cluster can be a shared war, crisis, election, market shock,
  regulatory conflict, cyber campaign, supply-chain disruption, or social
  controversy

Anti-repetition rule:
- The same major story should not be reused as a main story on consecutive days
  unless there is clearly meaningful new information
- Treat "still important" and "new today" as separate tests
- If updates are weak, move the story to the short secondary section instead of
  reusing it as a full main story

Meaningful update criteria:
A story may return as a main story only if there is substance such as:
- a new official statement
- a newly disclosed number, forecast, or document
- a meaningful policy, legal, or negotiation step
- movement into a new phase
- a meaningful Japan-side response
- infrastructure disruption or operational change
- a security consequence
- a materially different interpretation today because facts changed

Explanation repetition suppression:
- Even if a topic reappears, do not re-explain the same background at full
  length
- Do not reuse near-identical wording across consecutive days
- Compress recurring background sharply
- Focus on what changed today
- Keep any refresher background to one short sentence at most
- The intended feeling is: 「今日、何が変わったかが分かった」
- The user should not feel: 「昨日の説明をまた聞いた」
- If a topic appeared as a main story within the last 3 daily runs, background
  should usually be limited to a very short refresher unless the story has
  moved into a clearly new phase

What changed today requirement:
- Every main story must clearly show what changed within the effective coverage
  window
- If the main value of a candidate is unchanged background, it does not belong
  as a full main story today

Short secondary section rule:
- Use the short secondary section for important follow-up items that still
  matter but do not justify full treatment today
- Use it when a continuing story has weak updates
- Use it when a candidate loses the freshness test
- Use it when cluster diversity requires demotion
- Keep these items concise and focused on what is being watched next

Headline-first and concrete-before-abstract requirement:
- Main stories must present a clear news title first
- The title should help the user understand what the story is immediately
- Each story should explain what happened today before moving into more
  abstract meaning
- If numbers matter, place the numbers early
- If the story is hard to picture, one short plain example or comparison may be
  used only when it truly helps
- Explain why the story surfaced when that background is needed
- Simplify abstract policy language into plain meaning whenever possible

Ear-first writing requirement:
- The script should sound natural by ear
- It should feel closer to a good radio or TV news explainer than to a written
  report
- Prefer short sentences
- One sentence should mainly carry one idea
- The wording should help the listener picture the situation first, then
  understand the meaning
- Minimize rigid repeated labels and repeated explanation patterns
- Do not add extra worksheet-like headings or classroom prompts beyond the
  required structure
- Vary sentence openings and transitions across stories

Scope and sources:
- Prefer primary or official sources whenever reasonably available
- Use major outlets such as NHK, Reuters, AP, Nikkei, and similar sources for
  verification and context
- If a primary source is missing, say so briefly
- Distinguish fact, background, and inference
- Mark uncertainty clearly

Google Docs integration:
- Reuse the existing repository integration for the fixed Google Document
- Look for tracked config and sync files first
- Prefer repository files such as config/google_doc_sync.json,
  scripts/sync_google_doc.py, README, docs, AGENTS.md, or similar tracked
  sources
- Treat tracked config as the source of truth
- After generating the final daily study script, overwrite the same fixed
  Google Document with that final study script
- Do not write the weekly rolling reference file into the Google Document
- Keep the same fixed Google Document URL
- Do not modify config/google_doc_sync.json unless a sync change is explicitly
  required
- Do not modify scripts/sync_google_doc.py unless a sync bug fix is explicitly
  required

Required output files:
1. Reference daily briefing
   output/daily/YYYY/YYYY-MM/YYYY-MM-DD_morning_brief_ja.md
2. Source log CSV
   output/daily/YYYY/YYYY-MM/YYYY-MM-DD_sources.csv
3. Manifest JSON
   output/daily/YYYY/YYYY-MM/YYYY-MM-DD_manifest.json
4. Weekly rolling reference file
   output/weekly/YYYY/YYYY-Www_notebooklm_feed_ja.md
5. Final study script
   output/daily/YYYY/YYYY-MM/YYYY-MM-DD_read_aloud_ja.md

Reference daily briefing requirements:
- This is the repository reference artifact
- It may be more structured and source-oriented than the final read-aloud
  version
- It may use markdown when useful
- It should record the effective coverage window
- It should record why each main story was selected today
- It should explicitly note what changed inside the effective coverage window
- It should note when a continuing story was demoted to the short secondary
  section because there was no material update
- It should note when a recurring topic received compressed background because
  it appeared recently
- It should note any cluster-overlap judgment that moved a candidate out of the
  main lineup
- It should note whether cyber was included or meaningfully considered
- It should note whether art or culture was included, considered, or absent
  despite meaningful candidates

Final daily study script requirements:
This is the most important artifact.
This is the version that must be written into the fixed Google Document.

Audience:
- Intelligent beginner
- Has a basic foundational map now
- Still needs gentle explanation
- Wants to understand what changed today
- Wants to hear clear headlines first

Tone:
- calm
- direct
- explanatory
- plain
- non-sensational
- beginner-friendly
- easy to listen to

Hard constraints:
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

Length target:
- Roughly 3,500 to 5,500 Japanese characters
- Keep it short enough to finish comfortably
- Keep it long enough to make the news meaningful
- If needed, reduce weak stories instead of bloating the script

TTS and formatting rule:
- The final read_aloud_ja.md file must be TTS-friendly plain text even though
  the file extension is .md
- The Google Document body must use the same TTS-friendly plain text
- Do not use markdown heading markers such as #, ##, or ###
- Do not use markdown bullet markers such as -, *, or numbered markdown lists
- Do not use backticks
- Use plain Japanese section labels suitable for text-to-speech
- Keep punctuation natural and not overly noisy

Final content structure:
Use this structure in the final read-aloud script.
Do not add extra sections.

Title
- Use a plain title line such as:
  YYYY年M月D日 朝のデイリーブリーフ

Short opening
- Keep it to 1 to 2 very short sentences
- Make it calm and direct
- Do not turn it into a lesson, essay, or long preview

今日の主要ニュース
- Keep this section very short
- Use it to orient the listener quickly
- Do not over-explain

本編
- Use 6 stories by default
- Use 7 only when clearly useful
- Use 5 only on genuinely light days

For each main story, use plain story-order labels such as:
一つ目
二つ目
三つ目
四つ目
五つ目
六つ目
七つ目

After the story-order label, write the story in a natural spoken flow:
- title
- one very short plain summary sentence
- concrete fact
- brief background or reason-for-occurrence when needed
- why it matters
- Japan or daily-life impact
- what to watch next

This flow should sound natural by ear, not like a checklist.

Do not use repeated mini-headings such as:
ニュースタイトル
一言でいうと
何が起きたか
なんでこの話が出てきたのか
なぜ重要か
日本への影響
次の焦点

短く追うニュース
- Use this section for important follow-up items that still matter but do not
  justify full main-story treatment today
- Keep items short and plain
- Focus on what is being watched and what would make the item rise again

今日ここだけ覚える
- End with exactly 3 short plain Japanese points
- Keep each point brief and memorable
- This is the ending, so keep it very short
- Do not add a long lesson, essay, or extra concluding section after it

Per-story writing rules:
- Start with the headline clearly
- Give fast understanding of what happened
- Say what happened before abstract interpretation
- If numbers matter, put the numbers early
- Explain in simple Japanese
- Make the day's delta clear
- Give enough explanation for meaning, but do not re-teach old background at
  full length
- If a key term appears, explain it immediately and briefly inside the prose
- If the story is hard to picture, one short plain example or comparison may be
  used only when it truly helps
- Keep paragraphs short
- One sentence should mainly carry one idea
- Do not repeat yesterday's explanation unless it is necessary for today's
  understanding
- Avoid near-identical wording from recent briefs
- Compress refresher background to one short sentence at most
- Focus on what changed today
- Explain background or reason-for-occurrence clearly when needed
- Simplify abstract policy language into plain meaning whenever possible

Quality bar before finishing:
- The script must be understandable to a beginner
- It must sound like a morning digest, not a repetitive worksheet
- It must feel broader and fresher than a structured explainer document
- It must give headline-first clarity
- It must provide enough explanation to make the news meaningful
- It must not feel like a dense analyst memo
- It must not over-repeat yesterday's background
- It must keep refresher background to one short sentence when the topic is
  recurring
- It must include a true Japan domestic policy / institution / social-system
  story when reasonably available
- It must treat cyber as a real candidate category when strong stories exist
- It may use art / culture when the story reveals broader social meaning
- It must not let art / culture disappear silently for long stretches if
  meaningful candidates exist
- It must avoid overloading the lineup with the same broad cluster
- Weak-update business stories must be demoted or excluded
- The short secondary section must absorb important but weak-update follow-ups
- The opening section must stay short
- 今日の主要ニュース must stay short
- 今日ここだけ覚える must contain exactly 3 short points
- The final read_aloud_ja.md and Google Document body must avoid noisy markdown
  syntax
- The fixed Google Document must be updated successfully

At the end of the run, print a concise markdown summary with:
- files created or updated
- story count
- top stories included
- short secondary items included
- any repeated main story and the material update that justified repeating it
- any topic from the last 3 days where the explanation was intentionally
  compressed
- any cluster-overlap judgment that demoted or excluded a candidate
- whether cyber was included or meaningfully considered
- whether art / culture was included, considered, or absent despite meaningful
  candidates
- effective coverage window
- whether the fixed Google Document was updated
- the fixed Google Document title and URL if available
- any missing primary sources
- any uncertainties or blocked items
