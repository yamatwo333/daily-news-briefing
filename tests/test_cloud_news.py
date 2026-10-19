import copy
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import re
import shutil
import subprocess
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

    def test_audio_cache_key_changes_when_same_edition_is_rebuilt(self):
        with tempfile.TemporaryDirectory() as temp:
            path=Path(temp)
            render(self.data,dict(duration_seconds=70,audio_sha256='a'*64),path)
            first=(path/'index.html').read_text()
            render(self.data,dict(duration_seconds=70,audio_sha256='b'*64),path)
            second=(path/'index.html').read_text()
            self.assertIn('audio.mp3?v='+'a'*64,first)
            self.assertIn('audio.mp3?v='+'b'*64,second)
            self.assertNotIn('audio.mp3?v='+'a'*64,second)

    @unittest.skipUnless(shutil.which('node'), 'Node is optional for this browser-script test')
    def test_staleness_notice_uses_jst_and_allows_30_minutes_after_7am_start(self):
        with tempfile.TemporaryDirectory() as temp:
            path=Path(temp)
            self.data['cutoff_at']='2026-10-19T07:05:00+09:00'
            self.data['written_at']='2026-10-19T07:10:00+09:00'
            # render validates dates; use the actual test date for input validation,
            # then substitute only the embedded clock-independent fixture cutoff.
            fixture=self.data['cutoff_at']
            self.data['cutoff_at']=self.now.isoformat()
            self.data['written_at']=self.now.isoformat()
            render(self.data,dict(duration_seconds=70),path)
            script=re.search(r'<script>(.*?)</script>',(path/'index.html').read_text(),re.S)[1]
            script=script.replace(json.dumps(self.data['cutoff_at']),json.dumps(fixture))
            code="""const vm=require('node:vm');
const input=JSON.parse(require('node:fs').readFileSync(0,'utf8'));
const results=input.times.map(t=>{const status={};const RealDate=Date;
class Clock extends RealDate{constructor(...args){super(...(args.length?args:[t]));}}
vm.runInNewContext(input.script,{Date:Clock,Intl,document:{getElementById:()=>status},setInterval:()=>{}});
return status;});process.stdout.write(JSON.stringify(results));"""
            times=['2026-10-19T22:29:00Z','2026-10-19T22:30:00Z','2026-10-19T01:00:00Z']
            out=subprocess.run(['node','-e',code],input=json.dumps(dict(script=script,times=times)),text=True,capture_output=True,check=True)
            before,after,today=json.loads(out.stdout)
            self.assertTrue(before['hidden'])
            self.assertFalse(after['hidden'])
            self.assertIn('本日分はまだ更新されていません',after['textContent'])
            self.assertTrue(today['hidden'])


if __name__ == '__main__':
    unittest.main()
