# Design principles

- `metadata/shinso-ondo.yaml` を唯一の正本とする
- YAMLの解釈をエントリーポイントから分離する
- 音源ファイルとの照合は `item.files[].file_name` の完全一致を優先する
- ファイル名stemによる照合は補助的な経路として残す
- 実ファイルへの書き込みは、プレビュー結果の検証後に別モジュールとして追加する
