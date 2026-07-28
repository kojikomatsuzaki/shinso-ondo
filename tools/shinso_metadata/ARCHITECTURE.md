# Metadata transformation flow

```text
metadata/shinso-ondo.yaml
        |
        v
loader.py
        |
        v
mapper.py ----> model.py
        |
        +----> matcher.py
        |
        +----> display.py
        |
        v
update_audio_metadata.py
```

`update_audio_metadata.py` はコマンドライン引数と処理順序だけを担当します。YAMLの解釈や音源照合は各モジュールへ分離し、将来の音源タグ書き込みやJSON-LD生成でも同じ正本読み込み・変換処理を再利用できる構成にしています。
