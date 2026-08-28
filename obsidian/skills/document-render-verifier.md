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

- [[skills/template-document-workflow|template-document-workflow]]

## Outputs

- `document-preview.pdf`
- `document-render-qa.json`
- `document-render-qa.md`

## Output consumers

### `document-preview.pdf`

- [[skills/template-document-workflow|template-document-workflow]]

### `document-render-qa.json`

- [[skills/template-document-workflow|template-document-workflow]]

### `document-render-qa.md`

- [[skills/template-document-workflow|template-document-workflow]]

## Evaluation

- Mode: `none`
- Passed: `None`
- Cases: `0`
- Recorded results: `0`

## Canonical source

`skills/document-render-verifier/SKILL.md`
