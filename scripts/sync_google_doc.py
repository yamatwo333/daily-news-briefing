#!/usr/bin/env python3
"""Push a generated Markdown file to a fixed Google Doc."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys
import urllib.error
import urllib.request


DEFAULT_TIMEOUT_SECONDS = 30
REPO_ROOT = Path(__file__).resolve().parents[1]
SYNC_CONFIG_PATH = REPO_ROOT / 'config' / 'google_doc_sync.json'
SYNC_CONFIG_KEYS = ('doc_id', 'doc_url', 'web_app_url', 'sync_secret', 'title')


class RecordingRedirectHandler(urllib.request.HTTPRedirectHandler):
    def __init__(self) -> None:
        super().__init__()
        self.redirect_chain: list[dict[str, object]] = []

    def redirect_request(self, req, fp, code, msg, headers, newurl):  # type: ignore[no-untyped-def]
        redirected = super().redirect_request(req, fp, code, msg, headers, newurl)
        if redirected is not None:
            self.redirect_chain.append(
                {
                    'status': code,
                    'from_url': req.full_url,
                    'from_method': req.get_method(),
                    'to_url': newurl,
                    'to_method': redirected.get_method(),
                }
            )
        return redirected


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description='Update the configured Google Doc with a Markdown file.'
    )
    parser.add_argument(
        'markdown_path',
        nargs='?',
        help=(
            'Path to the generated Markdown file. '
            'Defaults to NEWS_ROLLING_MARKDOWN_PATH.'
        ),
    )
    parser.add_argument(
        '--web-app-url',
        help=(
            'Apps Script web app URL. Priority: explicit argument, '
            'then config/google_doc_sync.json, then GOOGLE_DOC_SYNC_WEB_APP_URL.'
        ),
    )
    parser.add_argument(
        '--secret',
        help=(
            'Shared secret for the Apps Script endpoint. Priority: explicit argument, '
            'then config/google_doc_sync.json, then GOOGLE_DOC_SYNC_SECRET.'
        ),
    )
    parser.add_argument(
        '--doc-id',
        help=(
            'Google Doc ID. Priority: explicit argument, then '
            'config/google_doc_sync.json, then GOOGLE_DOC_SYNC_DOC_ID.'
        ),
    )
    parser.add_argument(
        '--doc-url',
        help=(
            'Google Doc URL. Priority: explicit argument, then '
            'config/google_doc_sync.json, then GOOGLE_DOC_SYNC_DOC_URL.'
        ),
    )
    parser.add_argument(
        '--title',
        help=(
            'Google Doc title. Priority: explicit argument, then '
            'config/google_doc_sync.json, then GOOGLE_DOC_SYNC_TITLE.'
        ),
    )
    parser.add_argument(
        '--timeout',
        type=int,
        default=DEFAULT_TIMEOUT_SECONDS,
        help=f'HTTP timeout in seconds. Defaults to {DEFAULT_TIMEOUT_SECONDS}.',
    )
    parser.add_argument(
        '--allow-empty',
        action='store_true',
        help='Allow replacing the Google Doc with empty Markdown.',
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Validate inputs without sending the update request.',
    )
    return parser.parse_args()


def main() -> int:
    load_env_file(REPO_ROOT / '.env')
    sync_config = load_sync_config(SYNC_CONFIG_PATH)
    args = parse_args()
    markdown_path = args.markdown_path or os.environ.get('NEWS_ROLLING_MARKDOWN_PATH')
    sync_settings = {
        'doc_id': resolve_setting(
            args.doc_id,
            sync_config,
            'doc_id',
            'GOOGLE_DOC_SYNC_DOC_ID',
        ),
        'doc_url': resolve_setting(
            args.doc_url,
            sync_config,
            'doc_url',
            'GOOGLE_DOC_SYNC_DOC_URL',
        ),
        'web_app_url': resolve_setting(
            args.web_app_url,
            sync_config,
            'web_app_url',
            'GOOGLE_DOC_SYNC_WEB_APP_URL',
        ),
        'sync_secret': resolve_setting(
            args.secret,
            sync_config,
            'sync_secret',
            'GOOGLE_DOC_SYNC_SECRET',
        ),
        'title': resolve_setting(args.title, sync_config, 'title', 'GOOGLE_DOC_SYNC_TITLE'),
    }

    if not markdown_path:
        print(
            'Missing Markdown path. Pass it as an argument or set NEWS_ROLLING_MARKDOWN_PATH.',
            file=sys.stderr,
        )
        return 2

    source = Path(markdown_path).expanduser()
    if not source.is_absolute() and not args.markdown_path:
        source = REPO_ROOT / source
    if not source.is_file():
        print(f'Markdown file not found: {source}', file=sys.stderr)
        return 2

    markdown = source.read_text(encoding='utf-8')
    if not args.allow_empty and markdown.strip() == '':
        print(f'Refusing to send empty Markdown: {source}', file=sys.stderr)
        return 2

    if not sync_settings['web_app_url']:
        print(
            'Missing web_app_url. Set --web-app-url, config/google_doc_sync.json, '
            'or GOOGLE_DOC_SYNC_WEB_APP_URL.',
            file=sys.stderr,
        )
        return 2
    if not sync_settings['sync_secret']:
        print(
            'Missing sync_secret. Set --secret, config/google_doc_sync.json, '
            'or GOOGLE_DOC_SYNC_SECRET.',
            file=sys.stderr,
        )
        return 2

    payload = {
        'secret': sync_settings['sync_secret'],
        'markdown': markdown,
        'text': markdown,
    }

    if args.dry_run:
        target = format_target(sync_settings)
        if target:
            print(
                f'Validated {source} ({len(markdown)} characters). '
                f'Target: {target}. No request sent.'
            )
        else:
            print(f'Validated {source} ({len(markdown)} characters). No request sent.')
        return 0

    result = post_json(sync_settings['web_app_url'], payload, args.timeout)

    result_document_id = result.get('documentId')
    if (
        sync_settings['doc_id']
        and result_document_id
        and result_document_id != sync_settings['doc_id']
    ):
        print(
            'Warning: Apps Script updated documentId '
            f'{result_document_id}, but config/google_doc_sync.json has doc_id '
            f'{sync_settings["doc_id"]}.',
            file=sys.stderr,
        )

    print(
        'Updated Google Doc '
        f'{result_document_id or sync_settings["doc_id"] or "(unknown id)"} with '
        f'{result.get("characters", len(markdown))} characters at '
        f'{result.get("updatedAt", "(unknown time)")}.'
    )
    return 0


def post_json(url: str, payload: dict[str, object], timeout: int) -> dict[str, object]:
    redirect_handler = RecordingRedirectHandler()
    opener = urllib.request.build_opener(redirect_handler)
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode('utf-8'),
        headers={
            'Content-Type': 'application/json; charset=utf-8',
            'User-Agent': 'daily-news-briefing-doc-sync/1.0',
        },
        method='POST',
    )

    try:
        with opener.open(request, timeout=timeout) as response:
            status = response.getcode()
            raw_body = response.read().decode('utf-8', errors='replace')
    except urllib.error.HTTPError as error:
        raw_body = error.read().decode('utf-8', errors='replace')
        raise RuntimeError(
            format_failure(error.code, redirect_handler.redirect_chain, raw_body)
        ) from error
    except urllib.error.URLError as error:
        raise RuntimeError(
            format_failure(
                None,
                redirect_handler.redirect_chain,
                '',
                f'Could not reach Apps Script web app: {error}',
            )
        ) from error

    try:
        parsed = json.loads(raw_body)
    except json.JSONDecodeError as error:
        raise RuntimeError(
            format_failure(
                status,
                redirect_handler.redirect_chain,
                raw_body,
                'Apps Script returned non-JSON response',
            )
        ) from error

    if not isinstance(parsed, dict):
        raise RuntimeError(
            format_failure(
                status,
                redirect_handler.redirect_chain,
                raw_body,
                'Apps Script returned unexpected JSON',
            )
        )

    if not parsed.get('ok'):
        raise RuntimeError(
            format_failure(
                status,
                redirect_handler.redirect_chain,
                raw_body,
                f'Apps Script reported failure: {parsed.get("error", parsed)}',
            )
        )

    return parsed


def format_failure(
    status: int | None,
    redirect_chain: list[dict[str, object]],
    raw_body: str,
    reason: str | None = None,
) -> str:
    lines = ['Google Doc sync failed.']
    if reason:
        lines.append(f'Reason: {reason}')
    lines.append(f'HTTP status: {status if status is not None else "(no HTTP response)"}')

    if redirect_chain:
        lines.append('Redirect chain:')
        for index, hop in enumerate(redirect_chain, start=1):
            lines.append(
                '  '
                f'{index}. HTTP {hop["status"]}: '
                f'{hop["from_method"]} {hop["from_url"]} -> '
                f'{hop["to_method"]} {hop["to_url"]}'
            )
    else:
        lines.append('Redirect chain: (none)')

    lines.append('Raw response body:')
    lines.append(raw_body if raw_body else '(empty)')
    return '\n'.join(lines)


def load_sync_config(path: Path) -> dict[str, object]:
    if not path.is_file():
        return {}

    try:
        parsed = json.loads(path.read_text(encoding='utf-8'))
    except json.JSONDecodeError as error:
        raise RuntimeError(f'Sync config is not valid JSON: {path}') from error

    if not isinstance(parsed, dict):
        raise RuntimeError(f'Sync config must be a JSON object: {path}')

    for key in SYNC_CONFIG_KEYS:
        value = parsed.get(key)
        if value is not None and not isinstance(value, str):
            raise RuntimeError(f'Sync config key {key} must be a string: {path}')

    return parsed


def resolve_setting(
    explicit_value: str | None,
    sync_config: dict[str, object],
    config_key: str,
    env_key: str,
) -> str | None:
    if explicit_value is not None:
        return explicit_value

    config_value = sync_config.get(config_key)
    if isinstance(config_value, str) and config_value:
        return config_value

    env_value = os.environ.get(env_key)
    if env_value:
        return env_value

    return None


def format_target(sync_settings: dict[str, str | None]) -> str | None:
    title = sync_settings.get('title')
    doc_url = sync_settings.get('doc_url')
    doc_id = sync_settings.get('doc_id')

    if title and doc_url:
        return f'{title} ({doc_url})'
    if doc_url:
        return doc_url
    if title:
        return title
    if doc_id:
        return doc_id
    return None


def load_env_file(path: Path) -> None:
    if not path.is_file():
        return

    for line in path.read_text(encoding='utf-8').splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith('#') or '=' not in stripped:
            continue

        key, value = stripped.split('=', 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except RuntimeError as error:
        print(str(error), file=sys.stderr)
        raise SystemExit(1)
