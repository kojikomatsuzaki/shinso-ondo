# Development check

変更後はリポジトリ直下で次を実行します。

```bash
python -m py_compile tools/update_audio_metadata.py tools/shinso_metadata/*.py
python tools/update_audio_metadata.py
```

照合結果が従来どおり `対応済み: 6`、`対応なし: 0` となることを確認してからマージします。
