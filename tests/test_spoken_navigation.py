import io
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace
import tempfile
import unittest
from unittest.mock import patch
import wave

from cloud_test import build


SCRIPT = ('まずは、経済・家計のニュースです。\n\n'
          '政策金利を据え置き。\n本文です。詳しく伝えます。\n\n'
          '家計向け支援を発表。\n次の記事です。\n\n'
          '続いて、国際のニュースです。\n\n'
          '首脳が会談。\n国際ニュースの本文です。')


class SpokenNavigationTests(unittest.TestCase):
    def test_structure_counts_articles_not_cues_or_headlines(self):
        self.assertEqual(build.validate_spoken_structure(SCRIPT),
                         dict(genres=2, stories=3))
        now = datetime.now(timezone.utc)
        data = dict(schema_version=1, id='test-20261031T000000Z',
                    cutoff_at=now.isoformat(), written_at=now.isoformat(),
                    manuscript=SCRIPT, sources=[dict(title='出典', url='https://example.com/news')])
        chunks = build.validate(data, now)
        self.assertEqual(''.join(t for t, _ in chunks), SCRIPT.replace('\n\n', ''))
        self.assertEqual([build.pause_seconds(chunks, i) for i in range(len(chunks))],
                         [1.8, 0.6, 0.08, 1.2, 0.6, 1.8, 1.8, 0.6, 0.0])
        for text in ['本文だけです。',
                     'まずは、経済のニュースです。\n\n見出しなしの本文です。',
                     'まずは、経済のニュースです。\n\n続いて、国際のニュースです。',
                     SCRIPT + '\n\n最後は、社会のニュースです。']:
            with self.subTest(text=text), self.assertRaises(ValueError):
                build.validate_spoken_structure(text)

    def test_synthesis_inserts_real_pcm_silence_at_each_boundary(self):
        chunks = [('まずは、経済・家計のニュースです。', 0),
                  ('政策金利を据え置き。', 1), ('\n本文です。', 1),
                  ('詳しく伝えます。', 1), ('次の記事です。', 2),
                  ('続いて、国際のニュースです。', 3)]
        pauses = [1.8, 0.6, 0.08, 1.2, 1.8, 0.0]
        self.assertEqual([build.pause_seconds(chunks, i) for i in range(len(chunks))], pauses)
        # A real WAV payload represents each engine sentence; only external
        # engine/encoder calls are mocked so the actual PCM assembly is checked.
        buffer = io.BytesIO()
        voiced = b'\x01\x00' * 100
        with wave.open(buffer, 'wb') as wav:
            wav.setparams((1, 2, 1000, 0, 'NONE', 'not compressed'))
            wav.writeframes(voiced)
        def request(base, path, *args, **kwargs):
            return b'{}' if path == '/audio_query' else buffer.getvalue()
        captured = []
        def encoder(command, **kwargs):
            if command[-1].endswith('audio.mp3'):
                Path(command[-1]).write_bytes(b'encoder fixture')
            if command[-1] == '-' and command[command.index('-i') + 1].endswith('raw.wav'):
                with wave.open(command[command.index('-i') + 1], 'rb') as wav:
                    captured.append(wav.readframes(wav.getnframes()))
            return SimpleNamespace(stderr='fixture')
        levels = dict(input_i='-18', input_tp='-2', input_lra='3',
                      input_thresh='-28', target_offset='0')
        with tempfile.TemporaryDirectory() as temp, \
             patch.object(build, 'check_engine'), \
             patch.object(build, 'request', side_effect=request), \
             patch.object(build.shutil, 'which', return_value='ffmpeg'), \
             patch.object(build.subprocess, 'run', side_effect=encoder), \
             patch.object(build, 'measurements', return_value=levels):
            result = build.synthesize(chunks, 'http://127.0.0.1:50021', Path(temp))
        expected = b''.join(voiced + b'\0' * round(1000 * pause) * 2 for pause in pauses)
        self.assertEqual(captured, [expected])
        self.assertEqual(result['duration_seconds'], 6.08)


if __name__ == '__main__':
    unittest.main()
