# Lyrics

「新荘音頭」（副題：「新荘よいとこ散歩道」）の歌詞公開ページおよび歌詞に関する保存資料を収録するディレクトリです。

本ディレクトリは、歌詞そのものを重複管理する場所ではなく、利用者向けの閲覧ページ、過去時点のスナップショット、および正本メタデータへの案内を提供します。

---

## Table of Contents

### 日本語

- [クイックアクセス](#クイックアクセス)
- [このディレクトリの役割](#このディレクトリの役割)
- [ディレクトリ構成](#ディレクトリ構成)
- [正本メタデータとの関係](#正本メタデータとの関係)
- [公開歌詞ページ](#公開歌詞ページ)
- [Legacy資料とスナップショット](#legacy資料とスナップショット)
- [典拠](#典拠)
- [利用・更新方針](#利用更新方針)
- [関連ディレクトリ](#関連ディレクトリ)
- [ライセンス](#ライセンス)

### English

- [Quick Access](#quick-access)
- [Role of This Directory](#role-of-this-directory)
- [Directory Structure](#directory-structure)
- [Relationship to the Canonical Metadata](#relationship-to-the-canonical-metadata)
- [Public Lyrics Page](#public-lyrics-page)
- [Legacy Material and Snapshot](#legacy-material-and-snapshot)
- [Source](#source)
- [Use and Maintenance Policy](#use-and-maintenance-policy)
- [Related Directories](#related-directories)
- [License](#license)

---

# 日本語

## クイックアクセス

| 内容 | ファイル・ページ |
|---|---|
| 利用者向け歌詞ページ | [`index.html`](index.html) |
| Legacy歌詞資料 | [`shinso-ondo-lyrics.md`](shinso-ondo-lyrics.md) |
| 正本メタデータ | [`../metadata/shinso-ondo.yaml`](../metadata/shinso-ondo.yaml) |
| メタデータ設計 | [`../metadata/README.md`](../metadata/README.md) |
| リポジトリ全体の説明 | [`../README.md`](../README.md) |

---

## このディレクトリの役割

`lyrics/` は、「新荘音頭」の歌詞へアクセスするための案内板です。

このディレクトリでは、次の三つの役割を明確に分けています。

1. 利用者向けの歌詞表示
2. 過去時点の歌詞資料の保存
3. 正本メタデータへの案内

歌詞やクレジットを複数のファイルで独立して更新するのではなく、正本を一つに定め、その内容を用途に応じて表示・保存します。

---

## ディレクトリ構成

```text
lyrics/
├── README.md
├── index.html
└── shinso-ondo-lyrics.md
```

| ファイル | 役割 |
|---|---|
| `README.md` | このディレクトリの構成・利用方法・更新方針を示す |
| `index.html` | 利用者向けに最新版の歌詞を表示する |
| `shinso-ondo-lyrics.md` | 2026年7月23日時点の歌詞を保存したLegacy資料 |

---

## 正本メタデータとの関係

歌詞、読み、クレジット、権利情報等の正本（Single Source of Truth）は、次のファイルです。

[`../metadata/shinso-ondo.yaml`](../metadata/shinso-ondo.yaml)

`lyrics/` 内の表示用・保存用ファイルは、それぞれ異なる目的を持ちますが、最新の作品情報を独立して管理する正本ではありません。

役割の関係は次のとおりです。

```text
metadata/shinso-ondo.yaml
        │
        ├── lyrics/index.html
        │      利用者向けの最新版表示
        │
        └── lyrics/shinso-ondo-lyrics.md
               過去時点のスナップショット
```

---

## 公開歌詞ページ

[`index.html`](index.html) は、一般利用者が歌詞を閲覧するための公開ページです。

最新版の歌詞を確認・利用する場合は、このページを参照してください。

このページは、正本メタデータを利用者向けに提示する表示層として位置づけています。

---

## Legacy資料とスナップショット

[`shinso-ondo-lyrics.md`](shinso-ondo-lyrics.md) は、2026年7月23日まで使用していた旧形式（Legacy）の歌詞ファイルです。

このファイルは、2026年7月23日時点の歌詞を示す**スナップショット**として保存しています。

保存の目的は次のとおりです。

- 過去のリポジトリ構成との整合性を保つ
- 旧形式で公開していた内容を確認できるようにする
- 歌詞・表記・クレジットの変更過程を記録する
- デジタルアーカイブの形成過程そのものを保存する

このファイルは歴史的・記録的資料であり、今後更新されません。

現在の最新版や正確な作品情報を確認する際は、次のいずれかを参照してください。

- [`../metadata/shinso-ondo.yaml`](../metadata/shinso-ondo.yaml)
- [`index.html`](index.html)

---

## 典拠

現在公開している歌詞およびクレジットは、関係者間の確認を経て確定した次の資料に基づいています。

**2026年7月26日付パンフレット  
『新荘音頭―新荘よいとこ散歩道―』**

典拠資料と正本メタデータは役割が異なります。

- 典拠資料：内容を確認・確定する根拠
- 正本メタデータ：確定した内容を構造化して管理する唯一の正本

パンフレットは、[`../publications/2026/`](../publications/2026/) に収録しています。

---

## 利用・更新方針

### 歌詞の修正

歌詞、読み、クレジット等を修正する場合は、原則として次の正本を更新します。

[`../metadata/shinso-ondo.yaml`](../metadata/shinso-ondo.yaml)

同じ情報を複数のファイルで個別に更新し、内容を二重管理することは避けます。

### 表示ページの更新

`index.html` は利用者向けの表示層です。

表示方法やレイアウトを変更する場合は `index.html` を更新しますが、歌詞本文の正本としては扱いません。

### Legacy資料の扱い

`shinso-ondo-lyrics.md` はスナップショットとして保存するため、内容を更新しません。

誤字や表記差が見つかった場合でも、過去時点の記録として維持し、必要に応じて注記やコミット履歴で説明します。

### 履歴の保存

変更内容、理由、日時はGitHubのコミット履歴として保存します。

公開版として固定する必要がある場合は、GitHub Releasesを使用します。

---

## 関連ディレクトリ

| ディレクトリ | 関係 |
|---|---|
| [`../metadata/`](../metadata/) | 歌詞・読み・クレジット等の正本メタデータ |
| [`../publications/`](../publications/) | 歌詞の典拠となるパンフレット等 |
| [`../audio/`](../audio/) | 公式音源 |
| [`../scores/`](../scores/) | 楽譜 |
| [`../contributors/`](../contributors/) | 制作者・協力者に関する情報 |
| [`../development/`](../development/) | 設計・実装・研究記録 |
| [`../README.md`](../README.md) | リポジトリ全体の入口と設計方針 |

---

## ライセンス

別途記載がある場合を除き、本ディレクトリ内の資料は、次のライセンスにより公開しています。

**Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International  
（CC BY-NC-SA 4.0）**

利用時には、作品名、著作権者・ライセンサー、作詞者およびライセンスを表示してください。

- 著作権者・ライセンサー：新荘音頭制作委員会
- ライセンス：[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.ja)
- 詳細：[`../LICENSE`](../LICENSE)

---

# English

## Quick Access

| Content | File or Page |
|---|---|
| Public lyrics page | [`index.html`](index.html) |
| Legacy lyrics material | [`shinso-ondo-lyrics.md`](shinso-ondo-lyrics.md) |
| Canonical metadata | [`../metadata/shinso-ondo.yaml`](../metadata/shinso-ondo.yaml) |
| Metadata design | [`../metadata/README.md`](../metadata/README.md) |
| Repository overview | [`../README.md`](../README.md) |

---

## Role of This Directory

The `lyrics/` directory is the access point for the lyrics of **Shinso Ondo**  
(*Shinso Yoitoko Sanpomichi*).

It clearly separates three responsibilities:

1. public presentation of the lyrics;
2. preservation of lyrics from a previous point in time; and
3. access to the canonical metadata.

Rather than maintaining lyrics and credits independently in multiple files, the archive defines one authoritative source and uses display and preservation files for distinct purposes.

---

## Directory Structure

```text
lyrics/
├── README.md
├── index.html
└── shinso-ondo-lyrics.md
```

| File | Role |
|---|---|
| `README.md` | Describes the directory structure, use, and maintenance policy |
| `index.html` | Presents the current lyrics to general users |
| `shinso-ondo-lyrics.md` | Preserves the lyrics as they appeared on July 23, 2026 |

---

## Relationship to the Canonical Metadata

The Single Source of Truth for the lyrics, readings, credits, rights information, and related work data is:

[`../metadata/shinso-ondo.yaml`](../metadata/shinso-ondo.yaml)

The display and preservation files in `lyrics/` serve different purposes, but neither is an independent authoritative source for current work data.

```text
metadata/shinso-ondo.yaml
        │
        ├── lyrics/index.html
        │      Current public display
        │
        └── lyrics/shinso-ondo-lyrics.md
               Historical snapshot
```

---

## Public Lyrics Page

[`index.html`](index.html) is the public-facing page for viewing the lyrics.

Users should refer to this page when checking or using the current lyrics.

The page is treated as a presentation layer for the canonical metadata.

---

## Legacy Material and Snapshot

[`shinso-ondo-lyrics.md`](shinso-ondo-lyrics.md) is the former lyrics file used until July 23, 2026.

It is preserved as a **snapshot of the lyrics as they appeared on July 23, 2026**.

The purposes of preserving this file are to:

- maintain continuity with the previous repository structure;
- make the earlier published content available for review;
- document changes to lyrics, wording, and credits; and
- preserve the formation process of the digital archive itself.

This file is historical and documentary material and will not be updated.

For the current lyrics and authoritative work information, refer to:

- [`../metadata/shinso-ondo.yaml`](../metadata/shinso-ondo.yaml); or
- [`index.html`](index.html).

---

## Source

The lyrics and credits currently published are based on the following source, finalized through confirmation among the relevant participants:

**Shinso Ondo: Shinso Yoitoko Sanpomichi  
Official pamphlet dated July 26, 2026**

The source material and the canonical metadata have different roles:

- Source material: evidence used to confirm and establish the content
- Canonical metadata: the sole structured authoritative source for managing the confirmed content

The pamphlet is stored in [`../publications/2026/`](../publications/2026/).

---

## Use and Maintenance Policy

### Revising the Lyrics

Changes to the lyrics, readings, credits, or related information should, in principle, be made in:

[`../metadata/shinso-ondo.yaml`](../metadata/shinso-ondo.yaml)

The same information should not be maintained independently in multiple files.

### Updating the Display Page

`index.html` is a public presentation layer.

Its layout or display behavior may be updated, but it is not treated as the authoritative source for the lyrics.

### Treatment of Legacy Material

`shinso-ondo-lyrics.md` is preserved as a snapshot and is not updated.

Even when typographical differences or outdated wording are identified, the file is retained as a record of the earlier state. Explanations may be added through notes or the GitHub commit history when necessary.

### Preserving History

The content, reason, and date of each change are preserved in the GitHub commit history.

GitHub Releases are used when a fixed published version is required.

---

## Related Directories

| Directory | Relationship |
|---|---|
| [`../metadata/`](../metadata/) | Canonical metadata for lyrics, readings, credits, and related information |
| [`../publications/`](../publications/) | Pamphlets and other source materials |
| [`../audio/`](../audio/) | Official audio recordings |
| [`../scores/`](../scores/) | Musical scores |
| [`../contributors/`](../contributors/) | Information about creators and contributors |
| [`../development/`](../development/) | Design, implementation, and research records |
| [`../README.md`](../README.md) | Main repository access point and design policy |

---

## License

Unless otherwise noted, materials in this directory are licensed under the:

**Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International  
(CC BY-NC-SA 4.0)**

Users must provide the title of the work, copyright holder and licensor, lyricists, and license information.

- Copyright holder and licensor: Shinso Ondo Production Committee
- License: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)
- Details: [`../LICENSE`](../LICENSE)
