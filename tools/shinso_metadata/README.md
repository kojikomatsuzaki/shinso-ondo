# shinso_metadata

`metadata/shinso-ondo.yaml` を正本として読み込み、用途別のメタデータへ変換するための内部パッケージです。

現段階では、音源ファイルと `performances` の照合および音源タグ用中間モデルの生成を担当します。MP3・WAVへの実書き込みはまだ行いません。

## モジュール

- `loader.py`: YAML正本の読み込み
- `model.py`: 用途別の中間データモデル
- `mapper.py`: YAMLから中間モデルへの変換
- `matcher.py`: 音源探索と演奏情報の照合
- `display.py`: プレビュー表示

エントリーポイントは従来どおり `tools/update_audio_metadata.py` です。
