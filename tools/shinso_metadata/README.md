# shinso_metadata

`metadata/shinso-ondo.yaml` を正本として読み込み、用途別のメタデータへ変換するための内部パッケージです。

音源ファイルと `performances` の照合、音源タグ用中間モデルの生成、MP3・WAVへのID3タグ書き込み、バックアップ、再読込検証を担当します。

## モジュール

- `loader.py`: YAML正本の読み込み
- `model.py`: 用途別の中間データモデル
- `mapper.py`: YAMLから中間モデルへの変換
- `matcher.py`: 音源探索と演奏情報の照合
- `display.py`: プレビュー表示
- `backup.py`: 書き込み前バックアップ
- `writer.py`: MP3・WAVへのID3タグ書き込み
- `verify.py`: 書き込み後または既存タグの検証

エントリーポイントは `tools/update_audio_metadata.py` です。

```bash
# プレビューのみ（ファイル変更なし）
python tools/update_audio_metadata.py

# 既存タグの検証（ファイル変更なし）
python tools/update_audio_metadata.py --verify

# バックアップ後に書き込み、自動検証
python tools/update_audio_metadata.py --write
```

バックアップは `backups/audio-tags/<実行時刻>/` に作成され、Gitでは追跡されません。
