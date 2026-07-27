# Metadata

「新荘音頭デジタルアーカイブ」の正本メタデータ、スキーマおよび統制語彙を管理するディレクトリです。

本ディレクトリは、アーカイブ全体の情報基盤として、実データ・構造・統制語彙を分離し、地域文化資料を継続的かつ再利用可能な形で管理します。

---

## Table of Contents

### 日本語

- [クイックアクセス](#クイックアクセス)
- [このディレクトリの役割](#このディレクトリの役割)
- [ディレクトリ構成](#ディレクトリ構成)
- [設計原則](#設計原則)
- [メタデータアーキテクチャ](#メタデータアーキテクチャ)
- [各ファイルの役割](#各ファイルの役割)
- [One Source, Multi Use](#one-source-multi-use)
- [想定する利用者](#想定する利用者)
- [利用・更新方針](#利用更新方針)
- [将来の拡張](#将来の拡張)
- [関連ディレクトリ](#関連ディレクトリ)
- [ライセンス](#ライセンス)

### English

- [Quick Access](#quick-access)
- [Role of This Directory](#role-of-this-directory)
- [Directory Structure](#directory-structure)
- [Design Principles](#design-principles)
- [Metadata Architecture](#metadata-architecture)
- [Role of Each File](#role-of-each-file)
- [One Source, Multi Use](#one-source-multi-use-1)
- [Intended Users](#intended-users)
- [Use and Maintenance Policy](#use-and-maintenance-policy)
- [Future Extensions](#future-extensions)
- [Related Directories](#related-directories)
- [License](#license)

---

# 日本語

## クイックアクセス

| 内容 | ファイル・ディレクトリ |
|---|---|
| 正本メタデータ | [`shinso-ondo.yaml`](shinso-ondo.yaml) |
| スキーマ | [`schema/shinso-ondo.schema.yaml`](schema/shinso-ondo.schema.yaml) |
| 役割語彙 | [`vocabularies/roles.yaml`](vocabularies/roles.yaml) |
| その他の統制語彙 | [`vocabularies/values.yaml`](vocabularies/values.yaml) |
| リポジトリ全体の説明 | [`../README.md`](../README.md) |

---

## このディレクトリの役割

`metadata/` は、「新荘音頭デジタルアーカイブ」における情報基盤です。

本ディレクトリでは、作品・表現・実演・権利・公開情報・歌詞・クレジット等に関する情報を正本として管理し、Webページ、公開資料、構造化データおよび将来の外部連携へ再利用できる状態を維持します。

この役割を明確にするため、次の三つを分離して管理します。

- 実データ（Instance）
- 構造（Schema）
- 統制語彙（Controlled Vocabulary）

---

## ディレクトリ構成

```text
metadata/
├── README.md
├── shinso-ondo.yaml
├── schema/
│   └── shinso-ondo.schema.yaml
└── vocabularies/
    ├── roles.yaml
    └── values.yaml
```

---

## 設計原則

本ディレクトリは、ルートREADMEに示した設計原則を、メタデータ管理のレイヤーで具体化します。

### One Source, Multi Use

同じ情報を複数箇所で個別に管理せず、役割ごとに正本を定め、複数の出力へ再利用します。

### Single Source of Truth

作品データ、構造定義、役割語彙、統制値について、それぞれ一つの正本を管理します。

### Human-Readable

人が内容を確認し、修正理由や構造を理解できる記述を採用します。

### Machine-Readable

YAMLによる構造化記述とスキーマによる検証を通じて、ソフトウェアによる処理・変換・再利用を可能にします。

### AI-Recognizable

見出し、ファイル名、階層構造、リンク関係および役割の明示によって、AIを活用した情報システムが各データの文脈と関係を把握しやすい構成を目指します。

---

## メタデータアーキテクチャ

本メタデータモデルでは、実データ・構造・統制語彙を明確に分離しています。

```text
Controlled Vocabulary
          │
          ▼
       Schema
          │
          ▼
 Canonical Metadata
```

それぞれの役割は次のとおりです。

| レイヤー | 役割 |
|---|---|
| Controlled Vocabulary | 使用できる役割名や値を定義する |
| Schema | キー、型、必須項目、配列、URI、日付形式等を定義する |
| Canonical Metadata | 実際の作品情報、クレジット、歌詞、権利情報等を記述する |

この三層構造により、保守性、再利用性、機械可読性、検証可能性および拡張性を確保します。

---

## 各ファイルの役割

### `shinso-ondo.yaml`

「新荘音頭デジタルアーカイブ」の正本メタデータです。

作品、表現、実演、権利、公開情報、歌詞、クレジット等の実データを管理します。

このファイルのみが、作品データの正本（Canonical Metadata）です。

---

### `schema/shinso-ondo.schema.yaml`

メタデータ構造を定義するスキーマです。

主に次の内容を定義します。

- キー名
- 必須項目
- データ型
- 日付形式
- URI形式
- 配列構造
- 列挙値
- バリデーション規則

このファイルは、メタデータの機械的検証（Validation）に使用します。

---

### `vocabularies/roles.yaml`

制作・創作・実演・監修等に関する役割（Role）の統制語彙です。

各役割について、次の情報を管理します。

- 優先語（Preferred Label）
- 定義（Definition）
- 上位概念
- 関連概念

---

### `vocabularies/values.yaml`

役割以外の統制語彙を管理します。

例：

- `agent_type`
- `relation`
- `resource_type`
- `manifestation_type`
- `file_role`
- `publication_status`
- `permission_status`
- `rights_status`
- `genre`

---

## One Source, Multi Use

本ディレクトリでは、役割ごとに正本を一つだけ管理します。

| 役割 | 正本 |
|---|---|
| 作品データ | `shinso-ondo.yaml` |
| 構造定義 | `schema/shinso-ondo.schema.yaml` |
| 役割語彙 | `vocabularies/roles.yaml` |
| 統制値 | `vocabularies/values.yaml` |

これは、One Source, Multi Use の原則を維持しながら、それぞれの責務を分離する設計です。

正本データは、将来的に次のような出力へ展開できます。

- 歌詞ページ
- メタデータ表示ページ
- Schema.org JSON-LD
- IIIF Manifest
- RDF
- 検索・案内・研究支援システム

---

## 想定する利用者

本ディレクトリは、主に次の利用者および利用環境を想定しています。

- デジタルアーカイブの管理者
- メタデータ設計者
- 開発者
- 地域文化・郷土史の研究者
- 構造化データを利用する情報システム
- AIを活用した検索・案内・研究支援システム

---

## 利用・更新方針

### 正本の更新

作品データを変更する場合は、原則として `shinso-ondo.yaml` を更新します。

歌詞ページやその他の表示用ファイルを直接修正し、同じ情報を別個に管理することは避けます。

### 構造の変更

キー、必須項目、型、配列構造等を変更する場合は、`schema/shinso-ondo.schema.yaml` も更新します。

### 語彙の追加・変更

役割名や統制値を追加・変更する場合は、対応する語彙ファイルを更新します。

### 履歴の保存

変更内容、理由、日時はGitHubのコミット履歴として保存します。

公開版として固定する必要がある場合は、GitHub Releasesを使用します。

---

## 将来の拡張

本メタデータモデルは、将来的に次の形式および技術への展開を想定しています。

- JSON-LD
- Schema.org
- IIIF Manifest
- RDF
- SKOS
- SHACL
- Linked Open Data（LOD）
- GitHub Actionsによる自動検証・変換
- 外部システムとのデータ連携

実データ、構造、統制語彙を分離することで、特定の出力形式に依存せず、将来の変換や相互運用性に対応できる設計としています。

---

## 関連ディレクトリ

| ディレクトリ | 関係 |
|---|---|
| [`../lyrics/`](../lyrics/) | 正本メタデータから歌詞を表示する利用者向けページ |
| [`../contributors/`](../contributors/) | 制作者・協力者に関する表示 |
| [`../development/`](../development/) | 設計・実装・研究記録 |
| [`../editorial-policy/`](../editorial-policy/) | 編集・更新に関する方針 |
| [`../README.md`](../README.md) | リポジトリ全体の入口と設計方針 |

---

## ライセンス

本メタデータモデルは、「新荘音頭デジタルアーカイブ」の一部として公開しています。

ライセンスについては、リポジトリルートの [`LICENSE`](../LICENSE) を参照してください。

---

# English

## Quick Access

| Content | File or Directory |
|---|---|
| Canonical metadata | [`shinso-ondo.yaml`](shinso-ondo.yaml) |
| Schema | [`schema/shinso-ondo.schema.yaml`](schema/shinso-ondo.schema.yaml) |
| Role vocabulary | [`vocabularies/roles.yaml`](vocabularies/roles.yaml) |
| Other controlled values | [`vocabularies/values.yaml`](vocabularies/values.yaml) |
| Repository overview | [`../README.md`](../README.md) |

---

## Role of This Directory

The `metadata/` directory is the information foundation of the Shinso Ondo Digital Archive.

It manages authoritative information about the work, expressions, performances, rights, publication, lyrics, and credits, and maintains that information for reuse in web pages, publications, structured data, and future external services.

To make these responsibilities explicit, the directory separates:

- instance data;
- schema definitions; and
- controlled vocabularies.

---

## Directory Structure

```text
metadata/
├── README.md
├── shinso-ondo.yaml
├── schema/
│   └── shinso-ondo.schema.yaml
└── vocabularies/
    ├── roles.yaml
    └── values.yaml
```

---

## Design Principles

This directory implements the design principles stated in the root README at the metadata-management layer.

### One Source, Multi Use

The same information is not maintained independently in multiple locations. One authoritative source is defined for each responsibility and reused for multiple outputs.

### Single Source of Truth

A single authoritative source is maintained for work data, schema definitions, role vocabularies, and controlled values.

### Human-Readable

The data and documentation are written so that people can inspect the content and understand its structure and the reasons for changes.

### Machine-Readable

Structured YAML and schema-based validation enable software processing, conversion, and reuse.

### AI-Recognizable

Headings, file names, directory structures, link relationships, and explicit role descriptions are organized so that AI-assisted information systems can more easily identify the context and relationships of the data.

---

## Metadata Architecture

This metadata model clearly separates instance data, structural definitions, and controlled vocabularies.

```text
Controlled Vocabulary
          │
          ▼
       Schema
          │
          ▼
 Canonical Metadata
```

| Layer | Role |
|---|---|
| Controlled Vocabulary | Defines permitted roles and values |
| Schema | Defines keys, data types, required fields, arrays, URIs, and date formats |
| Canonical Metadata | Records actual work information, credits, lyrics, and rights information |

This three-layer architecture supports maintainability, reusability, machine readability, validation, and extensibility.

---

## Role of Each File

### `shinso-ondo.yaml`

The canonical metadata file for the Shinso Ondo Digital Archive.

It manages instance data concerning the work, expressions, performances, rights, publication information, lyrics, and credits.

This file is the only authoritative source for the work data.

---

### `schema/shinso-ondo.schema.yaml`

The schema defining the metadata structure.

It primarily defines:

- key names;
- required fields;
- data types;
- date formats;
- URI formats;
- array structures;
- enumerated values; and
- validation rules.

This file is used for machine validation of the metadata.

---

### `vocabularies/roles.yaml`

The controlled vocabulary for roles related to creation, production, performance, supervision, and related activities.

For each role, it manages:

- preferred labels;
- definitions;
- broader concepts; and
- related concepts.

---

### `vocabularies/values.yaml`

This file manages controlled values other than roles.

Examples include:

- `agent_type`
- `relation`
- `resource_type`
- `manifestation_type`
- `file_role`
- `publication_status`
- `permission_status`
- `rights_status`
- `genre`

---

## One Source, Multi Use

This directory maintains one authoritative source for each responsibility.

| Responsibility | Authoritative Source |
|---|---|
| Work data | `shinso-ondo.yaml` |
| Structural definition | `schema/shinso-ondo.schema.yaml` |
| Role vocabulary | `vocabularies/roles.yaml` |
| Controlled values | `vocabularies/values.yaml` |

This design separates responsibilities while maintaining the principle of One Source, Multi Use.

The canonical data may be reused for future outputs such as:

- lyrics pages;
- metadata display pages;
- Schema.org JSON-LD;
- IIIF Manifests;
- RDF; and
- search, guidance, and research-support systems.

---

## Intended Users

This directory is primarily intended for:

- digital archive administrators;
- metadata designers;
- developers;
- researchers in local culture and local history;
- information systems that reuse structured data; and
- AI-assisted search, guidance, and research-support systems.

---

## Use and Maintenance Policy

### Updating Canonical Data

Changes to work data should, in principle, be made in `shinso-ondo.yaml`.

The same information should not be maintained independently by directly editing lyrics pages or other display files.

### Changing the Structure

When keys, required fields, data types, or array structures are changed, `schema/shinso-ondo.schema.yaml` should also be updated.

### Adding or Changing Vocabulary

When roles or controlled values are added or changed, the corresponding vocabulary file should be updated.

### Preserving History

The content, reason, and date of each change are preserved in the GitHub commit history.

GitHub Releases are used when a fixed published version is required.

---

## Future Extensions

This metadata model is designed for future development into formats and technologies including:

- JSON-LD;
- Schema.org;
- IIIF Manifests;
- RDF;
- SKOS;
- SHACL;
- Linked Open Data (LOD);
- automated validation and conversion using GitHub Actions; and
- data exchange with external systems.

By separating instance data, structure, and controlled vocabularies, the model can support future transformation and interoperability without depending on a single output format.

---

## Related Directories

| Directory | Relationship |
|---|---|
| [`../lyrics/`](../lyrics/) | Public-facing lyrics pages generated from or linked to the canonical metadata |
| [`../contributors/`](../contributors/) | Information about creators and contributors |
| [`../development/`](../development/) | Design, implementation, and research records |
| [`../editorial-policy/`](../editorial-policy/) | Editorial and maintenance policies |
| [`../README.md`](../README.md) | Main repository access point and design policy |

---

## License

This metadata model is published as part of the Shinso Ondo Digital Archive.

See [`LICENSE`](../LICENSE) in the repository root for licensing information.
