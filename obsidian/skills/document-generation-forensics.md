---
type: skill
generated: true
name: "document-generation-forensics"
category: "internal"
userFacing: false
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/document-generation-forensics/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# document-generation-forensics

Extrahiert reproduzierbare Provenienz-, Metadaten- und Strukturhinweise aus Text-, DOCX-, PDF-, XLSX- und PPTX-Artefakten, ohne aus Dateieigenschaften allein LLM-Autorschaft abzuleiten. Als Fach-Skill für LLM-Generierungsprüfungen verwenden, wenn Dateiherkunft, Generator-Tooling, Revisionen oder formatbezogene Spuren getrennt von Sprachmustern erhoben werden müssen.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- —

## Required by

- [[skills/llm-generation-evidence-assessment|llm-generation-evidence-assessment]]
- [[skills/llm-generation-review-workflow|llm-generation-review-workflow]]

## Outputs

- `document-forensics.json`
- `document-forensics.md`

## Output consumers

### `document-forensics.json`

- [[skills/llm-generation-evidence-assessment|llm-generation-evidence-assessment]]
- [[skills/llm-generation-review-workflow|llm-generation-review-workflow]]

### `document-forensics.md`

- [[skills/llm-generation-evidence-assessment|llm-generation-evidence-assessment]]
- [[skills/llm-generation-review-workflow|llm-generation-review-workflow]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/document-generation-forensics/SKILL.md`
