---
type: skill
generated: true
name: "legal-matter-wayfinder"
category: "analysis"
userFacing: true
evaluationPassed: false
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 0
sourcePath: "skills/legal-matter-wayfinder/SKILL.md"
tags:
  - skill
  - skill-category/analysis
---

# legal-matter-wayfinder

Zerlegt komplexe Legal- und Compliance-Matters in priorisierte tatsächliche, rechtliche, wirtschaftliche und regulatorische Investigations mit Evidenzbedarf und Stop Conditions. Verwenden, wenn die nächste sichere Legal-Aktion durch mehrere unbekannte oder voneinander abhängige Fragen blockiert ist.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/analysis|analysis]]

## Requires

- [[skills/current-law-context|current-law-context]]
- [[skills/research-to-evidence-note|research-to-evidence-note]]

## Required by

- [[skills/legal-compliance-office|legal-compliance-office]]

## Outputs

- `legal-dependency-graph.json`
- `legal-investigation-backlog.json`
- `legal-wayfinding-brief.md`

## Output consumers

### `legal-dependency-graph.json`

- [[skills/legal-compliance-office|legal-compliance-office]]

### `legal-investigation-backlog.json`

- [[skills/legal-compliance-office|legal-compliance-office]]

### `legal-wayfinding-brief.md`

- [[skills/legal-compliance-office|legal-compliance-office]]

## Evaluation

- Mode: `compatibility`
- Passed: `False`
- Cases: `3`
- Recorded results: `0`

## Canonical source

`skills/legal-matter-wayfinder/SKILL.md`
