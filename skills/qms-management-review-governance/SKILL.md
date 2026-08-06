---
name: qms-management-review-governance
description: Bereitet Medical-Device-/IVD-QMS-Management-Reviews aus bestätigten QMS-, Audit-, CAPA-, Complaint-, Risk-, Supplier- und Performance-Evidenzen vor und trennt Inputs, Decisions, Actions und offene Datenlücken.
userFacing: true
implicitInvocation: true
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires: 
  - medical-device-qms-iso13485
  - iso13485-qms-audit
  - medical-device-capa
  - project-status-brief
outputs: 
  - management-review-brief.json
  - management-review-actions.json
  - management-review-brief.md
lastEvaluated: 2026-08-04
---

# qms-management-review-governance

## Zweck

Ersetzt die breite QMR-Persona durch einen klaren Management-Review-/Governance-Skill, der keine operativen Subsysteme dupliziert.

## Trigger

Verwenden für QMS Management Review, Quality Objectives/KPI Review, prior action follow-up, resource/quality governance oder Executive QMS Decision Preparation.

## Gemeinsame Regulated-Engineering-Regeln

- Aussagen mit regulatorischer Wirkung trennen `regulation/law`, `standard`, `guidance`, `organizational-policy` und `interpretation`.
- Zeitabhängige regulatorische Fakten benötigen `asOf` und eine nachvollziehbare Source-Referenz; fehlt sie, bleibt der Punkt `unknown`.
- Volltexte urheberrechtlich geschützter Standards werden nicht reproduziert. Verwende zugängliche autoritative Quellen und organisationslizenzierte Normtexte nur als Evidenz.
- Fehlende Evidenz ist kein positiver Compliance-Nachweis.
- Bei High-Impact-Klassifikation, Zulassung, Zertifizierung, Freigabe oder Legal Interpretation wird die erforderliche menschliche/behördliche Autorität nicht simuliert.

## Fachregeln

- Required Review Inputs werden aus anwendbarem QMS/Regulatory Context und Organisationsverfahren bestimmt, nicht aus einer statischen universellen Agenda.
- Jeder Input trägt period/asOf, source, completeness und trendability; fehlende Daten bleiben dataGap.
- Quality KPIs benötigen Definition, Datenquelle, Owner, Zeitraum und Ziel-/Escalation-Kontext; keine generischen Benchmarktargets werden erfunden.
- Decisions needed, decisions made und follow-up actions bleiben getrennt; meeting preparation ist kein Entscheidungsnachweis.
- Actions übernehmen Owner/Due Date nur wenn bestätigt und bleiben pending bis externer Nachweis vorliegt.
- QMS Suitability/Adequacy/Effectiveness Conclusions müssen auf sichtbarer Evidence und offenen Gaps beruhen.

## Workflow

1. Review Scope/Period/Criteria bestimmen.
2. QMS-, Audit-, CAPA-, Complaint-, Risk-, Supplier-, Regulatory- und prior-action Inputs inventarisieren.
3. Completeness/Trends/Contradictions und Data Gaps bewerten.
4. Decision Needs, Resource/Improvement Topics und Quality Objective Changes vorbereiten.
5. Bestätigte Decisions/Actions getrennt dokumentieren und an Follow-up Tracking übergeben.

## Wayfinder-kompatible Übergabe

Wenn der nächste sichere Schritt durch Unsicherheit blockiert ist, gib eine begrenzte Übergabe mit diesen Feldern aus: `facts, assumptions, hypotheses, unknowns, blockers, decisions, investigations, risks`. Investigations müssen eine einzelne Frage, benötigte Evidenz, Stop Condition und Nicht-Ziele enthalten.

## Compliance Traceability

Verknüpfe relevante Ergebnisse mit `compliance-traceability-v1` als `obligation -> product-requirement -> risk/rationale -> implementation/control -> verification -> evidence -> status`. Quellenbezogene regulatorische Claims folgen `regulatory-source-evidence-v1`.

## Grenzen

- Keine Managemententscheidung erfinden.
- Keine generischen KPI-Zielwerte als Norm.
- Kein Ersatz für Audit, CAPA oder Regulatory Strategy.

## Qualitätsgate

Pass nur, wenn Facts/Interpretations getrennt, Freshness sichtbar, zentrale Claims rückverfolgbar, Unknowns nicht positiv umgedeutet, Cross-Skill-Grenzen respektiert und die nächste Aktion ohne versteckte Regulatory-Annahme ausführbar ist.
