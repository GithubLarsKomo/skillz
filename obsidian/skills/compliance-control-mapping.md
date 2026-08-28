---
type: skill
generated: true
name: "compliance-control-mapping"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/compliance-control-mapping/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# compliance-control-mapping

Übersetzt verifizierte Compliance-Pflichten in prüfbare Control Objectives, präventive/detektive/korrigierende Kontrollen, Owner, Frequenzen, Systeme und Evidenz und identifiziert Design- und Coverage-Gaps. Verwenden nach einem Compliance Obligation Register.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/compliance-obligation-register|compliance-obligation-register]]
- [[skills/legal-compliance-risk-assessment|legal-compliance-risk-assessment]]

## Required by

- [[skills/compliance-control-assurance|compliance-control-assurance]]
- [[skills/compliance-management-workflow|compliance-management-workflow]]
- [[skills/investigation-findings-remediation|investigation-findings-remediation]]

## Outputs

- `compliance-control-design-note.md`
- `compliance-control-gaps.json`
- `compliance-control-map.json`

## Output consumers

### `compliance-control-design-note.md`

- [[skills/compliance-control-assurance|compliance-control-assurance]]
- [[skills/compliance-management-workflow|compliance-management-workflow]]
- [[skills/investigation-findings-remediation|investigation-findings-remediation]]

### `compliance-control-gaps.json`

- [[skills/compliance-control-assurance|compliance-control-assurance]]
- [[skills/compliance-management-workflow|compliance-management-workflow]]
- [[skills/investigation-findings-remediation|investigation-findings-remediation]]

### `compliance-control-map.json`

- [[skills/compliance-control-assurance|compliance-control-assurance]]
- [[skills/compliance-management-workflow|compliance-management-workflow]]
- [[skills/investigation-findings-remediation|investigation-findings-remediation]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/compliance-control-mapping/SKILL.md`
