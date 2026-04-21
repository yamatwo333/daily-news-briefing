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

Keep daily outputs beginner-friendly, plain, calm, and headline-first. Use 6
stories by default, 7 only when clearly useful, and 5 on genuinely light days.
Every main story should begin with a clear title, explain what changed today,
and preserve breadth across fields including cyber and culture when warranted.
Major continuing themes without meaningful updates belong in `短く追うニュース`
instead of being repeated as full stories, and recurring topics should sharply
compress repeated background. The final read-aloud script mirrored to Google
Docs should avoid noisy markdown symbols for TTS-friendly reading.

## Quick sync check

After generating a Markdown artifact, create a local `.env` from `.env.example`
and validate without updating Google Docs:

```sh
python3 scripts/sync_google_doc.py path/to/generated.md --dry-run
```

For full setup and sync operation, see `docs/google-doc-sync.md`.
