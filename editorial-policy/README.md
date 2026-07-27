# Editorial Policy

## 目次

- [クイックアクセス](#クイックアクセス)
- [このディレクトリの役割](#このディレクトリの役割)
- [ディレクトリ構成](#ディレクトリ構成)
- [編集方針の対象](#編集方針の対象)
- [正本メタデータとの関係](#正本メタデータとの関係)
- [版管理と保存方針](#版管理と保存方針)
- [利用・保守方針](#利用保守方針)
- [関連ディレクトリ](#関連ディレクトリ)
- [ライセンス](#ライセンス)
- [English](#english)

---

## クイックアクセス

- GitHub Pages
  - `editorial-policy/index.html`
- Canonical Metadata
  - `metadata/shinso-ondo.yaml`
- Repository Policy
  - ルートディレクトリの `README.md`

---

## このディレクトリの役割

このディレクトリでは、「新荘音頭デジタルアーカイブ」における編集方針を公開します。

編集方針は、資料の収集、記述、公開、更新、権利処理および管理に関する基本的な考え方を示すものです。

`index.html` は、GitHub Pagesで公開する正式な編集方針ページです。

本ディレクトリは編集方針の公開を目的とするものであり、作品情報、歌詞、制作・協力者情報、音源情報等の正本を管理する場所ではありません。

---

## ディレクトリ構成

```text
editorial-policy/
├── README.md
└── index.html
```

---

## 編集方針の対象

編集方針では、主として次の事項を扱います。

- アーカイブの基本方針
- 収録対象
- 情報源と記述の根拠
- メタデータの位置付け
- 原資料と解説・注記の区別
- 人名およびクレジットの記録
- ファイル名および識別方法
- 更新および版管理
- 訂正および情報提供への対応
- 著作権および利用条件
- 個人情報およびプライバシー
- アクセシビリティ
- 地域的文脈の尊重
- 編集および管理体制

編集方針の本文は、`index.html` で公開します。

本READMEでは、編集方針の内容を重複して掲載せず、このディレクトリの役割とリポジトリ内での位置付けを説明します。

---

## 正本メタデータとの関係

作品、歌詞、制作・協力者、音源、クレジットおよび関連資料に関する構造化データは、原則として次のファイルを正本（Single Source of Truth）として管理します。

```text
metadata/shinso-ondo.yaml
```

編集方針は、正本メタデータに記録する情報の根拠、記述方法および更新方法を定めます。

一方、具体的な作品情報やクレジット情報は、編集方針ページへ直接記載して管理するのではなく、正本メタデータへ記録します。

正本メタデータと各公開ページの関係については、ルートディレクトリおよび `metadata/` ディレクトリの `README.md` を参照してください。

---

## 版管理と保存方針

編集方針の変更履歴は、GitHubのコミット履歴によって管理します。

現在有効な編集方針は `index.html` で公開し、過去の状態は原則としてGitの履歴から確認します。

リポジトリ全体のCurrent、Legacy、Git HistoryおよびGitHub Releasesに関する方針は、ルートディレクトリの `README.md` を参照してください。

---

## 利用・保守方針

- 編集方針の本文は `index.html` で管理します。
- 編集方針を変更する場合は、正本メタデータおよび各公開ページとの整合性を確認します。
- 資料の追加、技術環境の変化、権利関係の確認その他の事情に応じて、編集方針を見直すことがあります。
- 編集方針と具体的なメタデータを混在させず、それぞれの役割を分けて管理します。
- 共通するアーカイブ設計、版管理および保存方針は、ルートディレクトリの `README.md` に集約します。

---

## 関連ディレクトリ

- `metadata/`
- `contributors/`
- `lyrics/`
- `scores/`
- `audio/`
- `publications/`

---

## ライセンス

このディレクトリに含まれるコンテンツは、リポジトリ全体のライセンスに従います。

---

# English

## Quick Access

- GitHub Pages
  - `editorial-policy/index.html`
- Canonical Metadata
  - `metadata/shinso-ondo.yaml`
- Repository Policy
  - Root `README.md`

---

## Role of This Directory

This directory publishes the editorial policy of the **Shinsō Ondo Digital Archive**.

The editorial policy sets out the basic principles governing the collection, description, publication, revision, rights management, and maintenance of archival materials.

`index.html` is the official editorial policy page published through GitHub Pages.

This directory is intended for the publication of editorial policy. It is not the canonical source for information about the work, lyrics, contributors, recordings, or related materials.

---

## Directory Structure

```text
editorial-policy/
├── README.md
└── index.html
```

---

## Scope of the Editorial Policy

The editorial policy primarily addresses the following areas:

- Basic principles of the archive
- Scope of collected materials
- Sources and evidence used for description
- Role of metadata
- Distinction between original materials and explanatory notes
- Recording of personal names and credits
- File naming and identification
- Revision and version management
- Corrections and submitted information
- Copyright and conditions of use
- Personal information and privacy
- Accessibility
- Respect for regional context
- Editorial and administrative responsibility

The full editorial policy is published in `index.html`.

This README does not duplicate the policy itself. Instead, it explains the role of this directory and its relationship to the rest of the repository.

---

## Relationship to the Canonical Metadata

Structured data concerning the work, lyrics, contributors, recordings, credits, and related materials is generally maintained in the following file as the canonical source, or Single Source of Truth:

```text
metadata/shinso-ondo.yaml
```

The editorial policy defines the principles used to determine the evidence, description methods, and revision procedures applied to the canonical metadata.

Specific information about the work or its contributors is not maintained directly in the editorial policy page. Such information is recorded in the canonical metadata.

For details about the relationship between the canonical metadata and public pages, see the root `README.md` and the README in the `metadata/` directory.

---

## Versioning and Preservation Policy

Changes to the editorial policy are recorded through the GitHub commit history.

The currently valid editorial policy is published in `index.html`, while previous states are generally preserved through Git history.

For repository-wide policies concerning Current materials, Legacy materials, Git History, and GitHub Releases, see the root `README.md`.

---

## Use and Maintenance Policy

- Maintain the full editorial policy in `index.html`.
- When revising the editorial policy, confirm its consistency with the canonical metadata and related public pages.
- Review the policy when new materials are added, technical conditions change, rights are clarified, or other relevant circumstances arise.
- Keep editorial principles separate from specific metadata records.
- Maintain repository-wide archive design, versioning, and preservation policies in the root `README.md`.

---

## Related Directories

- `metadata/`
- `contributors/`
- `lyrics/`
- `scores/`
- `audio/`
- `publications/`

---

## License

The contents of this directory are distributed under the same license as the repository.
