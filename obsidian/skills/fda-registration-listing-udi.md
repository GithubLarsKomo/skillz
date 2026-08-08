---
type: skill
generated: true
name: "fda-registration-listing-udi"
category: "regulated-engineering"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/fda-registration-listing-udi/SKILL.md"
tags:
  - skill
  - skill-category/regulated-engineering
---

# fda-registration-listing-udi

Bereitet FDA Establishment Registration, Device Listing und UDI/GUDID-Masterdaten für Medical Devices strukturiert vor, trennt 21 CFR 807 von UDI-Pflichten und simuliert weder Registrierung noch Identifier-Vergabe.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/regulated-engineering|regulated-engineering]]

## Requires

- [[skills/decision-record|decision-record]]
- [[skills/medical-device-labeling-ifu|medical-device-labeling-ifu]]
- [[skills/regulated-product-context|regulated-product-context]]
- [[skills/regulatory-evidence-traceability|regulatory-evidence-traceability]]

## Required by

- —

## Outputs

- `fda-device-listing-readiness.json`
- `fda-registration-readiness.json`
- `gudid-udi-readiness.json`

## Output consumers

### `fda-device-listing-readiness.json`

- Terminal or currently unconsumed output.

### `fda-registration-readiness.json`

- Terminal or currently unconsumed output.

### `gudid-udi-readiness.json`

- Terminal or currently unconsumed output.

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/fda-registration-listing-udi/SKILL.md`
