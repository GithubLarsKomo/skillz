---
type: skill
generated: true
name: "person-profile-document-delivery"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/person-profile-document-delivery/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# person-profile-document-delivery

Überführt einen fachlich und sprachlich finalisierten Personenreport in konsistente DOCX- und PDF-Ausgaben, wählt bei vorhandenem Corporate-Kontext passende Renderer oder Templates und erzwingt visuelle QA ohne inhaltliches Re-Authoring. Verwenden, wenn ein Personenprofil als professionelles editierbares DOCX und/oder finales PDF ausgeliefert werden soll.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/precision-writing-revision|precision-writing-revision]]

## Required by

- [[skills/person-research-report-workflow|person-research-report-workflow]]

## Outputs

- `person-profile-delivery.json`
- `person-profile-report.docx`
- `person-profile-report.pdf`

## Output consumers

### `person-profile-delivery.json`

- [[skills/person-research-report-workflow|person-research-report-workflow]]

### `person-profile-report.docx`

- [[skills/person-research-report-workflow|person-research-report-workflow]]

### `person-profile-report.pdf`

- [[skills/person-research-report-workflow|person-research-report-workflow]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/person-profile-document-delivery/SKILL.md`
