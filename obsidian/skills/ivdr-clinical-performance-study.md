---
type: skill
generated: true
name: "ivdr-clinical-performance-study"
category: "regulated-engineering"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/ivdr-clinical-performance-study/SKILL.md"
tags:
  - skill
  - skill-category/regulated-engineering
---

# ivdr-clinical-performance-study

Plant klinische IVD-Performance-Evidenz nach IVDR/ISO 20916 mit Risiko-, Bias-, Endpunkt- und Gap-Kontrolle.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/regulated-engineering|regulated-engineering]]

## Requires

- [[skills/mdcg-guidance-navigator|mdcg-guidance-navigator]]
- [[skills/medical-device-risk-management-iso14971|medical-device-risk-management-iso14971]]
- [[skills/regulated-product-context|regulated-product-context]]
- [[skills/regulatory-evidence-traceability|regulatory-evidence-traceability]]

## Required by

- [[skills/ivdr-performance-evaluation|ivdr-performance-evaluation]]

## Outputs

- `clinical-performance-evidence.json`
- `clinical-performance-study-plan.json`
- `performance-study-gaps.json`

## Output consumers

### `clinical-performance-evidence.json`

- [[skills/ivdr-performance-evaluation|ivdr-performance-evaluation]]

### `clinical-performance-study-plan.json`

- [[skills/ivdr-performance-evaluation|ivdr-performance-evaluation]]

### `performance-study-gaps.json`

- [[skills/ivdr-performance-evaluation|ivdr-performance-evaluation]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/ivdr-clinical-performance-study/SKILL.md`
