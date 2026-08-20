---
type: skill
generated: true
name: "round-based-requirements-grilling"
category: "internal"
userFacing: false
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/round-based-requirements-grilling/SKILL.md"
tags:
  - skill
  - skill-category/internal
---

# round-based-requirements-grilling

Führt Requirements Engineering als datengetriebenen, rundenbasierten Grilling-Prozess durch. Die konkrete Grilling-Engine, Runtime, Authentifizierung, Statuslogik, Rundensemantik und Deploymentregeln werden ausschließlich aus dem aktuellen main-Stand von GithubLarsKomo/grilling bezogen. Grilling klärt fachliche Entscheidungen; die normative SPEC.md wird anschließend durch conversation-to-spec erzeugt.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/internal|internal]]

## Requires

- —

## Required by

- [[skills/role-requirements-grilling|role-requirements-grilling]]

## Outputs

- `GRILL-REPORT.md`
- `requirements-handoff.json`

## Output consumers

### `GRILL-REPORT.md`

- [[skills/role-requirements-grilling|role-requirements-grilling]]

### `requirements-handoff.json`

- [[skills/role-requirements-grilling|role-requirements-grilling]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/round-based-requirements-grilling/SKILL.md`
