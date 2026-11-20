# G00-A01 — Independent production workflows (2026-11-17)

Status: bounded first source pass, descriptive R1 for supported claims only. No tools run, assets downloaded, code executed or methods validated. Links publicly readable at inspection unless noted; licenses/redistribution remain unqualified. Baseline registry IDs retained.

## Qualified source observations

| ID | Public evidence (inspected 2026-11-17) | Supported claim / limitation |
|---|---|---|
| SRC001 | [SNK KOF XII official gallery](https://kofaniv.snk-corp.co.jp/english/info/15th_anniv/2d_dot/creation/index.php), EN, studio diagram | 2D concept, 3D model and animation, drawing based on 3D, finishing. Images/labels; no complete settings or production assets authorized. A. |
| SRC011 | [Fabien Sanglard, SHMUP source code, 2011-06-30](https://www.fabiensanglard.net/shmup_source_code/index.php), EN, developer account | Early Java method uses perspective background, depth reset and orthographic gameplay; author reports discontinuity between gameplay and cinematics. Later method derives entity matrices from screen coordinates each frame in 3D. Source linked, not compiled. B/C. |
| SRC013 | [APO+ CGWORLD interview, 2021](https://cgworld.jp/interview/202109-mouse.html), JP, artist interview in sponsored article | Blender layout/light study, full manual Photoshop redraw, Aseprite animation, AE supplementary effects. Reported 20–40 h for Photoshop; 480x270 typical overall artwork, not a sprite spec. B. |
| SRC008 | [Advent Softworks interview, 2025-05-31](https://retrorgb.com/new-indie-racer-linear-s-to-replicate-saturns-rendering-in-unity3d.html), EN, developer interview | VDP-inspired layer structure, quantized colors and quad shaders; use checkerboard mesh in place of problematic transparency. Framework described, no code inspected. C. |
| SRC010 | [Simulant Dreamcast guide](https://www.simulant.dev/docs/guides/dreamcast.md), EN, developer documentation | Homebrew target-specific asset/renderer constraints and cross-build instructions. Actual limits should be cross-checked with hardware/SDK sources before adopting them; no build tested. B. |
| SRC021 | [congusbongus, 3D Rendered Pixel Sprites, 2017-03-06](https://cxong.github.io/2017/03/3d-rendered-pixel-sprites), EN, hobbyist development account | C-Dogs SDL walk update: required frame count 40→144, Blender/Python rendering, ImageMagick tonal adjustment and sheet assembly, reported no manual retouching. Before/after examples, no rerun performed. B. |
| SRC022 | [Rubén López, Quantum Derail visual workflow, 2018-02-01](https://rubenlopezg.wordpress.com/2018/02/01/creating-a-2d-pointnclick-adventure-with-blender/), EN, independent developer account | Rendered foreground/background, generic vs room-specific sprites, floor lightmap sampling to tint sprites, dependency-aware Python-generated Makefile builds. Old Blender 2.79-era workflow; port required. B. |
| SRC023 | [Yaba Sanshiro, Rebuilding VDP2, 2026-05-31](https://www.yabasanshiro.com/blog/2026-05-31_new_vdp2_emulation), EN, emulator developer account | Texture-on-polygon approach replaced by hardware-order per-pixel compositor. Describes distinction from ordinary stacked alpha blending; verify implementation/edge cases against code and documentation before emulation claim. C. |
| SRC024 | [CEDEC+KYUSHU 2026, インデックスカラーでゲームのドット絵を描こう](https://cedec-kyushu.jp/2026/session/12.html), JP, session abstract (Takahiro Hosoya, Tenda Games) | Palette organization, recoloring, primitive shading planned subjects; abstract only, not lecture content or executable recipe. R0. |

## Japanese independent leads (R0, snippets only)

- SRC025 [ゲームヘル2000 ドット絵Tips](https://w.atwiki.jp/yaruhara/pages/43.html), 2006 personal/community game-author notes.
- SRC026 [TAM プログラマ流、初心者向けドット絵講座（人物、基本ポーズ編）](https://note.com/tamtamgames/n/na0b1852a5e7c), independent developer's construction process.
- SRC027 [桝久堂 ドット絵講座を受講してみた。](https://www.maskedo.com/post-8633/), experienced fighting-game sprite maker's critique of instruction.
- SRC028 [ドット絵描こうZ — 第23ドット 『ドット絵講座サイトのリンク集』](https://blog.livedoor.jp/dotez/archives/50825315.html), historical lead graph; individual URLs may be dead.
- SRC029 [heriet — 2017年のドット絵界隈Topics](https://note.com/heriet/n/n12bca60d4c02), historical community/source map.
- SRC030 [Blender Studio — Exploring 3D Pixel Art in Blender 4.2](https://studio.blender.org/blog/3d-pixel-art-in-blender/), search result advertises a project file; direct access returned 402, no file inspected.
- SRC031 [Pribambase](https://github.com/AlienPolygon/pribambase), live Aseprite/Blender texture editing; documentation and compatibility still to inspect.

Gunvolt and KOF XIII interviews resolved but detailed relevant passages not fully qualified in this pass: keep SRC002/SRC003 as discovery leads pending exact passage capture. Other baseline sources unreviewed. No complete audit or exhaustive corpus claim.

## Synthesis (our classification, not historical lineages)

Three distinct raster workflows: (1) generated raster with automated adjustment, (2) 3D-assisted manual revision, (3) 3D visual reference followed by independently authored raster. They allocate artistic control and labor differently. Compare using the same original geometry/brief; no assumption of universal superiority.

Projection architecture bifurcates between independently composited gameplay and projection-constrained 3D entities. The latter offers potential continuity with cinematics but is not required for a simple fixed-camera STG. Compositor and historical-hardware semantics are a separate investigation.

## Search and limitations

Queries included ドット絵 メイキング ゲーム 自作, Blender ドット絵 スプライト レンダリング, 同人シューティング 開発 3D 背景, 3D rendered pixel sprites, Sega Saturn PROJECT S and SHMUP source code. Older Japanese community pages emerged through date-oriented searches; several initial searches overreturned recent tools and marketing. Next sweep should follow the Japanese link network and qualify direct raster instruction, not simply accumulate newer exporters.

Next bounded experiment: [G03-P01](studies/G03-P01.md). Source entries above carry stable IDs and extend rather than replace the original registry.
