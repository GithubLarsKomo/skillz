---
type: skill
generated: true
name: "workflow-benchmark-authoring"
category: "internal"
userFacing: false
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/workflow-benchmark-authoring/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# workflow-benchmark-authoring

Erstellt ausführbare, domänenübergreifende Workflow-Benchmarks aus kanonischen Skill-Orchestratoren, Dependency Closure, Artifact Ownership, Lifecycle/Discoverability und Evaluationsevidenz. Verwenden als internen Governance-Worker, wenn neue End-to-End-Architekturpfade als versionierte Regression Contracts abgesichert werden sollen.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- [[skills/artifact-contract-normalizer|artifact-contract-normalizer]]
- [[skills/skill-evaluation-suite-authoring|skill-evaluation-suite-authoring]]

## Required by

- —

## Outputs

- `workflow-benchmark-authoring-report.md`
- `workflow-benchmark-regression.py`
- `workflow-benchmark-spec.json`

## Output consumers

### `workflow-benchmark-authoring-report.md`

- Terminal or currently unconsumed output.

### `workflow-benchmark-regression.py`

- Terminal or currently unconsumed output.

### `workflow-benchmark-spec.json`

- Terminal or currently unconsumed output.

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/workflow-benchmark-authoring/SKILL.md`
