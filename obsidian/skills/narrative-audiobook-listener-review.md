---
type: skill
generated: true
name: "narrative-audiobook-listener-review"
category: "internal"
userFacing: false
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/narrative-audiobook-listener-review/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# narrative-audiobook-listener-review

Prüft finale narrative Prosa aus der Perspektive eines anspruchsvollen Hörbuchnutzers ohne Bildschirm auf Verständlichkeit, Figuren-/POV-Orientierung, Dialogzuordnung, Rhythmus, Hörermüdung, Kapitelwiedereinstieg und TTS-Robustheit, ohne literarische Eigenart in Tutorial-Sprache umzuschreiben. Verwenden als Gate vor Creative-Writing-EPUB-Ausgabe; nicht als Fakten-, Canon- oder Voice-Audio-Performance-Review.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- —

## Required by

- [[skills/creative-writing-epub-delivery|creative-writing-epub-delivery]]

## Outputs

- `narrative-listener-review.json`
- `narrative-listener-review.md`

## Output consumers

### `narrative-listener-review.json`

- [[skills/creative-writing-epub-delivery|creative-writing-epub-delivery]]

### `narrative-listener-review.md`

- Terminal or currently unconsumed output.

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/narrative-audiobook-listener-review/SKILL.md`
