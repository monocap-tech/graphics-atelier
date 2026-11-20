# G02-APERTURE-03 — Game-native dimensional contracts and executable paneling

2026-11-19. Bounded follow-up to [G02-APERTURE-01](G02-APERTURE-01.md) and [02](G02-APERTURE-02.md). R1 source observations; R0 unified contract and historical claims beyond explicit testimony. No commercial capture, code execution, production prototype, original hardware measurement or series launch.

## A. Independent Famicom programming literature

SUZUKI PLAN's educational 6502 repository, section $2005 / Window, reports this retrospective convention, expressed in 8×8 native character cells (not an original Nintendo guideline):
| Role | px | cells | centered half-open bounds in nominal raster |
|---|---|---|---|
| Nominal raster | 256×240 | 32×30 | [0,256)×[0,240) |
| Effective visible (有効可視範囲) | 240×224 | 30×28 | [8,248)×[8,232) |
| Safe visible (安全可視範囲) | 224×208 | 28×26 | [16,240)×[16,224) |

Bounds calculated from reported margins. Do not assert all CRTs clip identically or confuse active raster with recommendation. The author's four logical BG screens include mirroring restrictions; a nominal 512×480 logical scroll address domain is not four independent physical nametables. The text describes changing scroll settings at sprite-zero timing to split a stationary score region from a scrolling region. A split changes local coordinate mapping, not physical output extent. Horizontal/vertical tile quantization is a candidate factor in safe-margin choice; no period causation proven.

## B. Direct game art production specification

Serial Games (2025-04-01) reports a portrait reference UI of 1080×1920, oversize background 1440×2520, and optional square 2520×2520 for broader screens. Significant composition remains in the reference rectangle; taller display fixes width, wider display fixes height. UI elements may retain position, track edges or stretch; actual device safe area is handled at development. Atlas capacity and image softness affect its extended-background choice. This is explicit game art procurement geometry, not a blanket platform rule.

Centered derived reference margins: (180,300) per side in the extended background, (720,300) in the optional square. With width fixed 1080, 9:21 needs 1080×2520; with height fixed 1920, portrait 3:4 needs 1440×1920 and 1:1 needs 1920×1920. These are unscaled illustrative examples, not observed layouts. Their union of centered required regions fits the stated extended or square bounding rectangle respectively; confirm actual anchors and device variants per project. The source distinguishes a device SafeArea from composition; notches and overlays can yield noncentral or irregular exclusions. It does not recommend cropping critical gameplay geometry without other checks.

## C. Console movie handoff

CRI Middleware CEDEC 2007 publicly hosted deck, section 16 slides labeled 69–75. It specifies a Wii application-dependent screen width w, obtained from the game developer by the movie encoder; widescreen source is resized to 720×480, cropped horizontally to w×480, encoded after resize to 640×480, then horizontally expanded at playback. The slides suggest (not mandate) w reflects screen design and television safety. This is a concrete interdepartmental display-to-asset contract; do not substitute a universal w or infer square pixels. The PDF text was read; screenshot attempts at zero-index 70/71 failed (cache miss); no visual figure claim.

## D. Manga paneling becomes executable composition

Koei Tecmo Holdings, patent application JP2020069317A (filed 2018-11-02, published 2020-05-07), Japanese description §3 and textual discussion of figs. 3–10. It explicitly invokes manga panel division and optional right-to-left/top-to-bottom reading sequence for bond-event presentation. Layout selection is game-state dependent; a sliding display region reveals panels. A distinct arrangement region is selected from coordinate-defined shapes; reusable character stills and background crops map to the chosen region, with size/orientation/face-centered positioning specified. The description recommends depicting extra body area for subsequent cut-ins. Related shadow, background, border and balloon processing is named. This is primary evidence of intentional manga-to-game compositional technique transfer in a patent proposal, **not** evidence of a particular released implementation, adoption of B4 dimensions, or historical transmission of TV safety standards to early games. Patent figures were not visually inspected; no legal status/coverage opinion.

## E. Art-directed aperture (another direct production case)

CGWORLD report of Akatsuki's 2017 conference on Hachigatsu no Cinderella Nine, §10: artwork presentation informs peripheral controls, and illustration center shifts between UI states; status appears after the full illustration is shown. This is documented intent and reported practice, not measured exact aperture dimensions or user-response proof. It separates invariant image content from state-dependent framing/occlusion and interaction.

## Consolidation and next gate

Represent output aperture T(device,t), core composition F, artwork/crop support B, class-specific safe regions S_j, local panel shapes P_i(t), and source-to-destination maps M_i. Distinguish a display mask from an artwork crop and a guide; keep feature anchors (face, action cue), interaction regions and render allocation distinct. Rectangular union coverage can be conservative; irregular cutouts may require masks. A source domain sufficient under admissible maps satisfies union of inverse images of target windows inside the source domain. A robust source-space critical cue K is contained in the intersection of mapped-back visible windows after subtracting occlusions. Dynamic framing may intentionally vary cue position or crop; declare exceptions and test each state, not one universal intersection. These are candidate abstractions, not claims about studios' actual implementations.

Three distinct evidence paths: broadcast safety and artist layout standards (AJA); console or device constraints informing game asset geometry; manga paneling directly named as an inspiration for game operations. Do not collapse them into B4 inheritance or a Japan-exclusive genealogy. No new global aspect ratio, safety fraction or default native sprite size adopted.

Next bounded inquiry: inspect specific public original developer art specifications or editor assets demonstrating concrete game source-frame/registration/pose-to-output mapping; prefer a named project or lawful sample with editable geometry and a documented runtime. Then bring the aperture family into the existing original G02 specimen and G09 handoff only when justified, rather than spinning up an extra prototype. Retain S06 chartered, not launched; no change to G06 or separate Suzuki/AM2 reconstruction.

## Local sources (accessed 2026-11-19)
- G02AP3-S01 R1 retrospective independent teaching text: [SUZUKI PLAN, mgp-fc](https://github.com/suzukiplan/mgp-fc), $2005 Window / Split window. Web text read; default-branch commit not pinned, no source run or original hardware measurement.
- G02AP3-S02 R1 firsthand company article: [Serial Games, スマホゲームアプリの画面デザインについて](https://www.serialgames.co.jp/information/946/), 2025-04-01; production size, SafeArea and UI adaptation/background sections read; linked visual examples not inspected.
- G02AP3-S03 R1 public historical middleware slides: [CRI Middleware CEDEC 2007 DS/Wii](https://www.cri-mw.co.jp/event/2007/2nt4hm0000001bs5-att/CEDEC2007_S02_wii_ds.pdf), section 16 pp.69–75 text; PDF screenshots failed. No confidential SDK consulted.
- G02AP3-S04 R1 patent description: [JP2020069317A](https://patents.google.com/patent/JP2020069317A/en), Japanese paragraphs §3/figures 3–10 descriptions, assignee/date metadata; figure images and released title not verified. Proposal only.
- G02AP3-S05 R1 contemporary conference report: [CGWORLD 2017, 八月のシンデレラナイン visual/UI](https://cgworld.jp/feature/201711-cgwcc2017-02.html), section 10, report text only.
- G02AP3-S06 R1 limited retrospective corroboration: [GAME Watch interview, PC Engine mini director 吉室](https://game.watch.impress.co.jp/docs/interview/1241110.html), 2020; consultations with original Hudson developers and change in Ys I/II display region reported, no exact geometry or original intent specification available.

No copied third-party art, PDFs, secret SDK or private material. No claim of JP universal method.

## Parallel panel grammar intake

[G02-PANEL-01](G02-PANEL-01.md) studies the manga panel as a semantic, sequential and layered compositional unit independently of aperture geometry. This does not replace the next source-frame/registration-to-runtime question.
