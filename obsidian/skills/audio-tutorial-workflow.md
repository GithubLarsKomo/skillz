---
type: skill
generated: true
name: "audio-tutorial-workflow"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/audio-tutorial-workflow/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# audio-tutorial-workflow

Überführt einen durch Grilling geklärten Tutorial-Auftrag in eine hörgerechte, kapitelstrukturierte Lernfassung und eine EPUB-Datei für TTS-Reader wie ElevenReader. Verwendet vor dem Rendering den vorhandenen Precision-Writing-Pfad, minimiert in deutschen Fassungen unnötige Anglizismen, verwendet für englische Fassungen amerikanisches Englisch und liefert eine passende Stimmenempfehlung oder einen Voice-Design-Prompt. Nicht verwenden, bevor Ziel, Zielgruppe, Tiefe, Stil und Ausgabeweg durch Grilling ausreichend geklärt sind.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/precision-writing-revision|precision-writing-revision]]
- [[skills/round-based-requirements-grilling|round-based-requirements-grilling]]
- [[skills/spoken-tutorial-listener-review|spoken-tutorial-listener-review]]

## Required by

- —

## Outputs

- `audio-tutorial-run.json`
- `spoken-tutorial.epub`
- `spoken-tutorial.md`
- `voice-guidance.md`

## Output consumers

### `audio-tutorial-run.json`

- Terminal or currently unconsumed output.

### `spoken-tutorial.epub`

- Terminal or currently unconsumed output.

### `spoken-tutorial.md`

- Terminal or currently unconsumed output.

### `voice-guidance.md`

- Terminal or currently unconsumed output.

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/audio-tutorial-workflow/SKILL.md`
