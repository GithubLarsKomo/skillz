---
type: skill
generated: true
name: "document-render-verifier"
category: "internal"
userFacing: false
evaluationPassed: null
evaluationMode: "none"
caseCount: 0
recordedResultCount: 0
sourcePath: "skills/document-render-verifier/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# document-render-verifier

Rendert ein DOCX und die daraus erzeugte PDF-Version seitenweise und verifiziert sichtbare Parität, Clipping, Font-/Glyph-Substitution, Tabellen-/Bild-Reflow, Seitenumbrüche, Header/Footer, Felder und Druckstabilität. Verwenden nach struktureller Dokument-QA als finales visuelles Gate; nicht als Ersatz für editierbare DOCX-Prüfung.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- [[skills/document-layout-qa|document-layout-qa]]

## Required by

- —

## Outputs

- `document-preview.pdf`
- `document-render-qa.json`
- `document-render-qa.md`

## Output consumers

### `document-preview.pdf`

- Terminal or currently unconsumed output.

### `document-render-qa.json`

- Terminal or currently unconsumed output.

### `document-render-qa.md`

- Terminal or currently unconsumed output.

## Evaluation

- Mode: `none`
- Passed: `None`
- Cases: `0`
- Recorded results: `0`

## Canonical source

`skills/document-render-verifier/SKILL.md`
