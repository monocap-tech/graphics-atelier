# G02-COMPOSITION-01 — Source-to-presentation contract across static and interactive media

**Status:** candidate design contract / R0, derived 2026-11-19 from bounded R1 documentary and code studies; not an adopted standard or completed specimen. **Scope:** G02 illustration/geometry handoff and optional G09 integration. No software or renderer selected; no user testing, runtime, metric calibration, or original source-art prototype carried out.

## Decision and provenance

Earlier [aperture studies](G02-APERTURE-01.md)–[03](G02-APERTURE-03.md) separately documented manga manuscript bounds, AJA animation registration and scan/safe frames, and concrete game display/artwork contracts. [Panel studies](G02-PANEL-01.md)–[06](G02-PANEL-06.md) documented the panel's semantic vocabulary, layered vs sequential composition, digital manga authoring/redistribution, ACBF polygon serialization, Krita transformed export, the guided reader's rectangle approximation, Panoply's independently interpolated rectangular cameras/artwork and SpriteStudio's documented animated cut-in masks. [Dimensional migration](G02-DIMENSIONAL-01.md) distinguishes units from modularity from representational custody. These are **comparators**, not a single continuous historical lineage. Documentary observation is not executable interoperability or empirical reader response. Specifically, neither B4→game inheritance nor a universal optimal ratio or shape grammar is established.

**Proposed invariant:** each artwork representation has an explicit provenance-preserving relationship to a declared target composition and its viewing conditions; every transformation is either demonstrably geometry-preserving under a defined tolerance or an explicitly approved artistic reinterpretation. Do not infer semantic equivalence from successful image export alone.

## Five linked specifications, not one image size

| Layer | Record and authority | Typical failure if omitted |
|---|---|---|
| S — Source | asset/variant ID; author and rights; editable layer IDs, illustration register and pose anchors; source coordinate basis, pixel density or physical units; original and allowable loss/omission | art supplied without reproducible adaptation or legal use |
| G — Geometry | separate working domain D, image support/bleed B, intended trim/presentation T, composition guide F, content-specific protected regions S_j, local apertures P_i; masks, boundaries and true shape vs box; units, registration and hard-clip vs soft-guide status | crop or mask confused with canvas or safe region |
| C — Composition | local image support, cue hierarchy, framing intent, placement/overlap, gaze/motion vectors, text and FX anchors, image-space/viewport-space positions, co-visible groups, intentional overflow | technically readable cuts destroy emphasis or neighboring context |
| Q — Sequence | intended panel precedence (may be partial), simultaneous events, persistent layers, page-turn/reveal group, optional alternate reading modes, narrative vs subjective time | page converted to single-panel strip with unapproved causal order |
| E — Execution | explicit source→native→logical→output maps; camera and viewport per device/state; clipping/matting, pixel aspect, sampling/rounding; timeline cursor vs clock, input and interruptions; render order/isolated cameras, fallback and supported-export set | crop padding, rescale drift, bad safe areas or unsynchronized events |

Names are local to this research, not adopted CELSYS, ACBF, AJA, SpriteStudio or engine schema. Not all targets require each field. A 2D sprite test may have no panel sequence; an independent splash illustration may have no simulated world. Record `not_applicable` rather than fabricate one.

## Coordinate and aperture discipline

1. Every region declares a coordinate frame (origin, direction, physical units or pixels, pixel aspect, pixel-center/edge convention), shape (rect, polygon, mask), role and boundary policy. Use immutable or versioned source registration where possible. Quantization and transform rounding are part of the export contract.
2. In a common coordinate frame, a *simple example* may have `F ⊆ T ⊆ B ⊆ D` and `S_j ⊆ T`. Neither F nor S_j must contain the other. Bleed panels, style illustrations and transparent source support can intentionally exceed guides. Never assume this nesting across independent untransformed coordinate frames.
3. For declared presentation variant `v` (device, aspect, state, camera pose, user input), let `A_v` map source coordinates to target coordinates, `T_v` be the required destination aperture, and `B` be source image support. Coverage is a test on the needed source footprint: `A_v^{-1}(T_v) ⊆ B` **where the map is invertible and image coverage is intended**. For perspective, many-to-one mappings or noninvertible transforms, use visibility sampling/rays and the projected support rather than a fictional inverse. For a moving camera, union the required source footprint over all approved `v,t`; protect critical cues against **all admissible crops only where universal visibility is intended**. An empty intersection is a design conflict requiring alternative layout, not a safe-area result.
4. A panel has at least **image support**, **semantic boundary**, **viewing bounds**, and **actual rendering clip** as potentially different regions. A bounding-box zoom is not polygon clipping. A screen overlay may obscure cues without reducing the world viewport dimensions. Split-screen, HUD, subtitles and effect layers need their own safe and priority rules. Explicitly identify transparent padding, sprite/attack envelope, atlas cell, stencil, and collision/hurtbox as *noninterchangeable* geometry.
5. Record two mappings for each object as relevant: subject/world→logical-view projection and authoring/master→native asset/export. The G02-P01 occupancy equation `rho=d*h/V` uses explicitly identified **world viewport height** `V`; output upscaling alone does not increase native representation density. Keep perspective/depth and nonuniform axes explicit. JIS B, AJA Fr01, TV safe margins, nominal Famicom raster and Panoply's example 1024×768 are evidence cases, not global settings.

## Relations and time

A `panel` may be a static cropped picture, a semantic figure/field, or an independently rendered camera. These choices require an explicit implementation tag. Store spatial overlap, layering/z-order, shared-image support, reading precedence, depicted-event relation (before/after/simultaneous/memory/unknown), semantic linkage (contrast, metaphor, object/motion continuity), and co-visibility as **separate relations**. A directed reading graph need not be a total order. Manga often shows many panels at once; screen playback need not preserve that without an editorial decision.

Separately identify (as applicable): simulated-world time; narrated-event time; subjective/represented time; presentation wall-clock; input or author-controlled progression step; and interpolated visual state. A pause can freeze simulation without halting presentation; a panel can persist through multiple story steps. Define event firing on transition vs completion, seek and reversal semantics and interruption/cancellation. No assumption that area determines duration, tilt entails a psychological effect, or panel spacing uniquely determines reader response (see [PANEL-02](G02-PANEL-02.md) negative results).

## Minimal interoperable record — *illustrative fields, not a fixed JSON/Unity schema*

```yaml
composition_id: original_character_v0
status: candidate
source:
  uri: "author-owned/master"
  rights: "self-authored; verify before distribution"
  frame: { units: px, origin: top-left, extent: [2048, 2048], registration: "ground-anchor" }
  cue_anchors: ["face-mark", "asymmetric-equipment", "ground-anchor"]
representations:
  - id: native_sprite
    target: "unspecified-gameplay-test"
    source_to_native: "documented transform + manual cleanup revision"
    visible_body_bounds: "to-measure"
    motion_envelope: "to-measure"
    cell_and_pivot: "to-declare"
  - id: optional_cutin
    target: "unselected; optional"
    source_to_native: "to-declare only if selected"
presentation_variants:
  - id: world_view
    logical_world_viewport: "to-select"
    output_aperture: "to-select"
    safe_regions: []
    clipping: "to-declare"
    ui_reserved_or_overlay: "to-declare"
    required_cues: ["face-mark", "asymmetric-equipment"]
sequence: { applicable: false }
evidence:
  observed: []
  tests_pending: ["registered-rescale", "native-density-vs-occupancy", "revision-propagation"]
```

These dimensions are **illustrative authoring values**, not an assignment to the G02-P01 specimen or accepted baseline. Prefer a small manifest that links real source files over duplicating vector/raster data. Protect asset licensing, version hashes and author/editor approvals.

## Bounded validation and refusal conditions

**Stage A — applicability:** select *one* existing G02-P01 original-art target; document its required representation(s), target camera/display conditions, protected identity cues and whether any panel/cut-in behavior is actually needed. Unselected features remain excluded. Attach provenance and permissions.

**Stage B — round-trip geometry:** for one original layer/cue/pivot and one cropped or scaled native export, transform stored anchors and panel/source boundaries through the documented map and check against independently measured output. Declare rounding tolerance **before execution**; test offsets, non-square/square source rectangles, negative local extents, transparent margins and boundaries. Compare a true polygon mask and its enclosing box only if a polygon panel is selected. Do not silently close shape loss by cropping art to the box.

**Stage C — composition and timing:** if a multi-panel format is selected, provide authored reading precedence, co-visibility groups and cue placement before and after conversion. Exercise full composition and viewport/crop variants. For interactive state, test hold, forward, reverse, seek and cancellation on original content; record world vs presentation clock behavior. A screenshot-only success cannot certify input/cancellation.

**Stage D — production revision:** change one approved character attribute (or relevant anchor or text) in the original editable master and confirm it propagates through native export, registration, any dependent composition and runtime import. Record redraw count, manual intervention, asset/sheet cost and failures. Repeat transfer with G02-P01 second distinct design only after the first passes its existing gates. G09 inherits qualified results rather than an untested specification.

**Stop or decline:** provenance/rights insufficient, source/native scale unresolvable, mask behavior differs across runtime/export mode, critical cue outside accepted presentation variant, interpolation/event semantics unclear, or implementation/revision costs disproportionate. Qualify intended creative differences as deliberate, not errors. Do not claim cross-platform pixel exactness or reader/emotion outcomes without the respective tests.

## Decision at this gate

**Retain as R0 candidate only** and link into the current [dimensional contract](../docs/DIMENSIONAL_CONTRACT.md), [G02-P01](studies/G02-P01.md), and [G09](QUEUE.md). The next useful deliverable is **the original G02 illustration/pose specimen with actual editable source and a registered native export**, not another abstract panel DSL, new engine, patent interpretation or inexhaustible survey. G02-A02 capture collection, S06 charter, G06 STD01, VIGIL, G07 deferment and independent Suzuki/AM2 reconstruction retain their own priorities. Full layered historical shōjo source image remains unverified.

## Evidence index, not extra source claims

See [G02-APERTURE-01](G02-APERTURE-01.md), [02](G02-APERTURE-02.md), [03](G02-APERTURE-03.md), [G02-PANEL-01](G02-PANEL-01.md)–[06](G02-PANEL-06.md), [G02-DIMENSIONAL-01](G02-DIMENSIONAL-01.md), [G02-FEATURE-01](G02-FEATURE-01.md) and [G02-P01](studies/G02-P01.md) for source links, evidence classes, incomplete inspections and individual reproducibility limits. No outside asset imported and no new public research source qualified in this synthesis.
