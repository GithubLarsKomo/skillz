---
type: skill
generated: true
name: "llm-generation-evidence-assessment"
category: "internal"
userFacing: false
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/llm-generation-evidence-assessment/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# llm-generation-evidence-assessment

Bewertet voneinander getrennte Sprach-, Provenienz-, Autorenprofil-, Struktur- und Inhaltsindikatoren darauf, wie stark sie eine LLM-Unterstützung eines Dokuments stützen oder relativieren, ohne unkalibrierte Detector-Scores in Autorschaftswahrscheinlichkeiten umzudeuten. Als Fach-Skill nach Artefaktforensik und Textmuster-Audit verwenden.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- [[skills/author-voice-profiler|author-voice-profiler]]
- [[skills/document-generation-forensics|document-generation-forensics]]
- [[skills/llm-prose-pattern-audit|llm-prose-pattern-audit]]

## Required by

- [[skills/llm-generation-review-workflow|llm-generation-review-workflow]]

## Outputs

- `llm-generation-assessment.json`
- `llm-generation-assessment.md`

## Output consumers

### `llm-generation-assessment.json`

- [[skills/llm-generation-review-workflow|llm-generation-review-workflow]]

### `llm-generation-assessment.md`

- [[skills/llm-generation-review-workflow|llm-generation-review-workflow]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/llm-generation-evidence-assessment/SKILL.md`
