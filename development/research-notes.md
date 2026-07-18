# Research Notes / 研究ノート

## 日本語

この文書には、「新荘音頭」公式デジタルアーカイブの構築・運用を、今後研究や実践報告として検討するための論点を記録します。

ここに記載する内容は、確定した研究成果ではなく、今後の調査、評価、執筆に向けた検討事項です。

---

## 想定する論文・実践報告の題目

### 仮題

- GitHubを利用した地域文化デジタルアーカイブの構築
- 地域文化資料の公開基盤としてのGitHubの可能性
- バージョン管理を備えた地域文化デジタルアーカイブの実践
- 音源・歌詞・楽譜・メタデータを統合した地域文化資料公開の試み
- GitHubと機関リポジトリを組み合わせた地域文化資料の公開と保存

題目は、実践報告、研究ノート、論文など、発表媒体に応じて調整する。

---

## 研究の背景

地域文化資料には、次のような複数の資料形態が含まれる。

- 音源
- 歌詞
- 楽譜
- 振付
- パンフレット
- 写真・画像
- 制作記録
- 権利情報
- 構造化メタデータ

これらは、単一のPDFやWebページだけでは十分に関連付けて公開しにくい。

また、公開後の修正履歴、ファイルの更新、権利情報の変更などを継続的に記録する仕組みも必要となる。

本アーカイブでは、GitHubのディレクトリ構造、変更履歴、Markdown、YAML、GitHub Pagesなどを利用し、複数形式の地域文化資料を一つの公開基盤上で管理することを試みている。

---

## 関連研究・先行事例

今後、次の分野に関する先行研究や実践事例を調査する。

- 地域文化資料のデジタルアーカイブ
- 音楽・舞踊資料のデジタル保存
- GitHubを利用した文化資源の公開
- 研究データのバージョン管理
- 機関リポジトリによる地域資料の公開
- IIIFを利用した画像・資料公開
- Linked Open DataおよびRDFによる文化資源記述
- 市民参加型・地域主体型デジタルアーカイブ
- 小規模組織によるデジタルアーカイブ運用

---

## 本実践の特徴

本アーカイブの特徴として、次の点を検討する。

### 複数形式の資料を一つのリポジトリで管理すること

音源、歌詞、楽譜、パンフレット、メタデータを、相互に関連付けながら公開している。

### 変更履歴を保存できること

Gitによるバージョン管理を利用し、資料や説明文の変更過程を記録できる。

### 公開資料と構造化メタデータを分離していること

人が読むMarkdownやPDFと、機械処理を想定したYAMLを分けて管理している。

### 制作過程と設計判断を記録していること

完成した資料だけでなく、設計方針、開発記録、研究上の検討事項も保存している。

### 小規模な地域団体でも運用可能な構成であること

大規模な専用システムを導入せず、一般に利用可能なサービスとオープンなファイル形式を組み合わせている。

---

## GitHubをデジタルアーカイブ基盤として利用する評価

今後、次の観点から評価する。

### 利点

- 無償または低コストで公開できる
- ファイル形式を限定せず管理できる
- 変更履歴を残せる
- Markdownによる説明が可能
- YAMLやJSONなどの構造化データを扱える
- GitHub Pagesによる一般向けWeb公開が可能
- リポジトリ全体を複製・保存できる

### 課題

- GitHubに不慣れな利用者には操作が分かりにくい
- 長期的なサービス継続を保証するものではない
- DOIが自動的に付与されるわけではない
- 大容量音声・映像ファイルの管理には制約がある
- 公的な保存機関としての永続性は持たない
- 権利管理や利用許諾を別途整理する必要がある

---

## 大学機関リポジトリとの比較

GitHubと大学機関リポジトリでは、目的と機能が異なる。

### GitHub

- 更新や修正が容易
- バージョン管理が可能
- 複数形式のファイルを柔軟に配置できる
- Webサイトとして展開できる
- 制作過程を記録しやすい

### 大学機関リポジトリ

- 研究成果としての保存に適している
- 機関による継続的な管理が期待できる
- メタデータ標準に基づく検索が可能
- DOIなどの永続的識別子を付与できる場合がある
- 正式な研究成果として引用しやすい

両者を対立的に捉えるのではなく、GitHubを更新・公開の場、機関リポジトリを保存・引用の場として組み合わせる可能性を検討する。

---

## GitHub Pages

GitHub Pagesを利用し、GitHubの操作に慣れていない一般利用者でも閲覧しやすいWebサイトを構築する。

想定するページは次のとおり。

- Home
- About
- Lyrics
- Audio
- Scores
- Publications
- Credits
- Rights and License
- Metadata

GitHubリポジトリを保存・管理基盤、GitHub Pagesを閲覧基盤として役割分担する。

---

## IIIFとの連携

将来的には、パンフレット、楽譜、振付図、写真などの画像資料について、IIIFによる公開を検討する。

検討事項は次のとおり。

- IIIF Presentation APIへの対応
- マニフェストの作成
- 楽譜やパンフレットのページ単位での表示
- 注釈情報の付与
- 他機関のIIIFビューアとの連携
- GitHub上でのIIIF関連ファイル管理

音声資料については、IIIFによる時間軸メディアの扱いも含めて検討する。

---

## RDFおよびLinked Open Dataへの変換

現在のYAMLメタデータを、将来的にRDFへ変換する可能性を検討する。

主な検討事項は次のとおり。

- 作品、歌詞、演奏、録音、ファイルの関係
- 人物・団体の識別
- 地名・地域情報の記述
- 権利情報の記述
- 既存語彙との対応
- URI設計
- JSON-LDへの変換
- 外部典拠とのリンク

YAMLは最終形式ではなく、将来的なデータ変換のための中間的な構造化記述として位置付けることもできる。

---

## DOI付与の可能性

GitHubリポジトリ自体には通常、永続的識別子は付与されない。

今後、次の方法を検討する。

- ZenodoとGitHubの連携
- 大学機関リポジトリへの登録
- 実践報告や研究ノートへのDOI付与
- バージョン単位での識別
- 音源、パンフレット、メタデータへの個別識別子付与

DOIを付与する場合は、更新可能なGitHubリポジトリと、固定された公開版との関係を明確にする必要がある。

---

## 評価方法

本アーカイブの評価方法として、次の観点を検討する。

- 利用者による閲覧のしやすさ
- ファイルへの到達のしやすさ
- メタデータの理解可能性
- 更新作業の負担
- 権利表示の分かりやすさ
- 検索エンジンからの発見可能性
- 他システムへのデータ移行の容易さ
- 地域団体による継続運用の可能性
- 教育・研究・地域活動での再利用事例

---

## 課題

現時点で想定される課題は次のとおり。

- 長期保存主体の確保
- GitHubサービスへの依存
- 音声・映像ファイルの容量
- 権利関係の継続的な確認
- メタデータ項目の標準化
- 人物名・団体名の典拠管理
- 一般利用者向け画面の整備
- アクセス統計の取得
- GitHub Pagesとリポジトリの情報同期
- 修正・追加時の確認手順

---

## 今後の展開

- GitHub Pagesの構築
- 振付動画および振付図の追加
- メタデータ項目の見直し
- JSONまたはJSON-LDへの変換
- IIIFマニフェストの試作
- RDF化の検討
- 機関リポジトリへの登録
- DOI付与方法の検討
- 利用状況および運用負担の評価
- 実践報告または研究ノートの執筆

---

# English

This document records research questions and topics for future study concerning the construction and operation of the **Shinso Ondo Official Digital Archive**.

The contents are working notes rather than finalized research findings. They are intended to support future investigation, evaluation, and publication.

---

## Possible Paper Titles

- Building a Local Cultural Digital Archive Using GitHub
- GitHub as a Platform for Publishing Local Cultural Heritage
- A Version-Controlled Digital Archive for Local Cultural Resources
- Integrating Audio, Lyrics, Scores, Publications, and Metadata in a Local Cultural Archive
- Combining GitHub and an Institutional Repository for Publication and Preservation

The title will be adjusted according to the intended publication format, such as a research note, case study, or academic article.

---

## Research Background

Local cultural heritage may include multiple types of resources:

- audio recordings
- lyrics
- musical scores
- choreography
- pamphlets
- photographs and images
- production records
- rights information
- structured metadata

These resources are difficult to represent adequately within a single PDF document or conventional web page.

A sustainable archive must also record revisions, file updates, and changes to rights information after publication.

This project explores the use of GitHub directories, version history, Markdown, YAML, and GitHub Pages to manage multiple types of local cultural resources within a single publication environment.

---

## Related Work

Future research will examine studies and practices related to:

- digital archives for local cultural heritage
- preservation of music and dance resources
- use of GitHub for cultural heritage publication
- version control for research data
- institutional repositories and local cultural materials
- IIIF-based publication
- RDF and Linked Open Data for cultural resources
- community-based digital archives
- sustainable digital archives operated by small organizations

---

## Distinctive Features

Possible distinctive features of this project include:

### Managing multiple resource types in one repository

Audio recordings, lyrics, scores, pamphlets, and metadata are published and linked within a single repository.

### Preserving revision history

Git version control records changes to files and documentation.

### Separating public materials from structured metadata

Human-readable Markdown and PDF files are managed separately from machine-readable YAML metadata.

### Recording the development process

The repository preserves not only completed resources, but also design decisions, development notes, and research questions.

### Supporting operation by a small local organization

The archive combines generally available services and open file formats without requiring a large proprietary archival system.

---

## Evaluating GitHub as a Digital Archive Platform

### Potential advantages

- low-cost public access
- support for multiple file formats
- version history
- Markdown documentation
- structured data such as YAML and JSON
- public websites through GitHub Pages
- repository cloning and replication

### Potential limitations

- GitHub may be difficult for nontechnical users
- long-term service continuity is not guaranteed
- DOI assignment is not automatic
- large audio and video files may be difficult to manage
- GitHub is not itself a public preservation institution
- rights and permissions must be managed separately

---

## Comparison with Institutional Repositories

GitHub and institutional repositories serve different purposes.

### GitHub

- supports continuous revision
- provides version control
- allows flexible organization of multiple file types
- can be developed into a public website
- preserves development records

### Institutional repositories

- support long-term preservation of scholarly outputs
- are managed by academic institutions
- use standardized metadata
- may assign persistent identifiers such as DOIs
- support formal academic citation

Rather than treating them as competing systems, this project will consider using GitHub for active publication and revision, and an institutional repository for preservation and citation.

---

## GitHub Pages

GitHub Pages may provide a public-facing website that is easier to use than the repository interface.

Possible pages include:

- Home
- About
- Lyrics
- Audio
- Scores
- Publications
- Credits
- Rights and License
- Metadata

The GitHub repository would serve as the management and preservation layer, while GitHub Pages would serve as the access layer.

---

## IIIF Interoperability

Future work may examine IIIF publication for pamphlets, musical scores, choreography diagrams, and photographs.

Possible topics include:

- IIIF Presentation API
- manifest creation
- page-level display of scores and pamphlets
- annotations
- interoperability with external IIIF viewers
- management of IIIF-related files in GitHub

The applicability of IIIF to time-based media such as audio may also be investigated.

---

## RDF and Linked Open Data

The current YAML metadata may later be transformed into RDF.

Possible topics include:

- relationships among works, lyrics, performances, recordings, and files
- identification of persons and organizations
- geographic description
- rights metadata
- alignment with existing vocabularies
- URI design
- JSON-LD transformation
- links to external authority data

YAML may therefore serve as an intermediate structured representation rather than the final metadata format.

---

## DOI Assignment

GitHub repositories do not normally receive persistent identifiers automatically.

Possible options include:

- GitHub and Zenodo integration
- deposit in an institutional repository
- DOI assignment to a research article or case report
- version-specific identifiers
- separate identifiers for audio, pamphlets, and metadata

Any DOI strategy must clarify the relationship between the continuously updated GitHub repository and fixed published versions.

---

## Evaluation Methods

Possible evaluation criteria include:

- ease of use
- ease of locating files
- understandability of metadata
- maintenance workload
- clarity of rights information
- discoverability through search engines
- ease of migration to other systems
- sustainability for a local organization
- reuse in education, research, and community activities

---

## Challenges

Current challenges include:

- identifying a long-term preservation organization
- dependence on GitHub
- storage limits for audio and video
- continuing rights clearance
- metadata standardization
- authority control for personal and organizational names
- public-facing interface design
- access analytics
- synchronization between GitHub Pages and the repository
- review procedures for future revisions

---

## Future Work

- build the GitHub Pages website
- add choreography videos and diagrams
- revise the metadata model
- transform YAML into JSON or JSON-LD
- prototype an IIIF manifest
- examine RDF conversion
- deposit materials in an institutional repository
- investigate DOI assignment
- evaluate use and maintenance costs
- prepare a case study or research note
