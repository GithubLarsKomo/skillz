---
type: skill
generated: true
name: "learning-artifact-qa"
category: "internal"
userFacing: false
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/learning-artifact-qa/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# learning-artifact-qa

Prüft HTML-, PPTX-, DOCX- und PDF-Lernartefakte sowie ihre SVG-/Bildassets gemeinsam gegen das kanonische Learning-Modell, Timestamp-/Claim-Traceability, SOP-Evidenzklassen, DESIGN.md und vollständige Render-Evidenz. Verwenden als finales Cross-Format-Gate; nicht als Ersatz für fachliche Quellanalyse.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- [[skills/learning-content-design-system|learning-content-design-system]]

## Required by

- [[skills/learning-delivery-workflow|learning-delivery-workflow]]

## Outputs

- `learning-artifact-qa.json`
- `learning-artifact-qa.md`

## Output consumers

### `learning-artifact-qa.json`

- [[skills/learning-delivery-workflow|learning-delivery-workflow]]

### `learning-artifact-qa.md`

- [[skills/learning-delivery-workflow|learning-delivery-workflow]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/learning-artifact-qa/SKILL.md`
