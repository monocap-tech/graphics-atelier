---
name: dot-art-construction
description: Deliberate and evaluate native-grid pixel-art construction for an identified target display and game context; distinguish art decisions from mechanically valid raster reduction.
---

# Dot-art construction — conditional production procedure

**Status:** GA-AGENT-01 R0 working instruction, **not** a validated artistry skill. Invocation: original character/prop/environment dot art, native-resolution sprite redesign, or a comparison with illustration-to-raster adaptation. See [knowledge routing](../../../knowledge/INDEX.md) and [decision template](../../../knowledge/DECISION_TEMPLATE.md).

**Upstream influence (not a verbatim import):** [with-pebbly/aseprite-ai-artist](https://github.com/with-pebbly/aseprite-ai-artist/tree/9def814c655acf86828f598ea88ca4cc41503389), specifically `skills/draw/SKILL.md`, `skills/review/SKILL.md` and `rules/03-silhouette-and-form.md`; MIT License, Copyright (c) 2026 with-pebbly. Preserve upstream's own [LICENSE](https://github.com/with-pebbly/aseprite-ai-artist/blob/9def814c655acf86828f598ea88ca4cc41503389/LICENSE) when copying any substantial portion. Here the workflow is independently worded and adapted to Graphics Atelier's target-led evidence protocol; no external software is included.

## Invariant

The artist/agent **allocates a constrained pixel field to an intended representational purpose**. The subject, native canvas, body/negative space, on-screen occupancy, animation and effects form one design problem. Neither the original illustration geometry nor a preferred palette is automatically authoritative. Re-enter earlier construction stages when later details reveal a structural failure.

## Step 0 — Establish task and preflight

1. Specify subject/identity, action or emotion to convey, camera and view angle, intended world viewport, expected displayed occupancy/range and competing background/HUD/FX. Clearly label user-supplied constraints versus experimental assumptions. If these are unknown, choose *test alternatives*, not a fictional standard.
2. Distinguish **native drawing bounds**, **authoring/work cell**, **alpha-visible bounds**, **animation envelope**, **ground/pivot**, **world/display mapping** and optional hitbox. Consult [dimensional contract](../../../docs/DIMENSIONAL_CONTRACT.md) and [G02-P01](../../../research/studies/G02-P01.md) where applicable.
3. Check actual tool availability. If Aseprite's integration is connected, verify sprite/layer/frame/palette state before changing anything. If not connected, do **not** hallucinate an editor call, claim a saved `.aseprite`, or silently replace a requested editor task with a PNG. A task asking only for a decision/design memo can proceed without editor access.

## Step 1 — Declare identity and loss budget

List the 2–5 distinctive cues that should remain identifiable, their priority and view/pose dependence. For each, specify acceptable merge, omission, exaggeration and whether its silhouette matters. Treat the reference illustration as a design source, **not** an immutable pixel stencil. Decide provisional native scale from game context and test at least one credible alternative when scale is unsettled.

## Step 2 — Construct spatial alternatives

At native resolution, stage a minimal flat-value silhouette (or a written plan when tools are unavailable). Allocate head, torso, limbs, equipment and empty spaces; consider pose, asymmetry, tangencies, attachment points and movement bounds. Check silhouette readability **before** committing detail. If it fails, alter proportions, occupancy, pose or canvas design instead of preserving the old mask.

Create two genuinely different treatments when this choice is consequential (e.g. faithful reduction versus redrawn mass hierarchy, or narrow realistic proportions versus proportionally enlarged head/equipment). Do not count a palette swap as a distinct structural alternative.

## Step 3 — Resolve interior form

Identify foreground/background overlaps, material regions and flat value/color groups. Apply shadow and highlight clusters as deliberate descriptions of form, considering light and display contrast. Choose contour/outline behavior and palette with the target context in mind. Add distinctive details and facial features only after their spatial budget has been established; face placement may require returning to Step 2.

A sequence of “silhouette → colors → details” is a **checkpoint arrangement**, not a one-way artistic law.

## Step 4 — Inspect in the correct context

- At **1× native**: inspect accidental tangencies, clusters, broken outlines, isolated pixels, excessive palette noise and ambiguous facial marks.
- At **intended display size**: inspect silhouette, pose, identity, contrast against representative world/HUD/FX, readability while moving and intentional stylization. A magnified contact sheet cannot substitute for this.
- For multiple frames/views: inspect ground registration, anchors, volume consistency, handedness, non-mirrored asymmetry and temporal continuity.
- Separate mechanical checks (bounds, pivot, palette count, alpha, exact exports) from artistic critique and independently observed viewer responses. In the absence of actual observers, **do not claim audience recognition or preferences**.

## Step 5 — Critique, revision, stop

Conduct a cold read of the result without relying on the intended identity label where possible. Name specific visible failures, propose the smallest appropriate structural or detail change, snapshot before editing, and compare before/after at matched conditions. A major silhouette redraw can be the *correct* revision: don't let a “keep all source pixels” policy block craft. If tools are unavailable, record these as **proposed**, not executed.

At most **one** art-feedback revision in GA-AGENT-01; further production runs require a separately authorized stage. Record the outcome with [DECISION_TEMPLATE](../../../knowledge/DECISION_TEMPLATE.md): retrieved evidence, considered alternatives, chosen design and disconfirming conditions, exact source/artifact custody, test status, limitations. An unexamined image is not an accepted sprite.

## Deliberation pitfalls

- 48px and 72px are **comparison candidates**, not global rules.
- h48 original Relay Courier A/B/C results in [G02-SPECIMEN-02](../../../research/G02-SPECIMEN-02.md) show constrained palette/feature corrections **without** a full native-silhouette redesign. Do not describe them as proof that the approach produces compelling dot art.
- A compositional transformation may intentionally break a source silhouette while better preserving identity, action or readability. State which value is being preserved.
- Follow upstream editor-specific tool syntax only when the matching tools are actually present and documented. A skill file is not an editor connection.
