# Metadata / メタデータ

This directory contains the structured metadata for the official digital archive of **Shinso Ondo – Shinso Yoitoko Sanpo-michi**.

このディレクトリには、『**新荘音頭―新荘よいとこ散歩道―**』公式デジタルアーカイブの構造化メタデータを収録しています。

The metadata is designed to be both **human-readable** and **machine-readable**, supporting long-term preservation, interoperability, and future reuse.

本メタデータは、人が読めることに加え、機械処理にも適した形式で記述しています。長期保存、相互運用、将来的な再利用を目的としています。

---

## Files / ファイル

| File | Description (English) | 説明（日本語） |
|---|---|---|
| `shinso-ondo.yaml` | Primary metadata record describing the work, lyrics, readings, contributors, performances, audio recordings, publication information, rights, and sources. | 作品情報、歌詞、読み仮名、クレジット、各録音版、音源、公開情報、権利情報、典拠を記述した主要メタデータです。 |

---

## Metadata Structure / メタデータ構造

| Section | Description (English) | 説明（日本語） |
|---|---|---|
| `work` | Basic description, place, publication information, and contributors. | 作品の基本情報、地域、公開情報、制作者情報です。 |
| `expression` | Lyrics, verse structure, readings in kana, and textual variants. | 歌詞構成、各番の歌詞、読み仮名、版に関する情報です。 |
| `performances` | Information about each recorded performance and its participants. | 斉唱版・独唱版など、各録音版と参加者の情報です。 |
| `rights` | Copyright, license, permissions, and access conditions. | 著作権、ライセンス、利用条件、公開条件です。 |
| `source` | Sources used to establish and verify the metadata. | メタデータの作成・確認に用いた典拠情報です。 |
| `notes` | Additional archival notes. | アーカイブ上の補足事項です。 |

---

## Purpose / 作成目的

This metadata was created to document and preserve the official digital archive of **Shinso Ondo**.

本メタデータは、『新荘音頭』公式デジタルアーカイブを記録し、保存するために作成しました。

It is intended to:

- preserve contextual information about the work
- document contributors and recording history
- distinguish and describe multiple recorded performances
- record copyright and licensing information
- support future conversion to other metadata formats, including JSON-LD, Dublin Core, MODS, and IIIF-related data

主な目的は次のとおりです。

- 作品に関する背景情報の保存
- 制作者、実演者、録音履歴の記録
- 複数の録音版の識別と記述
- 著作権およびライセンス情報の保存
- JSON-LD、Dublin Core、MODS、IIIF関連データなど、他形式への将来的な変換基盤

---

## Authoritative Record / 正本

`shinso-ondo.yaml` is the **authoritative metadata record** for this repository.

本リポジトリでは、`shinso-ondo.yaml` をメタデータの**正本**として位置付けます。

When descriptions in README files, web pages, or other derivative materials differ from this YAML record, the YAML record takes precedence.

README、Webページ、その他の派生資料に記載された内容と本YAMLの内容に差異がある場合は、本YAMLの記述を優先します。

Future metadata formats and display data may be generated from this record.

将来的に作成する他形式のメタデータや表示用データは、この正本を基に生成することを想定しています。

---

## License / ライセンス

Unless otherwise noted, this metadata is distributed under the same license as the archive.

特記のない限り、本メタデータはアーカイブ本体と同一のライセンスで公開します。

**CC BY-NC-SA 4.0**  
**表示―非営利―継承 4.0 国際**

---

*Official Digital Archive of Shinso Ondo*  
*新荘音頭公式デジタルアーカイブ*
