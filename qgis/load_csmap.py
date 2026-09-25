"""CS立体図のラスタタイルをすべて QGIS に一括で追加する。

使い方:
  - QGIS の Python コンソールで実行する（プラグイン > Python コンソール > エディタで開いて ▶）
  - またはスタンドアロンで実行して .qgz を書き出す:
      "C:/Program Files/QGIS 3.34.12/bin/python-qgis-ltr.bat" qgis/load_csmap.py qgis/csmap.qgz

レイヤー一覧は public/style/pale.json と src/layers.ts から生成したもの。
zmax は csmap-tiles の datasets.json、外部配信分は実タイルの取得確認による。
"""

import sys

from qgis.core import (
    QgsApplication,
    QgsCoordinateReferenceSystem,
    QgsDataSourceUri,
    QgsLayerMetadata,
    QgsProject,
    QgsRasterLayer,
)

# (id, 表示名, タイルURL, zmax, 出典, 出典URL)
CS_LAYERS = [
    ('miyagi-cs', '宮城県CS立体図', 'https://shi-works.com/raster-tiles/pref-miyagi/miyagi-csmap-tiles/{z}/{x}/{y}.webp', 17, '宮城県CS立体図(宮城県グリッドデータを加工して作成)', 'https://miyagi.dataeye.jp/resources/1523'),
    ('yamagata-shonai-cs', '山形県(庄内)CS立体図', 'https://rinya-tiles.geospatial.jp/csmap_028_2025/{z}/{x}/{y}.webp', 18, '林野庁 山形県(庄内森林計画区)CS立体図', 'https://www.geospatial.jp/ckan/dataset/028_syounai'),
    ('fukushima-cs', '福島県CS立体図', 'https://www2.ffpri.go.jp/soilmap/tile/cs_fukushima/{z}/{x}/{y}.png', 17, '森林総合研究所 CS立体図', 'https://www2.ffpri.go.jp/soilmap/data-src.html'),
    ('tochigi-cs', '栃木県CS立体図', 'https://rinya-tochigi.geospatial.jp/2023/rinya/tile/csmap/{z}/{x}/{y}.png', 18, '栃木県微地形図（CS立体図）', 'https://www.geospatial.jp/ckan/dataset/csmap_tochigi'),
    ('saitama-cs', '埼玉県CS立体図', 'https://shi-works.com/raster-tiles/pref-saitama/saitama-csmap-tiles/{z}/{x}/{y}.webp', 18, '埼玉県CS立体図(埼玉県3次元点群データを加工して作成)', 'https://portal-pref-saitama.hub.arcgis.com/'),
    ('tokyo-23ku-cs', '東京都(区部)CS立体図', 'https://shi-works.com/raster-tiles/tokyo-digitaltwin/23ku-csmap-tiles/{z}/{x}/{y}.webp', 19, '東京都(区部)CS立体図(東京都デジタルツイン実現プロジェクト 区部点群データを加工して作成)', ''),
    ('tokyo-tama-cs', '東京都(多摩地域)CS立体図', 'https://shi-works.com/raster-tiles/tokyo-digitaltwin/tama-csmap-tiles/{z}/{x}/{y}.webp', 19, '東京都(多摩地域)CS立体図(東京都デジタルツイン実現プロジェクト 多摩地域点群データを加工して作成)', 'https://www.geospatial.jp/ckan/dataset/tokyopc-tama-2023'),
    ('tokyo-shima-01-cs', '東京都(島しょ地域・大島)CS立体図', 'https://shi-works.com/raster-tiles/tokyo-digitaltwin/shima-01-izu-oshima-csmap-tiles/{z}/{x}/{y}.webp', 19, '東京都(島しょ地域)CS立体図(東京都デジタルツイン実現プロジェクト 島しょ地域点群データを加工して作成)', 'https://www.geospatial.jp/ckan/dataset/tokyopc-shima-2023'),
    ('tokyo-shima-02-cs', '東京都(島しょ地域・利島・新島・式根島・神津島)CS立体図', 'https://shi-works.com/raster-tiles/tokyo-digitaltwin/shima-02-toshima-kozushima-csmap-tiles/{z}/{x}/{y}.webp', 19, '東京都(島しょ地域)CS立体図(東京都デジタルツイン実現プロジェクト 島しょ地域点群データを加工して作成)', 'https://www.geospatial.jp/ckan/dataset/tokyopc-shima-2023'),
    ('tokyo-shima-03-cs', '東京都(島しょ地域・三宅島)CS立体図', 'https://shi-works.com/raster-tiles/tokyo-digitaltwin/shima-03-miyakejima-csmap-tiles/{z}/{x}/{y}.webp', 19, '東京都(島しょ地域)CS立体図(東京都デジタルツイン実現プロジェクト 島しょ地域点群データを加工して作成)', 'https://www.geospatial.jp/ckan/dataset/tokyopc-shima-2023'),
    ('tokyo-shima-04-cs', '東京都(島しょ地域・御蔵島)CS立体図', 'https://shi-works.com/raster-tiles/tokyo-digitaltwin/shima-04-mikurajima-csmap-tiles/{z}/{x}/{y}.webp', 19, '東京都(島しょ地域)CS立体図(東京都デジタルツイン実現プロジェクト 島しょ地域点群データを加工して作成)', 'https://www.geospatial.jp/ckan/dataset/tokyopc-shima-2023'),
    ('tokyo-shima-05-cs', '東京都(島しょ地域・八丈島)CS立体図', 'https://shi-works.com/raster-tiles/tokyo-digitaltwin/shima-05-hachijojima-csmap-tiles/{z}/{x}/{y}.webp', 19, '東京都(島しょ地域)CS立体図(東京都デジタルツイン実現プロジェクト 島しょ地域点群データを加工して作成)', 'https://www.geospatial.jp/ckan/dataset/tokyopc-shima-2023'),
    ('tokyo-shima-06-cs', '東京都(島しょ地域・青ヶ島)CS立体図', 'https://shi-works.com/raster-tiles/tokyo-digitaltwin/shima-06-aogashima-csmap-tiles/{z}/{x}/{y}.webp', 19, '東京都(島しょ地域)CS立体図(東京都デジタルツイン実現プロジェクト 島しょ地域点群データを加工して作成)', 'https://www.geospatial.jp/ckan/dataset/tokyopc-shima-2023'),
    ('kanagawa-cs', '神奈川県CS立体図', 'https://shi-works.com/raster-tiles/pref-kanagawa/kanagawa-csmap-tiles/{z}/{x}/{y}.webp', 18, '神奈川県CS立体図(データ提供:(神奈川県環境農政局緑政部森林再生課))', 'https://www.geospatial.jp/ckan/dataset?q=%E7%A5%9E%E5%A5%88%E5%B7%9D%E7%9C%8C+3%E6%AC%A1%E5%85%83%E7%82%B9%E7%BE%A4&sort=metadata_modified+desc'),
    ('noto-nagaoka-rinya-cs', '能登・長岡CS立体図(林野庁2025)', 'https://rinya-tiles.geospatial.jp/csmap_r06eq_2025/{z}/{x}/{y}.webp', 18, '林野庁 令和6年能登半島地震CS立体図(能登・長岡)', 'https://www.geospatial.jp/ckan/dataset/r6_noto-peninsula-earthquake'),
    ('toyama-cs', '富山県CS立体図', 'https://shi-works.com/raster-tiles/pref-toyama/toyama-csmap-tiles/{z}/{x}/{y}.webp', 18, '富山県CS立体図(富山県 数値標高モデル（DEM）を加工して作成)', 'https://www.geospatial.jp/ckan/dataset/dem'),
    ('noto-cs', '能登CS立体図(速報成果)', 'https://rinya.geospatial.jp/tile/csmaptile_noto/{z}/{x}/{y}.png', 17, '林野庁能登地域CS立体図(発災後)', 'https://www.geospatial.jp/ckan/dataset/r6_noto-peninsula-earthquake'),
    ('noto-cs-final', '能登CS立体図(最終成果)', 'https://shi-works.com/raster-tiles/rinya/noto-2024-csmap-tiles/{z}/{x}/{y}.webp', 18, '林野庁能登地域CS立体図(能登地域0.5mDEM(発災後)を加工して作成)', 'https://www.geospatial.jp/ckan/dataset/r6_noto-peninsula-earthquake'),
    ('yamanashi-cs', '山梨県CS立体図', 'https://shi-works.com/raster-tiles/pref-yamanashi/yamanashi-csmap-tiles/{z}/{x}/{y}.webp', 18, '山梨県CS立体図(山梨県グリッドデータDEMを加工して作成)', 'https://www.geospatial.jp/ckan/dataset/yamanashi-pointcloud-2024'),
    ('nagano-cs', '長野県CS立体図(1m)', 'https://tile.geospatial.jp/CS/VER2/{z}/{x}/{y}.png', 18, '長野県CS立体図（長野県林業総合センター）', 'https://www.geospatial.jp/ckan/dataset/nagano-csmap'),
    ('nagano-05m-cs', '長野県CS立体図(0.5m)', 'https://shi-works.com/raster-tiles/pref-nagano/nagano-csmap-tiles/{z}/{x}/{y}.webp', 18, 'この長野県CS立体図(0.5m)は長野県林務部長の承認を得て森林計画図を使用して作成したものである。承認番号 7森政第51-3号', 'https://www.geospatial.jp/ckan/dataset/r3-4-50cmdem'),
    ('nagano-inatani-cs', '長野県(伊那谷)CS立体図', 'https://rinya-tiles.geospatial.jp/csmap_067_2025/{z}/{x}/{y}.webp', 18, '林野庁 長野県(伊那谷森林計画区)CS立体図', 'https://www.geospatial.jp/ckan/dataset/inatani_067'),
    ('gifu-cs', '岐阜県CS立体図', 'https://kenzkenz2.xsrv.jp/gihucs/{z}/{x}/{-y}.png', 18, '岐阜県CS立体図', 'https://www.geospatial.jp/ckan/dataset/cs-2019-geotiff'),
    ('shizuoka-cs', '静岡県CS立体図', 'https://shi-works.com/raster-tiles/pref-shizuoka/shizuoka-csmap-tiles/{z}/{x}/{y}.webp', 18, '静岡県CS立体図', 'https://www.geospatial.jp/ckan/dataset/shizuoka-2023-csmap'),
    ('aichi-owari-nishimikawa-cs', '愛知県(尾張西三河)CS立体図', 'https://rinya-tiles.geospatial.jp/csmap_078_2025/{z}/{x}/{y}.webp', 18, '林野庁 愛知県(尾張西三河森林計画区)CS立体図', 'https://www.geospatial.jp/ckan/dataset/owarinishimikawa_078'),
    ('aichi-higashimikawa-cs', '愛知県(東三河)CS立体図', 'https://rinya-tiles.geospatial.jp/csmap_079_2025/{z}/{x}/{y}.webp', 18, '林野庁 愛知県(東三河森林計画区)CS立体図', 'https://www.geospatial.jp/ckan/dataset/higashimikawa_079'),
    ('mie-kitaise-cs', '三重県(北伊勢)CS立体図', 'https://rinya-tiles.geospatial.jp/csmap_081_2025/{z}/{x}/{y}.webp', 18, '林野庁 三重県(北伊勢森林計画区)CS立体図', 'https://www.geospatial.jp/ckan/dataset/kitaise_081'),
    ('shiga-cs', '滋賀県CS立体図', 'https://forestgeo.info/opendata/25_shiga/csmap_2023/{z}/{x}/{y}.webp', 18, '滋賀県CS立体図(林野庁 微地形表現図)', 'https://www.geospatial.jp/ckan/dataset/rinya-shiga-maptiles'),
    ('kyoto-cs', '京都府CS立体図', 'https://shi-works.com/raster-tiles/pref-kyoto/kyoto-csmap-tiles/{z}/{x}/{y}.webp', 18, '京都府CS立体図(京都府「数値標高モデル（DEM）」を加工して作成)', 'https://www.geospatial.jp/ckan/dataset/dem05_kyoto'),
    ('osaka-cs', '大阪府CS立体図', 'https://shi-works.com/raster-tiles/pref-osaka/osaka-csmap-tiles/{z}/{x}/{y}.webp', 18, '大阪府CS立体図', 'https://www.geospatial.jp/ckan/dataset/cs'),
    ('hyogo-cs', '兵庫県CS立体図', 'https://rinya-hyogo.geospatial.jp/2023/rinya/tile/csmap/{z}/{x}/{y}.png', 18, '兵庫県微地形図（CS立体図）', 'https://www.geospatial.jp/ckan/dataset/csmap_hyogo'),
    ('wakayama-cs', '和歌山県CS立体図', 'https://shi-works.com/raster-tiles/pref-wakayama/wakayama-csmap-tiles/{z}/{x}/{y}.webp', 17, '和歌山県CS立体図(和歌山県3次元点群データを加工して作成)', 'https://wakayamaken.geocloud.jp/mp/22'),
    ('tottori-cs', '鳥取県CS立体図', 'https://rinya-tottori.geospatial.jp/tile/rinya/2024/csmap_tottori/{z}/{x}/{y}.png', 18, '鳥取県CS立体図', 'https://www.geospatial.jp/ckan/dataset/csmap_tottori'),
    ('tottori-2025-cs', '鳥取県CS立体図(2025年)', 'https://shi-works.com/raster-tiles/pref-tottori/tottori-csmap-tiles/{z}/{x}/{y}.webp', 18, '鳥取県CS立体図(鳥取県「数値標高モデル(DEM)0.5m」を加工して作成)', 'https://www.geospatial.jp/ckan/dataset/dem05_tottori'),
    ('okayama-cs', '岡山県CS立体図(林野庁0.5m)', 'https://www2.ffpri.go.jp/soilmap/tile/cs_okayama/{z}/{x}/{y}.png', 17, '森林総合研究所CS立体図', 'https://www2.ffpri.go.jp/soilmap/data-src.html'),
    ('okayama-2024-cs', '岡山県CS立体図(岡山県0.5m)', 'https://shi-works.com/raster-tiles/pref-okayama/okayama-csmap-tiles/{z}/{x}/{y}.webp', 18, '岡山県CS立体図(岡山県グリッドデータを加工して作成)', 'https://i-box.pref.okayama.jp/datasets/251'),
    ('hiroshima-cs', '広島県CS立体図(林野庁0.5m)', 'https://www2.ffpri.go.jp/soilmap/tile/cs_hiroshima/{z}/{x}/{y}.png', 17, '森林総合研究所CS立体図', 'https://www2.ffpri.go.jp/soilmap/data-src.html'),
    ('hiroshima-05m-cs', '広島県CS立体図(広島県0.5m)', 'https://shi-works.com/raster-tiles/pref-hiroshima/hiroshima-0.5m-csmap-tiles/{z}/{x}/{y}.webp', 18, '広島県CS立体図(広島県3次元点群データを加工して作成)', 'https://hiroshima-dobox.jp/index2'),
    ('hiroshima-1m-cs', '広島県CS立体図(広島県1m)', 'https://shi-works.com/raster-tiles/pref-hiroshima/hiroshima-1m-csmap-tiles/{z}/{x}/{y}.webp', 17, '広島県CS立体図(広島県3次元点群データを加工して作成)', 'https://hiroshima-dobox.jp/index2'),
    ('tokushima-yoshinogawa-cs', '徳島県(吉野川)CS立体図', 'https://rinya-tiles.geospatial.jp/csmap_116_2025/{z}/{x}/{y}.webp', 18, '林野庁 徳島県(吉野川森林計画区)CS立体図', 'https://www.geospatial.jp/ckan/dataset/yoshinokawa_116'),
    ('tokushima-naka-kaifu-cs', '徳島県(那賀・海部川)CS立体図', 'https://rinya-tiles.geospatial.jp/csmap_117_2025/{z}/{x}/{y}.webp', 18, '林野庁 徳島県(那賀・海部川森林計画区)CS立体図', 'https://www.geospatial.jp/ckan/dataset/tokushima_aerial_laser'),
    ('ehime-cs', '愛媛県CS立体図', 'https://rinya-ehime.geospatial.jp/tile/rinya/2024/csmap_Ehime/{z}/{x}/{-y}.png', 18, '愛媛県CS立体図', 'https://www.geospatial.jp/ckan/dataset/csmap_ehime'),
    ('kochi-cs', '高知県CS立体図', 'https://rinya-kochi.geospatial.jp/2023/rinya/tile/csmap/{z}/{x}/{y}.png', 18, '高知県微地形図（CS立体図）', 'https://www.geospatial.jp/ckan/dataset/csmap_kochi'),
    ('kumamoto-oita-cs', '熊本県・大分県CS立体図', 'https://www2.ffpri.go.jp/soilmap/tile/cs_kumamoto_oita/{z}/{x}/{y}.png', 17, '森林総合研究所 CS立体図', 'https://www2.ffpri.go.jp/soilmap/data-src.html'),
    ('oita-nanbu-cs', '大分県(大分南部)CS立体図', 'https://rinya-tiles.geospatial.jp/csmap_143_2025/{z}/{x}/{y}.webp', 18, '林野庁 大分県(大分南部森林計画区)CS立体図', 'https://www.geospatial.jp/ckan/dataset/oita_aerial_laser'),
    ('r2-7-gouu-cs', '令和2年7月豪雨CS立体図(九州)', 'https://rinya-tiles.geospatial.jp/csmap_r0207tr_2025/{z}/{x}/{y}.webp', 18, '林野庁 令和2年7月豪雨CS立体図', 'https://www.geospatial.jp/ckan/dataset/r2_7_gouu'),
]

BASEMAP = (
    "地理院タイル(淡色地図)",
    "https://cyberjapandata.gsi.go.jp/xyz/pale/{z}/{x}/{y}.png",
    18,
)


def xyz_layer(name, url, zmax):
    uri = QgsDataSourceUri()
    uri.setParam("type", "xyz")
    uri.setParam("url", url)
    uri.setParam("zmin", "0")
    uri.setParam("zmax", str(zmax))
    layer = QgsRasterLayer(bytes(uri.encodedUri()).decode(), name, "wms")
    if not layer.isValid():
        print(f"読み込み失敗: {name} {url}")
    return layer


def load(project):
    root = project.layerTreeRoot()
    group = root.insertGroup(0, "CS立体図")
    for _id, name, url, zmax, attribution, href in CS_LAYERS:
        layer = xyz_layer(name, url, zmax)
        md = QgsLayerMetadata(layer.metadata())
        md.setRights([f"出典: {attribution} {href}".strip()])
        layer.setMetadata(md)
        project.addMapLayer(layer, False)
        group.addLayer(layer)

    base = xyz_layer(*BASEMAP)
    project.addMapLayer(base, False)
    root.addLayer(base)

    project.setCrs(QgsCoordinateReferenceSystem("EPSG:3857"))
    print(f"CS立体図 {len(CS_LAYERS)} レイヤーを追加しました")


if QgsApplication.instance() is not None:
    # QGIS の Python コンソールから実行
    load(QgsProject.instance())
else:
    out = sys.argv[1] if len(sys.argv) > 1 else "csmap.qgz"
    app = QgsApplication([], False)
    app.initQgis()
    project = QgsProject.instance()
    load(project)
    project.write(out)
    print(f"書き出し: {out}")
    app.exitQgis()
