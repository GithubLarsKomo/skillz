---
type: skill
generated: true
name: "spoken-tutorial-listener-review"
category: "internal"
userFacing: false
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/spoken-tutorial-listener-review/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# spoken-tutorial-listener-review

Prüft eine hörgerecht redigierte Tutorial-Fassung aus der Perspektive eines anspruchsvollen regelmäßigen Hörbuch- und Podcastnutzers, der ohne Bildschirm zuhört. Bewertet Verständlichkeit, Hörermüdung, Rhythmus, Wiederholung, Wiedereinstieg, Aufzählungen, Informationsdichte und natürliche Sprache und gibt ein hartes Freigabe-Gate für Audio-Tutorials aus. Nicht als Fakten- oder Fachreview verwenden.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- —

## Required by

- [[skills/audio-tutorial-workflow|audio-tutorial-workflow]]

## Outputs

- `spoken-tutorial-listener-review.json`
- `spoken-tutorial-listener-review.md`

## Output consumers

### `spoken-tutorial-listener-review.json`

- [[skills/audio-tutorial-workflow|audio-tutorial-workflow]]

### `spoken-tutorial-listener-review.md`

- [[skills/audio-tutorial-workflow|audio-tutorial-workflow]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/spoken-tutorial-listener-review/SKILL.md`
