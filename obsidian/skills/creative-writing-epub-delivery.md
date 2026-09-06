---
type: skill
generated: true
name: "creative-writing-epub-delivery"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/creative-writing-epub-delivery/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# creative-writing-epub-delivery

Liefert final freigegebene Science-Storytelling- oder Fiction-Manuskripte als ElevenReader-orientiertes EPUB3 aus, nachdem ein narrativer Hörbuchnutzer-Review bestanden wurde, und erzeugt genrespezifische Voice Guidance. Verwendet den generischen EPUB3-Renderer content-neutral; tatsächliche ElevenReader-Import- und Voice-Performance werden ohne realen Plattformtest nicht behauptet.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/epub3-publication-renderer|epub3-publication-renderer]]
- [[skills/narrative-audiobook-listener-review|narrative-audiobook-listener-review]]

## Required by

- [[skills/creative-writing-workflow|creative-writing-workflow]]

## Outputs

- `creative-epub-delivery.json`
- `creative-voice-guidance.md`
- `creative-writing.epub`

## Output consumers

### `creative-epub-delivery.json`

- Terminal or currently unconsumed output.

### `creative-voice-guidance.md`

- Terminal or currently unconsumed output.

### `creative-writing.epub`

- Terminal or currently unconsumed output.

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/creative-writing-epub-delivery/SKILL.md`
