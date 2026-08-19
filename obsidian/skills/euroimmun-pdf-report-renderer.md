---
type: skill
generated: true
name: "euroimmun-pdf-report-renderer"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 4
recordedResultCount: 4
sourcePath: "skills/euroimmun-pdf-report-renderer/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# euroimmun-pdf-report-renderer

Erzeugt aus dem kanonischen EUROIMMUN-DOCX-Report ein professionelles PDF mit identischem Styling und aktuellem EUROIMMUN-From-Revvity-Kopf. Verwendet den DOCX-Renderer als einzige Layoutquelle, konvertiert ohne inhaltliches Re-Authoring und erzwingt eine visuelle PDF-Endkontrolle.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/euroimmun-docx-report-renderer|euroimmun-docx-report-renderer]]

## Required by

- —

## Outputs

- `euroimmun-report.pdf`

## Output consumers

### `euroimmun-report.pdf`

- Terminal or currently unconsumed output.

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `4`
- Recorded results: `4`

## Canonical source

`skills/euroimmun-pdf-report-renderer/SKILL.md`
