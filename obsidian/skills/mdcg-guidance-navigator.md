---
type: skill
generated: true
name: "mdcg-guidance-navigator"
category: "regulated-engineering"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/mdcg-guidance-navigator/SKILL.md"
tags:
  - skill
  - skill-category/regulated-engineering
---

# mdcg-guidance-navigator

Ermittelt für Medical-Device-/IVD-Fragen die aktuell anwendbaren MDCG-Dokumente aus offiziellen EU-Quellen, inklusive Revision, Status, Scope, Freshness und Änderungen gegenüber einem früheren Stand. Verwenden, wenn aktuelle MDCG-Guidance identifiziert oder ein Guidance-Set aktualisiert werden muss; der Skill entscheidet selbst keine Compliance oder Klassifikation.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/regulated-engineering|regulated-engineering]]

## Requires

- [[skills/regulated-product-context|regulated-product-context]]
- [[skills/regulatory-evidence-traceability|regulatory-evidence-traceability]]
- [[skills/research-to-evidence-note|research-to-evidence-note]]

## Required by

- [[skills/ivdr-class-d-conformity|ivdr-class-d-conformity]]
- [[skills/ivdr-clinical-performance-study|ivdr-clinical-performance-study]]
- [[skills/ivdr-device-classification|ivdr-device-classification]]
- [[skills/ivdr-field-safety-corrective-action|ivdr-field-safety-corrective-action]]
- [[skills/ivdr-fsca-status-final-reporting|ivdr-fsca-status-final-reporting]]
- [[skills/ivdr-performance-evaluation-report|ivdr-performance-evaluation-report]]
- [[skills/ivdr-pmpf|ivdr-pmpf]]
- [[skills/ivdr-pms-vigilance|ivdr-pms-vigilance]]

## Outputs

- `mdcg-guidance-changes.json`
- `mdcg-guidance-set.json`

## Output consumers

### `mdcg-guidance-changes.json`

- [[skills/ivdr-class-d-conformity|ivdr-class-d-conformity]]
- [[skills/ivdr-clinical-performance-study|ivdr-clinical-performance-study]]
- [[skills/ivdr-device-classification|ivdr-device-classification]]
- [[skills/ivdr-field-safety-corrective-action|ivdr-field-safety-corrective-action]]
- [[skills/ivdr-fsca-status-final-reporting|ivdr-fsca-status-final-reporting]]
- [[skills/ivdr-performance-evaluation-report|ivdr-performance-evaluation-report]]
- [[skills/ivdr-pmpf|ivdr-pmpf]]
- [[skills/ivdr-pms-vigilance|ivdr-pms-vigilance]]

### `mdcg-guidance-set.json`

- [[skills/ivdr-class-d-conformity|ivdr-class-d-conformity]]
- [[skills/ivdr-clinical-performance-study|ivdr-clinical-performance-study]]
- [[skills/ivdr-device-classification|ivdr-device-classification]]
- [[skills/ivdr-field-safety-corrective-action|ivdr-field-safety-corrective-action]]
- [[skills/ivdr-fsca-status-final-reporting|ivdr-fsca-status-final-reporting]]
- [[skills/ivdr-performance-evaluation-report|ivdr-performance-evaluation-report]]
- [[skills/ivdr-pmpf|ivdr-pmpf]]
- [[skills/ivdr-pms-vigilance|ivdr-pms-vigilance]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/mdcg-guidance-navigator/SKILL.md`
