---
type: skill
generated: true
name: "travel-destination-research"
category: "internal"
userFacing: false
evaluationPassed: false
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 0
sourcePath: "skills/travel-destination-research/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# travel-destination-research

Recherchiert und bewertet Reiseziele gegen einen bestätigten Travel Context und trennt belegte Zielmerkmale, Saisonalität, praktische Eignung und Evidenzlücken.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- [[skills/research-to-evidence-note|research-to-evidence-note]]
- [[skills/source-to-context|source-to-context]]

## Required by

- [[skills/travel-agency-workflow|travel-agency-workflow]]

## Outputs

- `travel-destination-evidence.json`
- `travel-destination-evidence.md`

## Output consumers

### `travel-destination-evidence.json`

- [[skills/travel-agency-workflow|travel-agency-workflow]]
- [[skills/travel-option-ranking|travel-option-ranking]]

### `travel-destination-evidence.md`

- [[skills/travel-agency-workflow|travel-agency-workflow]]

## Evaluation

- Mode: `compatibility`
- Passed: `False`
- Cases: `3`
- Recorded results: `0`

## Canonical source

`skills/travel-destination-research/SKILL.md`
