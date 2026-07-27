# Contributors

## 目次

- [クイックアクセス](#クイックアクセス)
- [このディレクトリの役割](#このディレクトリの役割)
- [ディレクトリ構成](#ディレクトリ構成)
- [制作・協力者情報の管理](#制作協力者情報の管理)
- [正本メタデータとの関係](#正本メタデータとの関係)
- [利用・保守方針](#利用保守方針)
- [関連ディレクトリ](#関連ディレクトリ)
- [ライセンス](#ライセンス)
- [English](#english)

---

## クイックアクセス

- GitHub Pages
  - `contributors/index.html`
- Canonical Metadata
  - `metadata/shinso-ondo.yaml`

---

## このディレクトリの役割

このディレクトリでは、『新荘音頭』の制作・協力者情報を公開します。

GitHub Pages の「制作・協力者」ページを構成し、作品制作に携わった人物・団体およびその役割を表示します。

本ディレクトリは、制作・協力者情報を公開するための表示層であり、クレジット情報の正本ではありません。

---

## ディレクトリ構成

```text
contributors/
├── README.md
└── index.html
```

---

## 制作・協力者情報の管理

`index.html` は `metadata/shinso-ondo.yaml` に記録された制作・協力者情報を読み込み、GitHub Pages 上で表示します。

表示対象には、

- 作品全体に関わる制作・協力者情報（`work.contributors`）
- 各音源に記録された歌唱・演奏者情報（`performances.performers`）
- 各音源の録音・制作等のクレジット情報（`performances.manifestation.credits`）

が含まれます。

表示時には、同一人物に関する複数のレコードを人物単位に統合し、重複する役割を整理したうえで、役割ごとに表示します。

---

## 正本メタデータとの関係

制作・協力者情報の正本（Single Source of Truth）は、`metadata/shinso-ondo.yaml` です。

本ディレクトリでは、このメタデータを利用して表示を生成します。

制作・協力者情報の追加・修正・削除は、`metadata/shinso-ondo.yaml` を更新してください。

リポジトリ全体の設計方針については、ルートディレクトリの `README.md` を参照してください。

---

## 利用・保守方針

- 制作・協力者情報は `metadata/shinso-ondo.yaml` を正本として管理します。
- `index.html` は正本メタデータから表示を生成します。
- 画像などの共通リソースは、リポジトリ共通の `images/` ディレクトリで管理します。

---

## 関連ディレクトリ

- `metadata/`
- `images/`

---

## ライセンス

このディレクトリに含まれるコンテンツは、リポジトリ全体のライセンスに従います。

---

# English

## Quick Access

- GitHub Pages
  - `contributors/index.html`
- Canonical Metadata
  - `metadata/shinso-ondo.yaml`

---

## Role of This Directory

This directory provides information about the contributors involved in the creation of **Shinsō Ondo**.

It contains the GitHub Pages source for the **Contributors** page and presents contributor information based on the project's canonical metadata.

This directory is a presentation layer and is not the canonical source of contributor metadata.

---

## Directory Structure

```text
contributors/
├── README.md
└── index.html
```

---

## Contributor Information

`index.html` reads contributor information from `metadata/shinso-ondo.yaml` and generates the Contributors page for GitHub Pages.

The displayed information includes:

- Work-level contributors (`work.contributors`)
- Performers recorded for each manifestation (`performances.performers`)
- Credits associated with each manifestation (`performances.manifestation.credits`)

During rendering, multiple records referring to the same person are grouped together, duplicate role entries are consolidated, and the resulting information is organized by role for display.

---

## Relationship to the Canonical Metadata

The canonical source (Single Source of Truth) for contributor information is `metadata/shinso-ondo.yaml`.

This directory generates its contents from that metadata.

To add, modify, or remove contributor information, edit `metadata/shinso-ondo.yaml`.

For the overall repository design, see the root `README.md`.

---

## Maintenance Policy

- Maintain contributor metadata in `metadata/shinso-ondo.yaml`.
- Generate contributor pages from the canonical metadata.
- Store shared image resources in the repository-wide `images/` directory.

---

## Related Directories

- `metadata/`
- `images/`

---

## License

The contents of this directory are distributed under the same license as the repository.
