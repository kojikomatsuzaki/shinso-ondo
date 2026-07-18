# Design Decisions / 設計方針

## 日本語

この文書では、「新荘音頭」公式デジタルアーカイブの設計において採用した主要な設計判断と、その理由を記録しています。

何を実装したかだけでなく、「なぜそのように設計したのか」を残すことで、将来の保守や再利用、研究資料として活用できることを目的としています。

---

## Repository Structure / リポジトリ構成

### Decision / 判断

文化資料、構造化メタデータ、開発資料を、それぞれ独立したディレクトリで管理します。

### Reason / 理由

役割を明確に分離することで、保守性を高めるとともに、長期保存や再利用を容易にします。

---

## Why GitHub / GitHubを採用した理由

### Decision / 判断

公開およびバージョン管理の基盤として GitHub を採用します。

### Reason / 理由

GitHubは変更履歴を保持できるだけでなく、

- バージョン管理
- 変更履歴の公開
- Issueによる議論
- GitHub Pagesによる公開
- オープンなアクセス

を一つのプラットフォームで実現できます。

---

## Why Markdown / Markdownを採用した理由

### Decision / 判断

人が読む文書はMarkdownで記述します。

### Reason / 理由

Markdownは

- 軽量
- 可読性が高い
- GitHubとの親和性が高い
- 長期保存に適している

という特徴があります。

---

## Why YAML / YAMLを採用した理由

### Decision / 判断

構造化メタデータはYAML形式で記述します。

### Reason / 理由

YAMLは

- 人にも読みやすい
- 機械でも処理しやすい
- Gitとの差分管理に適している
- JSONへ容易に変換できる

という特徴があり、将来的なIIIF、RDF、Linked Open Dataとの連携にも適しています。

---

## Why CC BY-NC-SA / CC BY-NC-SAを採用した理由

### Decision / 判断

公開資料は原則として CC BY-NC-SA 4.0 で公開します。

### Reason / 理由

地域文化資料の教育利用や非営利での活用を促進するとともに、

- 著作者表示
- 非営利利用
- 継承

を条件とすることで、文化資源として継続的な活用を目指します。

---

## Why English README / 英語READMEを作成した理由

### Decision / 判断

主要な説明文書は日英併記とします。

### Reason / 理由

本アーカイブは日本国内だけでなく、デジタルアーカイブや地域文化資料に関心を持つ海外の研究者にも利用されることを想定しています。

---

## ASCII Filenames / ASCIIファイル名を採用した理由

### Decision / 判断

公開するファイル名はASCII文字のみを使用します。

### Reason / 理由

一部のメールソフトでは、日本語ファイル名を含むURLが途中で切れてしまい、正常にリンクとして認識されない場合があります。

また、OS、Webブラウザ、メールソフト、GitHubなど複数の環境での互換性を高めるため、公開ファイル名はASCII文字へ統一しています。

---

## Future Interoperability / 将来的な相互運用性

本アーカイブは、将来的に次のような技術との連携を視野に入れて設計しています。

- JSON
- RDF
- Linked Open Data (LOD)
- IIIF
- 大学機関リポジトリ
- DOI付与

---

# English

This document records the major design decisions made during the development of the **Shinso Ondo Official Digital Archive**.

Its purpose is to document not only *what* was implemented, but also *why* each decision was made, supporting future maintenance, reuse, and scholarly documentation.

(The following sections correspond to the Japanese version above.)

- Repository Structure
- Why GitHub
- Why Markdown
- Why YAML
- Why CC BY-NC-SA
- Why English README
- ASCII Filenames
- Future Interoperability
