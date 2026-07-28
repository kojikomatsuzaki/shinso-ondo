(() => {
  "use strict";

  const STORAGE_KEY = "shinso-ondo-language";
  const translations = {
    ja: {
      skip: "本文へ移動", workSubtitle: "新荘よいとこ散歩道", menu: "メニュー", materials: "公開資料", guide: "案内",
      audio: "音源", lyrics: "歌詞", scores: "楽譜", pamphlet: "パンフレット", aboutShinso: "新荘地区について",
      aboutOndo: "新荘音頭について", contributors: "制作・協力者", rights: "権利・利用条件", metadata: "メタデータ",
      noticeTitle: "このデジタルアーカイブは現在整備中です",
      noticeText: "一部のページや資料は、現在作成または確認を進めています。内容は今後も順次追加・更新していきます。",
      introLead: "「新荘音頭」は、茨城県水戸市新荘地区の風景を歌にし、地域のイベントを象徴するものとして制作した音頭です。2026（令和8）年7月26日、水戸市立新荘小学校校庭で催された「第25回新荘夏まつり」において初演されました。",
      introText: "このサイトでは、「新荘音頭」の公式音源、歌詞、楽譜、パンフレット、制作・協力者情報などをデジタルアーカイブとして収集・保存し、公開しています。",
      publicTitle: "新荘音頭を知る・楽しむ", publicText: "新荘地区や新荘音頭について知り、音源や歌詞、楽譜などの公開資料をご覧いただけます。",
      aboutShinsoCard: "新荘って？", aboutShinsoText: "新荘地区の歴史や地域の概要を紹介します。",
      aboutOndoCard: "新荘音頭って？", aboutOndoText: "新荘音頭が制作された経緯や作品の概要を紹介します。",
      viewPage: "ページを見る →", audioText: "新荘音頭の公式音源と関連情報を掲載しています。", listenAudio: "音源を聴く →",
      lyricsText: "全七番の歌詞、読み方、クレジットを掲載しています。", viewLyrics: "歌詞を見る →",
      scoresText: "新荘音頭の楽譜画像と関連情報を掲載しています。", viewScores: "楽譜を見る →",
      publicationsText: "パンフレットなど、公開用に制作された資料を掲載しています。", viewPublications: "刊行物を見る →",
      contributorsText: "新荘音頭の制作・演奏・運営に携わった方々を紹介します。", viewContributors: "制作・協力者を見る →",
      researchTitle: "技術者・研究者の方へ", researchText: "構造化メタデータ、編集方針、設計・開発記録、権利情報などを公開しています。",
      structuredMetadata: "構造化メタデータ", metadataText: "YAML形式の正本メタデータと、その設計・利用方法を掲載しています。", viewMetadata: "メタデータを見る →",
      editorialPolicy: "編集方針", editorialText: "資料の選定、記述、更新、訂正に関する基本方針を掲載しています。", viewPolicy: "編集方針を見る →",
      development: "設計・開発・研究記録", developmentText: "設計判断、開発履歴、研究上の記録をまとめています。", viewRecords: "記録を見る →",
      rightsLicense: "権利・ライセンス", rightsText: "著作権、クレジット、利用条件に関する情報を掲載しています。", viewRights: "権利情報を見る →",
      footerTitle: "新荘音頭 公式デジタルアーカイブ", managedBy: "管理："
    },
    en: {
      skip: "Skip to main content", workSubtitle: "Shinsō Yoi Toko Sanpomichi", menu: "Menu", materials: "Public Materials", guide: "Guide",
      audio: "Audio", lyrics: "Lyrics", scores: "Scores", pamphlet: "Pamphlet", aboutShinso: "About the Shinsō District",
      aboutOndo: "About Shinsō Ondo", contributors: "Contributors", rights: "Rights and Terms of Use", metadata: "Metadata",
      noticeTitle: "This digital archive is currently under development",
      noticeText: "Some pages and materials are still being prepared or reviewed. Additional content and updates will be published progressively.",
      introLead: "“Shinsō Ondo” is a traditional-style community dance song created to celebrate the scenery of the Shinsō district in Mito, Ibaraki Prefecture, and to serve as a symbol of local events. It was first performed on July 26, 2026, at the 25th Shinsō Summer Festival, held on the grounds of Mito Municipal Shinsō Elementary School.",
      introText: "This website collects, preserves, and provides public access to the official recordings, lyrics, musical scores, pamphlets, and information about the people and organizations involved in the production of “Shinsō Ondo” as a digital archive.",
      publicTitle: "Discover and Enjoy Shinsō Ondo", publicText: "Learn about the Shinsō district and Shinsō Ondo, and explore publicly available recordings, lyrics, scores, and related materials.",
      aboutShinsoCard: "What is Shinsō?", aboutShinsoText: "An introduction to the history and character of the Shinsō district.",
      aboutOndoCard: "What is Shinsō Ondo?", aboutOndoText: "An introduction to the background and overview of Shinsō Ondo.",
      viewPage: "View page →", audioText: "Official recordings of Shinsō Ondo and related information.", listenAudio: "Listen to audio →",
      lyricsText: "All seven verses, readings, and lyric credits.", viewLyrics: "View lyrics →",
      scoresText: "Musical score images and related information.", viewScores: "View scores →",
      publicationsText: "Pamphlets and other materials created for public distribution.", viewPublications: "View publications →",
      contributorsText: "The people involved in the production, performance, and operation of Shinsō Ondo.", viewContributors: "View contributors →",
      researchTitle: "For Researchers and Developers", researchText: "Structured metadata, editorial policies, development records, and rights information.",
      structuredMetadata: "Structured Metadata", metadataText: "The authoritative YAML metadata and information about its design and use.", viewMetadata: "View metadata →",
      editorialPolicy: "Editorial Policy", editorialText: "Policies for selecting, describing, updating, and correcting materials.", viewPolicy: "View policy →",
      development: "Design, Development, and Research Records", developmentText: "Records of design decisions, development history, and research notes.", viewRecords: "View records →",
      rightsLicense: "Rights and License", rightsText: "Copyright, credits, and terms of use.", viewRights: "View rights information →",
      footerTitle: "Shinsō Ondo Official Digital Archive", managedBy: "Managed by: "
    }
  };

  const html = document.documentElement;
  const languageButton = document.getElementById("language-toggle");
  const menuButton = document.getElementById("menu-toggle");
  const menu = document.getElementById("site-menu");
  const menuClose = document.getElementById("menu-close");
  const backdrop = document.getElementById("menu-backdrop");

  const saved = localStorage.getItem(STORAGE_KEY);
  const browserIsJapanese = (navigator.languages || [navigator.language]).some((lang) => String(lang).toLowerCase().startsWith("ja"));
  let currentLanguage = saved === "ja" || saved === "en" ? saved : browserIsJapanese ? "ja" : "en";

  function applyLanguage(language) {
    currentLanguage = language;
    html.lang = language;
    document.querySelectorAll("[data-i18n]").forEach((element) => {
      const value = translations[language][element.dataset.i18n];
      if (typeof value === "string") element.textContent = value;
    });
    languageButton.textContent = language === "ja" ? "English" : "日本語";
    languageButton.setAttribute("aria-label", language === "ja" ? "Switch to English" : "日本語表示に切り替える");
    menu.setAttribute("aria-label", language === "ja" ? "サイト内メニュー" : "Site menu");
    menuClose.setAttribute("aria-label", language === "ja" ? "メニューを閉じる" : "Close menu");
    document.title = language === "ja" ? "新荘音頭 公式デジタルアーカイブ" : "Shinsō Ondo Official Digital Archive";
    localStorage.setItem(STORAGE_KEY, language);
  }

  function openMenu() {
    menu.classList.add("is-open");
    backdrop.hidden = false;
    document.body.classList.add("menu-open");
    menu.setAttribute("aria-hidden", "false");
    menuButton.setAttribute("aria-expanded", "true");
    menuClose.focus();
  }

  function closeMenu(restoreFocus = true) {
    menu.classList.remove("is-open");
    backdrop.hidden = true;
    document.body.classList.remove("menu-open");
    menu.setAttribute("aria-hidden", "true");
    menuButton.setAttribute("aria-expanded", "false");
    if (restoreFocus) menuButton.focus();
  }

  languageButton.addEventListener("click", () => applyLanguage(currentLanguage === "ja" ? "en" : "ja"));
  menuButton.addEventListener("click", () => menu.classList.contains("is-open") ? closeMenu() : openMenu());
  menuClose.addEventListener("click", () => closeMenu());
  backdrop.addEventListener("click", () => closeMenu());
  menu.querySelectorAll("a").forEach((link) => link.addEventListener("click", () => closeMenu(false)));
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && menu.classList.contains("is-open")) closeMenu();
  });

  applyLanguage(currentLanguage);
})();
