# Google Docs sync

The local script sends a generated Markdown file to a Google Apps Script web app,
and the web app replaces the body of one fixed Google Doc.

For the daily briefing workflow, sync the final daily study script
(`output/daily/YYYY/YYYY-MM/YYYY-MM-DD_read_aloud_ja.md`) to Google Docs. Keep
the weekly rolling file as a local reference artifact, not the Google Doc body.

## Recommended ownership

- Own the Google Doc and Apps Script project with `yamato.masunaka@gmail.com`.
- Share the Google Doc with `yamato.masunaka@appirits.com` as a viewer.
- In NotebookLM, add that shared Google Doc from Drive using `yamato.masunaka@appirits.com`.

NotebookLM imports a Drive source as a copy, so after each document update you
still need to sync the source inside NotebookLM.

## Apps Script setup

1. Create one Google Doc in the `yamato.masunaka@gmail.com` account.
2. Copy the document ID from its URL.
3. Open Apps Script with the same `yamato.masunaka@gmail.com` account.
4. Paste `apps-script/Code.gs` into the script project.
5. Add script properties:
   - `DOC_ID`: the fixed Google Doc ID
   - `SYNC_SECRET`: a long random shared secret
   - `ALLOW_EMPTY`: optional; set to `true` only if empty document updates are intentional
6. Deploy as a web app:
   - Execute as: me
   - Who has access: anyone with the link
7. Copy the `/exec` web app URL.

## Configuration

`config/google_doc_sync.json` is the tracked source for the current fixed Google
Doc sync settings:

- `title`
- `doc_id`
- `doc_url`
- `web_app_url`
- `sync_secret`

Do not change this file unless the fixed Google Doc target or Apps Script
deployment changes. If this repository is ever moved to a broader audience,
rotate the secret and move private sync values into `.env`.

For fixed document metadata, the sync script resolves values in this order:

1. `config/google_doc_sync.json`, if the key exists
2. `.env`

For `web_app_url` and `sync_secret`, explicit command-line arguments still
override tracked config when needed.

## Local setup

Create a local `.env` file for generated Markdown path and secret sync values:

```sh
NEWS_ROLLING_MARKDOWN_PATH=output/daily/YYYY/YYYY-MM/YYYY-MM-DD_read_aloud_ja.md
GOOGLE_DOC_SYNC_WEB_APP_URL=https://script.google.com/macros/s/REPLACE_WITH_DEPLOYMENT_ID/exec
GOOGLE_DOC_SYNC_SECRET=replace-with-a-long-random-secret
```

Do not commit `.env`.

## Run

```sh
python3 scripts/sync_google_doc.py "$NEWS_ROLLING_MARKDOWN_PATH"
```

You can pass the Markdown path directly instead:

```sh
python3 scripts/sync_google_doc.py output/daily/YYYY/YYYY-MM/YYYY-MM-DD_read_aloud_ja.md
```

Validate local inputs without updating Google Docs:

```sh
python3 scripts/sync_google_doc.py output/daily/YYYY/YYYY-MM/YYYY-MM-DD_read_aloud_ja.md --dry-run
```

## Automation placement

Run the sync script after generating the final daily study script. Keep generated
Markdown as the local artifact, and treat Google Docs as the NotebookLM-facing
mirror.
