---
type: skill
generated: true
name: "author-voice-profiler"
category: "communication-memory"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/author-voice-profiler/SKILL.md"
tags:
  - skill
  - skill-category/communication-memory
---

# author-voice-profiler

Extrahiert aus authentischen deutschen oder englischen Referenztexten ein beobachtbares, genrebezogenes Author-Voice-Profil für spätere Textüberarbeitung, ohne psychologische Eigenschaften zu erfinden oder Rohkorpora unnötig zu persistieren. Verwenden, wenn ein Rewriter reproduzierbar näher an einer bestätigten persönlichen Schreibweise arbeiten soll.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/communication-memory|communication-memory]]

## Requires

- —

## Required by

- [[skills/llm-generation-evidence-assessment|llm-generation-evidence-assessment]]
- [[skills/llm-generation-review-workflow|llm-generation-review-workflow]]
- [[skills/precision-writing-revision|precision-writing-revision]]

## Outputs

- `author-voice-profile.json`
- `author-voice-profile.md`

## Output consumers

### `author-voice-profile.json`

- [[skills/llm-generation-evidence-assessment|llm-generation-evidence-assessment]]
- [[skills/llm-generation-review-workflow|llm-generation-review-workflow]]
- [[skills/precision-writing-revision|precision-writing-revision]]

### `author-voice-profile.md`

- [[skills/llm-generation-evidence-assessment|llm-generation-evidence-assessment]]
- [[skills/llm-generation-review-workflow|llm-generation-review-workflow]]
- [[skills/precision-writing-revision|precision-writing-revision]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/author-voice-profiler/SKILL.md`
