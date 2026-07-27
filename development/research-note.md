# Research Notes / 研究ノート

## 目次

- [この文書の役割](#この文書の役割)
- [記録方針](#記録方針)
- [既存のオープンな基盤を組み合わせる意義](#既存のオープンな基盤を組み合わせる意義)
- [正本管理と公開表示の分離](#正本管理と公開表示の分離)
- [Git履歴を保存手段として利用すること](#git履歴を保存手段として利用すること)
- [公開サイトと管理基盤の役割分担](#公開サイトと管理基盤の役割分担)
- [クレジットを構造化して記録する意義](#クレジットを構造化して記録する意義)
- [小規模アーカイブの継続性](#小規模アーカイブの継続性)
- [相互運用性と将来の展開](#相互運用性と将来の展開)
- [今後検討する課題](#今後検討する課題)
- [English](#english)

---

## この文書の役割

この文書では、「新荘音頭デジタルアーカイブ」の構築と運用を通して得られた観察、課題および研究上の論点を記録します。

設計判断そのものは `design-decisions.md`、実装・更新の履歴は `development-notes.md` に記録します。

この文書は論文本文ではありません。実践の過程で得られた知見や疑問を残し、後の分析や論文執筆に利用するための研究ノートです。

---

## 記録方針

この文書では、次の内容を区別して記録します。

- 実装・運用を通して確認できた事実
- その事実から考えられる解釈
- 現段階では結論を出せない課題
- 今後検証する必要がある仮説

実践から得られた観察と、一般化された結論を混同しないようにします。

また、本事例だけで確認されたことを、他の地域文化資料にもそのまま適用できるとは限りません。普遍的な方法として提示できる部分と、本事例の条件に依存する部分を分けて検討します。

---

## 既存のオープンな基盤を組み合わせる意義

### 観察

本アーカイブでは、Git、GitHub、GitHub Pages、Markdown、YAML、HTML、CSSおよびJavaScriptなど、既存の技術と公開基盤を組み合わせて資料を管理・公開しています。

専用のデジタルアーカイブシステムを新たに開発しなくても、次の機能を構成できました。

- 資料の保存
- 変更履歴の記録
- 構造化メタデータの管理
- Webサイトでの公開
- 公開版の固定
- ファイルの再利用

### 研究上の論点

誰でも利用できる既存のオープンな基盤を組み合わせることで、小規模な地域文化資料についても、継続的かつ実践的なデジタルアーカイブを構築できる可能性があります。

ただし、利用料金が低いことやソフトウェアが公開されていることだけでは、継続性は保証されません。

構築と保守に必要な知識、管理者の負担、外部サービスへの依存、引継ぎの方法も含めて検討する必要があります。

---

## 正本管理と公開表示の分離

### 観察

歌詞やクレジットを複数のHTMLやMarkdownファイルへ直接記載すると、訂正時に更新漏れや不一致が生じる可能性があります。

本アーカイブでは、構造化メタデータを正本として管理し、公開ページが必要な情報を正本から読み込む構成を採用しました。

これにより、情報を保存する場所と、利用者に提示する画面を分けることができました。

### 研究上の論点

正本管理は、単に同じ情報を一か所へ置くことではありません。

次の点を明確にする必要があります。

- どの情報を正本に含めるか
- 資料ファイルそのものとメタデータをどう区別するか
- 公開ページに直接記述してよい情報は何か
- 正本を更新した際に、どの表示へ反映されるか
- 旧版をどのように確認できるようにするか

正本と表示を分離することで、One Source, Multi Useを実現しやすくなります。

一方で、データ形式や表示処理が複雑になると、更新できる人が限定される可能性があります。

---

## Git履歴を保存手段として利用すること

### 観察

Gitでは、ファイルの変更前後と変更時点を記録できます。

そのため、修正のたびに旧版ファイルを別名で保存しなくても、過去の状態を履歴から確認できます。

また、GitHub Releasesを利用することで、特定時点の公開版を固定して保存できます。

### 研究上の論点

Git履歴は、資料の変更過程を記録する手段として有効です。

ただし、Git履歴とアーカイブ上の版管理は同じではありません。

検討すべき点には、次のものがあります。

- コミットを資料の版として扱えるか
- 公開版として固定すべき変更は何か
- Gitを利用しない閲覧者へ旧版をどう示すか
- 削除されたファイルをどのように説明するか
- GitHub以外の場所へ履歴を保存する必要があるか

Gitは変更履歴を保持できますが、それだけで長期保存が成立するとは限りません。

---

## 公開サイトと管理基盤の役割分担

### 観察

GitHubのリポジトリ画面は、ファイル構成や変更履歴を確認するには適しています。

一方、地域住民や一般利用者が文化資料を閲覧する入口としては、必ずしも分かりやすいとは限りません。

本アーカイブでは、GitHub Pagesによる公開サイトを利用者向けの入口とし、GitHubのリポジトリを管理・保存の基盤として利用しています。

### 研究上の論点

公開サイトと管理基盤を分けることにより、それぞれに異なる役割を持たせることができます。

- 公開サイト  
  資料を探し、読み、聴き、利用するための画面
- リポジトリ  
  ファイル、メタデータ、変更履歴および開発記録を管理する場所

ただし、両者を分離すると、どちらが正式な情報なのか分かりにくくなる可能性があります。

公開サイト、正本メタデータ、資料ファイルおよびGit履歴の関係を、利用者と管理者の双方へ明確に示す必要があります。

---

## クレジットを構造化して記録する意義

### 観察

「新荘音頭」の制作には、作詞、作曲、編曲、演奏、歌唱、振付、監修、編集、パンフレット制作など、複数の人物と役割が関係しています。

同一人物が複数の役割を担う場合もあります。

制作・協力者情報を文章中の謝辞としてだけ記載すると、人物、役割および作品との関係を再利用しにくくなります。

### 研究上の論点

クレジットは、作品に付随する補助的な情報ではなく、作品がどのような協働によって成立したかを示す重要なメタデータと考えられます。

構造化する際には、次の点を検討する必要があります。

- 人物と役割をどの単位で記録するか
- 一人が複数の役割を持つ場合にどう表現するか
- 個人名と団体名をどう区別するか
- 日本語表記、読み、英語表記をどう対応させるか
- 制作時の役割とアーカイブ構築時の役割をどう区別するか

クレジットの整理は、権利表示だけでなく、地域文化資料の成立過程を保存することにもつながります。

---

## 小規模アーカイブの継続性

### 観察

既存のサービスやプレーンテキスト形式を利用することで、専用システムの開発費用やサーバー管理の負担を抑えることができます。

一方、現在の構築と更新は、特定の管理者が技術的作業の多くを担っています。

### 研究上の論点

費用を抑えられることと、継続して運用できることは同じではありません。

小規模アーカイブの継続性を考える際には、少なくとも次の点を検討する必要があります。

- 管理者が更新できなくなった場合の引継ぎ
- アカウントと権限の管理
- メタデータ編集方法の共有
- 使用している外部サービスの変更や終了
- ファイルと履歴のバックアップ
- 技術に詳しくない関係者が修正へ参加する方法
- 公開後の問い合わせや訂正への対応

技術的に公開できることだけでなく、誰がどのように管理を引き継げるかが重要です。

---

## 相互運用性と将来の展開

### 観察

構造化メタデータを、公開ページや資料ファイルから分けて管理することで、同じ情報を別の形式へ変換できる可能性があります。

想定される展開には、JSON、JSON-LD、RDF、IIIF Manifest、機関リポジトリへの登録などがあります。

### 研究上の論点

形式変換が可能であることと、実際に相互運用できることは同じではありません。

外部形式へ展開するためには、次の検討が必要です。

- 各項目を外部の語彙やスキーマへどう対応させるか
- 人物、団体、場所および作品へ識別子を付与するか
- 音源、楽譜、歌詞および画像の関係をどう記述するか
- 権利情報を機械可読な形でどう表現するか
- 変換後のデータを誰が検証するか
- 外部サービスと連携した後も正本をどこに置くか

将来的な連携先を列挙するだけでなく、現在のメタデータがどこまで変換に耐えられるかを検証する必要があります。

---

## 今後検討する課題

今後、次の点を継続して検討します。

### 利用者

- 地域住民はどのような経路でアーカイブへ到達するか
- 利用者はGitHubを意識せず資料を利用できるか
- 歌詞、音源、楽譜および地域情報をどのように関連付けるか
- スマートフォンでの閲覧にどのような課題があるか

### 管理

- 管理者以外が安全に情報を訂正する方法
- 制作委員会による確認と承認の手順
- GitHubアカウントやリポジトリの継承
- 定期的なバックアップと保存先

### メタデータ

- 人物、団体、場所および資料の識別方法
- 日本語と英語の対応関係
- 読みや異表記の記録
- 外部スキーマとの対応
- 更新日、公開日および制作日の区別

### 研究

- 本事例に固有の条件と、他地域にも適用できる要素の区別
- 構築費用だけでなく、保守に要する時間と作業の記録
- 公開後の利用状況を評価する方法
- 地域文化の保存と地域活動への再利用の関係
- 専用システムを用いる場合との比較

---

# English

## Role of This Document

This document records observations, issues, and research questions identified through the development and operation of the **Shinsō Ondo Digital Archive**.

Design decisions are recorded in `design-decisions.md`, while implementation and update history is recorded in `development-notes.md`.

This document is not a completed research paper. It serves as a research notebook connecting practical work with later analysis and scholarly writing.

---

## Documentation Policy

This document distinguishes among:

- facts confirmed through implementation and operation;
- interpretations that may be drawn from those facts;
- issues that cannot yet be resolved;
- hypotheses requiring further examination.

Observations from the project should not automatically be treated as conclusions applicable to every local cultural archive.

Elements that may be generalized must be distinguished from those dependent on the particular conditions of this case.

---

## Significance of Combining Existing Open Infrastructure

### Observation

The archive combines existing technologies and public infrastructure, including Git, GitHub, GitHub Pages, Markdown, YAML, HTML, CSS, and JavaScript.

Without developing a dedicated digital archive system, the project has been able to provide:

- preservation of materials;
- revision history;
- management of structured metadata;
- Web publication;
- fixed public releases;
- reuse of files and metadata.

### Research Question

Combining existing and openly available infrastructure may make it possible to build a practical and sustainable digital archive for small-scale local cultural materials.

However, low financial cost and openly available software do not by themselves guarantee continuity.

Required technical knowledge, maintenance workload, dependence on external services, and succession arrangements must also be examined.

---

## Separation of Canonical Metadata and Public Presentation

### Observation

When lyrics and credits are written separately in multiple HTML or Markdown files, revisions may produce omissions and inconsistencies.

The archive therefore maintains structured metadata as a canonical source and displays the required information through public pages.

This separates preserved information from its presentation to users.

### Research Question

Canonical management involves more than storing the same information in one location.

It requires clarification of:

- what information belongs in the canonical source;
- how resource files differ from metadata;
- what may be written directly in public pages;
- which displays are affected by a metadata revision;
- how previous versions remain accessible.

Separating canonical metadata from presentation supports the principle of One Source, Multi Use.

At the same time, increasing technical complexity may limit the number of people able to maintain the archive.

---

## Use of Git History as a Preservation Mechanism

### Observation

Git records changes to files and makes previous states available.

This allows earlier versions to remain accessible without preserving every revision as a separately named file.

GitHub Releases can also preserve selected public versions.

### Research Question

Git history is useful for documenting the process of change, but Git history and archival version management are not identical.

Questions include:

- whether a commit should be treated as a version of a cultural resource;
- which revisions should be fixed as public releases;
- how previous versions should be presented to users unfamiliar with Git;
- how deleted files should be explained;
- whether history should also be preserved outside GitHub.

Git can retain revision history, but revision history alone does not guarantee long-term preservation.

---

## Division of Roles Between the Public Website and the Management Platform

### Observation

The GitHub repository interface is useful for examining files, structures, and revision history.

It is not necessarily an accessible entry point for residents and general users seeking cultural resources.

The archive therefore uses GitHub Pages as the public-facing interface and the GitHub repository as the management and preservation platform.

### Research Question

Separating the public website from the management platform allows each to serve a different purpose.

- Public website: finding, reading, listening to, and using resources
- Repository: managing files, metadata, revision history, and development records

However, this separation may make it difficult to understand which location contains the authoritative information.

The relationship among the public website, canonical metadata, resource files, and Git history must therefore be made clear.

---

## Significance of Structured Credits

### Observation

The production of Shinsō Ondo involved multiple people and roles, including lyrics, music, arrangement, performance, vocals, choreography, supervision, editing, and pamphlet production.

Some individuals performed more than one role.

When contributor information is recorded only as acknowledgements in prose, the relationships among people, roles, and the work are difficult to reuse.

### Research Question

Credits may be understood not merely as supplementary acknowledgements but as important metadata documenting the collaborative process through which a cultural work was created.

Questions include:

- how people and roles should be represented;
- how multiple roles held by one person should be expressed;
- how individuals and organizations should be distinguished;
- how Japanese names, readings, and English forms should correspond;
- how production roles should be distinguished from archival roles.

Structuring credits supports not only rights documentation but also preservation of the work’s production history.

---

## Continuity of a Small-Scale Archive

### Observation

Using existing services and plain-text formats reduces the cost of dedicated system development and server administration.

However, much of the current technical work is performed by a particular administrator.

### Research Question

Low cost does not necessarily mean sustainable operation.

Continuity requires consideration of:

- succession when the current administrator can no longer maintain the project;
- account and permission management;
- shared procedures for editing metadata;
- changes to or termination of external services;
- backup of files and revision history;
- participation by contributors without advanced technical knowledge;
- responses to corrections and inquiries after publication.

The ability to publish an archive must be considered separately from the ability to maintain it over time.

---

## Interoperability and Future Development

### Observation

Separating structured metadata from public pages and resource files may allow the same information to be transformed into formats such as JSON, JSON-LD, RDF, IIIF Manifests, or institutional repository records.

### Research Question

The ability to convert a file does not by itself establish interoperability.

Further examination is required regarding:

- mapping local fields to external vocabularies and schemas;
- identifiers for people, organizations, places, and works;
- representation of relationships among recordings, scores, lyrics, and images;
- machine-readable rights information;
- validation of transformed data;
- the location of the canonical source after external integration.

Future services should not merely be listed as possible destinations. The current metadata must be examined to determine whether it can support meaningful transformation and reuse.

---

## Issues for Further Examination

### Users

- How local residents reach the archive
- Whether users can access resources without understanding GitHub
- How lyrics, recordings, scores, and local information should be connected
- Accessibility and usability on smartphones

### Management

- Safe correction of information by people other than the administrator
- Review and approval procedures involving the production committee
- Succession of GitHub accounts and repository management
- Regular backup procedures and storage locations

### Metadata

- Identification of people, organizations, places, and resources
- Correspondence between Japanese and English
- Readings and variant forms
- Mapping to external schemas
- Distinction among creation, publication, and revision dates

### Research

- Distinguishing case-specific conditions from transferable elements
- Recording maintenance time and labor as well as financial cost
- Evaluating use after publication
- Relationship between cultural preservation and reuse in community activities
- Comparison with dedicated digital archive systems
