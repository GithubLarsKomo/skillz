---
type: skill
generated: true
name: "compliance-management-workflow"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/compliance-management-workflow/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# compliance-management-workflow

Orchestriert ein evidenzbasiertes Compliance-System von aktuellem Obligation Register über Risk-based Control Mapping und Assurance bis zu Gaps, Remediation, Change Monitoring und Final Gate. Verwenden für Compliance-Frameworks und Management-Reviews jenseits einzelner Rechtsfragen.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/compliance-control-assurance|compliance-control-assurance]]
- [[skills/compliance-control-mapping|compliance-control-mapping]]
- [[skills/compliance-obligation-register|compliance-obligation-register]]
- [[skills/legal-matter-final-gate|legal-matter-final-gate]]

## Required by

- [[skills/executive-legal-compliance-governance|executive-legal-compliance-governance]]

## Outputs

- `compliance-gap-remediation-plan.json`
- `compliance-management-handoff.json`
- `compliance-management-status.json`

## Output consumers

### `compliance-gap-remediation-plan.json`

- [[skills/executive-legal-compliance-governance|executive-legal-compliance-governance]]

### `compliance-management-handoff.json`

- [[skills/executive-legal-compliance-governance|executive-legal-compliance-governance]]

### `compliance-management-status.json`

- [[skills/executive-legal-compliance-governance|executive-legal-compliance-governance]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/compliance-management-workflow/SKILL.md`
