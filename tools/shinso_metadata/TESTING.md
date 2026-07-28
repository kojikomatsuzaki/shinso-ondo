# Testing

このリファクタリングでは表示内容と照合件数を変更しないことを受入条件とします。

```bash
python -m py_compile tools/update_audio_metadata.py tools/shinso_metadata/*.py
python tools/update_audio_metadata.py
```

期待値:

```text
○ 対応済み : 6
△ 対応なし : 0
```
