# 公開資料 / Publications

このディレクトリには、**新荘音頭デジタルアーカイブ**に関するパンフレットなどの公開資料を収録しています。

公開資料は、視覚的な再現性を保ちながら、文字検索やテキスト抽出が可能な形式で提供することを基本とします。

---

## 目次

- [クイックアクセス](#クイックアクセス)
- [このディレクトリの役割](#このディレクトリの役割)
- [ディレクトリ構成](#ディレクトリ構成)
- [公開資料](#公開資料)
- [正本メタデータとの関係](#正本メタデータとの関係)
- [版管理・保存方針](#版管理保存方針)
- [利用・保守方針](#利用保守方針)
- [関連ディレクトリ](#関連ディレクトリ)
- [ライセンス](#ライセンス)
- [English](#english)
  - [Quick Access](#quick-access)
  - [Role of This Directory](#role-of-this-directory)
  - [Directory Structure](#directory-structure)
  - [Official Publications](#official-publications)
  - [Relationship to the Canonical Metadata](#relationship-to-the-canonical-metadata)
  - [Versioning and Preservation Policy](#versioning-and-preservation-policy)
  - [Use and Maintenance Policy](#use-and-maintenance-policy)
  - [Related Directories](#related-directories)
  - [License](#license)

---

## クイックアクセス

- [2026年公開資料](./2026/)
- [新荘音頭パンフレット（2026年7月26日公開）](./2026/shinso-ondo-pamphlet-20260726.pdf)
- [リポジトリ全体のREADME](../README.md)
- [正本メタデータ](../metadata/shinso-ondo.yaml)

---

## このディレクトリの役割

`publications/` は、新荘音頭に関して正式に公開されたパンフレットなどの資料を、公開年ごとに整理して保存するためのディレクトリです。

このディレクトリには、原則として次の資料を収録します。

- 正式に公開されたパンフレット
- 配布用冊子
- 解説資料
- その他、新荘音頭制作委員会が公開資料として位置づけた文書

制作途中の版、校正用ファイル、作業用データは、正式な公開資料としては収録しません。

---

## ディレクトリ構成

```text
publications/
├── README.md
└── 2026/
    ├── README.md
    └── shinso-ondo-pamphlet-20260726.pdf
```

公開資料は、原則として公開年ごとのサブディレクトリに収録します。

---

## 公開資料

現在公開している資料は次のとおりです。

### 2026年

- [`shinso-ondo-pamphlet-20260726.pdf`](./2026/shinso-ondo-pamphlet-20260726.pdf)
  - 資料名：新荘音頭パンフレット
  - 対象作品：新荘音頭 ― 新荘よいとこ散歩道
  - 公開日：2026年7月26日
  - 形式：PDF
  - 特徴：フォント埋め込み済み・文字検索可能

PDF内で使用されているフォントはサブセットとして埋め込まれており、閲覧環境に同一フォントがない場合でも、版面を維持して表示できます。

また、文字情報を保持しているため、文字検索やテキスト抽出が可能です。

---

## 正本メタデータとの関係

新荘音頭に関する基本情報の正本は、次のファイルです。

```text
metadata/shinso-ondo.yaml
```

公開資料は、制作時点における情報を固定した、公開物としての記録です。

そのため、パンフレットに記載された内容と、後日更新された正本メタデータの内容が異なる場合があります。

現在の作品情報、クレジット、ライセンス情報などを確認する場合は、正本メタデータを参照してください。

---

## 版管理・保存方針

このディレクトリには、正式に公開された版を保存します。

制作途中の版、校正中の版、誤って登録されたファイルなどは、独立した公開資料として保存せず、必要に応じてGitの履歴から確認します。

リポジトリ全体に共通する次の区分については、ルートディレクトリの [`README.md`](../README.md) を参照してください。

- Current Edition
- Legacy Edition
- Git History

---

## 利用・保守方針

公開資料は、可能な限り次の条件を満たす形式で提供します。

- フォントが埋め込まれている
- 文字検索が可能である
- テキストを抽出できる
- 閲覧環境による版面の変化を抑えられる
- 長期的な閲覧と再利用に適している

アウトライン化したPDFは、印刷工程などで技術的に必要な場合を除き、通常の公開版としては使用しません。

検索可能なPDFで版面を維持できる場合は、視覚的な再現性と機械可読性を両立できるため、そのPDFを正式公開版とします。

---

## 関連ディレクトリ

- [`../metadata/`](../metadata/) — 正本メタデータ
- [`../lyrics/`](../lyrics/) — 歌詞
- [`../scores/`](../scores/) — 楽譜
- [`../audio/`](../audio/) — 音源
- [`../contributors/`](../contributors/) — 制作関係者
- [`../editorial-policy/`](../editorial-policy/) — 編集方針

---

## ライセンス

新荘音頭の歌詞、楽曲、振付および関連資料の利用条件については、ルートディレクトリの [`README.md`](../README.md) と各資料内の表示を参照してください。

原則として、新荘音頭デジタルアーカイブの対象資料には、**Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International（CC BY-NC-SA 4.0）**が適用されます。

ただし、個別の資料に異なる権利表示がある場合は、その表示を優先します。

---

# English

This directory contains pamphlets and other official publications related to the **Shinsō Ondo Digital Archive**.

Publications are provided in formats that preserve their visual presentation while retaining searchable and extractable text whenever possible.

---

## Quick Access

- [Publications released in 2026](./2026/)
- [Shinsō Ondo Pamphlet, released July 26, 2026](./2026/shinso-ondo-pamphlet-20260726.pdf)
- [Repository README](../README.md)
- [Canonical metadata](../metadata/shinso-ondo.yaml)

---

## Role of This Directory

The `publications/` directory preserves officially released pamphlets and other documents related to Shinsō Ondo, organized by year of publication.

This directory may contain:

- officially released pamphlets
- booklets prepared for distribution
- explanatory materials
- other documents designated as official publications by the Shinsō Ondo Production Committee

Drafts, proofreading files, intermediate revisions, and working data are not treated as official publications.

---

## Directory Structure

```text
publications/
├── README.md
└── 2026/
    ├── README.md
    └── shinso-ondo-pamphlet-20260726.pdf
```

Publications are generally stored in subdirectories corresponding to their year of release.

---

## Official Publications

The following publication is currently available.

### 2026

- [`shinso-ondo-pamphlet-20260726.pdf`](./2026/shinso-ondo-pamphlet-20260726.pdf)
  - Title: Shinsō Ondo Pamphlet
  - Work: *Shinsō Ondo – Shinsō Yoitoko Sanpomichi*
  - Release date: July 26, 2026
  - Format: PDF
  - Features: embedded fonts and searchable text

The fonts used in the PDF are embedded as subsets. This allows the document to preserve its visual layout even when the same fonts are not installed on the viewing device.

The document also retains text information, allowing text search and extraction.

---

## Relationship to the Canonical Metadata

The canonical source of basic information about Shinsō Ondo is:

```text
metadata/shinso-ondo.yaml
```

Each publication is a fixed record of the information presented at the time of its release.

The information printed in a pamphlet may therefore differ from canonical metadata that has subsequently been updated.

For the current work information, credits, and licensing information, refer to the canonical metadata.

---

## Versioning and Preservation Policy

This directory preserves officially released editions.

Drafts, intermediate revisions, proofreading files, and mistakenly committed files are not preserved as separate official publications. When necessary, their technical editing history can be reviewed through Git.

For the repository-wide distinction among the following categories, see the root [`README.md`](../README.md):

- Current Edition
- Legacy Edition
- Git History

---

## Use and Maintenance Policy

Whenever possible, publications are provided in formats that meet the following conditions:

- fonts are embedded
- text is searchable
- text can be extracted
- layout changes between viewing environments are minimized
- the format is suitable for long-term access and reuse

Outlined PDFs are not normally used as public editions unless they are technically required for printing or another production process.

When a searchable PDF can preserve the intended layout, it is used as the official public edition because it combines visual fidelity with machine readability.

---

## Related Directories

- [`../metadata/`](../metadata/) — Canonical metadata
- [`../lyrics/`](../lyrics/) — Lyrics
- [`../scores/`](../scores/) — Musical scores
- [`../audio/`](../audio/) — Audio recordings
- [`../contributors/`](../contributors/) — Contributors
- [`../editorial-policy/`](../editorial-policy/) — Editorial policy

---

## License

For the terms governing the lyrics, music, choreography, and related materials, see the root [`README.md`](../README.md) and the rights statement included in each publication.

As a general rule, materials in the Shinsō Ondo Digital Archive are made available under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License（CC BY-NC-SA 4.0）**.

When an individual publication includes a different rights statement, that statement takes precedence.
