---
type: skill
generated: true
name: "ivdr-device-classification"
category: "regulated-engineering"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/ivdr-device-classification/SKILL.md"
tags:
  - skill
  - skill-category/regulated-engineering
---

# ivdr-device-classification

Erstellt für ein IVD eine evidenzgebundene IVDR-Qualifikations- und Klassifikationshypothese nach Artikel 47/Anhang VIII mit expliziter Regelbegründung, konkurrierenden Regeln, Unsicherheiten und aktueller MDCG-Guidance. Verwenden für Class A/B/C/D Assessments; keine endgültige Behörden-/NB-Entscheidung simulieren.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/regulated-engineering|regulated-engineering]]

## Requires

- [[skills/mdcg-guidance-navigator|mdcg-guidance-navigator]]
- [[skills/regulated-product-context|regulated-product-context]]
- [[skills/regulatory-evidence-traceability|regulatory-evidence-traceability]]

## Required by

- [[skills/eudamed-udi-ivd|eudamed-udi-ivd]]
- [[skills/ivdr-class-d-conformity|ivdr-class-d-conformity]]
- [[skills/ivdr-companion-diagnostic-consultation|ivdr-companion-diagnostic-consultation]]

## Outputs

- `ivdr-classification-assessment.json`
- `ivdr-classification-rationale.md`

## Output consumers

### `ivdr-classification-assessment.json`

- [[skills/eudamed-udi-ivd|eudamed-udi-ivd]]
- [[skills/ivdr-class-d-conformity|ivdr-class-d-conformity]]
- [[skills/ivdr-companion-diagnostic-consultation|ivdr-companion-diagnostic-consultation]]

### `ivdr-classification-rationale.md`

- [[skills/eudamed-udi-ivd|eudamed-udi-ivd]]
- [[skills/ivdr-class-d-conformity|ivdr-class-d-conformity]]
- [[skills/ivdr-companion-diagnostic-consultation|ivdr-companion-diagnostic-consultation]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/ivdr-device-classification/SKILL.md`
