---
type: skill
generated: true
name: "artifact-contract-normalizer"
category: "internal"
userFacing: false
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/artifact-contract-normalizer/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# artifact-contract-normalizer

Analysiert und normalisiert Skill-Artefaktverträge für eindeutige Producer-Ownership, explizite consumes-Beziehungen, Orchestrator-vs-Worker-Grenzen und sichere Compatibility-Referenzen. Verwenden intern bei Architekturrefactorings und Output-Ambiguitäten; keine Consumer- oder Producer-Beziehungen ohne Vertragsbeleg erfinden.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- [[skills/skill-portfolio-audit|skill-portfolio-audit]]

## Required by

- [[skills/workflow-benchmark-authoring|workflow-benchmark-authoring]]

## Outputs

- `artifact-contract-normalization.json`

## Output consumers

### `artifact-contract-normalization.json`

- [[skills/workflow-benchmark-authoring|workflow-benchmark-authoring]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/artifact-contract-normalizer/SKILL.md`
