# G02-APERTURE-01 — Dimensional apertures and compositional geometry

2026-11-19. Intake into G02-P01 and the cross-domain dimensional contract; reference lead for Round 01 S06, not a launch of that series. R1 for documented conventions, R0 for the cross-medium model and historical transmission. No new specimen, hardware measurement, engine implementation, print test or historical genealogy is established.

## Source-qualified reference geometry

A Japanese submission manuscript is not a single rectangle. CELSYS support (2014-09-14) describes a widely used B4 configuration, explicitly allowing destination-specific requirements; the I-C manufacturer confirms the sheet and nominal finish dimensions. The current CELSYS manual distinguishes the following independently configurable entities.

| Role | Japanese term | B4 example (width × height, mm) |
|---|---|---|
| Authoring substrate D | 用紙サイズ / 原稿用紙 | 257 × 364 (JIS B4, not ISO B4) |
| Extended image domain B | 裁ち落とし枠 | 230 × 320 **if** 5 mm bleed per edge is chosen; illustrative only |
| Nominal trim T | 仕上がり枠 | 220 × 310 in manuscript coordinates |
| Panel-placement guide F | 基本枠 / 内枠 | 180 × 270 |
| Protected region S | セーフライン | publisher/printer-specified; no universal numerical value |
| Local composition P_i | コマ枠 | variable; gutters, polygons, masks and intentional overflows |

The basic frame and safe line are distinct (G02AP-S03/04). The prior conversational shorthand equating them is superseded. For the centered example, T is inset 18.5 mm horizontally and 27 mm vertically from D; F is inset 20 mm on every edge from T. D is approximately 1:√2 (portrait width:height), whereas F is exactly 2:3 and T is 22:31. The 5 mm bleed is a hypothetical parameter, not a claim about the I-C product or all submissions. Actual printed edition dimensions may differ after reduction, cropping, or imposition. These numerical relationships do not establish why a particular convention arose.

## Functional analogue, not identity or historical descent

| Print role | Moving-image / interactive analogue | Limit |
|---|---|---|
| Working sheet D | source canvas, working image domain, allocated render extent | storage, authoring and raster extents need not coincide |
| Bleed B outside trim | overscan allowance or guard-band / extended render coverage | trim tolerance, CRT overscan, rasterizer guard band and effects padding have different mechanisms |
| Trim T | intended visible output / clean aperture | pixel-aspect correction, crop and display scaling are separate; encoded pixels are not automatically the displayed region |
| Panel guide F | layout grid, designated world/HUD composition guide | a guide need not clip or protect content |
| Safe S | action/graphics-safe bounds, device-specific UI safe region | readability and physical visibility are different constraints |
| Panels P_i | local viewport, split screen, inset, cut-in or masked composition | manga panels also encode sequential reading; a viewport maps coordinates, a scissor clips pixels; neither is a semantic panel by itself |

QuickTime tapt explicitly stores clean (clef), production (prof) and encoded-pixel (enof) dimensions. Production mode corrects pixel aspect without clean cropping; encoded mode does neither. These mode dimensions may be expressed in different coordinates; do not treat them as literal nested rectangles until mapped to a common coordinate system. EBU R 95 gives 3.5% action-safe and 5% graphics-safe margins **per edge** for 16:9 television (93% and 90% retained per axis respectively). It is a comparator, not a mandatory game or arcade safe-area specification. No SMPTE clause or original arcade overscan value is claimed.

## Candidate formalism

Let D be a continuous authoring region, B extended image support, T nominal presentation aperture, F compositional guide, S_j one or more protected regions by content class, and P_i local apertures. In a simple nested configuration F ⊆ T ⊆ B ⊆ D and S_j ⊆ T. Ordinary panels can lie in F; bleed panels and deliberate border breaks may extend beyond F/S_j to T or B. F and S_j need not contain each other. A panel's content support may exceed its displayed mask.

Represent each region by coordinate system, origin, units, geometry (rectangle or mask), role, policy (hard clip / soft guide / protection / extension), parent or reference frame, and provenance. Store maps from authoring to native representation to logical composition to physical display separately; record sampling and pixel aspect, scaling/letterbox, viewport and clip, and device-specific safe-area variation. For rectangle R with origin (x0,y0) and positive extent (w,h), normalize coordinates with ((x−x0)/w,(y−y0)/h). Reconstruct exact boundaries with the documented inverse map, offset and rounding policy. Measure body and full pose envelopes relative to the intended world viewport, not blindly to substrate/encoded raster or physical screen. Preserve G02-P01's occupancy rho=d*h/V, with V explicitly defined per aperture. If a HUD overlays rather than reserves space, record its obstruction separately. Aperture and collision/interaction domains are not interchangeable.

For a declared set of possible visible windows T_e (e.g. trim displacement or physical screen crop), a robust safe region can be defined as the intersection of T_e, optionally eroded by a content-specific clearance; coverage for edge-to-edge imagery can be defined by their union. This is a proposed tolerance model, not an attribution to manga publishers or broadcast engineers.

## Research implications and bounded validation

- Recover Japanese manuscript, anime layout (SRC037), camera/compositing, arcade/CRT and modern game display conventions separately; establish dated source-to-source transmission only with evidence. A/JIS B modularity, golden ratio and proportion rules remain independent hypotheses.
- Add aperture roles, extents, offsets and clipping vs guide semantics to the G02-A02 capture/measurement record. Compare actual lawful uncropped gameplay frames and documented native dimensions, not promotional crops. Measure at least two independently attested production cases where possible.
- For G02-P01's original character specimen, retain source canvas, visible body, motion extent, cell/pivot, logical viewport, HUD reservations and output crop as separate records. Use a declared test aperture and vary occupancy vs native detail independently. Add one boundary-crossing attack/effect and verify intended clipping and cue survival at output size. Compare a reserved HUD vs overlay or inset only if target warrants; no additional compulsory prototype or global default.
- The authoring brief should communicate reference frame, core cues safe under target variants, optional overflow, registration, native export envelope and permissible crop before artists draw. G09 may consume only qualified contract values. G06 may consult local composition and FX overflow without changing its cursor; Suzuki/AM2 reconstruction remains separate.

## Source registry (local IDs; accessed 2026-11-19)

- G02AP-S01 R1: I-C, [アイシー漫画原稿用紙B4（プロ漫画家・投稿用）/110kg](https://www.icscr.jp/products/genko_110-b4/). Manufacturer web text: sheet 257×364 and finish 220×310, submission use. Product images and physical sheets not measured.
- G02AP-S02 R1: CELSYS support, [CLIP STUDIO PAINT EXでの漫画投稿用原稿用紙サイズ](https://www.clip-studio.com/clip_site/support/help/detail/svc/53/tid/74832), support replies 2014-09-14: 257×364, 220×310, 180×270; requests checking exact submission destination. Not universal.
- G02AP-S03 R1: CELSYS manual [プリセット / マンガ用キャンバスの各部名称](https://help.clip-studio.com/ja-jp/manual_jp/210_files/プリセット.htm), text read: roles of paper, inner, trim and bleed frames.
- G02AP-S04 R1: CELSYS manual [新規キャンバスを作成する](https://help.clip-studio.com/ja-jp/manual_jp/210_files/新規キャンバスを作成する.htm), comic settings G–J: separately adjustable bleed, inner frame and safe line.
- G02AP-S05 R1: CELSYS manual [コマ割り【PRO/EX】](https://help.clip-studio.com/ja-jp/manual_jp/540_comic/コマ割り【PRO__47_EX】.htm), panel snapping and splitting/gutter text; no panel imagery reproduced.
- G02AP-S06 R1: Apple [Track aperture mode dimensions atom](https://developer.apple.com/documentation/quicktime-file-format/track_aperture_mode_dimensions_atom.md), full Markdown text read; companion [productionAperture](https://developer.apple.com/documentation/avfoundation/avvideoaperturemode/productionaperture) and [encodedPixels](https://developer.apple.com/documentation/avfoundation/avvideoaperturemode/encodedpixels) indexed descriptions only. No container parsed.
- G02AP-S07 R1: EBU [R 095, Safe areas for 16:9 television production](https://tech.ebu.ch/publications/r095), 2017 edition landing page and FAQ read; PDF not opened or audited.
- Existing SRC037, SRC040, SRC043 retained as adjacent leads; this intake does not upgrade their status by association.

Source texts summarized, no third-party imagery or private materials imported. No proof of historical paper-to-game transmission; no universal dimensional or ratio prescription.
