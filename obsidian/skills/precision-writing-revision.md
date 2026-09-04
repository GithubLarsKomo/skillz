---
type: skill
generated: true
name: "precision-writing-revision"
category: "workflow"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/precision-writing-revision/SKILL.md"
tags:
  - skill
  - skill-category/workflow
---

# precision-writing-revision

Orchestriert die sprachgenaue Überarbeitung deutscher oder englischer Reports, Memos und Sachtexte durch Muster-Audit, optionales Author-Voice-Profil, Precision Rewrite und anschließende Fidelity-Prüfung. Verwenden, wenn ein vollständiger wiederholbarer Editierworkflow statt einer isolierten Umformulierung gewünscht ist.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/workflow|workflow]]

## Requires

- [[skills/author-voice-profiler|author-voice-profiler]]
- [[skills/llm-prose-pattern-audit|llm-prose-pattern-audit]]
- [[skills/precision-language-rewriter|precision-language-rewriter]]
- [[skills/rewrite-fidelity-verifier|rewrite-fidelity-verifier]]

## Required by

- [[skills/audio-tutorial-workflow|audio-tutorial-workflow]]
- [[skills/person-profile-document-delivery|person-profile-document-delivery]]
- [[skills/person-research-report-workflow|person-research-report-workflow]]

## Outputs

- `final-revised-text`
- `precision-writing-report.json`

## Output consumers

### `final-revised-text`

- [[skills/audio-tutorial-workflow|audio-tutorial-workflow]]
- [[skills/person-profile-document-delivery|person-profile-document-delivery]]
- [[skills/person-research-report-workflow|person-research-report-workflow]]

### `precision-writing-report.json`

- [[skills/audio-tutorial-workflow|audio-tutorial-workflow]]
- [[skills/person-profile-document-delivery|person-profile-document-delivery]]
- [[skills/person-research-report-workflow|person-research-report-workflow]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/precision-writing-revision/SKILL.md`
