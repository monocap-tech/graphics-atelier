# G00-A04 — Multipart authorship, the grid and runtime handoff

2026-11-18. R1 documentary findings and original isolated control; no editor, engine or third-party code executed.

## Qualified sources

| ID | Source | Observation and limits |
|---|---|---|
| SRC062 | [SpriteStudio 7, アニメーションを作成する](https://www.webtech.co.jp/help/ja/spritestudio7/starter/creating/) | Official JP guide: project SSPJ, SSCE cell map (texture plus extraction metadata), SSAE animation, SSEE effects, cell pivot and parent/child organization. Distinguish reference texture, cell, part, transform, order and animation. |
| SRC063 | [SEGA TECH Blog, Anima2Dでキャラクターアニメーションを作ろう！編, 2018-03-26](https://techblog.sega.jp/entry/2018/03/26/100000) | JP corporate technical tutorial. Motion requirements precede part separation; rotate parts in Photoshop to inspect gaps, extend hidden artwork, one alphanumeric-named layer/PNG per part, atlas and automated Unity import. Anima2D-era instructions, not contemporary package compatibility certification or a claim of historical Treasure practice. |
| SRC064 | [さらえみ, SpriteStudio制作例](https://saraemi.com/2112spstudio-making/) | Independent operator account, JP: define cells and origins, setup, explicit visual priority, parent/child tree, keys for position/rotation/scale/visibility/opacity. No source project obtained. |
| SRC065 | [SpriteStudio 7.6.0 release notes](https://www.webtech.co.jp/help/ss7_releasenote/ver760/) | Official JP: CleanEdge for rotated outlines, Kuwahara filter for reduced-size rendering (example 512x512 canvas to 64x64 viewport), outline generation, pixel simulation and viewport. As of 2026-09-17 preview options not reflected in Player; use SSCE rendering or PNG frames. This is documentation not measured filter behavior or player status after that date. |
| SRC066 | [SpriteStudio nearest filtering guide](https://www.webtech.co.jp/help/ja/spritestudio7/guide/reference/texturefiltermode/) | Official JP: nearest texture filtering can be set project-wide or per cell map. Does not imply transformed geometry lands on shared output grid. |
| SRC067 | [Muscat, ドット絵のアニメーション×実写映像の試験的作品のメイキング](https://note.com/muscat_dot/n/n3594bd3c3911) | Independent JP artist: export layered transparent parts without individual trim, combine in Aseprite, rough motion guide, rotate at joints and manually repair pixels, composite with AE; experimental video, not game runtime validation. |
| SRC068 | [AnimeEffects](https://animeeffectsdevs.github.io/jp/) and [history](https://animeeffectsdevs.github.io/jp/about/) | Independent Japanese-origin open-source animation tool, initially by hidefuku; community continuation from 2019. No format, licensing or runtime interoperability audit. |
| SRC069 | [SpriteStudio beginner tutorial](https://www.webtech.co.jp/help/ja/spritestudio7/starter/spritestudio_start/) | Official JP concrete import/registration/attachment instructions; layer-preserving PSD conversion distinct from plain image import; example tool attachment and priority. |
| SRC070 | [SpriteStudio Starter](https://www.webtech.co.jp/spritestudio/starter.html) | Official JP free annually renewed license with registration, Windows/macOS, eligibility table prior fiscal-year revenue under JPY10m; verify actual terms/use eligibility before acquisition. No registration or software installation performed. |

R0 leads (full page failed or not opened): SRC071 [HSP wiki 多関節](https://wiki.hsp.moe/%E5%B0%8F%E3%83%AF%E3%82%B6%EF%BC%8F%E5%A4%9A%E9%96%A2%E7%AF%80.html) (cache miss; programming and possible Bullet x Ecology bridge); SRC072 [SMT V UI production interview](https://www.webtech.co.jp/blog/news/15819/) (503; excerpt mentions SpriteStudio null parts and UMG coexistence; do not claim full workflow); SRC073 [SpriteStudio pixel-art simulation guide](https://www.webtech.co.jp/help/ja/spritestudio7/guide/pixelart/) (existing SRC038 lead, 503; use SRC065 for supported release claims instead); SRC074 [Bonesmith](https://paspallas.itch.io/bonesmith) (search excerpt about angle-specific sprite variants, not inspected or tested); SRC075 [Pixel Puppettier](https://github.com/zephyrux-lux/Pixel-Puppettier) (search excerpt on layer rigs and baked cels, no source audit). Search queries included 多関節 スプライト シューティング 自作, SpriteStudio ドット絵 回転, パーツ分け アニメーション 作成 and Japanese independent tool alternatives.

## Synthesis

Four separable authoring strategies: hand-drawn full frames; transform-and-correct in Aseprite; authoring rig baked into grid-aligned frames; live hierarchy evaluated at runtime (optionally using angle-specific drawings or a logical raster pass). One project may mix these. Mechanical assets, irregular human poses and effects have different tolerance for continuous transforms. Do not conclude hand drawing is unnecessary or that nearest sampling alone ensures logical alignment.

Procurement relationship: request motion envelopes, overlap/hidden areas, named editable layers and registration/pivots; do not assume a finished standing illustration contains occluded regions. Part boundaries are chosen according to motion requirements and labor, not maximum segmentation.

See [G03-P02](studies/G03-P02.md) for a shared-grid and hierarchical-transform experiment, with a proposed actual authoring comparison.
