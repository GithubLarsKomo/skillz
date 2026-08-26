---
type: skill
generated: true
name: "rewrite-fidelity-verifier"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/rewrite-fidelity-verifier/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# rewrite-fidelity-verifier

Vergleicht Ausgangs- und überarbeiteten Sachtext auf fachliche und epistemische Treue, einschließlich Zahlen, Quellen, Terminologie, Negationen, Modalität, Bedingungen, Kausalität und Claims. Verwenden nach sprachlicher Überarbeitung, um stilistische Verbesserung von inhaltlicher Veränderung zu trennen.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- —

## Required by

- [[skills/precision-writing-revision|precision-writing-revision]]
- [[skills/presentation-language-rewriter|presentation-language-rewriter]]

## Outputs

- `fidelity-review.md`
- `rewrite-fidelity.json`

## Output consumers

### `fidelity-review.md`

- [[skills/precision-writing-revision|precision-writing-revision]]
- [[skills/presentation-language-rewriter|presentation-language-rewriter]]

### `rewrite-fidelity.json`

- [[skills/precision-writing-revision|precision-writing-revision]]
- [[skills/presentation-language-rewriter|presentation-language-rewriter]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/rewrite-fidelity-verifier/SKILL.md`
