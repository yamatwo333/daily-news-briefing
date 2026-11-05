import io
import json
from datetime import datetime, timezone
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch
import wave

from cloud_test import build
from cloud_test.daily_guard import coverage_decision
from cloud_test.verify_publication import check_once, PublicationPending
from test_availability import candidates


def edition():
    now = datetime.now(timezone.utc).isoformat()
    text = 'まずは、社会のニュースです。\n\n' + '\n\n'.join(
        f'検査記事{i}の見出しです。\n' + '確認済み事実と必要な背景を短く説明する文章です。' * 12
        for i in range(12))
    return dict(schema_version=1, id='test-20261105T000000Z',
                cutoff_at=now, written_at=now, manuscript=text,
                sources=[dict(title='検査出典', url='https://example.com/news')],
                edition=dict(kind='normal', story_count=12),
                listening_policy=build.LISTENING_POLICY)


class ListeningBudgetTests(unittest.TestCase):
    def test_legacy_scheduler_input_gets_new_build_policy_without_prose_changes(self):
        data = edition()
        del data['listening_policy']
        original = json.dumps(data, ensure_ascii=False)
        build.validate(data)
        prepared = build.prepare_new_input(data)
        self.assertEqual(prepared['listening_policy'], build.LISTENING_POLICY)
        self.assertEqual(prepared['manuscript'], data['manuscript'])
        self.assertEqual(json.dumps(data, ensure_ascii=False), original)
        data['manuscript'] += '確認済みの追加文です。' * 100
        with self.assertRaises(ValueError):
            build.prepare_new_input(data)

    def test_new_normal_does_not_force_old_4300_minimum(self):
        data = edition()
        self.assertTrue(3200 <= len(data['manuscript']) < 4300)
        build.validate(data)
        result = coverage_decision(candidates(12), manuscript_characters=len(data['manuscript']))
        self.assertEqual(result['action'], 'prepare_normal')
        self.assertEqual(result['edition_kind'], 'normal')

    def test_overlong_draft_must_be_edited_even_after_research_deadline(self):
        for count in [7, 12, 18]:
            result = coverage_decision(candidates(count), 1800, manuscript_characters=4201)
            self.assertEqual(result['action'], 'shorten_manuscript')
            self.assertFalse(result['write_input'])
        data = edition()
        data['manuscript'] += '確認済みの追加文です。' * 100
        with self.assertRaises(ValueError):
            build.validate(data)

    def test_final_encoded_mp3_not_only_pcm_is_measured(self):
        buffer = io.BytesIO()
        with wave.open(buffer, 'wb') as wav:
            wav.setparams((1, 2, 1000, 0, 'NONE', 'not compressed'))
            wav.writeframes(b'\x01\x00' * 1000)
        def request(base, path, *args, **kwargs):
            return b'{}' if path == '/audio_query' else buffer.getvalue()
        levels = dict(input_i='-18', input_tp='-2', input_lra='3', input_thresh='-28', target_offset='0')
        for duration in ['480.125', '600', '600.001', 'nan']:
            def external(command, **kwargs):
                if '-show_entries' in command:
                    return SimpleNamespace(stdout=duration)
                if command[-1].endswith('audio.mp3'):
                    Path(command[-1]).write_bytes(b'encoded audio fixture')
                return SimpleNamespace(stderr='fixture')
            with self.subTest(duration=duration), tempfile.TemporaryDirectory() as temp, \
                 patch.object(build, 'check_engine'), \
                 patch.object(build, 'request', side_effect=request), \
                 patch.object(build.shutil, 'which', side_effect=lambda name: name), \
                 patch.object(build.subprocess, 'run', side_effect=external), \
                 patch.object(build, 'measurements', return_value=levels):
                if duration in ['600.001', 'nan']:
                    with self.assertRaises(ValueError):
                        build.synthesize([('検査用本文です。', 0)], 'http://127.0.0.1:50021', Path(temp))
                    self.assertFalse((Path(temp) / 'index.html').exists())
                else:
                    result = build.synthesize([('検査用本文です。', 0)], 'http://127.0.0.1:50021', Path(temp))
                    self.assertEqual(result['duration_seconds'], float(duration))

    def test_public_receipt_requires_policy_and_ten_minute_cap(self):
        import hashlib
        data, audio = edition(), b'audio fixture'
        with tempfile.TemporaryDirectory() as temp:
            directory = Path(temp)
            build.render(data, dict(duration_seconds=480, mp3_bytes=len(audio),
                         audio_sha256=hashlib.sha256(audio).hexdigest()), directory)
            (directory / 'audio.mp3').write_bytes(audio)
            fetch = lambda name: (directory / name).read_bytes()
            self.assertEqual(check_once(data, fetch)['result'], 'verified')
            legacy_input = dict(data)
            del legacy_input['listening_policy']
            self.assertEqual(check_once(legacy_input, fetch)['result'], 'verified')
            manifest = json.loads(fetch('manifest.json'))
            manifest['duration_seconds'] = 600.01
            (directory / 'manifest.json').write_text(json.dumps(manifest))
            with self.assertRaises(ValueError):
                check_once(data, fetch)
            with self.assertRaises(ValueError):
                check_once(legacy_input, fetch)
            manifest['duration_seconds'] = 480
            del manifest['listening_policy']
            (directory / 'manifest.json').write_text(json.dumps(manifest))
            with self.assertRaises(PublicationPending):
                check_once(data, fetch)
            with self.assertRaises(ValueError):
                build.render(data, dict(duration_seconds=601), directory)
