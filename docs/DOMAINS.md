# Domain map

Stable provisional identifiers denote capabilities rather than applications. The interface branch is kept distinct and linked to graphics at their shared boundaries.

| ID | Domain | Example output |
|---|---|---|
| VG01 | Raster construction | palette, pixel placement, shading, outlines, authored raster asset |
| VG02 | Animation and articulation | key poses, multipart animation, prerender-and-correct workflow |
| VG03 | Polygonal construction | modular textured environment, simple lighting and geometry budgets |
| VG04 | Spatial composition | scrolling and parallax, camera sequences, hybrid projection |
| VG05 | Effects | trails, lasers, particles, distortion, procedural geometry |
| VG06 | Illustrative and dramatic composition | environment variants, character illustration, directed transitions |
| VG07 | Graphics architecture | logical framebuffer, sampling, scaling, priority and blending |
| VG08 | Production infrastructure | validation, packing, compilers, editor tooling and diagnostics |
| IP01 | Information architecture / screen composition | layout, hierarchy, viewport and HUD allocation |
| IP02 | Interface states and interaction | navigation, operational contracts, feedback, interruption |
| IP03 | Temporal and audiovisual authorship | motion grammar, easing, sound relations, interpretation |
| IP04 | Interface systems and handoff | editable components, runtime binding, accessibility/localization |
| IP05 | Art direction and economy | choice of treatment, intentional omission, alternatives and critique |

Tool candidates, not mandates: Aseprite (raster, metadata); Blender (geometry and prerender); Illustrator or equivalent (vectors); Figma or equivalent (states); After Effects or equivalent (temporal prototypes); Clip Studio or equivalent (illustration); Effekseer (effects); Unity (test host); Wwise (audio integration when justified).

Architecture candidates from earlier arcade-board research: explicit sprite/background/polygon/effect processors, logical framebuffer and compositor, distinction between object and display scaling, palette and asset metadata. A 640x480, 4:3, 60 Hz logical display is an experimental candidate only; compare against alternatives and do not impose it on every target. No emulation mandate.
