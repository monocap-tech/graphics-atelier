# G02-SPECIMEN-01 — Relay Courier: first source→registered raster export

**Date:** 2026-11-19. **Status:** locally executed, bounded mechanical test (EK-D); artistic/reader and runtime conclusions **not tested**. **Companion:** [G02-P01](studies/G02-P01.md), [G02-COMPOSITION-01](G02-COMPOSITION-01.md). This is an *original vector diagnostic character*, not finished pixel art, a game or a recommended character scale.

## Produced and custody

Original character **Relay Courier** has crest hair, diagonal cheek stripe, asymmetrical left shoulder relay and separately drawn arms/legs/boots, from editable SVG layers. Four poses: neutral, stride, extended attack, recoil. A neutral revision changes **only** the relay-lens fill. Original self-authored geometry; no scanned commercial drawings, third-party sprite assets, commissioned rights or source genealogy. The neutral editable SVG is checked into [assets/g02/relay-courier/relay_courier_neutral.svg](../assets/g02/relay-courier/relay_courier_neutral.svg).

The **complete generated fixture** (five SVG masters, original Python `build.py`, 20 RGBA native sprite exports, 8 previews, CSV, JSON manifest, README), plus a source-only ZIP, are delivered as downloadable attachments in the conversation. Neither ZIP nor all pose PNGs are committed to this Git branch during this pass; the Git checkout alone therefore does **not** reproduce every claimed image. Record the boundary explicitly, and migrate the executable package into version control if continued as a production asset.

Delivered package SHA-256: `95e4975d1fcbb3a62e93be6fdc9cd2e260f42035d2b5e9849180188a20fa6e0c`; source-only SHA-256: `8ec41878e58aa37a56841be929cbcd0cab01142dfafaccbd745943802a2c4a32`. The script SHA-256: `8683dce27381bc36a6849243fcdbc4821f6030a02c47a4161cde7025398dda7f`. Python Pillow 12.3.0, CairoSVG 2.8.2; generated standalone, not in Unity. One can extract either ZIP and run `python build.py --out build_new`.

## Predeclared coordinate design

- Editable SVG user-coordinate workspace D: 256×320, top-left origin, x-right/y-down; registered ground point (128,295).
- Per-pose source image support B: measured alpha, not the SVG canvas. At 4× neutral render the 128-threshold bounding rectangle is (250,150,716,1184) in scaled coordinates, so neutral source visible upright height is 258.5 source units.
- Native sample classes: nominal upright h∈{48,72,96,128} px, all rendered by the *same source scale* s=h/258.5; per-pose heights can differ. Reproducible transform: render original SVG to rounded (256s,320s), paste at `(round(96−128s), round(174−295s))` into a transparent 192×192 cell; registered cell pivot (96,174), fixed across variants. Source-to-cell anchor floating error checked ≤1 native px.
- Native alpha-visible bounds, source support and registered working cell are separate objects. Cell 192×192 is deliberately wasteful; no atlas optimization, hitbox or final memory budget endorsed.
- Illustrative display mockups: 640×360 **logical world viewport**, top 52 px indicated as an overlay band; neutral visible height matched to 112 logical pixels (~31.1% occupancy), nearest-neighbor resampling of registered cells. This is a *selected experimental fixture*, not the earlier 84 px/640×360 default or an adopted rendering contract. A fixed-native h96 sequence with display heights 84,112,140 separately varies screen occupancy. No input/gameplay/Unity timing or final-output pixel-aspect test.

## Mechanical results

| Nominal neutral h | Alpha-visible h | Neutral nontransparent bounds within 192×192 | Isolated cheek stripe support | Revision-changed RGBA pixels |
|---:|---:|---|---:|---:|
| 48 | 48 | (84,126)–(105,174) | 2 | 9 |
| 72 | 71 | (77,103)–(110,174) | 5 | 17 |
| 96 | 96 | (71,78)–(114,174) | 9 | 29 |
| 128 | 127 | (64,47)–(122,174) | 17 | 47 |

**Pass:** all 16 original pose outputs have in-cell alpha bounds and ≤1 px registration error; neutral height errors ≤2 px. All four revised neutral native exports differ from originals while retaining exactly the original alpha-visible bounding boxes. Isolated cue-layer opaque pixel counts: crest {74,159,287,504}; cheek {2,5,9,17}; shoulder-relay {43,96,178,306}; colored relay lens {7,16,28,48} for h 48/72/96/128. Threshold is alpha≥128. These are *pixel support*, not recognition or contrast measurements. Re-running the script into a second output directory gave **28 of 28 PNG files byte-identical** in the tested environment. Hashes/coordinates for each source and pose appear in the downloadable JSON/CSV.

**Interpretation:** registration, rasterization, a controlled transform and a single-field source revision can be exercised. Small cues collapse quickly: two distinct opaque cheek-layer pixels at h48 cannot certify an identifiable cheek marking. Automatic CairoSVG rasterization is neither manual low-resolution cleanup nor an independent pixel-art design. No selection of the best native size is defensible yet.

## Absent gates and next bounded work

- G02-P01's reference/capture Gate 1 is still open; no commercial assets were copied and no production-camera/native density relation inferred.
- Gate 2 is **partially** satisfied: source SVG, four original pose drawings, native crops and comparative mockups exist; predeclared human/art-direction appraisal, manually redesigned low-res alternative, representative background/action and native visual acceptance thresholds remain open.
- Gate 3 **not done:** no temporal animation sequence, Unity/engine import, live player capture, hitbox, atlas packing, timing, actual editor-visible revision or event/cancellation test.
- Gate 4 **not done:** no second independent design transfer.
- G09 remains downstream. No new standalone study or fixed global design ratio.
- The next meaningful operation is **one** situated comparison on the existing artwork: direct downsample versus manually cleaned source at an explicitly chosen camera and background, then check asset import and one revision. If that fails, revise or stop. Do not pile on more source-format surveys.

This finding does not validate any Japanese universal design method, manga-to-game lineage, emotional effect, audience legibility claim or production-ready art.
