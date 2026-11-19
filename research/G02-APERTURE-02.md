# G02-APERTURE-02 — AJA Fr01: animation layout as paper-to-screen contract

2026-11-19. Follow-up to [G02-APERTURE-01](G02-APERTURE-01.md); upgrades SRC037 to R1 for its specified geometry and stated rationale. Independent bounded intake, not launch of Round 01 S06 or a new implementation.

## Direct evidence

The Association of Japanese Animations (AJA) publishes a voluntary HD 16:9 layout-paper recommendation, an explanatory document, and AI/PSD/PDF templates. The standard's purpose is to reduce inconsistencies and configuration mistakes in inter-company animation, finishing and compositing workflows; it reports previously heterogeneous company layouts, not universal historical uniformity. Explanatory PDF pages 1–2 and the one-page template have been visually inspected. The template shows a solid main frame, dashed inner/outer frames, center cross, edge midpoints, and three peg holes (central round hole/side slots). Template dimensions below derive from the written specification, not pixel measurements.

| Role | Fr01 value | Purpose |
|---|---|---|
| D, sheet | A4 landscape 297 × 210 mm | familiar duplication and lower procurement cost |
| T, main frame | 10 × 5.625 in; 254 × 142.875 mm | 16:9 output; decimal raster conversion |
| S, safety frame (optional guide) | 90% per axis; 228.6 × 128.5875 mm | allowance for receiver display variability |
| B, scan frame (optional guide) | 110% per axis; 279.4 × 157.1625 mm | drawing/finishing and camera movement |
| Registration | frame center 104.775 mm below peg-hole center; centered horizontally; top-to-peg center approx. 10–12 mm selectable | align drawings and scans while permitting handling |

The rationale mentions an NHK active-scan information range of 93% horizontal / 93.1% vertical, citing a 2007/2008 Japanese film-TV engineering handbook; AJA uses symmetric 90% for convenience. This is direct evidence that a television visibility constraint was explicitly considered in Japanese animation authoring conventions. The handbook itself is not independently inspected; no date for Fr01's initial adoption is asserted. The 110% extent was judged necessary by production practitioners; further substrate margin guards against paper damage. A4 and inch-based imaging frame were independently motivated, not a golden/silver-ratio derivation. Size and registration are contract parameters; subsidiary guides are optional.

## Derived geometry (not an official additional requirement)

With top-left sheet origin, choose illustrative peg y=11 mm (allowed range). Frame center is (148.5,115.775) mm. Centered T top-left is (21.5,44.3375), S (34.2,51.48125), B (8.8,37.19375). The sheet and main frame have different centers vertically; never assume the sheet center is the camera origin. Normalize to T with (x−21.5)/254 and (y−44.3375)/142.875. For a centered guide, S has normalized bounds [0.05,0.95] on each axis and B [−0.05,1.05]. Explicit edge coordinates, not merely width and height, are needed.

The 2016-02 METI project report, アニメーション デジタル作画導入のためのマニュアル, section 2.4 pp.35–36, explicitly gives scan pixels as length in inches × scan dpi and uses AJA's 10-inch frame to derive 192 dpi (1920 × 1080). At a sampling density r pixels/inch, T=(10r,5.625r), S=0.9T and B=1.1T. These derived examples use integer extents (no claim about a studio's actual scanning preferences):
| r | T | S | B |
|---:|---|---|---|
| 96 | 960×540 | 864×486 | 1056×594 |
| 192 | 1920×1080 | 1728×972 | 2112×1188 |
| 384 | 3840×2160 | 3456×1944 | 4224×2376 |

At 128 dpi T=1280×720, S=1152×648, B=1408×792; a centered crop maps B's offset (64,36) to T's origin. Rasterization must still declare edge rounding, origin, filtering and registration; dpi metadata alone cannot prove acquired detail. No scan/export performed. The report's text was retrieved, but rendering its relevant PDF page failed twice (cache miss); no independent visual claim from its figure is made.

## Layout as handoff, not merely framing

Commercial animation director 益山亮司 (2021-07-11) distinguishes background layout documentation (cut identity, time/place/weather, lighting and duration) from rough key animation; camera/slide instructions must remain intelligible and avoid regions vulnerable to copying or registration-hole replacement. Compositor 泉津井陽一 (2016-02-22) describes layout as the arrangement of character/background/motion plus camera and effects directions, and the time sheet as temporal sequencing/layering; the compositor constructs the actual data from these upstream directions. These are practitioner descriptions, not observations of internal studio files. The layout carries spatial, temporal and production annotations; a logical runtime viewport would be only one recipient of that data.

## Transfer boundary / next targeted question

The previous R0 common-coordinate model has an explicit adjacent-domain exemplar: F may be a layout guide, T a reference camera aperture, S visibility protection, B drawn coverage, and a peg reference fixes transforms independently of all. For real camera motion define T(t), and distinguish coverage union over intended camera paths from device-visible intersections for critical cues. A fixed 110% B does not cover arbitrary motion and zoom: test intended trajectories against actual available image support before declaring acceptance.

Add registration reference, nominal and swept viewport bounds, and source-to-output transform trace to G02-P01 and G09's existing contracts when relevant. Do not import A4, 16:9 or 90/110% as game defaults. Next bounded source question: find a directly attested Japanese game authoring/display or arcade production document with independently stated source frame, visible frame, registration and/or safety margin; compare without requiring a common lineage. Keep this separate from Suzuki/AM2 ROM analysis; no new prototype, paper purchase or series launch authorized.

## Sources (local IDs, accessed 2026-11-19)

- G02AP2-S01 / SRC037: AJA, [AJA推奨レイアウト用紙規格](https://aja.gr.jp/jigyou/chousa/aja_layout), clauses 1–8; R1 primary specification.
- G02AP2-S02: AJA, [解説](https://aja.gr.jp/assets/files/aja_layout/aja_layout_doc.pdf), pp.1–2 text and rendered pages inspected; concluding clause 8 read as text. R1 primary rationale. NHK figures secondhand.
- G02AP2-S03: AJA, [Fr01 PDF template](https://aja.gr.jp/assets/files/aja_layout/aja_layout.pdf), page 1 visually inspected; R1 confirmation of guide/registration arrangement, not independent metrology.
- G02AP2-S04: METI project report, [アニメーション デジタル作画導入のためのマニュアル](https://www.dcaj.or.jp/project/report/pdf/2015/dc_15_02.pdf), 2016-02, §2.4 pp.35–36 extracted text; R1 bounded; screenshot inaccessible, full report not audited.
- G02AP2-S05: 益山亮司, [基礎② レイアウト用紙への指示書き](https://note.com/masuyama56/n/nf2c4075c23c4), 2021-07-11, R1 first-person professional instructional text; image annotations not inspected.
- G02AP2-S06: 泉津井陽一, [もっとアニメを知るための撮影講座 第３回](https://animestyle.jp/2016/02/22/9799/), 2016-02-22, R1 practitioner text; no project materials reproduced.

No commercial art, PDF, template source or images imported. R1 establishes documented anime/broadcast and raster-workflow relationships only; historical manga-to-game and anime-to-game transmission remain R0.
