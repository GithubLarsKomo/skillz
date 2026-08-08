---
type: skill
generated: true
name: "opaque-system-analysis"
category: "internal"
userFacing: false
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/opaque-system-analysis/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# opaque-system-analysis

Rekonstruiert das kleinste evidenzbasierte Verhaltens- und Schnittstellenmodell eines opaken oder unzureichend dokumentierten Systems, Artefakts, Protokolls oder Dateiformats, wenn Quellcode oder belastbare Dokumentation für die nächste Engineering-Entscheidung nicht ausreichen. Verwenden, bevor Diagnose oder Implementierung beginnt, wenn erst beobachtbares Verhalten, Zustände, Inputs, Outputs oder Verträge erschlossen werden müssen; nicht für Exploit-Entwicklung, allgemeine Fehlersuche mit ausreichender Sichtbarkeit oder breite Projektplanung.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- —

## Required by

- —

## Outputs

- `opaque-analysis-evidence.md`
- `recovered-system-model.json`
- `remaining-unknowns.json`

## Output consumers

### `opaque-analysis-evidence.md`

- Terminal or currently unconsumed output.

### `recovered-system-model.json`

- Terminal or currently unconsumed output.

### `remaining-unknowns.json`

- Terminal or currently unconsumed output.

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/opaque-system-analysis/SKILL.md`
