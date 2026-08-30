---
type: skill
generated: true
name: "tax-procedure-matter-workflow"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/tax-procedure-matter-workflow/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# tax-procedure-matter-workflow

Orchestriert steuerliche Verfahrens-Matters von Erklärung und Bescheidabgleich über Betriebsprüfung, Korrektur, Einspruch und gerichtliche Eskalation, hält Fristen, Verfahrensstand, Evidence und materielle Tax Positions zusammen und routet Vertretung oder Steuerstraf-/Counsel-Fragen an befugte Professionals.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/current-tax-context|current-tax-context]]
- [[skills/tax-position-register|tax-position-register]]
- [[skills/tax-professional-routing|tax-professional-routing]]

## Required by

- —

## Outputs

- `tax-assessment-reconciliation.json`
- `tax-procedure-action-plan.json`
- `tax-procedure-deadlines.json`
- `tax-procedure-status.json`

## Output consumers

### `tax-assessment-reconciliation.json`

- Terminal or currently unconsumed output.

### `tax-procedure-action-plan.json`

- Terminal or currently unconsumed output.

### `tax-procedure-deadlines.json`

- Terminal or currently unconsumed output.

### `tax-procedure-status.json`

- Terminal or currently unconsumed output.

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/tax-procedure-matter-workflow/SKILL.md`
