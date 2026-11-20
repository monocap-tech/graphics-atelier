# Integration: authored presentation and economy

## Two complementary kinds of laboratory

An authored target-acquisition indicator explores the communication of changing state: SEARCH, ACQUIRE, LOCK, LOST. A small puzzle game's fixed screen and restrained HUD explore what deserves articulation at all. These are complementary, not competing, directions.

The first asks: what can a visual/temporal construction express, and does it remain correct under live input and interruptions? The second asks: what must be visible, where, when, and at what cost to the gameplay composition?

## Public case: Relay Yard

The [public project](https://github.com/monocap-tech/relay-yard) is a compact Lights Out-derived puzzle-platformer. Its [SceneUI.cs](https://github.com/monocap-tech/relay-yard/blob/main/Assets/Scripts/SceneUI.cs) handles progress, time, best and record labels. Its [ResetHoldController.cs](https://github.com/monocap-tech/relay-yard/blob/main/Assets/Scripts/ResetHoldController.cs) separates the actual continuous hold requirement from the display ring: early release clears held duration immediately while displayed progress drains over time; mouse click takes a separate immediate path. Source defaults are 0.9 s hold and 0.25 s drain, not evidence of actual inspector settings or usability validation.

Use this as an implementation example of semantic/presentation separation. The letterboxed layout is a candidate retrospective study; inspect the tested original scene and captures before asserting precise layout properties. The migrated standalone repository lacks the exact font and some audio and is not independently verified as equivalent to the earlier build.

## Bridge lab (proposed)

Design a single stateful HUD cue in a restrained screen, using identical underlying state transitions across two different expressive treatments and a plain baseline. For example: an acquisition or reset hold indicator, with cancellation, confirmation and interrupted transitions.

- Specify information, urgency, competing stimuli and viewport allocation before styling.
- Compare simple direct runtime implementation with a modular authoring handoff (vector source, state mock, motion specification, live implementation) only where the extra steps answer a real question.
- Keep operational and display state separate. Test rapid cancellation, re-entry, false confirmation, different aspect ratios and silent/reduced-motion feedback.
- Compare reading accuracy, legibility against background action, appropriateness, authoring time and editability. Preserve reasons to reject costly or decorative treatment.
- Transfer the same principle to a different context; do not equate visual resemblance with transfer.

This lab integrates graphic construction, information architecture, motion and runtime, without assuming that every element requires elaborate animation or a large toolchain.

## Asset-to-presentation interface (proposed)

G02-P01 supplies the upstream design and acquisition interface: original illustration, registered pose set, scale and representation definitions, editable layer masters, export metadata and provenance. G09 should demonstrate that an approved source change (for example a costume accent or attachment point) can propagate through sprite and one additional relevant representation without breaking registration or gameplay legibility. Keep source artwork distinct from runtime atlas data and collisions; the renderer does not dictate a universal art canvas. See [G02-P01](../research/studies/G02-P01.md).

Related UI research remains separately maintained. No nonpublic curriculum files or original source artwork are reproduced here. Our bridge is a new proposed experiment, not an assertion that the earlier studies have been completed.
