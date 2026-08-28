---
type: skill
generated: true
name: "legal-matter-final-gate"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/legal-matter-final-gate/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# legal-matter-final-gate

Prüft vor Abschluss, Unterzeichnung, Veröffentlichung oder irreversibler Legal-/Compliance-Aktion, ob Specialist-Fragen, aktuelle Rechtsgrundlage, Risiken, Freigaben und externe Authority-Gates ausreichend geklärt sind. Verwenden als letztes Matter-Gate; der Skill erteilt keine externe Genehmigung.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/legal-compliance-risk-assessment|legal-compliance-risk-assessment]]
- [[skills/privilege-and-counsel-routing|privilege-and-counsel-routing]]

## Required by

- [[skills/legal-compliance-office|legal-compliance-office]]

## Outputs

- `legal-final-gate.json`
- `legal-open-points.md`

## Output consumers

### `legal-final-gate.json`

- [[skills/legal-compliance-office|legal-compliance-office]]

### `legal-open-points.md`

- [[skills/legal-compliance-office|legal-compliance-office]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/legal-matter-final-gate/SKILL.md`
