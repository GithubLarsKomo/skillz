---
type: skill
generated: true
name: "ivdr-scientific-validity"
category: "regulated-engineering"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/ivdr-scientific-validity/SKILL.md"
tags:
  - skill
  - skill-category/regulated-engineering
---

# ivdr-scientific-validity

Bewertet die wissenschaftliche Validität eines IVD evidenzgebunden und trennt Association, Claim, Evidenzstärke und Gap.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/regulated-engineering|regulated-engineering]]

## Requires

- [[skills/regulated-product-context|regulated-product-context]]
- [[skills/regulatory-evidence-traceability|regulatory-evidence-traceability]]
- [[skills/research-to-evidence-note|research-to-evidence-note]]

## Required by

- [[skills/ivdr-performance-evaluation|ivdr-performance-evaluation]]

## Outputs

- `scientific-validity-assessment.json`
- `scientific-validity-report.md`

## Output consumers

### `scientific-validity-assessment.json`

- [[skills/ivdr-performance-evaluation|ivdr-performance-evaluation]]

### `scientific-validity-report.md`

- [[skills/ivdr-performance-evaluation|ivdr-performance-evaluation]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/ivdr-scientific-validity/SKILL.md`
