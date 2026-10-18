import copy
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import tempfile
import unittest
from cloud_test.build import validate, render


class TestNews(unittest.TestCase):
    def setUp(self):
        self.now = datetime.now(timezone.utc)
        self.data = dict(schema_version=1, id="test-20261018T073000Z",
            cutoff_at=self.now.isoformat(), written_at=self.now.isoformat(),
            manuscript=("確認した事実を伝える音声の試験です。" * 8 +
                        "\n\n次のニュースです。"),
            sources=[dict(title="発表元", url="https://example.com/news")])

    def test_text_is_not_lost_between_sentences(self):
        chunks=validate(self.data, self.now)
        self.assertEqual("".join(text for text, _ in chunks),
                         self.data["manuscript"].replace("\n\n", ""))
        self.assertEqual(chunks[-1][1], 1)

    def test_expired_and_future_cutoffs_are_rejected(self):
        for offset in [timedelta(days=-3), timedelta(hours=1)]:
            data=copy.deepcopy(self.data)
            data['cutoff_at']=(self.now + offset).isoformat()
            with self.assertRaises(ValueError): validate(data, self.now)

    def test_timestamp_without_zone_is_rejected(self):
        self.data['cutoff_at']='2026-10-18T16:00:00'
        with self.assertRaises(ValueError): validate(self.data, self.now)

    def test_sources_cannot_contain_credentials_or_javascript(self):
        for url in ['javascript:alert(1)', 'https://secret@example.com']:
            self.data['sources'][0]['url']=url
            with self.assertRaises(ValueError): validate(self.data, self.now)

    def test_untrusted_text_is_escaped_and_only_site_files_are_written(self):
        self.data['manuscript'] += '<img src=x onerror=alert(1)>'
        self.data['sources'][0]['title']='<script>bad</script>'
        audio=dict(duration_seconds=70, mp3_bytes=10000)
        with tempfile.TemporaryDirectory() as temp:
            directory=Path(temp)
            render(self.data,audio,directory)
            html=(directory/'index.html').read_text()
            self.assertNotIn('<img src=x',html)
            self.assertNotIn('<script>bad',html)
            self.assertIn('&lt;img',html)
            self.assertEqual((directory/'script.txt').read_text(), self.data['manuscript'])
            self.assertEqual(set(p.name for p in directory.iterdir()),
                {'index.html','script.txt','manifest.json','sources.json','.nojekyll'})
            self.assertEqual(json.loads((directory/'manifest.json').read_text())['id'],self.data['id'])


if __name__ == '__main__':
    unittest.main()
