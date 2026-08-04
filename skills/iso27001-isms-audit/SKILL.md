---
name: iso27001-isms-audit
description: Plant und bewertet ISO-27001-ISMS-Audits mit Scope-/SoA-Kontext, unabhängiger Control-Evidence und nachvollziehbarem Sampling, ohne Zertifiziererrolle oder universelle Sample-/Finding-Regeln zu erfinden.
userFacing: true
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires: 
  - medical-device-isms-governance
  - two-axis-compliance-review
outputs: 
  - isms-audit-plan.json
  - isms-audit-findings.json
  - isms-audit-report.md
lastEvaluated: 2026-08-04
---

# iso27001-isms-audit

## Zweck

Spezialisiert den gemeinsamen Compliance-Review-Kern für ISMS-Audits und hält Control Testing von ISMS-Governance und technischen Security-Tests getrennt.

## Trigger

Verwenden für interne ISO-27001-Audits, Stage-1/Stage-2-Readiness, Surveillance-/Recertification-Prep, SoA-/Control-Review oder Finding Follow-up.

## Gemeinsame Regulated-Engineering-Regeln

- Aussagen mit regulatorischer Wirkung trennen `regulation/law`, `standard`, `guidance`, `organizational-policy` und `interpretation`.
- Zeitabhängige regulatorische Fakten benötigen `asOf` und eine nachvollziehbare Source-Referenz; fehlt sie, bleibt der Punkt `unknown`.
- Volltexte urheberrechtlich geschützter Standards werden nicht reproduziert. Verwende zugängliche autoritative Quellen und organisationslizenzierte Normtexte nur als Evidenz.
- Fehlende Evidenz ist kein positiver Compliance-Nachweis.
- Bei High-Impact-Klassifikation, Zulassung, Zertifizierung, Freigabe oder Legal Interpretation wird die erforderliche menschliche/behördliche Autorität nicht simuliert.

## Fachregeln

- Audit Type, Scope, Criteria, SoA-Kontext, Auditor Independence und prior findings werden vor dem Plan fixiert.
- Sampling Method und Sample Size werden aus Population, Risk, Control Frequency, Change und Assurance Need begründet, nicht als universelle Tabelle übernommen.
- Control Design, Implementation und Operating Effectiveness werden getrennt bewertet.
- Finding Classification und Response Expectations folgen anwendbarer Methodik/Certification Context; der Skill erfindet keine Standardfristen.
- Re-performance oder technische Tests werden nur durchgeführt, wenn Toolzugang, Autorisierung und Safety-Grenzen dies erlauben; andernfalls Evidence Request.
- Product Cybersecurity Findings werden über definierte Interfaces an Product Risk/CAPA übergeben statt im ISMS-Audit gelöst.

## Workflow

1. Audit Type/Scope/Criteria/SoA/Independence bestimmen.
2. Risk-based Plan und Sample Rationale erstellen.
3. Design/Implementation/Operating Effectiveness evidenzbasiert testen.
4. Findings und Contradictions mit Provenance dokumentieren.
5. Corrective-Action-/Retest-Handoff planen.

## Wayfinder-kompatible Übergabe

Wenn der nächste sichere Schritt durch Unsicherheit blockiert ist, gib eine begrenzte Übergabe mit diesen Feldern aus: `facts, assumptions, hypotheses, unknowns, blockers, decisions, investigations, risks`. Investigations müssen eine einzelne Frage, benötigte Evidenz, Stop Condition und Nicht-Ziele enthalten.

## Compliance Traceability

Verknüpfe relevante Ergebnisse mit `compliance-traceability-v1` als `obligation -> product-requirement -> risk/rationale -> implementation/control -> verification -> evidence -> status`. Quellenbezogene regulatorische Claims folgen `regulatory-source-evidence-v1`.

## Grenzen

- Keine Zertifizierungsentscheidung.
- Keine universelle Sample Size oder Response Deadline.
- Keine unautorisierte technische Sicherheitsprüfung.

## Qualitätsgate

Pass nur, wenn Facts/Interpretations getrennt, Freshness sichtbar, zentrale Claims rückverfolgbar, Unknowns nicht positiv umgedeutet, Cross-Skill-Grenzen respektiert und die nächste Aktion ohne versteckte Regulatory-Annahme ausführbar ist.
