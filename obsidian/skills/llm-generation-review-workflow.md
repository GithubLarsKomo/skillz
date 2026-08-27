---
type: skill
generated: true
name: "llm-generation-review-workflow"
category: "analysis"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/llm-generation-review-workflow/SKILL.md"
tags:
  - skill
  - skill-category/analysis
---

# llm-generation-review-workflow

Orchestriert eine evidenzbasierte Prüfung von Text, DOCX, PDF, XLSX und PPTX auf Hinweise einer LLM-/GenAI-Beteiligung durch Dateiforensik, LLM-Prosa-Musteranalyse, optionalen Author-Voice-Vergleich, formatbezogene Inhaltsprüfung und konservative Evidenzsynthese. Verwenden bei Fragen wie „Ist das KI-generiert?“, „Prüfe dieses Dokument auf ChatGPT/LLM“ oder bei dokumentierter Herkunftsprüfung; keine binäre Detector-Gewissheit behaupten.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/analysis|analysis]]

## Requires

- [[skills/author-voice-profiler|author-voice-profiler]]
- [[skills/document-generation-forensics|document-generation-forensics]]
- [[skills/llm-generation-evidence-assessment|llm-generation-evidence-assessment]]
- [[skills/llm-prose-pattern-audit|llm-prose-pattern-audit]]

## Required by

- —

## Outputs

- `llm-generation-review.json`
- `llm-generation-review.md`

## Output consumers

### `llm-generation-review.json`

- Terminal or currently unconsumed output.

### `llm-generation-review.md`

- Terminal or currently unconsumed output.

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/llm-generation-review-workflow/SKILL.md`
