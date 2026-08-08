---
type: skill
generated: true
name: "ivdr-companion-diagnostic-consultation"
category: "regulated-engineering"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/ivdr-companion-diagnostic-consultation/SKILL.md"
tags:
  - skill
  - skill-category/regulated-engineering
---

# ivdr-companion-diagnostic-consultation

Bewertet IVDR-Companion-Diagnostic-Scope und bereitet die Notified-Body-Konsultation mit EMA oder zuständiger Arzneimittelbehörde nach Artikel 48 evidenzgebunden vor, ohne Performance Evaluation oder externe Stellungnahme zu simulieren.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/regulated-engineering|regulated-engineering]]

## Requires

- [[skills/decision-record|decision-record]]
- [[skills/ivdr-device-classification|ivdr-device-classification]]
- [[skills/ivdr-performance-evaluation|ivdr-performance-evaluation]]
- [[skills/regulated-product-context|regulated-product-context]]
- [[skills/regulatory-evidence-traceability|regulatory-evidence-traceability]]

## Required by

- —

## Outputs

- `cdx-consultation-readiness.json`
- `cdx-medicinal-product-linkage.json`
- `cdx-scope-assessment.json`

## Output consumers

### `cdx-consultation-readiness.json`

- Terminal or currently unconsumed output.

### `cdx-medicinal-product-linkage.json`

- Terminal or currently unconsumed output.

### `cdx-scope-assessment.json`

- Terminal or currently unconsumed output.

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/ivdr-companion-diagnostic-consultation/SKILL.md`
