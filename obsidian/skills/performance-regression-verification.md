---
type: skill
generated: true
name: "performance-regression-verification"
category: "engineering"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/performance-regression-verification/SKILL.md"
tags:
  - skill
  - skill-category/engineering
---

# performance-regression-verification

Verifiziert nach einer Software-Optimierung funktionale Gleichwertigkeit und messbare Performance-Verbesserung gegen eine unveränderte Baseline, bewertet Rauschen und Trade-offs und erzeugt dauerhafte Performance-Gates oder Regression-Guards, wenn sie stabil genug sind. Verwenden nach Implementierung eines Performance-TASK.md; nicht für reine Code-Ästhetik oder ungemessene Optimierungsbehauptungen.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/engineering|engineering]]

## Requires

- [[skills/performance-baseline|performance-baseline]]
- [[skills/test-driven-vertical-slice|test-driven-vertical-slice]]
- [[skills/two-axis-code-review|two-axis-code-review]]

## Required by

- [[skills/optimize-software-performance|optimize-software-performance]]

## Outputs

- `performance-regression-guard.md`
- `performance-result.json`
- `performance-result.md`

## Output consumers

### `performance-regression-guard.md`

- [[skills/optimize-software-performance|optimize-software-performance]]

### `performance-result.json`

- Ambiguous producer contract; no inferred consumer edge.

### `performance-result.md`

- [[skills/optimize-software-performance|optimize-software-performance]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/performance-regression-verification/SKILL.md`
