import copy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from cloud_test.build import render, validate
from cloud_test.daily_guard import coverage_decision, classify_fetch_error
from cloud_test.verify_publication import check_once, PublicationPending


def candidates(count):
    return [dict(id=str(i), body_verified=True, facts_verified=True,
                 in_window=True, newsworthy=True,
                 source_urls=['https://example.com/news/' + str(i)])
            for i in range(count)]


class AvailabilityTests(unittest.TestCase):
    def test_actual_url_inaccessible_envelope_is_article_scoped(self):
        error = dict(message='Internal Error ()\nURL https://example.com/news is not accessible via this tool.')
        result = classify_fetch_error(error)
        self.assertEqual(result['action'], 'exclude_article')
        self.assertFalse(result['retry_url'])
        self.assertFalse(result['alternate_route'])
        # An explicit denial wins even when the transport text looks identical.
        error['code'] = 'POLICY_DENIED'
        self.assertEqual(classify_fetch_error(error)['action'], 'stop_operation')
        self.assertEqual(classify_fetch_error(dict(message='Internal Error ()'))['action'], 'stop_operation')

    def test_morning_failure_case_preserves_seven_verified_stories(self):
        # The old ten-minute/two-pass shortcut must not discard normal-volume work.
        early = coverage_decision(candidates(7), 600, True,
                                  coverage_gaps=['主要記事の本文未取得'], manuscript_characters=2506)
        self.assertEqual(early['action'], 'continue_research')
        result = coverage_decision(candidates(7), 1800, coverage_gaps=['主要記事の本文未取得'],
                                   manuscript_characters=2506)
        self.assertEqual(result['action'], 'prepare_compact')
        self.assertEqual(result['verified_ids'], [str(i) for i in range(7)])
        self.assertEqual(result['edition_kind'], 'compact')

    def test_research_continues_before_budget_instead_of_early_abandonment(self):
        result = coverage_decision(candidates(7), 240)
        self.assertEqual(result['action'], 'continue_research')
        self.assertFalse(result['write_input'])
        self.assertEqual(coverage_decision(candidates(7), 240, True)['action'], 'continue_research')

    def test_unverified_stale_nonnews_and_invalid_sources_never_enter_subset(self):
        stories = candidates(6)
        for i, field in enumerate(['body_verified', 'facts_verified', 'in_window', 'newsworthy']):
            stories[i][field] = False
        stories[4]['source_urls'] = ['https://secret@example.com/private']
        result = coverage_decision(stories, 1800, manuscript_characters=500)
        self.assertEqual(result['verified_ids'], ['5'])
        self.assertEqual(result['action'], 'prepare_compact')
        self.assertEqual(coverage_decision(stories[:5], 1800)['action'], 'stop_no_verified_news')

    def test_normal_coverage_still_publishes_and_gaps_cannot_be_hidden(self):
        self.assertEqual(coverage_decision(candidates(12), 400, manuscript_characters=3700)['action'], 'prepare_normal')
        result = coverage_decision(candidates(12), 600, manuscript_characters=3700,
                                  coverage_gaps=['未確認の重要分野'])
        self.assertEqual(result['action'], 'prepare_normal')
        self.assertEqual(result['coverage_gaps'], ['未確認の重要分野'])
        with self.assertRaises(ValueError):
            coverage_decision([candidates(1)[0]] * 2, 600)

    def test_story_count_alone_does_not_make_a_short_manuscript_normal(self):
        draft = coverage_decision(candidates(12), 600)
        self.assertEqual(draft['action'], 'draft_normal')
        self.assertFalse(draft['write_input'])
        short = coverage_decision(candidates(12), 1800, manuscript_characters=2506)
        self.assertEqual(short['action'], 'expand_verified_manuscript')
        self.assertFalse(short['write_input'])
        full = coverage_decision(candidates(12), 1800, manuscript_characters=3900,
                                 expansion_attempted=True)
        self.assertEqual(full['action'], 'prepare_normal')

    def test_early_last_resort_requires_actual_breadth_time_and_exhaustion(self):
        audit = dict(discovery_complete=True, research_passes=3,
                     publisher_origins=['A', 'B', 'C', 'D', 'E'],
                     examined_candidates=24, exhaustion_reason='残る候補は本文未取得か重要性不足',
                     manuscript_characters=2506)
        self.assertEqual(coverage_decision(candidates(10), 900, **audit)['action'], 'prepare_compact')
        self.assertEqual(coverage_decision(candidates(10), 899, **audit)['action'], 'continue_research')
        for key, value in [('research_passes', 2), ('publisher_origins', ['A'] * 5),
                           ('examined_candidates', 23), ('exhaustion_reason', '')]:
            incomplete = dict(audit, **{key: value})
            self.assertEqual(coverage_decision(candidates(10), 900, **incomplete)['action'], 'continue_research')

    def test_compact_draft_does_not_authorize_a_public_write(self):
        result = coverage_decision(candidates(10), 1800)
        self.assertEqual(result['action'], 'draft_compact')
        self.assertFalse(result['write_input'])
        self.assertEqual(result['fallback_reason'], 'research_deadline_reached')

    def test_build_refuses_to_label_twelve_short_items_as_normal(self):
        now = datetime.now(timezone.utc).isoformat()
        def manuscript(repeats):
            return 'まずは、社会のニュースです。\n\n' + '\n\n'.join(
                f'検査記事{i}の見出しです。\n' + '確認済み事実を説明する検査用の文章です。' * repeats
                for i in range(12))
        data = dict(schema_version=1, id='test-20261104T000000Z',
                    cutoff_at=now, written_at=now, manuscript=manuscript(5),
                    sources=[dict(title='検査用出典', url='https://example.com/news')],
                    edition=dict(kind='normal', story_count=12))
        with self.assertRaises(ValueError):
            validate(data)
        data['manuscript'] = manuscript(20)
        validate(data)

    def test_compact_roundtrip_requires_matching_count_and_public_disclosure(self):
        now = datetime.now(timezone.utc).isoformat()
        data = dict(schema_version=1, id='test-20261104T000000Z',
                    cutoff_at=now, written_at=now,
                    manuscript='まずは、社会のニュースです。\n\n検査用の見出しです。\n' +
                    'これは検査専用の文章です。' * 10,
                    sources=[dict(title='検査用出典', url='https://example.com/news')],
                    edition=dict(kind='compact', story_count=1))
        validate(data)
        invalid = copy.deepcopy(data)
        invalid['edition']['story_count'] = 2
        with self.assertRaises(ValueError):
            validate(invalid)
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp)
            audio = b'test-only audio fixture'
            (path/'audio.mp3').write_bytes(audio)
            render(data, dict(duration_seconds=12, mp3_bytes=len(audio),
                   audio_sha256=hashlib.sha256(audio).hexdigest()), path)
            files = {p.name: p.read_bytes() for p in path.iterdir()}
        self.assertEqual(check_once(data, files.__getitem__)['result'], 'verified')
        hidden = dict(files)
        hidden['index.html'] = hidden['index.html'].replace('1本の短縮版'.encode(), '通常版'.encode())
        with self.assertRaises(PublicationPending):
            check_once(data, hidden.__getitem__)
        wrong = dict(files)
        manifest = json.loads(wrong['manifest.json'])
        manifest['edition']['kind'] = 'normal'
        wrong['manifest.json'] = json.dumps(manifest).encode()
        with self.assertRaises(PublicationPending):
            check_once(data, wrong.__getitem__)


if __name__ == '__main__':
    unittest.main()
