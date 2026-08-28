---
type: skill
generated: true
name: "procedure-sop-extractor"
category: "workflow"
userFacing: true
evaluationPassed: null
evaluationMode: "none"
caseCount: 0
recordedResultCount: 0
sourcePath: "skills/procedure-sop-extractor/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# procedure-sop-extractor

Rekonstruiert aus multimodaler Videoevidenz einen nachvollziehbaren Ablauf mit Zweck, Voraussetzungen, Materialien, Schritten, Kontrollpunkten, Warnungen, Akzeptanzkriterien und Troubleshooting und kennzeichnet jeden Punkt als observed, derived oder recommended. Verwenden für Anleitungen und SOP-Entwürfe aus Demonstrationsvideos; nicht zur Freigabe einer regulierten oder sicherheitskritischen Unternehmens-SOP ohne externe Validierung.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/multimodal-learning-analysis|multimodal-learning-analysis]]

## Required by

- [[skills/youtube-learning-workflow|youtube-learning-workflow]]

## Outputs

- `derived-procedure.json`
- `derived-sop.md`

## Output consumers

### `derived-procedure.json`

- [[skills/youtube-learning-workflow|youtube-learning-workflow]]

### `derived-sop.md`

- [[skills/youtube-learning-workflow|youtube-learning-workflow]]

## Evaluation

- Mode: `none`
- Passed: `None`
- Cases: `0`
- Recorded results: `0`

## Canonical source

`skills/procedure-sop-extractor/SKILL.md`
