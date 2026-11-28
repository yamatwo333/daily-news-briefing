# NEWS：PC停止中の一回限りの試験

この変更は試験専用。ニュースの収集・選定・執筆はChatGPTの既存利用枠で行い、GitHub Actionsには出来上がった原稿の音声化と配信だけを任せる。有料AI APIは使わない。

## 試験の経路

1. Web標準予約タスクが、実行時のニュースを調査し、原稿と出典を作る。
2. GitHub接続で `news-cloud-test` ブランチの `inbox/latest.json` を作成または更新する。
3. その更新を受け、公開リポジトリの標準Ubuntu runnerでVOICEVOX CPU版0.25.2を起動する。
4. 玄野武宏・1.3倍でMP3を生成し、原稿・出典・確認日時とともにGitHub Pagesへ配信する。
5. 予約タスクの報告とGitHub実行記録、公開ページのテストIDを照合する。PC電源状態は利用者が確認する。

Googleドキュメントへの上書きは、このプログラムからは行わない。必要な場合は予約タスクのGoogle Drive接続で個別に確認し、旧公開設定の秘密値は利用しない。

## 変更範囲と運用条件

- `main` への取り込みは不要。試験ブランチへの原稿更新だけで実行する。
- 毎朝の定期実行はまだ登録しない。一回限りのPC停止試験が通るまで、本番化しない。
- GitHub Pagesはリポジトリ設定のSourceをGitHub Actionsにする。既存サイトがある場合は上書きせず停止する。
- 試験用の `github-pages` environmentは、この試験ブランチからの配信を許可する必要がある。既存の保護ルールは勝手に解除しない。
- 0ドルのActions支出上限が利用停止を伴う状態であることを確認する。課金設定を変更せず、有料runner・外部API・有料ホスティングを使わない。
- 公開対象は生成した `site` のみ。設定ファイルやソースリポジトリ全体は公開成果物へ入れない。
- 音声は最新1回分のみ公開。配信用の一時artifactは1日で期限切れ、キャッシュは作成しない。音声をGit履歴へ追加しない。
- 原稿の検査・音声化が失敗した場合は配信しない。ページには最後に成功した回の確認日時を表示し、古い回を当日版と扱わない。

## 受け渡すJSON

```json
{
  "schema_version": 1,
  "id": "test-YYYYMMDDTHHMMSSZ",
  "cutoff_at": "実際に確認した日時。ISO 8601、タイムゾーン付き",
  "written_at": "執筆終了日時。ISO 8601、タイムゾーン付き",
  "manuscript": "URLやMarkdown見出しを含まない読み上げ原稿。話題の間は空行。",
  "sources": [
    {"title": "記事または一次資料の表題", "url": "https://..."}
  ]
}
```

タイムゾーンのない日時、48時間以上前の確認日時、確認より前の執筆時刻、未来日時、9,000字超の原稿などは止める。件数や日時をでっち上げて検査を通さない。音声設定は実装側で固定し、受け渡すJSONからエンジン接続先や実行コマンドを指定することはできない。

## 確認方法

```sh
python3 -m unittest discover -s tests -p 'test_cloud_news.py'
python3 cloud_test/build.py inbox/latest.json site --validate-only
python3 cloud_test/build.py inbox/latest.json site
```

最後の操作には、ローカルのVOICEVOX 0.25.2（port 50021）とffmpegが必要。`site` は新規ディレクトリにする。Actionsでは自動的に準備する。生成したmanifestには原稿・音声のSHA-256、テストID、確認日時、合成時間、長さ、設定を記録する。PCを停止していたかどうかはこのmanifestから推測しない。

## 公式資料

- [Webとデスクトップの予約実行の違い](https://learn.chatgpt.com/docs/automations)
- [GitHub Actionsの無料条件・保存容量・支出停止](https://docs.github.com/en/billing/concepts/product-billing/github-actions)
- [GitHub Pagesの独自workflow](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
- [Pagesの上限と利用条件](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits)
- [VOICEVOX ENGINE](https://github.com/VOICEVOX/voicevox_engine)
- [玄野武宏などの音声利用規約](https://www.virvoxproject.com/voicevox%E3%81%AE%E5%88%A9%E7%94%A8%E8%A6%8F%E7%B4%84)

クレジット：VOICEVOX:玄野武宏。中立的なニュース試聴用。第三者の公式番組とは関係しない。
