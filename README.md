# 新荘音頭（Shinsō Ondo）

## Official Digital Archive

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
![GitHub last commit](https://img.shields.io/github/last-commit/kojikomatsuzaki/shinso-ondo)
![GitHub repo size](https://img.shields.io/github/repo-size/kojikomatsuzaki/shinso-ondo)
![GitHub commit activity](https://img.shields.io/github/commit-activity/y/kojikomatsuzaki/shinso-ondo)
![Digital Archive](https://img.shields.io/badge/Digital%20Archive-Official-blue)

> 茨城県水戸市新荘地区の「新荘夏まつり」で歌い踊られる郷土芸能「新荘音頭」の公式デジタルアーカイブです。

このリポジトリでは、「新荘音頭」に関する音源、歌詞、楽譜、パンフレット、メタデータ、制作・協力者情報および制作記録を収集・整理・保存・公開しています。

---

## 目次

- [クイックアクセス](#クイックアクセス)
- [このリポジトリについて](#このリポジトリについて)
- [公開資料](#公開資料)
- [リポジトリ構成](#リポジトリ構成)
- [正本メタデータ](#正本メタデータ)
- [クレジット情報](#クレジット情報)
- [このアーカイブの特徴](#このアーカイブの特徴)
- [バージョン管理と保存方針](#バージョン管理と保存方針)
- [ライセンス](#ライセンス)
- [著作権者・許諾者](#著作権者許諾者)
- [Roadmap](#roadmap)
- [English](#english)

---

## クイックアクセス

- [新荘音頭デジタルアーカイブ](https://kojikomatsuzaki.github.io/shinso-ondo/)
- [歌詞](https://kojikomatsuzaki.github.io/shinso-ondo/lyrics/)
- [制作・協力者](https://kojikomatsuzaki.github.io/shinso-ondo/contributors/)
- [正本メタデータ](metadata/shinso-ondo.yaml)
- [2026年公式パンフレット](publications/2026/shinso-ondo-pamphlet-20260726.pdf)
- [ライセンス](LICENSE)

---

## このリポジトリについて

このリポジトリは、小松崎浩司（Hiroshi Komatsuzaki）が管理する「新荘音頭」の公式デジタルアーカイブです。

GitHubのバージョン管理機能を活用し、次のことを目的として整備しています。

- 資料の保存
- 更新履歴の管理
- 修正前を含む版の保存
- マルチメディア資料の公開
- メタデータの整備
- 制作・協力者情報の記録
- 継続的な公開・改善
- 研究・教育・地域活動における再利用

公開後に資料、メタデータまたはクレジット情報を修正した場合でも、変更前の状態、変更内容および変更日時を履歴として確認できます。

---

## 公開資料

現在公開している主な資料は次のとおりです。

| ディレクトリ | 内容 |
|---|---|
| `lyrics/` | 歌詞および歌詞公開ページ |
| `scores/` | 楽譜 |
| `audio/` | 公式音源 |
| `publications/` | パンフレット等の出版物 |
| `metadata/` | 作品・音源・クレジット等のメタデータ |
| `contributors/` | 制作・協力者情報の公開ページ |

### 2026年公開資料

| 資料 | 内容 |
|---|---|
| `publications/2026/shinso-ondo-pamphlet-20260726.pdf` | 「新荘音頭」公式パンフレット |

収録内容およびファイルの位置付けについては、`publications/2026/README.md` をご覧ください。

資料は今後も順次追加・更新します。

---

## リポジトリ構成

主なディレクトリの役割は次のとおりです。

| ディレクトリ | 役割 |
|---|---|
| `metadata/` | 正本メタデータの管理 |
| `lyrics/` | 歌詞の公開 |
| `scores/` | 楽譜の保存・公開 |
| `audio/` | 音源の保存・公開 |
| `publications/` | パンフレット等の保存・公開 |
| `contributors/` | 制作・協力者情報の表示 |
| `editorial-policy/` | 編集方針の公開 |
| `about-ondo/` | 「新荘音頭」に関する解説 |
| `about-shinso/` | 新荘地区に関する解説 |
| `images/` | Webサイトで使用する画像の共通管理 |
| `js/` | Webサイトで使用するJavaScript |
| `development/` | 開発・設計・研究に関する記録 |

各ディレクトリ固有の役割、構成および保守方針については、それぞれの `README.md` を参照してください。

---

## 正本メタデータ

作品情報、歌詞、制作・協力者、音源およびクレジットに関する構造化データは、原則として次のファイルを正本（Single Source of Truth）として管理します。

```text
metadata/shinso-ondo.yaml
```

歌詞ページや制作・協力者ページなどの公開ページは、この正本メタデータを読み込み、用途に応じた形で表示します。

```text
metadata/shinso-ondo.yaml
        │
        ├── lyrics/index.html
        ├── contributors/index.html
        └── その他の公開・再利用形式
```

同じ情報を複数のファイルへ個別に転記して管理するのではなく、一つの正本から複数の公開形式を生成・表示する **One Source, Multi Use** を基本方針としています。

情報の追加・修正・削除を行う場合は、表示先のHTMLを直接書き換えるのではなく、原則として `metadata/shinso-ondo.yaml` を更新します。

---

## クレジット情報

本アーカイブでは、作詞、作曲、編曲、振付、歌唱、演奏、録音、音楽編集、パンフレット制作、企画、監修およびデジタルアーカイブ管理等に関するクレジット情報を、作品とともに保存すべき重要なメタデータとして扱います。

クレジット情報の正本は `metadata/shinso-ondo.yaml` です。

制作・協力者情報は、正本メタデータをもとに次のページで公開しています。

- `contributors/index.html`
- `contributors/README.md`

クレジット情報の追加・修正・削除は、`metadata/shinso-ondo.yaml` を更新してください。

---

## このアーカイブの特徴

本デジタルアーカイブでは、次の仕組みを組み合わせています。

- GitHubによるバージョン管理
- Markdownによる資料解説
- YAMLによる正本メタデータ管理
- HTMLおよびJavaScriptによる公開ページ
- PDF・PNG・WAV等のマルチメディア公開
- GitHub Releasesによる公開版の保存
- オープンライセンスによる再利用促進

これらを組み合わせることで、

**「保存するだけではなく、利用され、継続的に育っていくデジタルアーカイブ」**

を目指しています。

完成した成果物だけではなく、それらがどのように整理・修正・発展してきたかという履歴も保存対象としています。

また、誰でも利用できる既存のオープンな基盤を組み合わせることで、地域文化のデジタルアーカイブを継続的かつ実践的に構築することを目指しています。

---

## バージョン管理と保存方針

本リポジトリでは、資料の状態を次の考え方で管理します。

### Current

現在公開し、継続して更新する資料です。

各ディレクトリでは、原則として現在有効な資料だけを管理します。

### Legacy

過去の構成との整合性や参照可能性を保つため、例外的に旧形式の資料を残す場合があります。

Legacy資料は、現在の正本や最新版ではないことを明示し、原則として更新しません。

### Git History

修正前の状態、中間版および削除済みファイルは、原則としてGitのコミット履歴で保存します。

現在のディレクトリ内に複数の旧版を並べて保存するのではなく、Gitの履歴から過去の状態を確認できる構成を基本とします。

### GitHub Releases

公開時点の資料一式や、まとまりのある公開版はGitHub Releasesで保存します。

| Version | 内容 |
|---|---|
| v1.0.0 | 初版公開 |
| v1.0.1 | クレジット・パンフレット等の修正版 |

GitHub Releasesでは公開版を、GitHubのコミット履歴では日々の更新履歴を確認できます。

---

## ライセンス

別途記載がある場合を除き、本リポジトリに収録された資料は、

**Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International  
（CC BY-NC-SA 4.0）**

により公開しています。

利用する際は、著作権者および制作者を適切に表示してください。

改変して公開する場合は、同一ライセンスを適用してください。

営利目的での利用はできません。

詳細は `LICENSE` をご覧ください。

---

## 著作権者・許諾者

**新荘音頭制作委員会**

---

## Roadmap

今後は、次の資料や機能を順次追加・整備する予定です。

- 振付資料
- 振付動画
- 写真資料
- 制作記録
- 関連史料
- 音源ページの拡充
- メタデータ公開ページ
- Schema.org JSON-LD
- IIIF Manifest
- GitHub Actionsによる静的生成

GitHubのコミット履歴およびReleasesは、本デジタルアーカイブの整備・修正・発展の履歴として継続的に保存されます。

---

# English

## Table of Contents

- [Quick Access](#quick-access)
- [About This Repository](#about-this-repository)
- [Published Materials](#published-materials)
- [Repository Structure](#repository-structure)
- [Canonical Metadata](#canonical-metadata)
- [Credit Information](#credit-information)
- [Features of This Archive](#features-of-this-archive)
- [Versioning and Preservation Policy](#versioning-and-preservation-policy)
- [License](#license-1)
- [Copyright Holder and Licensor](#copyright-holder-and-licensor)
- [Roadmap](#roadmap-1)

---

## Quick Access

- [Shinsō Ondo Digital Archive](https://kojikomatsuzaki.github.io/shinso-ondo/)
- [Lyrics](https://kojikomatsuzaki.github.io/shinso-ondo/lyrics/)
- [Contributors](https://kojikomatsuzaki.github.io/shinso-ondo/contributors/)
- [Canonical Metadata](metadata/shinso-ondo.yaml)
- [Official 2026 Pamphlet](publications/2026/shinso-ondo-pamphlet-20260726.pdf)
- [License](LICENSE)

---

## About This Repository

This repository is the official digital archive of **Shinsō Ondo**, a local folk dance song performed during the **Shinsō Summer Festival** in the Shinsō District of Mito City, Ibaraki, Japan.

The archive is maintained by **Hiroshi Komatsuzaki**.

It collects, organizes, preserves, and provides access to audio recordings, lyrics, musical scores, pamphlets, metadata, contributor information, and production records related to Shinsō Ondo.

This repository uses GitHub’s version control features for the following purposes:

- Preservation of materials
- Management of revision history
- Preservation of previous states
- Publication of multimedia materials
- Metadata management
- Documentation of contributors
- Continuous publication and improvement
- Reuse in research, education, and community activities

When materials, metadata, or credits are revised after publication, previous states, details of the changes, and the dates of those changes remain traceable through the repository history.

---

## Published Materials

The main materials currently available are organized as follows:

| Directory | Contents |
|---|---|
| `lyrics/` | Lyrics and the public lyrics page |
| `scores/` | Musical scores |
| `audio/` | Official audio recordings |
| `publications/` | Publications and pamphlets |
| `metadata/` | Metadata for the work, recordings, and credits |
| `contributors/` | Public contributor information |

### Materials Published in 2026

| Material | Description |
|---|---|
| `publications/2026/shinso-ondo-pamphlet-20260726.pdf` | Official Shinsō Ondo pamphlet |

For details about the contents and status of the file, see `publications/2026/README.md`.

Additional materials will be added and updated over time.

---

## Repository Structure

The main directories have the following roles:

| Directory | Role |
|---|---|
| `metadata/` | Management of canonical metadata |
| `lyrics/` | Publication of lyrics |
| `scores/` | Preservation and publication of musical scores |
| `audio/` | Preservation and publication of audio recordings |
| `publications/` | Preservation and publication of pamphlets and related materials |
| `contributors/` | Presentation of contributor information |
| `editorial-policy/` | Publication of editorial policies |
| `about-ondo/` | Information about Shinsō Ondo |
| `about-shinso/` | Information about the Shinsō District |
| `images/` | Shared management of images used by the website |
| `js/` | JavaScript used by the website |
| `development/` | Development, design, and research records |

For directory-specific roles, structures, and maintenance policies, see the `README.md` file in each directory.

---

## Canonical Metadata

Structured data concerning the work, lyrics, contributors, recordings, and credits is generally maintained in the following file as the canonical source, or Single Source of Truth:

```text
metadata/shinso-ondo.yaml
```

Public pages, including the lyrics and contributors pages, read this canonical metadata and present it in forms appropriate to their respective purposes.

```text
metadata/shinso-ondo.yaml
        │
        ├── lyrics/index.html
        ├── contributors/index.html
        └── other publication and reuse formats
```

Rather than maintaining the same information separately in multiple files, this archive follows a **One Source, Multi Use** approach in which multiple presentation and reuse formats are generated from a single canonical source.

When information needs to be added, modified, or removed, `metadata/shinso-ondo.yaml` should generally be updated instead of editing the displayed HTML directly.

---

## Credit Information

This archive treats credits for lyrics, music, arrangement, choreography, vocals, performance, recording, music editing, pamphlet production, planning, supervision, digital archive management, and related activities as important metadata that should be preserved together with the work.

The canonical source for credit information is `metadata/shinso-ondo.yaml`.

Contributor information based on the canonical metadata is published through:

- `contributors/index.html`
- `contributors/README.md`

To add, modify, or remove credit information, edit `metadata/shinso-ondo.yaml`.

---

## Features of This Archive

This digital archive combines:

- Version control with GitHub
- Documentation using Markdown
- Canonical metadata management using YAML
- Public pages using HTML and JavaScript
- Publication of multimedia materials in formats such as PDF, PNG, and WAV
- Preservation of published versions through GitHub Releases
- Promotion of reuse through open licensing

Through these methods, the archive aims to be:

**“A digital archive that is not merely preserved, but actively used and continuously developed.”**

The archive preserves not only completed materials, but also records of how those materials have been organized, revised, and developed over time.

It also seeks to demonstrate that a sustainable and practical digital archive for local cultural heritage can be developed by combining existing open platforms that are available to anyone.

---

## Versioning and Preservation Policy

This repository manages materials according to the following principles.

### Current

Current materials are actively published and maintained.

As a general rule, each directory contains only the materials that are currently valid.

### Legacy

Older formats may exceptionally be retained when necessary to preserve compatibility with previous repository structures or to maintain reference access.

Legacy materials must be clearly identified as neither canonical nor current and are not normally updated.

### Git History

Previous states, intermediate versions, and deleted files are generally preserved through the Git commit history.

Rather than keeping multiple obsolete versions in the current directory structure, previous states should normally remain accessible through Git history.

### GitHub Releases

GitHub Releases preserve sets of materials representing significant published versions.

| Version | Description |
|---|---|
| v1.0.0 | Initial release |
| v1.0.1 | Revised credits, pamphlet, and related materials |

Published versions can be viewed through GitHub Releases, while individual updates can be traced through the GitHub commit history.

---

## License

Unless otherwise noted, materials in this repository are licensed under the:

**Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International  
(CC BY-NC-SA 4.0)**

Users must provide appropriate attribution to the copyright holders and creators.

Adapted materials must be distributed under the same license.

Commercial use is not permitted.

See `LICENSE` for details.

---

## Copyright Holder and Licensor

**Shinsō Ondo Production Committee**

---

## Roadmap

Future additions and improvements may include:

- Choreography documentation
- Choreography videos
- Photographs
- Production records
- Related historical materials
- Expanded audio pages
- A metadata publication page
- Schema.org JSON-LD
- IIIF Manifest
- Static generation using GitHub Actions

The GitHub commit history and Releases will continue to preserve the development, revision, and growth of this digital archive.
