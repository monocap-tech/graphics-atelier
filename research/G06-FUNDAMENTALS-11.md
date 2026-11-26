# G06-F11 — Transfer case: illustrated/rigged subject and authored game-effects clearing

Date: 2026-11-18. **Status: R1 first-party presentation text + reporting, no editor execution or timed scene audit.** **Deliberately exits** the bounded *Space Harrier* [F10](G06-FUNDAMENTALS-10.md) branch. The objective is to test whether one **question** from that case—how a strong effect leaves its subject/action visible—also appears in a different historical game-production configuration, without claiming identical shapes, mechanisms, artistic genealogy or universal perception. F01–F09 foundations still apply; G06 [STD01](../docs/EFFECTS_STANDARD.md) sets future production acceptance. **No prototype, source-art import, proprietary slide reuse, commercial runtime execution or viewer experiment.**

## Bounded comparison selected — Last Cloudia, 2019

**Why this comparator:** *Last Cloudia* is a commercial Japanese RPG released 2019-04-15, with pixel-art playable character sprites, 3D backgrounds, illustrated/animated character displays, real-time artist-authored effects and composited directed special attacks. It is different enough from a 1985 Sega hardware-sprite arcade shooting game to challenge our assumptions; we did not choose it as a successor or copy of *Space Harrier*. One specifically documented production talks about **subject visibility, effect-palette construction, layered illustrated artwork and synchronization with the moving figure**. This is not a ranking of the game and not an invitation to use expensive 2019 middleware.

### Source custody

| ID | Source / inspected modality | Evidence and limit |
|---|---|---|
| F11-S01 | [CEDEC 2019 / Unite Tokyo *Last Cloudia × SPARK GEAR* speaker presentation, hosted as a 51-slide deck](https://www.slideshare.net/slideshow/unite-tokyo-2019sparkcreativevfxsparkgear/176310173), speaker **和泉森人**, AIDIS Lead VFX Designer | **Firsthand production slide text inspected in public HTML's indexed slide transcript, particularly excerpt slides 4–9** (publisher image links were returned but image-fetch cache missed). Specific visible text supports palette/alpha-crunch, hit-center clearing, **five-layer interleaving (three SPARK / two Spine)**, animated sword-surface masking and bone attachment, masked distortion over illustration. **Slide diagrams/photos not independently analyzed; no video playback**. Slide numbering in HTML is compressed P.44/P.55/P.66 etc.; these denote slides 4/5/6, *not* page 44/55/66 of a longer manuscript. Copyright and speaker's rights remain with original sources; nothing mirrored. |
| F11-S02 | [CGWORLD, Shunsuke Yasuda, “Spineと連携し『動くイラスト』を作成！”](https://cgworld.jp/feature/201909-cedec-spark.html), **2019-09-25**, event report of AIDIS SVP/art director **岩崎優** and VFX designer **和泉森人** | **Reporter-mediated original named production testimony**: studio selected middleware for designer-only editing, multifunctionality and declared licensing; core pixel-art characters vs nonpixel effects; internal Unity-based camera editor for ultimate attacks; existing effect assets re-treated with palette texture to suit pixel-art/3D surroundings; effects deliberately designed **not to hide character sprites**. Character/arc illustrations separated into alternating three SPARK/two Spine layers; a moving sword from Spine and its multicolor surface from SPARK coordinate by bone attachment; Shinigami Melza distortion via illustration-matched mesh and mask. The report mentions some illustrated presentations as long as **2,000 frames**; this is claimed sequence length, not checked unique drawing count or an instruction to use 2,000 images. No actual art source, client build, per-frame timed playback, editor or runtime measurement. |
| F11-S03 | [G06-F10 *Space Harrier* encounter source ledger](G06-FUNDAMENTALS-10.md), **2021 IGCC critic / MAME hardware emulation source** | Cross-case comparator only. Independent commentator reports after hit the explosive subject rapidly falls and becomes a ground explosion, plausibly clearing enemy sightlines; modern emulator supports moving/scaled sprites but **original timed event and substitution mechanism NOT verified**. Do not upgrade F10 by comparing it to 2019 creator evidence. |
| F11-S04 | [Arc System Works, 2025 Part 1 public technique lecture summary](https://gamemakers.jp/article/2025_10_10_120081/), **2025-10-10** report of 2021 CGWORLD talk (videos not watched in this pass); [official ASW Academy](https://www.arcsystemworks.jp/academy/) | **Secondary independent, named modern comparator R1:** *Guilty Gear -Strive-* devs present large-area effects behind actor, small sparks in front, rendering priority and alternatives like dithering/hand-added effects to keep actor legible amid flashy attacks. This confirms **another production discusses** actor/FX occlusion, not common ancestry or demonstrated perceptual optimum. |

## What the 2019 production source actually says

### P.4 — Palette art direction as an editable operation

The slide states that a grayscale texture combined with a palette texture enables deliberate transitions among **hard edge / soft glow**. Narrowing the alpha transition (termed **アルファクランチ**) yields a crisp contour; broader additive blur can be layered to preserve visible light. It names effect texture offset/palette adjustment to reuse source material rather than always create a special texture. This is a *source-art and representation contract* across different illustration styles, not simply shader novelty. **No texture bytes, grayscale levels, LUT shape, shader implementation, sRGB policy or timing parameter values are supplied in the inspected text**, so they remain unknown; no machine-specific thresholds inferred.

The same slide explicitly describes a **hit effect that clears from its center after occurrence, with an aftereffect** (発生後、余韻を残しつつ中央から晴れていくデザイン). Here the *designer's own text* supports a visibility-directed operation; in F10 an outside critic attributed an analogous function to the falling arcade explosion. These are **similar high-level dramaturgical solutions**, not the same action trajectory or inferred ancestral transmission.

### P.5 — A single illustration as a multi-department moving composition

For illustrated character/arc displays, the source illustration is divided into **five layers, arranged three SPARK and two Spine** while respecting drawing order and parts that pass in front of/behind other parts. This is a *specific production example*, not a five-layer standard, not five images only, and not a division into 3D geometry versus illustration by simple category. The image asset's underlying linework, colors and occluded surfaces remain important during motion; F06 has already established the general rigging/part-separation problem.

CGWORLD says these images can be animated for extended durations, sometimes 2,000 frames. The number does **not** reveal source drawings, skeleton keys, pixel asset sizes or unique 2D frames.

### P.6–7 — Anchored artistic phenomena, not independent decorative overlays

A sword's underlying movement is authored with **Spine**. Its animated iridescent surface comes from **SPARK**, with **UV scrolling constrained by a mask in the sword's shape** and anchored to a skeletal bone. The same integration supports bright orb tips and a monster's flowing drool; the latter uses a polyline particle with spring/rope-like behavior. Different expressive/physical parts thus can have **different procedural authorship and timing authority** while sharing an on-screen subject.

Do not infer the 2019 systems' proprietary engine code, exact latency, a universal rigging rule, or that particles are required to animate fluids and decorative marks.

### P.8–10 — When the effect becomes part of the illustration

The published slide text describes a **mesh matched to the original illustration**, separate UV coordinates for depth/distortion, and a mask channel controlling where distortion applies. The creator recounts trying to animate an illustration in SPARK even before specialist Spine artists were present, using distortions as a practical substitute for absent rigging infrastructure. This is an **artist's process account and constraint adaptation**, not proof that mesh distortion fully equals dedicated hand-drawn or skeletal animation.

A visually finished illustrated figure and its flame aura may share a silhouette; decomposing them strictly into ‘subject’ and ‘effect’ could fail to preserve the aesthetic objective. That echoes the **separability caveat** found much earlier in F01's manga research, with a very different actual production representation.

## Cross-case finding — why this matters

| Question | Space Harrier 1985 (F10) | Last Cloudia 2019 (F11) | G06 production implication |
|---|---|---|---|
| **Where is image activity authored?** | Sprite graphics/scaler and game event state; exact studio artwork unknown | Pixel sprites + original illustrations + Spine rigs + SPARK effects + in-house Unity camera direction | Don't make a generic 'FX file' stand in for all authoring data |
| **How does a strong impact vacate its own focal center?** | Critic reports downward explosion and ground-specific presentation; timing unverified | Developer slide explicitly states center-clearing hit effect with residual impression | Evaluate **exit/clearing**, not only onset/peak; these are analogies, not same technique |
| **Who owns subject-attached motion?** | Proposed event-driven sprite replacement/position; no actual game state recovered | A sword moves with Spine; rainbow sheath/UV effect follows by bone attachment and shape mask | Anchor/registration and lifetime need explicit ownership across art+effect |
| **How is visual style fitted to art?** | Sprite banks/palettes/scaler constrained by 1985 memory; exact art masters absent | Palette-LUT/gray source with alpha-crunch sharpness, optional soft glow, reused library | Separate editable tonal source/edge quality from rendered blend and platform |
| **What controls the composition?** | Arcade camera, checkerboard ground, scaled projected enemies/shot action | 3D game scene + authored Unity camera for special attacks + alternating front/back illustration layers | Review against original character/background/camera and concurrent activity |
| **What is the source quality?** | Independent critic, later gameplay reviewer, emulated hardware code; no clip | First-person indexed 2019 technical slide descriptions + event report; images/motion/editor unmeasured | Evidence kinds and maturity separate; **no claim of same genealogical line** |

### Relation to other practices already examined

- **F02–F04 manga**: a graphic treatment depends on composition and what remains visible, not just the shape's name. F11 offers a *documented game-specific* instance, **not** a historical proof of direct manga-to-game transfer.
- **F05 effects drawing**: one original drawing can be divided and slid to direct composite motion; F11 shows different software-specific illustration partition and bone-attached motion, not the same technique or early film ancestry.
- **F06 rigging/part ownership**: source illustration and skeletal motion remain separately editable; the art/motion/FX attachment must be authored deliberately.
- **F08 realism**: physical plausibility can be traded against silhouette, effect overlap and timing; use natural simulation only where it answers the chosen scene problem.

## What we can actually carry into a future original production project

The **transferable questions** are now more precise and can be turned into art-authoring specifications without inheriting any commercial resources:
1. Does the effect show the intended cause and immediate force **without long-term occlusion** of the relevant character, obstacle, bullet or next action? Does it have a deliberately authored exit/reveal, not merely arbitrary particle decay?
2. Can the artist control **hardness of the edge, palette identity, soft light and residue** independently without damaging the source drawing or imposing a fake one-size pixel effect? Is the effect's look reviewed at final display scale?
3. Where phenomena attach to a moving actor or illustrated object, is **anchor, mask, draw order, temporal event and layer ownership** explicit? Can the figure and its surrounding treatment be revised separately and together?
4. Does a small scene allow **a clean comparison**: one restrained treatment; one more spectacular layer/exit; one bright or crowded adverse setting? No premise that the visually largest effect is the best one.
5. Can the original art/effect editor sources survive **import, one real critique/revision pass and transfer to one different figure/event** without guessing proprietary internal tools?

These are **questions, not proven results**. F11 is R1 documentation and cannot independently close FX-A/S/C/R/I or R3/4. It is not a request to buy SPARK, use Spine/Unity, build another mini-app, imitate Last Cloudia art, or claim the opening spectator response was measured. Before any G06 production stage, select a lawful original art scene, exact source/public references, representation/display contract, and feasible editable tools.

## Deliberate stop

F11 is **one** comparative practice case, not the start of a new infinite case-number series. F10 closed *Space Harrier* active study at R1 with deferred clip; F11 confirms by first-person production evidence that **composition-preserving effect exit, illustration/FX attachment and editable art treatment** are active independent game craft concerns. The next G06 step should **synthesize F01–F11 into a bounded original art-authoring decision** under [STD01](../docs/EFFECTS_STANDARD.md) rather than add F12/F13 every time a new game is found. It may also intentionally return to G02 illustration-feature survival if the selected target needs original character art. No 'required game clone', custom VFX editor, producer-team reconstruction or full Japanese effects history is implied.
