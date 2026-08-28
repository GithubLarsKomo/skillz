---
type: skill
generated: true
name: "privilege-and-counsel-routing"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/privilege-and-counsel-routing/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# privilege-and-counsel-routing

Bewertet für einen Legal Matter Schutz-, Vertraulichkeits- und Eskalationsbedarf, ohne pauschal anwaltliches Privileg zu behaupten, und routet Fragen nach interner Bearbeitung, qualifiziertem externem Counsel, Behörde, Notar oder sonstiger zwingender Autorität. Verwenden früh im Matter und erneut vor irreversiblen Rechtsentscheidungen.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/legal-matter-intake|legal-matter-intake]]

## Required by

- [[skills/legal-compliance-office|legal-compliance-office]]
- [[skills/legal-matter-final-gate|legal-matter-final-gate]]

## Outputs

- `counsel-scope.json`
- `external-counsel-brief.md`
- `privilege-routing.json`

## Output consumers

### `counsel-scope.json`

- [[skills/legal-compliance-office|legal-compliance-office]]
- [[skills/legal-matter-final-gate|legal-matter-final-gate]]

### `external-counsel-brief.md`

- [[skills/legal-compliance-office|legal-compliance-office]]
- [[skills/legal-matter-final-gate|legal-matter-final-gate]]

### `privilege-routing.json`

- [[skills/legal-compliance-office|legal-compliance-office]]
- [[skills/legal-matter-final-gate|legal-matter-final-gate]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/privilege-and-counsel-routing/SKILL.md`
