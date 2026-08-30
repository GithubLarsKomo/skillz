---
type: skill
generated: true
name: "travel-stay-research"
category: "internal"
userFacing: false
evaluationPassed: false
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 0
sourcePath: "skills/travel-stay-research/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# travel-stay-research

Recherchiert geeignete Unterkünfte und bewertet Lage, Eigenschaften, Qualitäts- und Review-Signale gegen den Travel Context ohne aktuelle Zimmerangebote als dauerhafte Produktevidenz zu behandeln.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- [[skills/research-to-evidence-note|research-to-evidence-note]]
- [[skills/source-to-context|source-to-context]]

## Required by

- [[skills/travel-agency-workflow|travel-agency-workflow]]

## Outputs

- `travel-stay-options.json`
- `travel-stay-options.md`

## Output consumers

### `travel-stay-options.json`

- [[skills/travel-agency-workflow|travel-agency-workflow]]
- [[skills/travel-availability-snapshot|travel-availability-snapshot]]
- [[skills/travel-option-ranking|travel-option-ranking]]

### `travel-stay-options.md`

- [[skills/travel-agency-workflow|travel-agency-workflow]]

## Evaluation

- Mode: `compatibility`
- Passed: `False`
- Cases: `3`
- Recorded results: `0`

## Canonical source

`skills/travel-stay-research/SKILL.md`
