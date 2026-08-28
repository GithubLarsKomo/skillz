---
type: skill
generated: true
name: "contract-matter-workflow"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/contract-matter-workflow/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# contract-matter-workflow

Führt den kanonischen Vertrags-Matter-State von Deal-Type-Analyse über Review oder Drafting, Risiko, Negotiation und iterative Redlines bis zum Legal Final Gate. Verwenden bei expliziter Contract-Matter-Steuerung; für normale Vertragsanfragen bleibt contract-workflow der bevorzugte user-facing Einstieg.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/agreement-type-analysis|agreement-type-analysis]]
- [[skills/contract-drafting|contract-drafting]]
- [[skills/contract-review|contract-review]]
- [[skills/legal-matter-final-gate|legal-matter-final-gate]]
- [[skills/legal-negotiation-strategy|legal-negotiation-strategy]]
- [[skills/legal-redline-review-loop|legal-redline-review-loop]]

## Required by

- [[skills/contract-workflow|contract-workflow]]

## Outputs

- `contract-matter-handoff.json`
- `contract-matter-plan.md`
- `contract-matter-status.json`

## Output consumers

### `contract-matter-handoff.json`

- [[skills/contract-workflow|contract-workflow]]

### `contract-matter-plan.md`

- [[skills/contract-workflow|contract-workflow]]

### `contract-matter-status.json`

- [[skills/contract-workflow|contract-workflow]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/contract-matter-workflow/SKILL.md`
