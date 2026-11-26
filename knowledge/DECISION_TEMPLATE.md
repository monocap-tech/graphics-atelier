# Decision record template — conditional graphical production

Use one record for a consequential choice. Keep entries short enough that another agent can audit the choice **without having lived through the conversation**. Fill every field or explicitly write “not tested / unknown / not applicable.”

```markdown
# DECISION-<ID> — <short question>
Date / workstream / author or agent:
Status: proposed | tested-locally | adopted-for-target | rejected | blocked
Maturity and evidence kinds (claim-specific): R__ / EK-__

## Goal and viewing conditions
Intended purpose, character/object identity, target camera/display state,
native/workspace/viewport distinction, timeline or action if relevant:
User-provided constraints vs trial assumptions:

## Evidence retrieved
- <file path>#<section>: what it supports, with maturity and limitation
- <file path>#<section>: competing evidence or contrary case
- External sources: URL, version, access/licensing/verification status

## Alternatives
A. <name>: representation, benefits, failure modes, costs
B. <name>: representation, benefits, failure modes, costs
What observation would change this ranking?

## Choice and intended loss
Chosen **for this target only**:
What to preserve / exaggerate / merge / omit:
Reasoning, uncertainties and rejected assumptions:

## Execution and actual observations
Tools, versions and preflight: 
Original editable source and revision custody:
Experiment commands / output paths / checked-in vs external artifacts:
Observed mechanical checks:
Observed artistic critique:
Viewer response, if measured:
Runtime/editor import, if actually executed:
Failures and negative evidence:

## Decision
Accept | revise | reject | defer; criterion and reason:
Next bounded experiment or stopping reason:
```

**Guardrail:** an intended test belongs in a *plan* field, never under “observed.” Link back to the evidence source rather than restating its findings as a new authority.
