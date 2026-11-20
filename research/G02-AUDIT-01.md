# G02-A01 — Proportional and illustration-adaptation source qualification

2026-11-18. R1 for bounded claims, not an implemented workflow. Public text/labels inspected; no commercial image files copied, no game captures measured, no licensing conclusions. This extends G00-A01 and G02-P01.

## Qualified production evidence

| Source | Bounded observation | Consequence / limitation |
|---|---|---|
| SRC003 [Dengeki, Gunvolt 3, 2022-10-29](https://dengekionline.com/articles/155178/), Fujii, section ユーザーに気づかれていないドット絵へのこだわり | Relative height, head-size consistency, facial resemblance, leg/body proportions, silhouette, light-dependent contours and perceived color receive separate attention. Adjacent colors and small colored areas can require correction. A, reported by artist. | Test identity and optical compensation as separate criteria; no pixel dimensions or exact palette specified. |
| SRC032 [4Gamer, NDC18, 2018-04-25](https://www.4gamer.net/games/368/G036860/20180425075/), report of Ishiwatari/Abe talk | Original GG storyboard/key drawing/digital spline/dot path learned from an animation studio; GGX dropped the spline step and redrew art instead of enlarging it. BlazBlue used 3D intermediates to equalize drawing quality; initially final color remained manual. A, secondary report of original production testimony. | High-resolution intermediates must earn their cost. No universally mandated conversion technique. |
| SRC034 [4Gamer, Type Lumina, 2021](https://www.4gamer.net/games/580/G058032/20210928001/), Serizawa, graphics discussion and 16:9 question | Older faces were enlarged to accommodate facial expression; higher resolution and Tsukihime R motivated revised proportions. Wider aspect required camera-scroll adjustments to retain aerial play. A, developer testimony. | Anatomy and viewport are coupled to expression and movement, not just visual scale. Exact character dimensions not disclosed in these passages. |
| SRC001 [SNK KOF XII official DOT Creation](https://kofaniv.snk-corp.co.jp/english/info/15th_anniv/2d_dot/creation/index.php) | Graphic concept → animated 3D model → 2D drawing based on motion → refined 2D concept and final detail. A, gallery captions. | Existing G00-A01 observation confirmed; precise scale and layer-file specifications not provided by captions. |
| SRC035 [桝久堂 格ゲー作画講座1](https://www.maskedo.com/howto01/), ©2010 | Earlier scale inconsistency incurred redraws; adopted 16 px grid, approximate 25 cm/grid, eight-head upright baseline for Kamen Rider fan sprites, visually checked against KOF/MUGEN. Landmarks compared against previous sprite at rough stage. B, independent account. | Approx. 64 native px/m and 128 px/2 m derived from author's grid, not a measured SNK standard. |
| SRC036 [RPG探検隊 ドット絵とサイズ](https://rpgex.sakura.ne.jp/home/log/2010-09-22.php), 2010-09-22 | Discusses screen-relative size and stylization simultaneously; gives illustrative 16–256 px classes from RPG to fighting art; recommends reconsidering layout if the sprite fails in context. B, independent production note. | Classes are author's reference examples, not measured values of commercial games. |
| SRC044 [桝久堂 格ゲー作画講座2](https://www.maskedo.com/howto02/) | Candidate economy: base, shadow, intermediate ramps; explains role and relative area of colors and how to extend ramps. B, independent account. | Build palettes by material and area rather than merely maximizing color count. Author's specific ratios/choices are local practice. |
| SRC045 [GameBusiness.jp NDC18 report, 2018-04-30](https://www.gamebusiness.jp/article/2018/04/30/14468.html) | Corroborating contemporary reporting of the Arc talk, initial GG 320×240 and 64×121 at 16 colors. | Same conference, not independent original evidence; further details not needed for this pass. |

SRC033 Under Night interview located on both pages but technical drawing passage not qualified in this pass. SRC037–043 not advanced. Copyright/reuse of images not assumed.

## First reported benchmark pair

Source SRC032, numerical prose in report (not direct measurement, not asset dump).

| Game | Reported display | Reported character dimensions | Colors | Motion drawings (reported) | Nominal h/V |
|---|---|---|---|---|---|
| Guilty Gear (1998, PS) | 320×240 | 64×121 | 16 | 282 | 0.50417 |
| Guilty Gear X (2000, NAOMI) | 640×480 | 136×288 | 32 | 545 | 0.60000 |
| BlazBlue (2009 PS3 context) | 1280×720 | not supplied as W×H | unknown here | unknown here | unknown |

The first two are ratios of reported nominal asset height to reported screen height, not measured idle-body occupancy. Native/display mapping, pose, character and trimming convention remain unverified. Rectangular pixel area ratio GGX/GG = (136×288)/(64×121) ≈ 5.06; reported motion drawing ratio ≈ 1.93. Their product ≈ 9.80 is a nominal rectangular pixel-position workload proxy only, not actual storage, labor or uncompressed byte count. The report calls the size increase fourfold; preserve dimensions and derived rectangle ratio separately rather than silently equating them. The report describes BlazBlue character dot count as sixteenfold relative to GG, insufficient to infer height or screen occupancy.

No inference of golden section: 0.600 and 0.618 are only close as abstract numbers, the former is not measured screen occupation, and two related products are not independent population observations.

## Next bounded capture pass

Select (not yet acquired) these exact candidate contexts; record game release, capture source and timestamp at acquisition. Prefer own lawful capture or identifiable official unmodified gameplay imagery; keep images outside public repo unless redistribution permitted.

| Candidate | Pose and camera | Target variable |
|---|---|---|
| Gunvolt 3, Switch, Kirin | neutral grounded, normal-stage camera, no attack effects | compact character silhouette and head-size budget |
| Guilty Gear X, NAOMI | ordinary duel idle at baseline camera, both characters visible | test nominal-versus-actual viewport mapping |
| KOF XIII, version/platform to identify | ordinary duel idle and one attack extension | model-assisted output comparison |
| Melty Blood Actress Again Current Code and Type Lumina, PC versions | comparable character (e.g. Shiki Tohno), stable grounded idle; additional aerial sequence for camera | within-series stylization and viewport change |
| Under Night In-Birth, chosen version | regular duel baseline idle | HD comparison after version/source identification |

Measure body bounds (exclude weapon, effect and stray hair where distinguishable), separate full visible sprite bounds, head landmark interval, viewport rectangle, baseline y, apparent pixel grid scale if demonstrated. Use half-open rectangle coordinates, top-left origin, and state uncertainty for each boundary. Screen occupancy uses displayed height / world viewport height, head ratio uses matched anatomical pose, and native height stays null unless mapping established. Track full gameplay frame and HUD-overlay status; do not subtract overlay pixels that still show world scene. A screenshot supports displayed measurement even when native grid is unknown.

The candidate references are not measured records. Advance with a small original four-pose illustration study alongside acquisition; do not block all work on the historical corpus. The experiment should distinguish fixed occupancy/varied native density from fixed density/varied camera, and compare a silhouette-only control, reduced guide, and deliberately corrected raster.

## Research synthesis

Candidate production contract: invariants (identity and relative scale), permitted representational changes (anatomy/optical correction), motion envelope, palette allocation, and runtime camera mapping. The source artwork is an upstream specification and reference, not a pixel-for-pixel authority. Explicitly budget several independent operations in artist handoff: rough pose approval, detail/identity review at target size, registration/export approval. No external procurement authorized.
