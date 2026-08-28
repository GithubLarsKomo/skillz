---
type: skill
generated: true
name: "template-document-workflow"
category: "workflow"
userFacing: true
evaluationPassed: null
evaluationMode: "none"
caseCount: 0
recordedResultCount: 0
sourcePath: "skills/template-document-workflow/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# template-document-workflow

Orchestriert die Erstellung oder Überarbeitung editierbarer DOCX-Dokumente auf Basis eines vorhandenen Word-Templates oder einer bestätigten Referenz, bewahrt fachlich finalisierten Inhalt, wendet Template-/Designregeln an und erzwingt strukturelle DOCX- sowie seitenweise DOCX/PDF-Render-QA. Verwenden für template-basierte Reports, Memos, Handouts und professionelle Dokumente; Corporate-Spezialregeln bleiben in dünnen Wrappern.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/document-layout-qa|document-layout-qa]]
- [[skills/document-render-verifier|document-render-verifier]]
- [[skills/document-template-profiler|document-template-profiler]]

## Required by

- —

## Outputs

- `document-delivery-manifest.json`
- `document-qa.md`
- `document.docx`
- `document.pdf`

## Output consumers

### `document-delivery-manifest.json`

- Terminal or currently unconsumed output.

### `document-qa.md`

- Terminal or currently unconsumed output.

### `document.docx`

- Terminal or currently unconsumed output.

### `document.pdf`

- Terminal or currently unconsumed output.

## Evaluation

- Mode: `none`
- Passed: `None`
- Cases: `0`
- Recorded results: `0`

## Canonical source

`skills/template-document-workflow/SKILL.md`
