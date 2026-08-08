---
type: skill
generated: true
name: "human-procedure-wizard"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/human-procedure-wizard/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# human-procedure-wizard

Führt sicher durch unvermeidbare menschliche Schritte in ansonsten agentengesteuerten Workflows, etwa Dashboard-Aktionen, Freigaben, Secret-Eingaben, physische Bestätigungen oder irreversible Cutover-Gates. Verwenden, wenn ein Agent den nächsten Schritt nicht selbst ausführen darf oder kann und danach verifizierbar weiterarbeiten soll; nicht für normale Anforderungsklärung oder reine Übergaben.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- —

## Required by

- —

## Outputs

- `human-procedure-plan.md`
- `human-procedure-result.json`

## Output consumers

### `human-procedure-plan.md`

- Terminal or currently unconsumed output.

### `human-procedure-result.json`

- Terminal or currently unconsumed output.

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/human-procedure-wizard/SKILL.md`
