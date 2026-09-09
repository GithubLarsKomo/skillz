---
type: skill
generated: true
name: "character-voice-fingerprint"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/character-voice-fingerprint/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# character-voice-fingerprint

Modelliert und prüft unterscheidbare Figurenstimmen aus Herkunft, sozialem Kontext, Beruf, Beziehung, Status und Stresszustand, ohne karikierenden Dialekt zu erzeugen. Verwenden für Ensemble-Fiction vor und während des Draftings sowie für Voice-Collision-Audits, Blind Attribution und Speaker-Swap-Tests.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/ensemble-character-architecture|ensemble-character-architecture]]

## Required by

- [[skills/fiction-series-writing-workflow|fiction-series-writing-workflow]]

## Outputs

- `character-voice-audit.json`
- `character-voice-fingerprint.json`
- `voice-collision-register.json`

## Output consumers

### `character-voice-audit.json`

- Terminal or currently unconsumed output.

### `character-voice-fingerprint.json`

- [[skills/fiction-series-writing-workflow|fiction-series-writing-workflow]]

### `voice-collision-register.json`

- [[skills/fiction-series-writing-workflow|fiction-series-writing-workflow]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/character-voice-fingerprint/SKILL.md`
