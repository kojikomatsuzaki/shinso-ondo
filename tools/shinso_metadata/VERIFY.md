# Verification

マージ前に、リポジトリ直下で次を実行します。

```bash
python -m py_compile tools/update_audio_metadata.py tools/shinso_metadata/*.py
python tools/update_audio_metadata.py
```

期待する照合結果は `対応済み: 6`、`対応なし: 0` です。
