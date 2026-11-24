import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest

from cloud_test import build
from test_listening_budget import edition


class ListeningHistoryTests(unittest.TestCase):
    def test_only_standalone_recap_at_end_is_addressable(self):
        data = edition()
        recap = '振り返ると、先週この制度が始まりました。'
        data['manuscript'] += recap
        data['optional_recap'] = dict(source_id='test-20261104T000000Z', sentences=[recap])
        chunks = build.validate(data)
        self.assertEqual(build.recap_range(data, chunks), (len(chunks)-1, len(chunks)))
        data['manuscript'] += '今日の新しい決定です。'
        with self.assertRaises(ValueError):
            build.validate(data)

    @unittest.skipUnless(shutil.which('node'), 'requires Node')
    def test_button_persists_and_skips_only_the_marked_source_segment(self):
        data = edition()
        old_id = data['id']
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp)
            def page():
                html = (path / 'index.html').read_text()
                tag = re.search(r'<button[^>]+id="listen-toggle"[^>]+>', html)[0]
                return [dict(re.findall(r'data-([a-z]+)="([^"]*)"', tag)),
                        re.findall(r'<script>(.*?)</script>', html, re.S)[-1]]
            audio = dict(duration_seconds=480)
            build.render(data, audio, path)
            old = page()
            data['id'] = 'test-20261106T000000Z'
            line = '振り返ると、先週この制度が始まりました。'
            data['manuscript'] += line
            data['optional_recap'] = dict(source_id=old_id, sentences=[line])
            build.render(data, dict(audio, recap_seconds=[12, 16]), path)
            new = page()
        code = """
const vm = require('node:vm'), assert = require('node:assert/strict');
const [old, next] = JSON.parse(require('fs').readFileSync(0, 'utf8'));
const db = new Map();
function open([dataset, js]) {
  const btn = {dataset, setAttribute(){}, addEventListener(k,f){this[k]=f}};
  const audio = {paused:false, seeking:false, addEventListener(k,f){this[k]=f}};
  vm.runInNewContext(js,{document:{getElementById:()=>btn, querySelector:()=>audio},
    localStorage:{getItem:k=>db.get(k),setItem:(k,v)=>db.set(k,v),removeItem:k=>db.delete(k)}});
  return {btn,audio};
}
const listen=(t)=>{const {audio}=open(next); audio.currentTime=t; audio.timeupdate(); return audio.currentTime};
assert.equal(listen(13),13);
open(old).btn.click();
assert.match(open(old).btn.textContent,/取り消す/);
assert.equal(listen(11),11); assert.equal(listen(13),16); assert.equal(listen(17),17);
open(old).btn.click(); assert.equal(listen(13),13);
"""
        subprocess.run(['node', '-e', code], input=json.dumps([old, new]), text=True, check=True)
