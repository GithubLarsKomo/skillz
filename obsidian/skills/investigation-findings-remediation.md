---
type: skill
generated: true
name: "investigation-findings-remediation"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/investigation-findings-remediation/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# investigation-findings-remediation

Übersetzt Untersuchungsevidenz in nachvollziehbare Findings, trennt Fakt, Inferenz und Rechtsbewertung und entwickelt Remediation-, Disziplinar-, Reporting-, CAPA-/Control- und Retest-Pfade. Verwenden am Ende oder bei Zwischenfeststellungen einer internen Investigation.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/compliance-control-mapping|compliance-control-mapping]]
- [[skills/legal-compliance-risk-assessment|legal-compliance-risk-assessment]]

## Required by

- [[skills/internal-investigation-workflow|internal-investigation-workflow]]

## Outputs

- `investigation-findings.json`
- `investigation-remediation-plan.json`
- `investigation-reporting-decisions.json`

## Output consumers

### `investigation-findings.json`

- [[skills/internal-investigation-workflow|internal-investigation-workflow]]

### `investigation-remediation-plan.json`

- [[skills/internal-investigation-workflow|internal-investigation-workflow]]

### `investigation-reporting-decisions.json`

- [[skills/internal-investigation-workflow|internal-investigation-workflow]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/investigation-findings-remediation/SKILL.md`
