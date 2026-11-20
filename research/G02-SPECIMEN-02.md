# G02-SPECIMEN-02 — Authored 48px pixel intervention under matched presentation

**2026-11-19** · **Executed locally: EK-D mechanical**, R0 artistic/perceptual conclusions; **not** an executed Unity import, shipped sprites or final native-size choice. Follow-up to [G02-SPECIMEN-01](G02-SPECIMEN-01.md), [G02-P01](studies/G02-P01.md) and the [candidate composition contract](G02-COMPOSITION-01.md).

## Precise question and controls

For the same original Relay Courier vector sources, native height **h48**, same registered **192×192** export cell and top-left **(96,174)** ground registration, compare:

| Condition | Actual operation | Claim boundary |
|---|---|---|
| A: original | Existing CairoSVG RGBA native reduction, antialiased | Original baseline, not hand-designed dot art |
| B: automatic | Binary alpha cutoff ≥128 and nearest Euclidean RGB match to an explicitly declared eleven-color palette | Automatic reduction only |
| C: authored | B + layer-informed rose-color guard, then 32 hand-specified native-pixel paint commands for crest, eyes/cheek, left relay and suit/belt, per pose with head offsets | Constrained pixel-level intervention, **not** a whole-body original pixel redraw, independent artist review or recognition evidence |

All controls use the same source, nominal native height, output cell, pivot and compositing target; the only image interventions are those above. Transparent source padding is retained intentionally. A 640×360 illustrative **logical viewport** with a displayed neutral height target 112px includes simple drawn scenery and a competing circular action cue, held constant across A/B/C. This is an offline Pillow **mock scene**, not Unity rendering or calibrated gameplay evidence.

Source poses: neutral, stride, extended attack and recoil. For each, literal-pixel edits use a declared pose-local head offset (neutral 0,0; stride 0,-1; attack 0,0; recoil +2,+1), while device/body coordinates stay fixed. Manual source instructions and exact color roles are recorded in [h48 pixel recipe](../assets/g02/relay-courier/H48_PIXEL_RECIPE.md). Program file and actual PNGs are preserved in a separately delivered ZIP. Pixels outside the source alpha≥128 support are not added; out-of-mask edits are logged. All original source images are self-authored and were already part of the downloadable parent fixture.

## Local measured results (not a user study)

| Pose | Source→automatic changed RGBA pixels | Automatic→C changed pixels | Effective explicit pixel paints | Guard corrections | Alpha≥128 bounds (x0,y0,x1,y1) |
|---|---:|---:|---:|---:|---|
| neutral | 551 | 38 | 19 | 21 | (84,126,105,174) |
| stride | 596 | 44 | 20 | 26 | (80,126,110,174) |
| attack | 633 | 45 | 20 | 26 | (80,126,117,174) |
| recoil | 605 | 40 | 21 | 22 | (83,128,106,174) |

Both B and C use at most ten opaque colors in these four tested outputs from the eleven-color declared palette; the PNG cell remains 192×192. Effective paints and guard corrections **overlap**, so their counts should not be added to predict the changed-pixel total. In the three-way contact, naive RGB nearest-color assignment visibly creates false rose/pink regions on ears and clothing. Retaining the source's separately named face-mark and relay-lens masks to restrict rose assignments removes these false positives, before the hand-entered corrections. This supports **data-driven color role custody**, not a quantitative preference claim.

For all four poses, source alpha≥128 silhouette bounding rectangle is invariant across A→B→C; output registration and cell extent are unchanged. The earlier neutral lens-color source revision was repeated through C: **7 changed RGBA pixels**, unchanged silhouette. Neither positive pixel count nor pigment contrast proves a human reader can identify the cheek mark.

A clean-directory replay of the authored-pixel script reproduced **20 generated files**, including **18 PNGs** and **2 metadata files**, byte-for-byte in the available environment. The byte equality includes PNG encodings from the tested Pillow version; it is not a cross-platform determinism promise. Assertions enforce silhouette bounds, binary opacity, input size, pivot pixel status, a changed manual condition and unchanged bounds under the lens revision. Color guard masks derive from the original SVG layer names via the original `build.py`. This is not a palette-optimization algorithm and the manually chosen pixel positions should not be reused blindly at other heights.

## Artifact custody

Full self-contained follow-up ZIP (delivered in conversation):
`G02-P01_Relay_Courier_h48_Retouch_and_Unity_Probe.zip`
SHA-256 `fb7401b4f60a7fc635212a9519b54ad3d30248e0f155de62e588670818e6d163` (175,546 bytes, 48 files). Contains original `build.py`, five SVGs, relevant original h48 PNGs, `pixel_cleanup.py`, the 18 generated comparison images, CSV edit log, JSON manifest, still previews and the Unity-side probe described below.

`pixel_cleanup.py` SHA-256 `a87dcabf2c4eb3fe5ed55834ac022eb472e70323ebb15ab35b299d514a316ed0`. Full algorithm is in the ZIP. Companion [recipe](../assets/g02/relay-courier/H48_PIXEL_RECIPE.md) gives the operation semantics and manual coordinates in Git, but is **not** an executable replacement for `build.py`.

No commercial images, game assets or third-party art are redistributed. Import script, PNGs, remaining pose SVGs and exporter are **not** fully tracked on this Git branch; the complete ZIP is an external conversation artifact, not a repository-attached release. This is a documented custody limitation, not a claim of end-to-end public reproducibility by cloning Git.

## Engine gate explicitly unexecuted

Included in ZIP: Unity Editor file `Unity/Assets/G02RelayCourier/Editor/G02ImportAudit.cs` SHA-256 `4ffd356d8db46156af26fa2d3ea527860682c28c630c82094d371e18a89644d1`; 13 192×192 images for four poses × three conditions plus cleaned color revision. The uncompiled editor-only script is designed to import each as single-point-filtered, uncompressed Sprite with 48 PPU, no mipmaps, custom normalized pivot **(0.5,0.09375)** (Unity bottom-left = (96,18) pixels; source top-left = (96,174)), and generate a comparison scene using an orthographic camera with half-height 360/112/2. At a 640×360 Game view, expected 48-native-px to 112-display-px scaling follows from geometry. This is a **test recipe**, not an actual Unity observation. Unity Editor executable unavailable in local research environment; nothing was compiled or rendered in the engine.

A useful next test is to run the editor audit, inspect actual Game-view screenshots at a declared 640×360 and a second output size, then compare whether face marking, left relay and hair crest remain readable in idle and one stress pose. Art-directed revision may prefer a wholly new h48 sprite instead of additional patching. Capture whether a changed source lens requires regeneration/import and whether custom pivots survive.

## Gate decision

G02-P01 Gate 2 has **one bounded manually specified low-native alternative** with reproducible raster/registration checks, but no independent artistic review and no validated representational quality. Gate 3 remains **open** until actual engine import/playback; no animation, motion timing, hitboxes, atlas/performance study, 3D projection or viewer observation. Gate 1 capture references, Gate 4 second-design transfer and downstream G09 remain open. A 48px source class, eleven-color palette, 112px viewing height, 192px cell and the tested editor import settings are only fixture conditions, not studio rules. Stop additional panel-format/literature expansion until these explicit gates can be judged.

No change to G06 effects STD01, G07 hold, S06 charter or independent Suzuki/AM2 investigation.
