# G00-A03 — EDGE, Edge3 and Aseprite: indexed production operations

2026-11-18. Bounded R1 source qualification plus one independent semantic control. No editor launched; historical prevalence and exact interchange compatibility not measured.

## Sources

| ID | Source | Bounded finding |
|---|---|---|
| SRC054 | [Takabo Soft, EDGE2 introduction](https://takabosoft.com/edge2/intro), JP, official | Multi-page layered documents, palette banks, color protection, patterned drawing, grid presets, native-size preview, page/layer/palette and capture animation, remembered export settings. These are documented capabilities, not proof that a particular studio used them. |
| SRC055 | [ドット絵講座EDGE編](https://zioru.x0.to/shop_plan_pixel_win_edge.htm), JP, independent tutorial | 16x16 exercise, 16px grid and 8px editing step; constructs a palette instead of using defaults, arranges related values together, develops outline/base/shadow/highlight and checks native preview. Author-specific pedagogy, not a universal convention. |
| SRC056 | [ネ実ツクスレ, ツクール2000用ドット絵講座](https://w.atwiki.jp/pokotan/pages/42.html), JP, community tutorial | Reports 24x32 character and 16x16 map cells; layered body/wear/hair, front-reference construction of other facings, copied/redrawn moving limbs, mirroring with color corrections, animation review. Verify RPG Maker specifications separately before using engine compatibility. |
| SRC057 | [Takabo Soft, Edge2→Edge3 migration](https://edge3.takabosoft.com/manual/getting-started/migration-from-edge2/), JP, official 2026 | Rewrite, old pages separated into frames/assets, project-persistent grids, capture→sprite panel; old general color mask and capture groups omitted. Indexed layer composite can display RGBA results beyond 256 colors; export choice matters. EDG3/EDG roundtrip can lose alpha. |
| SRC058 | [Edge3 features](https://edge3.takabosoft.com/features/) / [June 2026 release report](https://www.famitsu.com/article/202606/76721), JP | Modern successor with parts assembly and frame animation; early access, not a stable long-term dependency. |
| SRC059 | [Aseprite indexed mode](https://aseprite.org/docs/color-mode/) / [Shading](https://aseprite.org/docs/shading/) | Index points to palette entry; editing an entry changes all referencing pixels; shading ink steps through selected colors. |
| SRC060 | [Aseprite CLI](https://aseprite.org/docs/cli/) / [Tags](https://aseprite.org/docs/tags/) / [Slices](https://aseprite.org/docs/slices/) | Batch palette substitution, sheet/JSON, grid/layer splitting options, animation tags, slice metadata and export; check installed version and actual output. |
| SRC061 | [ドット絵講座2018](https://speakerdeck.com/oinari/dotutohui-jiang-zuo-2018) | R0: search excerpt shows EDGE/GIF/palette training; direct fetch cache miss, no slides inspected. |

## Comparative production operations

| Operation | EDGE2 model | Candidate Aseprite equivalent / gap |
|---|---|---|
| Color roles | indexed palette banks | indexed document plus variant palettes; CLI palette replacement; test transparency/order |
| Ramp construction | ordered ramps; protected color indices | shading ink and selected ramp; selection/layer lock as partial substitute, not proven equivalent to general color mask |
| Registration | grid presets and editing units | grid/snap and layer/frame organization; verify selection step behavior |
| Frame animation | page animation/onion skin | timeline frames, tags, onion skin |
| Assembly | capture regions and capture groups | slices, split-grid, layers plus external/runtime assembly where necessary; tags alone do not implement multipart transforms |
| Native inspection | position window | Preview window; check 1:1 and final composed scale |
| Repeat export | remembered EDG export recipe | explicit CLI command and source/export separation |

A 24x32 cell is not a 24x32 opaque figure; grid constraints can come from runtime content formats rather than artistic preference. Compare with G02 dimensional contract. Layered reusable references also do not establish that all anatomy or animation should be modular: test asymmetry, pose and lighting before mirroring.

## Operational consequence

Palette replacement and appearance-preserving index remapping are distinct operations. Color-count budget must specify whether transparent index counts (G02-A01 Maskedo convention does); rendered composite may exceed native palette if alpha/blend operations are allowed. Palette ownership must be explicit. See [G01-P01](studies/G01-P01.md) and [semantic control](../labs/G01-P01/indexed_control.mjs).

The control is an executable independent mathematical fixture, not validation of EDGE or Aseprite behavior. The next practical pass should run the actual GUI/CLI export, then test registration and ownership in an engine. Do not build a replacement editor without an observed gap.
