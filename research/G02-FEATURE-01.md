# G02-FEATURE-01 — Illustration-to-dot-art feature survival: thread intake

Date: 2026-11-18. **Status: bounded intake / R1 for inspected source statements; no R3 production demonstration.** Domains VG01/VG06/VG07/VG08, with VG02, IP01 and G03 interfaces. Extends [G02-P01](studies/G02-P01.md), [G02-A01](G02-AUDIT-01.md), and [G02-A02](G02-ATLAS-01.md). This record consolidates the 2026-11-18 discussion of two Japanese art-instruction scans, comparative feature treatment, low-resolution adaptation, and historical practices. It does **not** start or take ownership of the concurrent Suzuki/AM2 technical research.

## Governing question and boundary

When translating an illustration, character model, or detailed render into authored dot art, **which properties must remain legible, which may be omitted/replaced/exaggerated, and how does this change with final screen-space size and display context?** An image has pixels; a *character* additionally has identity, silhouette, anatomical relationships, pose, material/lighting interpretation and social/expressive cues. A raster similarity metric does not establish that the latter survived.

Keep distinct: (1) the character/design brief; (2) illustrated source and editable layer structure; (3) representation-specific manually revised art; (4) runtime graphics selection and scaling; (5) actual display, background and motion; (6) interaction rules. Historical artwork selection does not by itself explain artistic intent.

## Private-use book corpus — inspected scan pages, not assets for publication

- **B01 — 『打てる！ドット絵超入門』, Aseprite v1.28**. User-supplied privately owned scan; 74 PDF pages. Cover/contents visually inspected; relevant PDF pages 10–14, 19–21, 27–35, 44–48. Guided example constructs a 100×100 canvas character from a sketch/reference; p.14 compares pixel curves and economical outlines; pp.19–21 discuss constrained color choices and correcting skin/other component colors in sequence; pp.27–35 refine outlines, tonal contrast and the final raster; pp.44–48 discuss ink/brush modes, alpha and pixel-perfect drawing. **EK-B** (practitioner instruction); the book is *one worked procedure*, not evidence of a national standard, industry-size ratio, historical arcade specification or automatic conversion algorithm. Certain explanations are interpretive summaries, not line-by-line English translations.
- **B02 — 『キャラ塗り上達術 決定版』, CLIP STUDIO PAINT PRO/EX, Impress**. User-supplied scan; **209 PDF pages** (file visibly continues through the colophon), printed page numbers often begin at the corresponding PDF page; cover, index (PDF pp.3–5), intro (6–7), and selected instructions visually inspected. Ten artist demonstrations cover アニメ塗り, ブラシ塗り, ブラシ＋厚塗り, 水彩塗り, 水彩＋厚塗り, 厚塗り, ギャルゲ塗り and 宝石塗り. Selected comparisons: eyes pp.14–15, 27–29, 90–92, 175–177, 201–203; skin/shadow color p.69; hair color p.93; blending p.124; late form revisions p.153; faceted material p.189; finishing p.204ff. The book illustrates layer roles, masks, brush settings, color samples and compositing rather than one universal construction order. **EK-B**; this concerns illustration methods, not originally authored game sprites. Exact numerical brush settings and translation nuance need enlarged page-by-page checking before quotation.

**Rights:** both scans were supplied for private analysis. Ownership of a physical copy does not imply redistribution rights for scans, figures, individual page crops, or derivative sprite sheets. This public repository stores only bibliographic pointers, paraphrased observations and original research plans; no page imagery, extracted assets or third-party native illustration files.

## Public sources checked for this intake

| Local ID | Source and inspectable evidence | Qualification |
|---|---|---|
| G02F-S01 | 有織はべり, [ドット絵での細かいデザインのデフォルメについて](https://note.com/ari_ori/n/nd77e2c3fe470), 2024-01-28. Same-character examples at 128, 32 and 24 px. Explicit **色のデフォルメ** (color adaptation) and **パーツの取捨選択** (selection/omission of components); accents and regions prioritized over tiny decorative detail. | **EK-B, R1**; author practice, not validated perceptual threshold |
| G02F-S02 | Kazuko Shibuya [2013 interview in English translation](https://shmuplations.com/kazukoshibuya/). Describes imagined non-pixelated 3D character before sprite drawing, starting from broad form and revising anatomy, mass and shading; interview also corrects a simplistic universal Amano-art→sprite genealogy. | **EK-A, R1** testimony in translation; check JP original for exact terminology |
| G02F-S03 | SNK, [KOF XII official 2D DOT creation gallery](https://kofaniv.snk-corp.co.jp/english/info/15th_anniv/2d_dot/creation/index.php). Captions state concept → 3D model/animation → 2D visual based on motion → final reference → detail/finalized raster. | **EK-A, R1**, documented stages, not reproducible settings |
| G02F-S04 | Gerstner, DeCarlo, Alexa, Finkelstein, Gingold, Nealen, [Pixelated Image Abstraction with Integrated User Constraints](https://cragl.cs.gmu.edu/pixelate/journal.html), *Computers & Graphics* 37(5), 2013, pp.333–347. Joint low-resolution feature mapping and palette selection with user constraints; compared with naïve methods and artist examples. | **EK-C, R1**, published algorithm and stated evaluation; code linked, **not rerun here** |
| G02F-S05 | [Fukutake, 移植版『スペースハリアー』におけるハリアーのドット絵大研究](https://www.space-harrier.com/sh30/sh30II_samp.pdf), fan comparative survey. Ports illustrate different source dimensions, silhouettes, color/outline and pose decisions. | **EK-C, R1 discovery/visual comparator**; independently verify individual measured dimensions and port/version before a standards claim |
| G02F-S06 | MAME [sega16sp.cpp](https://github.com/mamedev/mame/blob/master/src/mame/sega/sega16sp.cpp) and [segahang.cpp](https://github.com/mamedev/mame/blob/master/src/mame/sega/segahang.cpp). Board-level register/zoom behavior, not Sega's original art-direction decisions. | **EK-C, R1** emulator reconstruction; version-pinned blob needed for an executable trace |

Separate interview claims in the discussion concerning Yoshikawa/Capcom design practices, SNK's sprite-first promotional art, M2's internal reconstructions, and Suzuki's object design have **not been newly verified within this intake**. They are follow-up leads only; do not promote to institutional history from conversational retelling. Suzuki/AM2 is owned by the other investigation thread.

## Feature survival — provisional operation taxonomy

| Intent / source property | Candidate adaptation | Risk / counterexample |
|---|---|---|
| Character identity; distinctive head/hair/equipment silhouette | preserve contour or redesign clusters; amplify one cue | exaggerated cue changes likeness or pose |
| Figure segmentation (wrist/hand, limb, costume boundary) | increase local contrast, add/remove separating accessory, reposition pixels | creates an unapproved design change |
| Iris/pupil/gaze/expression | prioritize pupil shape and eyelid direction before tiny reflections | bright one-pixel highlight may dominate at small sizes |
| Major color identity and focal hierarchy | preserve large color areas and accents; hue shifts for separation | physical/source color may be sacrificed |
| Surface material (hair, fabric, gem, metal) | choose a few indicative edge/cluster/reflection marks | generic gradient/palette quantization confuses materials |
| Viewpoint/pose/handedness | author alternate facing or key pose rather than mirror | asset count rises; source symmetry not established |
| Light, softness, optical effect | edit original pixels for intended display and background | display artifact confused with intrinsic asset color |

These are **hypotheses and documented individual techniques**, not empirically ranked rules. A source feature may disappear, be reauthored or be replaced by another cue; exact source-pixel retention is neither necessary nor sufficient for preservation of expressive function.

## Conversation-derived pilot experiments (not validated result)

A diagnostic used eye crops from the printed B02 scan (not native artwork) to compare ordinary area averaging, 16-color reduction and *manually marked* feature retention at 12/16/24/32-pixel crop widths. The discussion reported higher local contrast after protecting a tiny highlight and noted that a protected pixel can become disproportionately prominent at very small sizes. **Record as exploratory observation only**: nonidentical eye examples, scan/JPEG artifacts, manually chosen coordinates/colors, no precommitted perceptual criteria, no controlled viewers, no verified independent rerun for this repository. The method cannot establish an optimal resolution, a universal feature budget, author preference or successful recreation of a commercial sprite. Related transient code and commercial-image crops remain outside this public repo.

## Architecture and proposed test (R0/R2 plan, not executed)

Treat the output as an **adaptation decision ledger**: for each character/pose/representation, register identity-bearing features, relational significance, allowed omission/contrast/exaggeration, budget, registered reference, native/display dimensions, sampling/compositor behavior and approval. Distinguish author-intent testimony from measured on-screen legibility. A staged original-art specimen, not an extracted commercial sprite, should compare:

1. **Matched display occupation**, varied native sprite density (e.g., 48/72/96 px) to isolate source detail budget.
2. **Matched native drawing**, varied display occupation/background/motion to isolate context.
3. **Matched original character and size**, baseline area-sample / palette-quantize / *manually redesigned* variants; protect same explicitly declared identity, gaze, asymmetry and material cues.
4. Independently register pixel/cluster metrics, visual hierarchy, workload, palette, export behavior and *actual* observer/artist judgments if such a claim is sought. Use a second original character for transfer. Avoid post-hoc thresholds.

The minimum-feature model is not simply \(p \ge \text{constant}\). A useful *candidate* formula is eye screen height \(P_e = H_{\mathrm{view}} r_{\mathrm{actor}} r_{\mathrm{eye}}\); this is geometric bookkeeping, **not** a universal feature threshold. Motion, viewing conditions and contrast alter the outcome. The final deliverable is the source-to-sprite-to-runtime editable contract already sought by G02-P01, not a generalized pixelizer by default.

## Space Harrier technical tangent: keep separately scoped

Discussion Investigations V–VIII branched into original arcade *Space Harrier* sprite zoom, sprite-RAM records and a proposed MAME trace. Two **local**, unrun diagnostic ZIP probes were prepared; synthetic analysis alone was reported. Neither a live arcade program trace nor a recovered graphics selection/LOD table has been demonstrated here. A change of sprite bank/offset may indicate animation, facing or slot reuse; it is **not** proof of distance-triggered art substitution. Hardware zoom reconstruction does not establish which features Sega artists intended to preserve. Do not ingest these probes as validated production tools, nor duplicate the parallel Suzuki investigation.

## Decision and bounded handoff

**Retain** documented manual adaptation, representation hierarchy, and feature-selection problem as G02 evidence. **Reject** claims of a single Japanese optimal sprite dimension, golden-ratio/paper-size cause, generally optimal eye size, a machine-derived visual identity score, or a proved Space Harrier enemy-art LOD schedule. **Defer** general algorithm/tooling or arcade-ROM provenance until the original-art pilot or separate hardware team makes it necessary.

**Next G02 action:** freeze a deliberately modest original character with an asymmetrical identity marker, one expressive face, two backgrounds and one motion; register retention/omission/exaggeration priorities **before** drawing; run three representation policies at matched output size and record revisions/time. Update the G02-P01 gates and dimensional atlas only on actually measured evidence. Do not displace the concurrent G06 or Suzuki workstreams.