# NEWS

GPTが選定・事実確認・執筆する日本語の朝ニュースです。音声・原稿・出典は毎日同じURLで提供します。

https://yamatwo333.github.io/daily-news-briefing/

## 現在の運用

既存のGPTクラウド予約が毎日6:30（Asia/Tokyo）に開始し、7時ごろの完成を目指します。原稿は既存のPro契約のGPTが作成し、有料AI API・他社モデルは使いません。Googleドキュメント同期は現行工程に含めません。

1. 正式ホスト型検索でニュース候補の記事本文を確認し、新しい日本語原稿を作成。
2. 現行ブランチHEADに固定した手順・オフライン判定・原稿検査を使用。VMからの外部コマンド通信は使用しない。
3. `news-cloud-test` の `inbox/latest.json` だけを1回更新。
4. GitHub Actionsが回帰テスト・原稿検査・VOICEVOX音声生成・Pages公開を実施。
5. GitHubの `verify-publication` が公開ページ・原稿・出典・音声の版、全文、ハッシュ、サイズを照合。deploy成功だけで公開照合済みとは扱わない。

現在の運用手順の正本は [docs/news_daily_runbook.md](docs/news_daily_runbook.md) です。予約はこの手順と `cloud_test/daily_guard.py` を毎回同じHEADから取得します。クラウドの古いローカルcheckoutや、過去の試験指示を現在の仕様と混同しません。

記事単位の取得不能はその記事を除外し、再取得や別経路での回避をせず、確認済みの別記事で継続します。本当の安全審査・明示的権限拒否は該当操作を停止します。使用しないVM外向きHTTPの状態を、別の権限境界を持つホスト型ツールの共通前提にはしません。

## 主なファイル

- `docs/news_daily_runbook.md`: 現行の毎朝配信手順・失敗時の扱い。
- `cloud_test/daily_guard.py`: オフラインの実行境界・取得エラー・重複配信判定。
- `cloud_test/build.py`: 原稿検査、玄野武宏の音声化、公開ページ生成。
- `cloud_test/verify_publication.py`: GitHub上で行う公開ファイルの独立照合。
- `tests/`: 起動状態、URL取得不能、明示的拒否、日時・重複・古い公開物・キャッシュの回帰テスト。
- `docs/daily_briefing_principles.md` と `docs/news_foundation_2026_ja.*`: 編集・ニュース理解の参考。古い同期・挨拶・定型構成などが現行手順や最新の利用者指示と衝突する場合は、現行方針を優先。

## 旧構成の資料

`scripts/sync_google_doc.py`、Apps Script、Google Docs同期設定、旧 `docs/automation_prompt_daily_briefing.md` は旧構成の参考資料です。現在の予約や同期を表す正本ではなく、このREADMEを読んだだけで実行・再設定しません。旧設定の秘密値・認証情報は読み出したり公開したりしません。

本番の閲覧先は固定URLですが、配信経路は引き続き `news-cloud-test` です。mainへのマージや権限拡大はこの更新に含めていません。
