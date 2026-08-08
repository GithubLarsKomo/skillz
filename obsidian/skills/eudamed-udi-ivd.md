---
type: skill
generated: true
name: "eudamed-udi-ivd"
category: "regulated-engineering"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/eudamed-udi-ivd/SKILL.md"
tags:
  - skill
  - skill-category/regulated-engineering
---

# eudamed-udi-ivd

Erzeugt IVD-UDI-/EUDAMED-Readiness-Datensätze aus Product Context, Classification und kontrollierter Device-Evidence.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/regulated-engineering|regulated-engineering]]

## Requires

- [[skills/ivdr-device-classification|ivdr-device-classification]]
- [[skills/medical-device-labeling-ifu|medical-device-labeling-ifu]]
- [[skills/regulated-product-context|regulated-product-context]]
- [[skills/regulatory-evidence-traceability|regulatory-evidence-traceability]]

## Required by

- —

## Outputs

- `eudamed-readiness.json`
- `ivd-udi-data-set.json`

## Output consumers

### `eudamed-readiness.json`

- Terminal or currently unconsumed output.

### `ivd-udi-data-set.json`

- Terminal or currently unconsumed output.

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/eudamed-udi-ivd/SKILL.md`
