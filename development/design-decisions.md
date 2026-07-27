# Design Decisions / 設計判断

## 目次

- [この文書の役割](#この文書の役割)
- [GitHubを基盤として採用した](#githubを基盤として採用した)
- [資料の役割に応じてディレクトリを分けた](#資料の役割に応じてディレクトリを分けた)
- [人が読む文書にMarkdownを採用した](#人が読む文書にmarkdownを採用した)
- [構造化メタデータにYAMLを採用した](#構造化メタデータにyamlを採用した)
- [構造化メタデータの正本を一つに集約した](#構造化メタデータの正本を一つに集約した)
- [公開ページと正本メタデータを分離した](#公開ページと正本メタデータを分離した)
- [主要な説明文書を日英併記とした](#主要な説明文書を日英併記とした)
- [English](#english)

---

## この文書の役割

この文書では、「新荘音頭デジタルアーカイブ」の構築において採用した主要な設計判断と、その理由を記録します。

現在の構成や運用方法を説明することではなく、設計時に何を選択し、なぜその選択を行ったのかを残すことを目的としています。

リポジトリ全体の現在の構成、運用方針、版管理および保存方針については、ルートディレクトリの `README.md` を参照してください。

---

## GitHubを基盤として採用した

### 判断

資料の保存、変更履歴の管理およびWeb公開の基盤として、GitHubを採用しました。

### 理由

資料の公開だけでなく、変更前の状態や修正の経緯を継続的に記録する必要があったためです。

GitHubでは、Gitによるバージョン管理、変更履歴の公開、GitHub Releasesによる版の保存、GitHub PagesによるWeb公開を、一つの基盤上で組み合わせることができます。

また、専用のデジタルアーカイブシステムを新たに開発・運用するのではなく、既存の公開基盤を利用することで、小規模な地域文化資料についても継続可能な構成を検討できると判断しました。

---

## 資料の役割に応じてディレクトリを分けた

### 判断

文化資料、構造化メタデータ、公開ページ、編集方針および開発記録を、それぞれの役割に応じたディレクトリで管理する構成としました。

### 理由

性格の異なる資料を同じ場所で管理すると、公開対象、編集対象および保守記録の区別が不明確になるためです。

役割ごとに分離することで、資料の追加、メタデータの修正、公開ページの変更および開発記録の追記を、相互に混同せず管理できるようにしました。

---

## 人が読む文書にMarkdownを採用した

### 判断

README、設計記録、開発記録など、人が読むことを主な目的とする文書にはMarkdownを採用しました。

### 理由

Markdownはプレーンテキストとして読み書きでき、特定の編集ソフトに強く依存しません。

また、Git上で変更箇所を確認しやすく、GitHub上でそのまま表示できるため、文書の継続的な修正と履歴管理に適していると判断しました。

---

## 構造化メタデータにYAMLを採用した

### 判断

作品および関連資料に関する構造化メタデータには、YAMLを採用しました。

### 理由

人が直接読み書きできる可読性と、プログラムから処理できる構造化形式の両方が必要だったためです。

YAMLは、階層構造や繰り返しを表現でき、Git上で変更箇所を比較しやすいという特徴があります。

また、必要に応じてJSON等の形式へ変換できるため、人による保守と機械処理の双方に利用できると判断しました。

---

## 構造化メタデータの正本を一つに集約した

### 判断

作品および関連資料に関する構造化メタデータは、原則として次のファイルへ集約しました。

```text
metadata/shinso-ondo.yaml
```

### 理由

同じ情報を複数のHTML、Markdownおよびメタデータファイルへ個別に記載すると、訂正時に更新漏れや内容の不一致が生じるためです。

構造化メタデータの正本を一つにすることで、情報の追加や訂正を一か所で行い、複数の用途へ展開できる構成としました。

なお、画像、音声、PDF等の資料ファイルそのものは、それぞれの資料ディレクトリで管理します。

---

## 公開ページと正本メタデータを分離した

### 判断

歌詞や制作・協力者情報などの公開ページは、正本メタデータとは別に作成し、必要な情報を `metadata/shinso-ondo.yaml` から読み込んで表示する構成としました。

### 理由

保存する情報と、利用者に提示する画面を分離するためです。

正本メタデータと公開ページを分けることで、同じ情報を複数のページへ重複して記載せず、用途に応じて異なる表示を行うことができます。

この構成は、一つの正本を複数の用途へ利用するという考え方に基づいています。

---

## 主要な説明文書を日英併記とした

### 判断

主要なREADMEおよび説明文書は、日本語と英語を併記する構成としました。

### 理由

日本語を主な利用言語としながら、海外の研究者や、地域文化資料およびデジタルアーカイブに関心を持つ利用者にも、リポジトリの構成や資料の位置付けを伝えられるようにするためです。

英語部分は日本語部分とは別の情報を管理するものではなく、原則として日本語の説明に対応する内容としました。

---

# English

## Table of Contents

- [Role of This Document](#role-of-this-document)
- [Adopt GitHub as the Primary Platform](#adopt-github-as-the-primary-platform)
- [Separate Directories According to the Roles of Their Contents](#separate-directories-according-to-the-roles-of-their-contents)
- [Adopt Markdown for Human-Readable Documents](#adopt-markdown-for-human-readable-documents)
- [Adopt YAML for Structured Metadata](#adopt-yaml-for-structured-metadata)
- [Maintain a Single Canonical Source for Structured Metadata](#maintain-a-single-canonical-source-for-structured-metadata)
- [Separate Public Pages from Canonical Metadata](#separate-public-pages-from-canonical-metadata)
- [Provide Major Explanatory Documents in Japanese and English](#provide-major-explanatory-documents-in-japanese-and-english)

---

## Role of This Document

This document records the major design decisions made during the development of the **Shinsō Ondo Digital Archive** and the reasons behind them.

Its purpose is not to describe the archive’s current structure or operating procedures, but to preserve what was selected during the design process and why each selection was made.

For the current repository structure, operating policies, versioning, and preservation policies, see the root `README.md`.

---

## Adopt GitHub as the Primary Platform

### Decision

GitHub was adopted as the platform for preserving materials, managing revision history, and publishing the archive on the Web.

### Reason

The archive needed to preserve not only published materials but also previous states and the processes through which revisions were made.

GitHub makes it possible to combine Git-based version control, public revision history, preservation of released versions through GitHub Releases, and Web publication through GitHub Pages on a single platform.

It was also selected as a way to explore a sustainable structure for a small-scale local cultural archive by using existing public infrastructure rather than developing and maintaining a dedicated digital archive system.

---

## Separate Directories According to the Roles of Their Contents

### Decision

Cultural materials, structured metadata, public pages, editorial policies, and development records were placed in directories corresponding to their respective roles.

### Reason

Managing materials with different functions in the same location would make it difficult to distinguish public resources, editable data, and maintenance records.

Separating them by role makes it possible to add resources, revise metadata, modify public pages, and update development records without confusing their respective purposes.

---

## Adopt Markdown for Human-Readable Documents

### Decision

Markdown was adopted for documents primarily intended for human readers, including README files, design records, and development records.

### Reason

Markdown can be read and edited as plain text and is not strongly dependent on a particular editing application.

It also makes revisions easy to compare in Git and can be displayed directly on GitHub, making it suitable for the continued revision and version control of documentation.

---

## Adopt YAML for Structured Metadata

### Decision

YAML was adopted for structured metadata concerning the work and its related resources.

### Reason

The archive required a format that could be read and edited directly by people while also being processed by software.

YAML can represent hierarchical and repeated structures and makes revisions relatively easy to compare in Git.

It can also be converted into formats such as JSON when required, making it suitable for both human maintenance and machine processing.

---

## Maintain a Single Canonical Source for Structured Metadata

### Decision

Structured metadata concerning the work and related resources was generally consolidated in the following file:

```text
metadata/shinso-ondo.yaml
```

### Reason

Maintaining the same information separately in multiple HTML, Markdown, and metadata files could result in omissions or inconsistencies when corrections were made.

Using a single canonical source makes it possible to add or correct information in one place and reuse it for multiple purposes.

Image, audio, PDF, and other resource files themselves remain managed in their respective material directories.

---

## Separate Public Pages from Canonical Metadata

### Decision

Public pages presenting lyrics, contributor information, and similar content were created separately from the canonical metadata and designed to read the required information from `metadata/shinso-ondo.yaml`.

### Reason

This separates the information being preserved from the interface through which it is presented to users.

By separating canonical metadata from public pages, the same information can be displayed in different ways without maintaining duplicate copies in multiple pages.

This structure is based on the use of one canonical source for multiple purposes.

---

## Provide Major Explanatory Documents in Japanese and English

### Decision

Major README files and explanatory documents were provided in both Japanese and English.

### Reason

Japanese remains the primary language of the archive, while English descriptions allow overseas researchers and users interested in local cultural materials and digital archives to understand the repository structure and the position of its resources.

The English sections do not maintain information separately from the Japanese sections. They generally provide corresponding descriptions.
