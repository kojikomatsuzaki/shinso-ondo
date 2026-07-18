# Metadata

## 日本語

このフォルダには、「新荘音頭」に関する構造化メタデータを収録しています。

メタデータは、人間が読むための解説ではなく、作品や公開資料に関する情報を機械可読な形で記録・管理することを目的としています。

現在公開しているメタデータは次のとおりです。

| ファイル | 内容 |
|----------|------|
| `shinso-ondo.yaml` | 新荘音頭の作品情報、歌詞、制作クレジット、演奏、公開音源、権利情報などを記録した構造化メタデータ |

## メタデータに含まれる情報

- 作品情報
- 地域情報
- 公開情報
- 制作者・クレジット
- 歌詞
- 演奏・録音
- 音源ファイル
- 権利情報
- ライセンス
- 典拠資料

## なぜYAMLを採用したのか

本アーカイブでは、メタデータの記述形式として **YAML** を採用しています。

YAMLを選択した理由は、単に人が読みやすいからではなく、デジタルアーカイブの運用や長期保存、将来的なデータ利活用を考慮したためです。

### 人にも読みやすい

YAMLはプレーンテキストで記述できるため、専用ソフトウェアがなくても内容を確認できます。作品情報やクレジット、権利情報などを、そのまま文書として読むことができます。

### Gitによる履歴管理に適している

本アーカイブはGitHubで管理しています。

YAMLは変更箇所が分かりやすく、Gitによる差分管理との相性が良いため、

- 誰が
- いつ
- 何を
- なぜ変更したのか

という履歴を継続的に管理できます。

### 他形式への変換が容易

YAMLはJSONとの親和性が高く、多くのプログラミング言語で利用されています。

そのため、将来的には必要に応じて

- JSON
- RDF
- Linked Open Data (LOD)
- IIIF関連データ

などへの変換や連携にも対応しやすい構成となっています。

### 人間向け資料との役割分担

パンフレットやREADMEは、人が閲覧するための資料です。

一方、このYAMLは、

- コンピュータが扱うための構造化データ
- 他システムとのデータ交換
- 将来的な再利用

を目的として整備しています。

同じ作品を扱っていても、それぞれ異なる役割を担っています。

### 長期保存を考慮した設計

文化資料のデジタルアーカイブでは、特定のソフトウェアやデータベースに依存しないことも重要です。

YAMLはオープンなテキスト形式であり、将来利用環境が変化しても比較的容易に読み取りや変換が可能です。

本アーカイブでは、公開資料（音源・楽譜・パンフレット等）と、それらを説明する構造化メタデータを分離して管理しています。この構成により、人が閲覧する資料と機械が処理する情報の双方を維持しながら、継続的な更新と長期保存、さらに将来的な再利用性の向上を目指しています。

---

# English

This directory contains structured metadata describing **Shinso Ondo**.

The metadata is intended for machine-readable description and long-term preservation rather than human-readable documentation.

## Contents

| File | Description |
|------|-------------|
| `shinso-ondo.yaml` | Structured metadata describing the work, lyrics, contributors, performances, recordings, publication, rights, and related resources. |

## Metadata includes

- Work description
- Geographic information
- Publication information
- Contributors
- Lyrics
- Performances
- Audio recordings
- Rights information
- License
- Bibliographic sources

## Why YAML?

This archive adopts **YAML** as its metadata format.

YAML was selected not only because it is human-readable, but also because it supports sustainable digital archiving, long-term preservation, and future data interoperability.

### Human-readable

YAML is plain text and can be read without specialized software.

### Version-control friendly

The archive is maintained on GitHub.

YAML works well with Git, making it easy to record who changed what, when, and why.

### Easy interoperability

YAML can be readily converted into JSON and processed by many programming languages.

Future interoperability with technologies such as **RDF**, **Linked Open Data (LOD)**, and **IIIF** is also envisioned.

### Separation of roles

The pamphlet and README files are intended for human readers.

The YAML metadata is intended for machine-readable description, data exchange, and future reuse.

Together they provide complementary views of the same cultural resource.

### Designed for long-term preservation

Digital archives should not depend on proprietary software or database systems.

By separating public-facing materials from structured metadata, this repository aims to improve long-term preservation, maintainability, and future reuse while keeping both human-readable documentation and machine-readable metadata in sync.
