---
type: skill
generated: true
name: "document-template-profiler"
category: "internal"
userFacing: false
evaluationPassed: null
evaluationMode: "none"
caseCount: 0
recordedResultCount: 0
sourcePath: "skills/document-template-profiler/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# document-template-profiler

Analysiert ein vorhandenes DOCX/DOTX-Template oder ein bestätigtes Referenzdokument und erzeugt ein wiederverwendbares, provenance-gebundenes Profil für Page Setup, Sections, Styles, Typografie, Header/Footer, Nummerierung, Tabellen, Felder, Content Controls und sichere Einfügepunkte. Verwenden vor template-treuer Dokumenterzeugung; nicht zum Erfinden eines Corporate Designs.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- —

## Required by

- [[skills/document-layout-qa|document-layout-qa]]
- [[skills/template-document-workflow|template-document-workflow]]

## Outputs

- `document-template-profile.json`
- `document-template-profile.md`

## Output consumers

### `document-template-profile.json`

- [[skills/document-layout-qa|document-layout-qa]]
- [[skills/template-document-workflow|template-document-workflow]]

### `document-template-profile.md`

- Terminal or currently unconsumed output.

## Evaluation

- Mode: `none`
- Passed: `None`
- Cases: `0`
- Recorded results: `0`

## Canonical source

`skills/document-template-profiler/SKILL.md`
