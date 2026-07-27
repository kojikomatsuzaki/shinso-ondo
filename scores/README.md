# Scores

「新荘音頭」（副題：「新荘よいとこ散歩道」）の公式楽譜を収録するディレクトリです。

本ディレクトリでは、演奏・閲覧・保存のための公式公開版の楽譜を提供するとともに、将来の版管理およびデジタルアーカイブとしての保存方針を示します。

---

## Table of Contents

### 日本語

- [クイックアクセス](#クイックアクセス)
- [このディレクトリの役割](#このディレクトリの役割)
- [ディレクトリ構成](#ディレクトリ構成)
- [公式公開版](#公式公開版)
- [正本メタデータとの関係](#正本メタデータとの関係)
- [将来の版管理](#将来の版管理)
- [典拠](#典拠)
- [利用・更新方針](#利用更新方針)
- [関連ディレクトリ](#関連ディレクトリ)
- [ライセンス](#ライセンス)

### English

- [Quick Access](#quick-access)
- [Role of This Directory](#role-of-this-directory)
- [Directory Structure](#directory-structure)
- [Official Published Edition](#official-published-edition)
- [Relationship to the Canonical Metadata](#relationship-to-the-canonical-metadata)
- [Future Version Management](#future-version-management)
- [Source](#source)
- [Use and Maintenance Policy](#use-and-maintenance-policy)
- [Related Directories](#related-directories)
- [License](#license)

---

# 日本語

## クイックアクセス

| 内容 | ファイル |
|------|---------|
| 公式楽譜 | [`shinso-ondo-score.pdf`](shinso-ondo-score.pdf) |
| 正本メタデータ | [`../metadata/shinso-ondo.yaml`](../metadata/shinso-ondo.yaml) |
| メタデータ設計 | [`../metadata/README.md`](../metadata/README.md) |
| リポジトリ概要 | [`../README.md`](../README.md) |

---

## このディレクトリの役割

`scores/` は、「新荘音頭」の公式楽譜を収録するディレクトリです。

ここで公開する楽譜は、

- 演奏
- 閲覧
- 印刷
- 保存
- 地域文化資料としての継承

を目的とした公式公開版として位置付けています。

---

## ディレクトリ構成

```text
scores/
├── README.md
└── shinso-ondo-score.pdf
```

| ファイル | 役割 |
|----------|------|
| `README.md` | このディレクトリの構成・利用方法・更新方針を示します。 |
| `shinso-ondo-score.pdf` | 現在公開している公式楽譜です。 |

---

## 公式公開版

現在公開している公式楽譜は

`shinso-ondo-score.pdf`

です。

演奏、閲覧、印刷、および引用の際には、この版を参照してください。

---

## 正本メタデータとの関係

作品名、作曲・編曲者、クレジット、権利情報などの構造化された作品情報は、

[`../metadata/shinso-ondo.yaml`](../metadata/shinso-ondo.yaml)

を正本（Single Source of Truth）として管理しています。

本ディレクトリのPDFは、作品を演奏・閲覧するための公式資料であり、作品情報そのものを管理する正本ではありません。

---

## 将来の版管理

将来、改訂版や新たな編曲版などが公開された場合には、過去に**実際に公開・配布された版**について、必要に応じてLegacy資料として保存します。

Legacy資料の目的は、

- 過去の公開版へのアクセス
- 地域文化資料の変遷の記録
- デジタルアーカイブとしての継続的な保存

です。

一方、

- 編集途中の作業ファイル
- 誤って公開したファイル
- 一時的な出力ファイル

についてはLegacy資料とはせず、Gitの履歴によって管理します。

---

## 典拠

現在公開している楽譜は、関係者間で確認・確定した公式資料に基づいています。

作品情報の構造化メタデータは、

[`../metadata/shinso-ondo.yaml`](../metadata/shinso-ondo.yaml)

で管理しています。

---

## 利用・更新方針

楽譜を改訂する場合は、現在の公式公開版を更新します。

過去の公開版を保存する必要が生じた場合のみ、Legacy資料として保存します。

編集途中のファイルや誤登録ファイルはリポジトリには残さず、Gitの履歴によって管理します。

---

## 関連ディレクトリ

| ディレクトリ | 内容 |
|--------------|------|
| [`../metadata/`](../metadata/) | 作品情報の正本 |
| [`../lyrics/`](../lyrics/) | 歌詞 |
| [`../audio/`](../audio/) | 音源 |
| [`../publications/`](../publications/) | パンフレット等の典拠資料 |
| [`../contributors/`](../contributors/) | 制作者・協力者 |
| [`../README.md`](../README.md) | リポジトリ全体の入口 |

---

## ライセンス

別途記載がある場合を除き、本ディレクトリ内の資料は

**Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International（CC BY-NC-SA 4.0）**

の条件で公開しています。

詳細は [`../LICENSE`](../LICENSE) を参照してください。

---

# English

## Quick Access

| Content | File |
|---------|------|
| Official score | [`shinso-ondo-score.pdf`](shinso-ondo-score.pdf) |
| Canonical metadata | [`../metadata/shinso-ondo.yaml`](../metadata/shinso-ondo.yaml) |
| Metadata documentation | [`../metadata/README.md`](../metadata/README.md) |
| Repository overview | [`../README.md`](../README.md) |

---

## Role of This Directory

The `scores/` directory contains the official published score of **Shinsō Ondo** (*Shinsō Yoitoko Sanpomichi*).

The score is provided as the official edition for performance, reference, preservation, and long-term archival use.

---

## Directory Structure

```text
scores/
├── README.md
└── shinso-ondo-score.pdf
```

---

## Official Published Edition

The current official score is

`shinso-ondo-score.pdf`.

Users should refer to this edition for performance, printing, and citation.

---

## Relationship to the Canonical Metadata

The structured work information—including title, credits, composer, arranger, and rights—is maintained in

[`../metadata/shinso-ondo.yaml`](../metadata/shinso-ondo.yaml)

as the Single Source of Truth.

The PDF score is the official published score, not the canonical source of the work metadata.

---

## Future Version Management

If revised or newly arranged editions are officially published in the future, previously published editions may be preserved as Legacy materials.

Legacy materials preserve

- previously published editions;
- the historical development of the work; and
- the long-term continuity of the digital archive.

Working files, temporary outputs, and mistakenly uploaded files are managed through Git history rather than being retained as Legacy materials.

---

## Source

The published score is based on officially confirmed reference materials.

The structured work metadata is maintained in

[`../metadata/shinso-ondo.yaml`](../metadata/shinso-ondo.yaml).

---

## Use and Maintenance Policy

When the score is revised, the current official edition is updated.

Only editions that have actually been published or distributed are preserved as Legacy materials.

Working files and accidental uploads are managed through Git history rather than being retained in the repository.

---

## Related Directories

| Directory | Description |
|-----------|-------------|
| [`../metadata/`](../metadata/) | Canonical metadata |
| [`../lyrics/`](../lyrics/) | Lyrics |
| [`../audio/`](../audio/) | Audio |
| [`../publications/`](../publications/) | Source publications |
| [`../contributors/`](../contributors/) | Contributors |
| [`../README.md`](../README.md) | Repository overview |

---

## License

Unless otherwise noted, the materials in this directory are licensed under the

**Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0).**

For details, see [`../LICENSE`](../LICENSE).

