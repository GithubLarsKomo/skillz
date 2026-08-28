---
type: skill
generated: true
name: "document-layout-qa"
category: "internal"
userFacing: false
evaluationPassed: null
evaluationMode: "none"
caseCount: 0
recordedResultCount: 0
sourcePath: "skills/document-layout-qa/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# document-layout-qa

Prüft editierbare DOCX-Dokumente strukturell gegen ein dokumentiertes Template-Profil auf Seiten-/Section-Setup, Style-Drift, Tabellenbreiten, Bild-/Caption-Verankerung, Listen/Nummerierung, Header/Footer, Felder, Seitenumbrüche und typische Overflow-/Reflow-Risiken. Verwenden vor finalem Render; nicht als Ersatz für die visuelle PDF-Prüfung.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- [[skills/document-template-profiler|document-template-profiler]]

## Required by

- [[skills/document-render-verifier|document-render-verifier]]
- [[skills/template-document-workflow|template-document-workflow]]

## Outputs

- `document-layout-qa.json`
- `document-layout-qa.md`

## Output consumers

### `document-layout-qa.json`

- [[skills/document-render-verifier|document-render-verifier]]
- [[skills/template-document-workflow|template-document-workflow]]

### `document-layout-qa.md`

- [[skills/template-document-workflow|template-document-workflow]]

## Evaluation

- Mode: `none`
- Passed: `None`
- Cases: `0`
- Recorded results: `0`

## Canonical source

`skills/document-layout-qa/SKILL.md`
