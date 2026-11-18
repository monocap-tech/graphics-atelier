# Dimensional contract — cross-domain regrouping (proposed)

2026-11-18. Synthesis of G00-A01, G02-A01, G02-P01 and the UI integration study. This is an investigation structure, not an adopted graphics standard or a measured result.

## Why cross-domain

The dimensions of an asset are consequences of a relationship between the authored subject, representational density, motion envelope, camera, and intended screen composition. They also constrain the set of actions and visual states that a designer can plausibly express. Conversely, gameplay and presentation outcomes can require revisions to the proportions or rendering regime. Do not treat graphics as a downstream skin on frozen mechanics, or use pixel count as the only metric of quality.

G02-P01 already specifies the detailed proportional and procurement inquiry. G03-P01's 64x64 cell is an isolated technique-test fixture, not a global asset standard. G08's interface composition and VG04/VG07 camera and display architecture feed into shared dimensions. Production feasibility includes drawing count, manual corrections and downstream revisions, not merely memory.

## Shared record (where applicable)

| Layer | Record |
|---|---|
| Subject | reference world height or abstract relative size; anatomy, recognizable landmarks, authorized stylization |
| Illustration | editable master, frame/cell vs visible bounds, reference proportions, pose/part breakdown, source density and adaptation/usage rights |
| Native representation | size in pixels or model units, visible bounds and motion envelope, registration and anchors, palette/edge handling/texture density |
| Camera/world | projection, depth or zoom, baseline, scale mapping; for perspective give local screen projection instead of assuming constant px/m |
| Logical composition | full logical frame, world viewport rectangle, HUD/letterbox/inset geometry, displayed occupancy; overlay does not automatically shrink viewport |
| Final display | output size, aspect ratio, scaling/filtering, safe area and sampling |
| Production | unique drawings/poses, work estimate and observed effort, export/atlas geometry, variant/revision cost |
| Behavior | interaction reach, movement clearance, projectile field and attention competition; record separate collision shapes, not equivalent to visible bounds |

For a baseline mapping, let V be world viewport height, h native visible upright height, H world height, q native head height, d displayed logical px per native px. Then screen occupancy rho=d*h/V; native density s=h/H; head count n=h/q. For perspective, varying pose, or nonuniform transforms, measure local projected bounds and qualify ratios. Atlas cells depend on registered motion envelope and packing, not upright height.

## Evidence and sequence

G02-AUDIT-01.md records the reported Guilty Gear/GGX numerical comparison and the independent Maskedo scale convention; neither is a universal Japanese standard. It also describes the next candidate capture pass. Golden-section and A/JIS B paper modularity remain distinct hypotheses; simple fractions, genre, camera, print/animation layout and hardware constraints are competing explanations. No causal paper-to-game rule is established.

Priority: G02-A02 bounded empirical capture/reference library, alongside G00-A02 independent raster source recovery. Run isolated G01/G03 experiments whenever useful, labeling their dimensions as local fixtures. Before selecting shared game asset standards, compare native density at fixed on-screen occupancy and occupancy at fixed native density. Include both small-footprint STG/action exemplars and large fighting-game comparators, and assess surrounding enemy/effect/UI density. G04/G05 should measure projected environmental/actor sizes and camera variation; G08 should examine how reserved interface space changes usable world composition, contrast and motion legibility. G09 consumes validated ranges and exceptions rather than arbitrary numbers.

The G02-P01 640x360/84 px reference body/128x128 cell/4x–8x source example remains an experimental candidate, not the answer. No budget, style, final aspect ratio, golden ratio, pixel density or purchase is adopted by this regrouping.
