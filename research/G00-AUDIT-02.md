# G00-A02 — Japanese independent raster and STG production

2026-11-18. R1 for bounded observations. No commercial artwork mirrored, no application run. This pass advances G00 and G02 jointly.

| ID | Source | Qualified contribution |
|---|---|---|
| SRC046 | [アトリエ・エクレア, Godot Engine シューティングゲーム制作日記](https://ateliereclair.blog.fc2.com/blog-entry-699.html), JP, dated entries Jan–Feb 2019 | Godot 3.1 beta1; 1920x1080 project, 960x600 test window, 2d stretch/keep, pixel snap. Player art 50x50 exported doubled then 1.5x node scale; later character/GUI scale 1.4 to reduce pixel deformation and adjust size. Background 960x600 doubled; explosion 200x200/frame, switched away from pixel art for appearance. Entries 017–019 describe aiming, lock gauge and tracking marker, unlock on disappearance or time-out. B/R1. No build or source code inspected. |
| SRC047 | [緒方ひろと, unityでの縦スクロールシューティングの解像度を考察する](https://note.com/ogatahiroto/n/n64b6b64185b8), JP, 2026-03-26 | Compares logical 240x320 and 240x360 for integer scaling at 720p/1080p and rotated display. Developer recommendation, not a universal historical rule. B/R1. |
| SRC048 | [緒方ひろと, ドット絵ゲームの解像度についての考察](https://note.com/ogatahiroto/n/n4908ddce4763), JP, 2025-07-13 | Considers 256x224, 320x180, 320x240; notes tension between integer fit, available gameplay area and 16x16 construction blocks. B/R1; personal preference and visual claims not independently tested. |
| SRC049 | [やぢおぅ / Yazioh, 単色 シューティングゲーム素材(1) 自機](https://note.com/yazioh/n/nf872f9520f65), JP, 2025-01-04 | Native 16x16 ship patterns in TinySprite text format, 256x192 sheet, conversion to BASIC/C. Author expressly waives copyright claims for supplied patterns; no general legal/license conclusion, no artwork copied here. B/R1; A02 atlas records derived counts from three text matrices. |
| SRC050 | [桝久堂, 格ゲー作画講座3](https://www.maskedo.com/howto03/), JP, copyright 2010 | Fighting-game sprite training prioritizes knowledge of anatomy, articulation and exercises over pixel placement in isolation. Personal experience; no quantitative training validation. B/R1. |
| SRC051 | [桝久堂, ドット絵講座を受講してみた。](https://www.maskedo.com/post-8633/), JP, 2014 | Independent cross-critique of online instruction; search excerpt only, R0 pending full-text inspection. |
| SRC052 | [the PIXEL MAGAZINE — LIBRARY](https://thepixel-mag.jp/library/), JP | Bibliographic network connecting Japanese pixel artists and EDGE instruction; search excerpt only, R0. |
| SRC053 | [ドット絵講座, R研究所, 2004](https://books.rakuten.co.jp/rb/10171716/), JP | Published manual with basics, intermediate palette/AA and applied animation, catalog record only; R0. |
| SRC005 | [NDL bibliographic record](https://ndlsearch.ndl.go.jp/books/R100000002-I000007662761) | Confirms 高野隼人, March 2005, 秀和システム, ISBN 4-7980-1011-1; not the book contents. |
| SRC044 | [桝久堂, 格ゲー作画講座2](https://www.maskedo.com/howto02/) | Additional qualification of palette constraint from indexed search excerpt: 16 total entries INCLUDING transparent; distinguish 15 opaque colors from G03's proposed 16 opaque limit. |

Searches included ドット絵講座 EDGE 個人, 格ゲー作画, シューティング 自機 サイズ, 縦スクロールシューティング 解像度 and older link networks. SRC025 and SRC028 direct fetch failed (cache miss and 502); Maskedo recommended links page /howto04 timed out. Do not claim the old network has been exhaustively recovered. The journal is stronger evidence than search snippets because dated development entries and revisions are inspectable.

## Consequence

Distinguish native drawing resolution, export resolution, world-to-logical projection, final display scaling, and layer-specific sampling. Independently authored effects need not inherit the raster actor's resolution; test composition and readability rather than assume all layers use one grid. The same lock-on journal provides a concrete G08 lead for state and presentation integration, not a validated substitute for the atelier curriculum.

See [G02-A02 atlas](G02-ATLAS-01.md) for dimensional comparison and first native matrix measurements.
