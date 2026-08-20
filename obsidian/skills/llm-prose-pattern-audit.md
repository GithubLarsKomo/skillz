---
type: skill
generated: true
name: "llm-prose-pattern-audit"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/llm-prose-pattern-audit/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# llm-prose-pattern-audit

Prüft deutsche und englische Sachtexte auf redaktionell relevante Muster generischer LLM-Prosa wie Signifikanzinflation, Pseudoanalyse, rhetorische Templates, Synonymvariation, Hedging, Nominalstil und syntaktische Gleichförmigkeit, ohne daraus KI-Autorschaft zu behaupten. Verwenden vor sprachgenauer Überarbeitung oder zur Stil-Diagnose.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- —

## Required by

- [[skills/precision-writing-revision|precision-writing-revision]]

## Outputs

- `prose-audit.json`
- `prose-audit.md`

## Output consumers

### `prose-audit.json`

- [[skills/precision-writing-revision|precision-writing-revision]]

### `prose-audit.md`

- [[skills/precision-writing-revision|precision-writing-revision]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/llm-prose-pattern-audit/SKILL.md`
