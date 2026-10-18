"""Validate one public news request, synthesize it locally, and build a Pages site.

No model API, Google Doc credential, repository configuration, or remote source
article is read by this program. News research and writing happen in ChatGPT.
"""
import argparse
from datetime import datetime, timedelta, timezone
import hashlib
import html
import io
import json
from pathlib import Path
import re
import shutil
import subprocess
import time
import urllib.parse
import urllib.request
import wave

VOICE = "VOICEVOX:玄野武宏"
SPEAKER_UUID = "c30dc15a-0992-4f8d-8bb8-ad3b314e6a6f"
ENGINE_VERSION = "0.25.2"
SETTINGS = dict(speedScale=1.3, intonationScale=0.8, pauseLengthScale=0.9,
                volumeScale=1.0, prePhonemeLength=0.1,
                postPhonemeLength=0.12, outputStereo=False)


def timestamp(value):
    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        raise ValueError("日時にはタイムゾーンが必要です")
    return dt


def validate(data, now=None):
    now = now or datetime.now(timezone.utc)
    if data.get("schema_version") != 1:
        raise ValueError("未対応のschema_version")
    if not re.fullmatch(r"test-[0-9]{8}T[0-9]{6}Z", data.get("id", "")):
        raise ValueError("不正なテストID")
    cutoff, written = timestamp(data["cutoff_at"]), timestamp(data["written_at"])
    if not now - timedelta(hours=48) <= cutoff <= written <= now + timedelta(minutes=5):
        raise ValueError("原稿が古いか、未来の日時です")
    if written - cutoff > timedelta(hours=6):
        raise ValueError("確認から執筆までの間隔が長すぎます")
    text = data["manuscript"]
    if not isinstance(text, str) or not 100 <= len(text) <= 9000:
        raise ValueError("原稿の長さは100〜9000文字です")
    if re.search(r"https?://|<script|sync_secret|sk-proj-", text, re.I):
        raise ValueError("読み上げ本文にURL・秘密値・スクリプトは使えません")
    sources = data["sources"]
    if not isinstance(sources, list) or not 1 <= len(sources) <= 60:
        raise ValueError("出典が必要です")
    for source in sources:
        url = urllib.parse.urlsplit(source["url"])
        if url.scheme != "https" or not url.hostname or url.username or url.password:
            raise ValueError("出典は認証情報を含まないHTTPS URLにしてください")
        if not isinstance(source.get("title"), str) or not 1 <= len(source["title"]) <= 300:
            raise ValueError("出典の表題が必要です")
    chunks = [(sentence + "。", i)
              for i, paragraph in enumerate(text.strip().split("\n\n"))
              for sentence in paragraph.split("。") if sentence.strip()]
    if not chunks or any(len(text) > 800 for text, _ in chunks):
        raise ValueError("1文が長すぎます")
    return chunks


def request(base, path, params=None, body=None, method="GET"):
    url = base + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    payload = None if body is None else json.dumps(body, ensure_ascii=False).encode()
    req = urllib.request.Request(url, data=payload, method=method,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=180) as response:
        return response.read()


def check_engine(base):
    if json.loads(request(base, "/version")) != ENGINE_VERSION:
        raise ValueError("VOICEVOXエンジンの版が試聴時と異なります")
    speakers = json.loads(request(base, "/speakers"))
    if not any(s.get("speaker_uuid") == SPEAKER_UUID and
               any(style.get("id") == 11 and style.get("name") == "ノーマル"
                   for style in s.get("styles", [])) for s in speakers):
        raise ValueError("玄野武宏のノーマル音声を確認できません")


def measurements(stderr):
    return json.loads(re.findall(r'\{\s*"input_i".*?\}', stderr, re.S)[-1])


def synthesize(chunks, base, directory):
    check_engine(base)
    start, parts, dimensions = time.monotonic(), [], None
    for n, (text, paragraph) in enumerate(chunks):
        query = json.loads(request(base, "/audio_query", {"text": text, "speaker": 11}, method="POST"))
        query.update(SETTINGS)
        content = request(base, "/synthesis", {"speaker": 11}, query, "POST")
        with wave.open(io.BytesIO(content), "rb") as wav:
            actual = wav.getnchannels(), wav.getsampwidth(), wav.getframerate()
            if dimensions is not None and actual != dimensions:
                raise ValueError("音声形式が途中で変化しました")
            dimensions = actual
            parts.append(wav.readframes(wav.getnframes()))
        if n + 1 < len(chunks):
            pause = 0.45 if paragraph != chunks[n + 1][1] else 0.08
            channels, width, rate = dimensions
            parts.append(b"\0" * round(rate * pause) * channels * width)
        print(f"音声合成 {n + 1}/{len(chunks)}", flush=True)
    channels, width, rate = dimensions
    pcm = b"".join(parts)
    seconds = len(pcm) / (channels * width * rate)
    if not 1 <= seconds <= 1800:
        raise ValueError("音声の長さが想定範囲外です")
    raw = directory / "raw.wav"
    with wave.open(str(raw), "wb") as wav:
        wav.setparams((channels, width, rate, 0, "NONE", "not compressed"))
        wav.writeframes(pcm)
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        raise RuntimeError("ffmpegがありません")
    command = [ffmpeg, "-hide_banner", "-nostdin"]
    first = subprocess.run(command + ["-i", str(raw), "-af",
        "loudnorm=I=-18:TP=-1.5:LRA=7:print_format=json", "-f", "null", "-"],
        capture_output=True, text=True, check=True)
    m = measurements(first.stderr)
    filter_ = ("loudnorm=I=-18:TP=-1.5:LRA=7:linear=true:"
        f"measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
        f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:"
        f"offset={m['target_offset']}")
    mp3 = directory / "audio.mp3"
    subprocess.run(command + ["-y", "-i", str(raw), "-af", filter_, "-ar", "44100",
        "-ac", "1", "-c:a", "libmp3lame", "-b:a", "128k", "-metadata",
        "artist=" + VOICE, str(mp3)], capture_output=True, check=True)
    check = subprocess.run(command + ["-i", str(mp3), "-af",
        "loudnorm=I=-18:TP=-1.5:LRA=7:print_format=json", "-f", "null", "-"],
        capture_output=True, text=True, check=True)
    levels = measurements(check.stderr)
    if float(levels["input_tp"]) >= 0 or mp3.stat().st_size > 25_000_000:
        raise ValueError("音量またはファイルサイズが想定範囲外です")
    raw.unlink()
    return dict(duration_seconds=round(seconds, 3),
                synthesis_seconds=round(time.monotonic() - start, 3),
                loudness_lufs=float(levels["input_i"]),
                true_peak_dbtp=float(levels["input_tp"]),
                mp3_bytes=mp3.stat().st_size,
                audio_sha256=hashlib.sha256(mp3.read_bytes()).hexdigest())


def render(data, audio, directory):
    esc = html.escape
    jst = timezone(timedelta(hours=9))
    cutoff = timestamp(data["cutoff_at"]).astimezone(jst).strftime("%Y年%m月%d日 %H:%M")
    completed = datetime.now(timezone.utc).astimezone(jst).strftime("%Y年%m月%d日 %H:%M")
    paragraphs = "\n".join(f"<p>{esc(p)}</p>" for p in data["manuscript"].strip().split("\n\n"))
    sources = "\n".join(f'<li><a href="{esc(s["url"], quote=True)}" rel="noreferrer">'
                         f'{esc(s["title"])}</a></li>' for s in data["sources"])
    duration = round(audio["duration_seconds"])
    html_text = f'''<!doctype html>
<html lang="ja"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex"><title>NEWS 試験配信</title>
<style>body{{max-width:760px;margin:40px auto;padding:0 20px;font:18px/1.9 system-ui,sans-serif;color:#202731;background:#faf9f6}}h1{{font-size:2rem}}audio{{width:100%;margin:18px 0}}.meta{{font-size:.9rem;color:#57616d}}.notice{{padding:12px 16px;border-left:4px solid #577b76;background:#edf2ee}}p{{margin:1.5em 0}}a{{color:#275c68}}button{{font:inherit}}summary{{cursor:pointer}}</style>
<h1>NEWS</h1><div class="notice">試験配信</div>
<p class="meta">ニュース確認の基準：{cutoff}（日本時間）<br>音声作成：{completed}（日本時間）<br>玄野武宏・1.3倍 ／ {duration // 60}分{duration % 60:02d}秒</p>
<audio controls preload="metadata" src="audio.mp3?{esc(data['id'])}">音声を再生できません。</audio>
<p><a href="audio.mp3" download>音声を保存</a> · <a href="script.txt">原稿を開く</a></p>
<details><summary>原稿を読む</summary>{paragraphs}</details>
<details><summary>出典</summary><ul>{sources}</ul></details>
<p class="meta">合成音声：{VOICE}<br>取得に失敗した回は更新されません。上記の日付を確認してください。</p>
<p class="meta">テストID：{esc(data['id'])}</p></html>'''
    (directory / "index.html").write_text(html_text)
    (directory / "script.txt").write_text(data["manuscript"])
    manifest = dict(schema_version=1, id=data["id"], cutoff_at=data["cutoff_at"],
                    written_at=data["written_at"], built_at=datetime.now(timezone.utc).isoformat(),
                    voice=VOICE, settings=SETTINGS, sentences=len(validate(data)),
                    manuscript_sha256=hashlib.sha256(data["manuscript"].encode()).hexdigest(),
                    **audio)
    (directory / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2))
    (directory / "sources.json").write_text(json.dumps(data["sources"], ensure_ascii=False, indent=2))
    (directory / ".nojekyll").touch()
    return manifest


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--engine", default="http://127.0.0.1:50021")
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()
    if args.input.stat().st_size > 120_000:
        raise ValueError("リクエストが大きすぎます")
    data = json.loads(args.input.read_text())
    chunks = validate(data)
    if args.validate_only:
        print(f"原稿確認済み：{len(chunks)}文")
        return
    if args.engine not in ("http://127.0.0.1:50021", "http://127.0.0.1:50101"):
        raise ValueError("音声エンジンはループバック接続に限定します")
    args.output.mkdir(parents=True, exist_ok=False)
    audio = synthesize(chunks, args.engine, args.output)
    manifest = render(data, audio, args.output)
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
