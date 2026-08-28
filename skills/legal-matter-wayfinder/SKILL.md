---
name: legal-matter-wayfinder
description: Zerlegt komplexe Legal- und Compliance-Matters in priorisierte tatsächliche, rechtliche, wirtschaftliche und regulatorische Investigations mit Evidenzbedarf und Stop Conditions. Verwenden, wenn die nächste sichere Legal-Aktion durch mehrere unbekannte oder voneinander abhängige Fragen blockiert ist.
userFacing: true
implicitInvocation: true
category: analysis
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - current-law-context
  - research-to-evidence-note
outputs:
  - legal-wayfinding-brief.md
  - legal-investigation-backlog.json
  - legal-dependency-graph.json
lastEvaluated: 2026-08-28
---

# Legal Matter Wayfinder

## Zweck

Finde bei großen Matters die kleinste Menge an Untersuchungen, die vor einer belastbaren Entscheidung wirklich nötig ist. Der Skill ist kein Engineering-Wayfinder und führt keine Fachsubsumtion an Stelle der Specialists durch.

## Investigations

Jede Investigation enthält:

- genau eine entscheidungsrelevante Frage,
- bekannte Facts und konkurrierende Hypothesen,
- benötigte Evidenz/Quelle,
- zuständigen Specialist oder Owner,
- Abhängigkeiten,
- `stopCondition`,
- Nicht-Ziele,
- Auswirkung auf die nächste Entscheidung.

## Priorisierung

Priorisiere nach Decision Criticality, Deadline, Irreversibilität, Exposure, Evidenzkosten und Abhängigkeiten. Recherche ohne absehbare Entscheidungswirkung wird zurückgestellt.

## Workflow

1. Open Questions aus Intake und Current Law Context konsolidieren.
2. Fragen nach Fact, Law, Rule Binding, Commercial, Regulatory, Technical und Authority klassifizieren.
3. Abhängigkeiten und Gate-Fragen bestimmen.
4. Minimal notwendige Investigations formulieren.
5. Specialist-/Research-Handoffs erzeugen.
6. Stoppen, sobald die nächste sichere Entscheidung möglich ist.

## Qualitätsgate

Pass nur, wenn jede Investigation eine einzelne Frage und Stop Condition besitzt und kein vollständiger Research-Rewrite ohne Entscheidungsbezug entsteht.