# CS 立体図タイルの配信 URL 移行案内

最終更新: 2026-09-06

本リポジトリで公開している CS 立体図タイル（23 データセット）の配信元を、Xserver（`*.xsrv.jp`）から
Cloudflare R2（`https://shi-works.com/`）へ移行しました。旧 URL を直接参照しているアプリ・スタイル定義・QGIS
プロジェクトなどは、下記の規則で書き換えてください。

## 旧 URL の停止時期

| 旧ホスト | 対象データセット | 停止 |
|---|---|---|
| `xs489works.xsrv.jp` | 大阪府、和歌山県、広島県 1m、東京都（島しょ地域 01〜06） | **2026-09-30** |
| `shiworks.xsrv.jp` | 静岡県、神奈川県、埼玉県、広島県 0.5m、東京都（区部・多摩地域）、能登地域 | 移行完了後に停止（時期は本ページで告知） |
| `shiworks2.xsrv.jp` | 京都府、宮城県、長野県、岡山県、鳥取県、富山県、山梨県 | 同上 |

## 書き換え規則

1. **ホスト名**: `https://xs489works.xsrv.jp/` `https://shiworks.xsrv.jp/` `https://shiworks2.xsrv.jp/` → `https://shi-works.com/`
2. **ディレクトリ名**: 下表のとおり `{出所}/{地域}-csmap-tiles` に統一（14 件が変更、9 件は変更なし）
3. **拡張子**: `.png` → **`.webp`**（品質 q=95 で再圧縮。見た目は変わらず、容量は 79% 減）

```
旧: https://xs489works.xsrv.jp/raster-tiles/pref-osaka/osaka-cs-tiles/{z}/{x}/{y}.png
新: https://shi-works.com/raster-tiles/pref-osaka/osaka-csmap-tiles/{z}/{x}/{y}.webp
```

ズームレベル・タイルサイズ（256px）・座標系（Web メルカトル、XYZ）は変わりません。
MapLibre GL JS / Mapbox GL JS / Leaflet / OpenLayers / QGIS / GDAL はいずれも WebP タイルをそのまま扱えます。

## 対応表

旧 URL と新 URL をそのまま併記します。ディレクトリ名が変わらないものも、ホスト名と拡張子は変わります。

| データセット | 旧 URL（停止予定） | 新 URL |
|---|---|---|
| 大阪府 | `https://xs489works.xsrv.jp/raster-tiles/pref-osaka/osaka-cs-tiles/{z}/{x}/{y}.png` | `https://shi-works.com/raster-tiles/pref-osaka/osaka-csmap-tiles/{z}/{x}/{y}.webp` |
| 静岡県 | `https://shiworks.xsrv.jp/raster-tiles/pref-shizuoka/shizuoka-cs-tiles/{z}/{x}/{y}.png` | `https://shi-works.com/raster-tiles/pref-shizuoka/shizuoka-csmap-tiles/{z}/{x}/{y}.webp` |
| 東京都（区部） | `https://shiworks.xsrv.jp/raster-tiles/tokyo-digitaltwin/tokyopc-23ku-2024-cs-tiles/{z}/{x}/{y}.png` | `https://shi-works.com/raster-tiles/tokyo-digitaltwin/23ku-csmap-tiles/{z}/{x}/{y}.webp` |
| 東京都（多摩地域） | `https://shiworks.xsrv.jp/raster-tiles/tokyo-digitaltwin/tokyopc-tama-2023-cs-tiles/{z}/{x}/{y}.png` | `https://shi-works.com/raster-tiles/tokyo-digitaltwin/tama-csmap-tiles/{z}/{x}/{y}.webp` |
| 東京都（伊豆大島） | `https://xs489works.xsrv.jp/raster-tiles/tokyo-digitaltwin/tokyopc-shima-01-2023-cs-tiles/{z}/{x}/{y}.png` | `https://shi-works.com/raster-tiles/tokyo-digitaltwin/shima-01-izu-oshima-csmap-tiles/{z}/{x}/{y}.webp` |
| 東京都（利島・新島・式根島・神津島） | `https://xs489works.xsrv.jp/raster-tiles/tokyo-digitaltwin/tokyopc-shima-02-2023-cs-tiles/{z}/{x}/{y}.png` | `https://shi-works.com/raster-tiles/tokyo-digitaltwin/shima-02-toshima-kozushima-csmap-tiles/{z}/{x}/{y}.webp` |
| 東京都（三宅島） | `https://xs489works.xsrv.jp/raster-tiles/tokyo-digitaltwin/tokyopc-shima-03-2023-cs-tiles/{z}/{x}/{y}.png` | `https://shi-works.com/raster-tiles/tokyo-digitaltwin/shima-03-miyakejima-csmap-tiles/{z}/{x}/{y}.webp` |
| 東京都（御蔵島） | `https://xs489works.xsrv.jp/raster-tiles/tokyo-digitaltwin/tokyopc-shima-04-2023-cs-tiles/{z}/{x}/{y}.png` | `https://shi-works.com/raster-tiles/tokyo-digitaltwin/shima-04-mikurajima-csmap-tiles/{z}/{x}/{y}.webp` |
| 東京都（八丈島） | `https://xs489works.xsrv.jp/raster-tiles/tokyo-digitaltwin/tokyopc-shima-05-2023-cs-tiles/{z}/{x}/{y}.png` | `https://shi-works.com/raster-tiles/tokyo-digitaltwin/shima-05-hachijojima-csmap-tiles/{z}/{x}/{y}.webp` |
| 東京都（青ヶ島） | `https://xs489works.xsrv.jp/raster-tiles/tokyo-digitaltwin/tokyopc-shima-06-2023-cs-tiles/{z}/{x}/{y}.png` | `https://shi-works.com/raster-tiles/tokyo-digitaltwin/shima-06-aogashima-csmap-tiles/{z}/{x}/{y}.webp` |
| 和歌山県 | `https://xs489works.xsrv.jp/raster-tiles/pref-wakayama/wakayamapc-cs-tiles/{z}/{x}/{y}.png` | `https://shi-works.com/raster-tiles/pref-wakayama/wakayama-csmap-tiles/{z}/{x}/{y}.webp` |
| 神奈川県 | `https://shiworks.xsrv.jp/raster-tiles/pref-kanagawa/kanagawapc-cs-tiles/{z}/{x}/{y}.png` | `https://shi-works.com/raster-tiles/pref-kanagawa/kanagawa-csmap-tiles/{z}/{x}/{y}.webp` |
| 能登地域（最終） | `https://shiworks.xsrv.jp/raster-tiles/rinya/noto-2024-csmap-tiles/{z}/{x}/{y}.png` | `https://shi-works.com/raster-tiles/rinya/noto-2024-csmap-tiles/{z}/{x}/{y}.webp` |
| 広島県 0.5m | `https://shiworks.xsrv.jp/raster-tiles/pref-hiroshima/hiroshimapc-2022-cs-tiles/{z}/{x}/{y}.png` | `https://shi-works.com/raster-tiles/pref-hiroshima/hiroshima-0.5m-csmap-tiles/{z}/{x}/{y}.webp` |
| 広島県 1m | `https://xs489works.xsrv.jp/raster-tiles/pref-hiroshima/hiroshimapc-cs-tiles/{z}/{x}/{y}.png` | `https://shi-works.com/raster-tiles/pref-hiroshima/hiroshima-1m-csmap-tiles/{z}/{x}/{y}.webp` |
| 京都府 | `https://shiworks2.xsrv.jp/raster-tiles/pref-kyoto/kyoto-csmap-tiles/{z}/{x}/{y}.png` | `https://shi-works.com/raster-tiles/pref-kyoto/kyoto-csmap-tiles/{z}/{x}/{y}.webp` |
| 山梨県 | `https://shiworks2.xsrv.jp/raster-tiles/pref-yamanashi/yamanashi-csmap-tiles/{z}/{x}/{y}.png` | `https://shi-works.com/raster-tiles/pref-yamanashi/yamanashi-csmap-tiles/{z}/{x}/{y}.webp` |
| 富山県 | `https://shiworks2.xsrv.jp/raster-tiles/pref-toyama/toyama-csmap-tiles/{z}/{x}/{y}.png` | `https://shi-works.com/raster-tiles/pref-toyama/toyama-csmap-tiles/{z}/{x}/{y}.webp` |
| 長野県 0.5m | `https://shiworks2.xsrv.jp/raster-tiles/pref-nagano/nagano-csmap-tiles/{z}/{x}/{y}.png` | `https://shi-works.com/raster-tiles/pref-nagano/nagano-csmap-tiles/{z}/{x}/{y}.webp` |
| 宮城県 | `https://shiworks2.xsrv.jp/raster-tiles/pref-miyagi/miyagi-csmap-tiles/{z}/{x}/{y}.png` | `https://shi-works.com/raster-tiles/pref-miyagi/miyagi-csmap-tiles/{z}/{x}/{y}.webp` |
| 岡山県 0.5m | `https://shiworks2.xsrv.jp/raster-tiles/pref-okayama/okayama-csmap-tiles/{z}/{x}/{y}.png` | `https://shi-works.com/raster-tiles/pref-okayama/okayama-csmap-tiles/{z}/{x}/{y}.webp` |
| 埼玉県 | `https://shiworks.xsrv.jp/raster-tiles/pref-saitama/saitama-csmap-tiles/{z}/{x}/{y}.png` | `https://shi-works.com/raster-tiles/pref-saitama/saitama-csmap-tiles/{z}/{x}/{y}.webp` |
| 鳥取県 | `https://shiworks2.xsrv.jp/raster-tiles/pref-tottori/tottori-csmap-tiles/{z}/{x}/{y}.png` | `https://shi-works.com/raster-tiles/pref-tottori/tottori-csmap-tiles/{z}/{x}/{y}.webp` |

## 置換の例

sed で一括置換する場合（GNU sed）:

```bash
sed -i -E \
  -e 's#https://(xs489works|shiworks|shiworks2)\.xsrv\.jp/raster-tiles/#https://shi-works.com/raster-tiles/#g' \
  -e 's#pref-hiroshima/hiroshimapc-2022-cs-tiles#pref-hiroshima/hiroshima-0.5m-csmap-tiles#g' \
  -e 's#pref-hiroshima/hiroshimapc-cs-tiles#pref-hiroshima/hiroshima-1m-csmap-tiles#g' \
  -e 's#pref-kanagawa/kanagawapc-cs-tiles#pref-kanagawa/kanagawa-csmap-tiles#g' \
  -e 's#pref-osaka/osaka-cs-tiles#pref-osaka/osaka-csmap-tiles#g' \
  -e 's#pref-shizuoka/shizuoka-cs-tiles#pref-shizuoka/shizuoka-csmap-tiles#g' \
  -e 's#pref-wakayama/wakayamapc-cs-tiles#pref-wakayama/wakayama-csmap-tiles#g' \
  -e 's#tokyo-digitaltwin/tokyopc-23ku-2024-cs-tiles#tokyo-digitaltwin/23ku-csmap-tiles#g' \
  -e 's#tokyo-digitaltwin/tokyopc-tama-2023-cs-tiles#tokyo-digitaltwin/tama-csmap-tiles#g' \
  -e 's#tokyo-digitaltwin/tokyopc-shima-01-2023-cs-tiles#tokyo-digitaltwin/shima-01-izu-oshima-csmap-tiles#g' \
  -e 's#tokyo-digitaltwin/tokyopc-shima-02-2023-cs-tiles#tokyo-digitaltwin/shima-02-toshima-kozushima-csmap-tiles#g' \
  -e 's#tokyo-digitaltwin/tokyopc-shima-03-2023-cs-tiles#tokyo-digitaltwin/shima-03-miyakejima-csmap-tiles#g' \
  -e 's#tokyo-digitaltwin/tokyopc-shima-04-2023-cs-tiles#tokyo-digitaltwin/shima-04-mikurajima-csmap-tiles#g' \
  -e 's#tokyo-digitaltwin/tokyopc-shima-05-2023-cs-tiles#tokyo-digitaltwin/shima-05-hachijojima-csmap-tiles#g' \
  -e 's#tokyo-digitaltwin/tokyopc-shima-06-2023-cs-tiles#tokyo-digitaltwin/shima-06-aogashima-csmap-tiles#g' \
  -e 's#(shi-works\.com/raster-tiles/[^"'"'"' ]*-csmap-tiles/\{z\}/\{x\}/\{y\})\.png#\1.webp#g' \
  path/to/style.json
```

## ライセンス

タイルは [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.ja) です。出典表示の文言と注意事項は
[README のライセンス節](README.md#ライセンス) を参照してください。

## 連絡先

不明点や、大量アクセスを伴う利用の予定がある場合は [@shi__works](https://x.com/shi__works) までご連絡ください。
