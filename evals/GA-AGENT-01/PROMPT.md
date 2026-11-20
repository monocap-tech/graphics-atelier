# GA-AGENT-01 — Fresh-agent probe (candidate prompt)

**Status:** prepared, **not executed**. This is one bounded evidence-to-decision test, not a sprite-art quality benchmark.

## Operator procedure

1. Check out the draft `research/foundation` branch at the GA-AGENT-01 instructions commit in a **fresh agent session**, with no prior Graphics Atelier chat transcripts, previous answers, evaluator notes or hidden hints. Give the agent only the task below, the checkout and its normal repository tools. **Do not show the evaluator's [RUBRIC.md](RUBRIC.md) to the subject agent**; for a stricter blind run, stage the worktree without that file.
2. The agent must read relevant repository documents itself. No drawing/editor integration is assumed. Do not give it a curated list of expected conclusions.
3. Save the response as an externally held test artifact or a clearly labeled report **after** the run. Assess using the separate rubric, then allow at most **one** revision to instructions/index/skill followed by a second fresh run; do not tune against unlimited examples.
4. Record exact agent/model version, working tree SHA, tool access, sources read, answer and evaluator decisions. Do not edit the user's artwork or other research streams during the probe.

## Task to paste, verbatim

> You are joining Graphics Atelier with access to this repository but no prior chat history. We need a native-grid character representation for an experimental game camera: logical world viewport 640×360, neutral pose and one action pose, busy effects near the player. The character brief is “Relay Courier”: recognizable hair crest, cheek marking and asymmetrical shoulder relay. No final native size, palette, body proportions or sprite cell have been selected. We do not have an active graphics editor connection.
>
> Produce a bounded **design decision memo**, not images or new source assets. Use repository evidence to propose **two materially different construction approaches**, explain what you would retain/change/omit, how the proposed choices relate to the displayed character and scene, what would falsify your preferred approach, and which measurements or reviews can actually be completed without a connected editor. Distinguish demonstrated facts from assumptions and unperformed tests; cite the exact repository documents and sections that support consequential claims. If you cannot decide on a native size, state what test would resolve it.

## Observable completion

Produce one memo in the [decision-record](../../knowledge/DECISION_TEMPLATE.md) structure or an equivalent compact format. It is allowed to conclude that the native scale remains indeterminate. **No artwork or engine run is needed to pass this particular test.**
