# daily-news-briefing

Generate a daily Japanese morning news digest, keep local reference outputs,
and mirror the final daily read-aloud study script into one fixed Google Doc
for NotebookLM.

## Repository layout

- `scripts/sync_google_doc.py`: push a generated Markdown file to Google Docs
- `apps-script/Code.gs`: Apps Script web app that receives the Markdown
- `config/google_doc_sync.json`: fixed Google Doc sync settings
- `docs/news_foundation_2026_ja.*`: foundational learning map for the daily brief
- `docs/daily_briefing_principles.md`: concise operating model for the daily brief
- `docs/automation_prompt_daily_briefing.md`: tracked reference copy of the daily automation prompt
- `docs/google-doc-sync.md`: setup and operation notes
- `output/`: ignored generated briefings

## Daily briefing model

The foundational document is the map. The daily brief is now an ear-first
morning news digest built on top of that map, not a worksheet-like lesson
script. Use
`docs/daily_briefing_principles.md` as the concise source of truth for
newsworthiness-first story selection, coverage windows, repetition control,
structure, and
beginner-friendly writing, and use
`docs/automation_prompt_daily_briefing.md` as the tracked source of truth for
the daily automation prompt.

Keep daily outputs beginner-friendly, plain, calm, headline-first, and easy to
follow by ear. Build the final read-aloud script around the five core sections
defined in `docs/daily_briefing_principles.md` (`政治・行政・司法`,
`国際・安全保障`, `経済・家計`, `社会・暮らし・インフラ`,
`産業・企業・テクノロジー`) and add one rotating sixth section only when
meaningful. The synced read-aloud body should start with a very short greeting,
move directly into the section-based digest, then use `そのほか、短く確認します。`
and `今日ここだけ覚える`, while avoiding noisy markdown symbols for
TTS-friendly reading. Use the two tracked docs above as the source of truth
for structure, prioritization, repetition control, and sync behavior.

## Quick sync check

After generating a Markdown artifact, create a local `.env` from `.env.example`
and validate without updating Google Docs:

```sh
python3 scripts/sync_google_doc.py path/to/generated.md --dry-run
```

For full setup and sync operation, see `docs/google-doc-sync.md`.
