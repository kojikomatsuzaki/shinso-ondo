# Audio

「新荘音頭」（副題：「新荘よいとこ散歩道」）の公式公開音源を収録するディレクトリです。

一般利用者向けの音源ページ：

- [`index.html`](index.html)
- 公開サイト：<https://kojikomatsuzaki.github.io/shinso-ondo/audio/>

本ディレクトリでは、3種類の公式公開音源を、試聴・配信用のMP3形式と保存用のWAV形式で提供します。

---

## 収録音源

| 版 | MP3 | WAV |
|---|---|---|
| 新荘音頭制作委員・新荘小学校管楽合奏部児童 斉唱版 | `shinso-ondo-shinsokai-shinsoelem.mp3` | `shinso-ondo-shinsokai-shinsoelem.wav` |
| 新荘小学校管楽合奏部児童 斉唱版 | `shinso-ondo-shinsoelem.mp3` | `shinso-ondo-shinsoelem.wav` |
| 塙亜樹 独唱版 | `shinso-ondo-hanawa-aki.mp3` | `shinso-ondo-hanawa-aki.wav` |

### ファイルの役割

- **MP3**：Web上での試聴および一般的な再生環境での利用に向けた配信用ファイル
- **WAV**：音質を保った保存用マスターファイル

---

## 主なクレジット

- 歌唱：新荘音頭制作委員
- 歌唱：新荘小学校管楽合奏部児童
- 歌唱：塙 亜樹
- 演奏：木管アンサンブル ツーウィー
- 録音時の指揮：馬立 明美
- 音源制作：小松崎 浩司

各音源に対応する出演者と制作情報の詳細は、正本メタデータを参照してください。

---

## 正本メタデータとの関係

作品名、演奏者、制作クレジット、公開ファイル、権利情報などの構造化された作品情報は、

- [`../metadata/shinso-ondo.yaml`](../metadata/shinso-ondo.yaml)

を正本（Single Source of Truth）として管理しています。

`audio/index.html` は一般利用者向けの表示ページ、`README.md` はリポジトリ利用者・保守担当者向けの説明文書として役割を分けています。

---

## 更新方針

- 本ディレクトリには公式公開音源のみを収録します。
- 音源を追加または差し替える場合は、正本メタデータも同時に更新します。
- MP3・WAV内部のメタデータは、正本YAMLを参照して更新します。
- 保存用ファイルと配信用ファイルを役割によって区別します。

音源メタデータの確認・書き込みには、リポジトリルートの`Makefile`から次のコマンドを利用できます。

```bash
make metadata
make verify
make write
```

---

## 関連ページ・ディレクトリ

- [`../lyrics/`](../lyrics/)：歌詞
- [`../scores/`](../scores/)：楽譜
- [`../contributors/`](../contributors/)：制作・協力者
- [`../metadata/`](../metadata/)：正本メタデータ
- [`../rights/`](../rights/)：権利とライセンス
- [`../publications/`](../publications/)：パンフレット等

---

## ライセンス

別途記載がある場合を除き、本ディレクトリ内の資料は、

**Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International（CC BY-NC-SA 4.0）**

の条件で公開しています。

詳細は、[`../rights/`](../rights/)および[`../LICENSE`](../LICENSE)を参照してください。

---

# English Summary

The `audio/` directory contains three official recordings of **Shinsō Ondo**, provided in MP3 format for online listening and access, and WAV format as preservation-quality master files.

The public-facing page is [`index.html`](index.html). Structured information about the recordings, performers, files, credits, and rights is maintained in [`../metadata/shinso-ondo.yaml`](../metadata/shinso-ondo.yaml) as the canonical metadata source.

Unless otherwise noted, the materials are licensed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0)**.
