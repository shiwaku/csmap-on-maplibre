/** パネルに並べるレイヤー1項目。ids は同時に切り替える MapLibre レイヤーID。 */
export type LayerDef = {
  /** 表示名 */
  name: string;
  /** 一括で表示/非表示を切り替える MapLibre レイヤーID */
  ids: string[];
  /** 初期表示 ON か（style JSON 側の visibility と一致させる） */
  on?: boolean;
};

/** CS立体図（各県公開のラスタタイル）。地域はほぼ重ならないため全ONでも実用になる。 */
export const CS_LAYERS: LayerDef[] = [
  { ids: ["miyagi-cs"], name: "宮城県CS立体図（宮城県／1m／2023）" },
  { ids: ["yamagata-shonai-cs"], name: "山形県(庄内)CS立体図（林野庁／0.5m／2022）" },
  { ids: ["fukushima-cs"], name: "福島県CS立体図（林野庁／1m／2011–2013）" },
  { ids: ["tochigi-cs"], name: "栃木県CS立体図（栃木県／-／2021–2022）" },
  { ids: ["saitama-cs"], name: "埼玉県CS立体図（埼玉県／0.5m／2024）" },
  { ids: ["tokyo-23ku-cs"], name: "東京都(区部)CS立体図（東京都／0.25m／2022–2023）" },
  { ids: ["tokyo-tama-cs"], name: "東京都(多摩地域)CS立体図（東京都／0.25m／2022）" },
  {
    ids: [
      "tokyo-shima-01-cs",
      "tokyo-shima-02-cs",
      "tokyo-shima-03-cs",
      "tokyo-shima-04-cs",
      "tokyo-shima-05-cs",
      "tokyo-shima-06-cs",
    ],
    name: "東京都(島しょ地域)CS立体図（東京都／0.25m／2022）",
  },
  { ids: ["kanagawa-cs"], name: "神奈川県CS立体図（神奈川県／0.5m／2019–2024）" },
  { ids: ["noto-nagaoka-rinya-cs"], name: "能登・長岡CS立体図（林野庁／0.5m／2023–2024）" },
  { ids: ["toyama-cs"], name: "富山県CS立体図（富山県／0.5m／2008–2020）" },
  { ids: ["noto-cs"], name: "能登CS立体図(速報成果)（林野庁／-／2023）" },
  { ids: ["noto-cs-final"], name: "能登CS立体図(最終成果)（林野庁／0.5m／2023–2024）" },
  { ids: ["yamanashi-cs"], name: "山梨県CS立体図（山梨県／0.5m／2019–2022）" },
  { ids: ["nagano-cs"], name: "長野県CS立体図（長野県／1m／2013–2014）" },
  { ids: ["nagano-05m-cs"], name: "長野県CS立体図（長野県／0.5m／2021–2022）" },
  { ids: ["nagano-inatani-cs"], name: "長野県(伊那谷)CS立体図（林野庁／0.5m／2013）" },
  { ids: ["gifu-cs"], name: "岐阜県CS立体図（岐阜県／-／2019）" },
  { ids: ["shizuoka-cs"], name: "静岡県CS立体図（静岡県／0.5m／-）" },
  { ids: ["aichi-owari-nishimikawa-cs"], name: "愛知県(尾張西三河)CS立体図（林野庁／0.5m／2018–2019）" },
  { ids: ["aichi-higashimikawa-cs"], name: "愛知県(東三河)CS立体図（林野庁／0.5m／2018–2019）" },
  { ids: ["mie-kitaise-cs"], name: "三重県(北伊勢)CS立体図（林野庁／0.5m／2013–2023）" },
  { ids: ["shiga-cs"], name: "滋賀県CS立体図（滋賀県／-／-）" },
  { ids: ["kyoto-cs"], name: "京都府CS立体図（京都府／0.5m／2019–2023）" },
  { ids: ["osaka-cs"], name: "大阪府CS立体図（大阪府／0.5m／2019–2020）" },
  { ids: ["hyogo-cs"], name: "兵庫県CS立体図（兵庫県／0.5m／2012–2021）" },
  { ids: ["wakayama-cs"], name: "和歌山県CS立体図（和歌山県／1m／-）" },
  { ids: ["tottori-cs"], name: "鳥取県CS立体図（鳥取県／0.5m／2018–2024）" },
  { ids: ["tottori-2025-cs"], name: "鳥取県CS立体図(県DEMから作成)（鳥取県／0.5m／2018–2024）" },
  { ids: ["okayama-cs"], name: "岡山県CS立体図（林野庁／0.5m／2018–2019）" },
  { ids: ["okayama-2024-cs"], name: "岡山県CS立体図（岡山県／0.5m／2018–2024）" },
  { ids: ["hiroshima-cs"], name: "広島県CS立体図（林野庁／0.5m／2018–2019）" },
  { ids: ["hiroshima-05m-cs"], name: "広島県CS立体図（広島県／0.5m／2022）", on: true },
  { ids: ["hiroshima-1m-cs"], name: "広島県CS立体図（広島県／1m／2014–2018）", on: true },
  { ids: ["tokushima-yoshinogawa-cs"], name: "徳島県(吉野川)CS立体図（林野庁／0.5m／2019–2022）" },
  { ids: ["tokushima-naka-kaifu-cs"], name: "徳島県(那賀・海部川)CS立体図（林野庁／0.5m／2018–2020）" },
  { ids: ["ehime-cs"], name: "愛媛県CS立体図（愛媛県／0.5m／2018）" },
  { ids: ["kochi-cs"], name: "高知県CS立体図（高知県／-／2018）" },
  { ids: ["kumamoto-oita-cs"], name: "熊本県・大分県CS立体図（林野庁／0.5m／2016）" },
  { ids: ["oita-nanbu-cs"], name: "大分県(大分南部)CS立体図（林野庁／0.5m／2020）" },
  { ids: ["r2-7-gouu-cs"], name: "令和2年7月豪雨CS立体図(九州)（林野庁／0.5m／2020）" },
];

/** CS立体図以外の重ねもの。 */
export const OTHER_LAYERS: LayerDef[] = [
  { ids: ["fude-polygon", "fude-line"], name: "法務省地図(2024年)" },
  { ids: ["plateau-bldg"], name: "3D都市モデル建築物(2023年)" },
  { ids: ["seamlessphoto"], name: "全国最新写真（シームレス）" },
  { ids: ["yamajiro", "yamajiro-label"], name: "山城（山城攻城記）" },
];

/** 不透明度スライダーが対象にする CS立体図の全レイヤーID。 */
export const CS_LAYER_IDS: string[] = CS_LAYERS.flatMap((d) => d.ids);
