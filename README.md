# daily-news-briefing

Generate a daily Japanese news learning brief, keep local reference outputs, and
mirror the final daily study script into one fixed Google Doc for NotebookLM.

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

The foundational document is the map. The daily brief is a guided daily practice
layer that applies that map to current events. Use
`docs/daily_briefing_principles.md` as the concise source of truth for story
selection, coverage windows, repetition control, and beginner-friendly writing.

Keep daily outputs beginner-friendly, plain, calm, and focused on 5 stories by
default. Use 6 only when one extra story is clearly useful, and 4 only on
genuinely light days. Every main story should explain what changed today; major
continuing themes without meaningful updates belong in `継続監視` instead of
being repeated as full stories. Recurring topics should not repeat yesterday’s
full background explanation unless there is a major phase change.

## Quick sync check

After generating a Markdown artifact, create a local `.env` from `.env.example`
and validate without updating Google Docs:

```sh
python3 scripts/sync_google_doc.py path/to/generated.md --dry-run
```

For full setup and sync operation, see `docs/google-doc-sync.md`.
