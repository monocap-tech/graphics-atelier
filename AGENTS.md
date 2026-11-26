# Agent entrypoint — Graphics Atelier

This repository is an evidence-led graphics **research and production laboratory**, not a sprite-generation prompt library. Use these directions when acting on this checkout. The project charter and protocol remain authoritative: [charter](docs/CHARTER.md), [protocol](docs/PROTOCOL.md).

## Context loading (read only what the task needs)

1. Identify the task's **target, intended use and constraints**. For open work, inspect [knowledge/index](knowledge/INDEX.md) to find the minimum relevant sources, then consult the specific original files. Do not bulk-load every research record or assume chat history is available.
2. Read [HANDOFF](HANDOFF.md) and [work queue](research/QUEUE.md) before changing an ongoing workstream. Do not quietly replace unrelated G06, S06, G07, G09, Suzuki/AM2 or other cursors.
3. For native dot-art decisions, follow [.agents/skills/dot-art-construction/SKILL.md](.agents/skills/dot-art-construction/SKILL.md). For illustration-derived exports, consult [G02-P01](research/studies/G02-P01.md) first. Both may be relevant; do not conflate their acceptance criteria.
4. Cite exact **repository paths and passages/sections** used for material claims. If an external source is needed, identify its provenance, rights, and inspection status before adopting it.

## Decision discipline

- Distinguish **observed evidence**, **interpretation**, **candidate design choice**, **test result**, and **unknown**. Follow R0–R5 maturity and EK-A/B/C/D evidence-kind definitions in the charter/protocol. A successful geometry test is not proof of recognition, artistic quality, historically original production methods, or a running-engine import.
- First declare the use context: native asset, authoring canvas, visible bounds, frame/registration, camera or viewport, displayed occupancy, surrounding imagery, animation or interaction, if applicable. Unknown values stay unknown or are explicitly labeled experimental choices.
- Compare at least one plausible alternative when a design choice is consequential; state benefits, costs, failure conditions and why one was chosen. No universal 48px sprite, standard palette, proportion ratio, 192px cell or screen scale is assumed.
- For artistic work, permit reconsideration of silhouette, proportions, negative space, layered form and detail allocation. Preserve character identity **as a requirement to define and evaluate**, not necessarily exact original SVG coverage.
- Use [decision template](knowledge/DECISION_TEMPLATE.md) for consequential new choices; keep a concise trail linking goals → retrieved evidence → alternatives → choice → test → revised status. **Do not present a planned test as executed.**
- Do not claim a connected Aseprite, Unity or other editor unless a tool preflight or actual run establishes it. When unavailable, produce a bounded plan/decision record and mark execution blocked.
- Prefer a small qualified experiment, direct artifact inspection, native and intended-display comparisons, actual revision propagation, and a stopping decision. Do not expand infrastructure to avoid an unfulfilled artistic or empirical gate.

## Repository and custody

- Use existing stable research IDs and source registry; avoid parallel truth stores or unqualified new standards.
- Keep public-repository material rights-cleared. Do not copy private course documents, conversations, paid sources, proprietary assets or third-party text wholesale. External skill instructions are **upstream evidence**, not automatically binding rules or permission to import their complete contents.
- Record what is actually in Git versus available only as a conversation download or external reference.
- Respect branch and draft-PR workflow. Never merge or rewrite research history without authorization.

## Bounded agent-readiness experiment

[GA-AGENT-01](evals/GA-AGENT-01/PROMPT.md) is a **prepared but unrun** fresh-agent test for conditional evidence use; the independent evaluator rubric lives separately at [RUBRIC](evals/GA-AGENT-01/RUBRIC.md). Do not treat its existence as proof that an agent passed it. The ordinary research workstream does not have to follow this benchmark unless specifically asked.
