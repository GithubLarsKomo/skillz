---
type: skill
generated: true
name: "tax-advisory-office"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/tax-advisory-office/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# tax-advisory-office

Orchestriert steuerliche Matters als Schwesterorganisation der Legal & Compliance Office von Intake, Current Tax Context und Specialist Routing über Tax Position, Szenarien und Professional Review bis zu Filing, Bescheid, Einspruch und Follow-up, ohne Fachlogik der Tax Specialists zu duplizieren oder eine Steuerberaterzulassung zu simulieren.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/current-tax-context|current-tax-context]]
- [[skills/tax-matter-final-gate|tax-matter-final-gate]]
- [[skills/tax-matter-intake|tax-matter-intake]]
- [[skills/tax-position-register|tax-position-register]]
- [[skills/tax-professional-routing|tax-professional-routing]]
- [[skills/tax-specialist-router|tax-specialist-router]]

## Required by

- [[skills/tax-legal-interface-specialist|tax-legal-interface-specialist]]

## Outputs

- `tax-matter-handoff.json`
- `tax-matter-plan.md`
- `tax-matter-status.json`

## Output consumers

### `tax-matter-handoff.json`

- [[skills/tax-legal-interface-specialist|tax-legal-interface-specialist]]

### `tax-matter-plan.md`

- [[skills/tax-legal-interface-specialist|tax-legal-interface-specialist]]

### `tax-matter-status.json`

- [[skills/tax-legal-interface-specialist|tax-legal-interface-specialist]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/tax-advisory-office/SKILL.md`
