---
type: skill
generated: true
name: "document-render-verifier"
category: "internal"
userFacing: false
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
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

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/document-render-verifier/SKILL.md`
