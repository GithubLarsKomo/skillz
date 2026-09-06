---
type: skill
generated: true
name: "epub3-publication-renderer"
category: "internal"
userFacing: false
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/epub3-publication-renderer/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# epub3-publication-renderer

Rendert einen finalen, kapitelstrukturierten Markdown-Text content-neutral als konservatives EPUB3 mit OPF-Spine, EPUB-Navigation, NCX-Kompatibilitätsnavigation, UTF-8, semantischen Absätzen und Scene Breaks und erzeugt eine strukturelle Validierungsnotiz. Interner Delivery-Worker; verändert keine Prosa und behauptet ohne Plattform-Smoke-Test keine verifizierte ElevenReader-Kompatibilität.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- —

## Required by

- [[skills/audio-tutorial-workflow|audio-tutorial-workflow]]
- [[skills/creative-writing-epub-delivery|creative-writing-epub-delivery]]

## Outputs

- `epub3-publication.epub`
- `epub3-validation.json`

## Output consumers

### `epub3-publication.epub`

- Terminal or currently unconsumed output.

### `epub3-validation.json`

- [[skills/audio-tutorial-workflow|audio-tutorial-workflow]]
- [[skills/creative-writing-epub-delivery|creative-writing-epub-delivery]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/epub3-publication-renderer/SKILL.md`
