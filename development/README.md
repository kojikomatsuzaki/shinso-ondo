# Development

## 目次

- [クイックアクセス](#クイックアクセス)
- [このディレクトリの役割](#このディレクトリの役割)
- [ディレクトリ構成](#ディレクトリ構成)
- [各文書の役割](#各文書の役割)
- [リポジトリとの関係](#リポジトリとの関係)
- [利用・保守方針](#利用保守方針)
- [関連ディレクトリ](#関連ディレクトリ)
- [ライセンス](#ライセンス)
- [English](#english)

---

## クイックアクセス

- Repository Policy
  - ルート `README.md`
- Canonical Metadata
  - `metadata/shinso-ondo.yaml`

---

## このディレクトリの役割

このディレクトリでは、「新荘音頭デジタルアーカイブ」の設計、実装、運用および研究に関する記録を管理します。

ここで扱う文書は、公開作品そのものではなく、アーカイブを継続的に構築・保守・発展させるための補助資料です。

作品情報、歌詞、音源、楽譜、制作・協力者情報などの公開資料は、それぞれのディレクトリで管理します。

---

## ディレクトリ構成

```text
development/
├── README.md
├── design-decisions.md
├── development-notes.md
└── research-notes.md
```

---

## 各文書の役割

### README.md

本ディレクトリの構成と各文書の役割を説明します。

### design-decisions.md

採用した設計判断と、その理由を記録します。

「何を実装したか」ではなく、「なぜその設計を採用したか」を記録する文書です。

### development-notes.md

アーカイブの構築・更新に関する主要な変更を時系列で記録します。

### research-notes.md

アーカイブ構築・運用を通して得られた知見、課題および研究上の論点を記録します。

---

## リポジトリとの関係

本ディレクトリは、公開資料や正本メタデータを管理する場所ではありません。

作品、歌詞、制作・協力者、音源および関連資料に関する構造化データは、原則として

```text
metadata/shinso-ondo.yaml
```

を正本（Single Source of Truth）として管理します。

また、リポジトリ全体の構成、版管理および保存方針については、ルートディレクトリの `README.md` を参照してください。

---

## 利用・保守方針

- 設計判断は `design-decisions.md` に記録します。
- 実装・更新履歴は `development-notes.md` に記録します。
- 研究上の知見は `research-notes.md` に記録します。
- 同一内容を複数の文書へ重複して記録しません。
- リポジトリ全体に関わる方針は、ルート `README.md` に集約します。

---

## 関連ディレクトリ

- `metadata/`
- `editorial-policy/`
- `contributors/`
- `lyrics/`
- `scores/`
- `audio/`
- `publications/`

---

## ライセンス

このディレクトリに含まれる文書は、リポジトリ全体のライセンスに従います。

---

# English

## Quick Access

- Repository Policy
  - Root `README.md`
- Canonical Metadata
  - `metadata/shinso-ondo.yaml`

---

## Role of This Directory

This directory contains documentation related to the design, implementation, maintenance, and research of the **Shinsō Ondo Digital Archive**.

The documents stored here support the development and long-term maintenance of the archive rather than describing the cultural resources themselves.

Public materials, including lyrics, recordings, scores, publications, and contributor information, are managed in their respective directories.

---

## Directory Structure

```text
development/
├── README.md
├── design-decisions.md
├── development-notes.md
└── research-notes.md
```

---

## Role of Each Document

### README.md

Explains the purpose of this directory and the role of each document.

### design-decisions.md

Records the major design decisions adopted during the project and the reasons behind them.

### development-notes.md

Records significant development and maintenance activities in chronological order.

### research-notes.md

Records observations, issues, and research findings obtained through the design, implementation, and operation of the archive.

---

## Relationship to the Repository

This directory is not used to manage public materials or canonical metadata.

Structured information concerning the work, lyrics, contributors, recordings, and related resources is generally maintained in

```text
metadata/shinso-ondo.yaml
```

as the canonical source (Single Source of Truth).

For repository-wide structure, versioning, and preservation policies, see the root `README.md`.

---

## Use and Maintenance Policy

- Record design decisions in `design-decisions.md`.
- Record implementation and maintenance history in `development-notes.md`.
- Record research findings in `research-notes.md`.
- Avoid duplicating the same information across multiple documents.
- Repository-wide policies are maintained in the root `README.md`.

---

## Related Directories

- `metadata/`
- `editorial-policy/`
- `contributors/`
- `lyrics/`
- `scores/`
- `audio/`
- `publications/`

---

## License

The documents in this directory are distributed under the same license as the repository.
