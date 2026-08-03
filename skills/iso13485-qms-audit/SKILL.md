---
name: iso13485-qms-audit
description: Plant und bewertet risikobasierte ISO-13485-QMS-Audits mit unabhängiger Evidenz, nachvollziehbarem Sampling und findingspezifischer Traceability, ohne fixe Frequenzen, Samplegrößen oder Schweregrade als Norm zu erfinden.
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires: 
  - medical-device-qms-iso13485
  - two-axis-compliance-review
outputs: 
  - qms-audit-plan.json
  - qms-audit-findings.json
  - qms-audit-report.md
lastEvaluated: 2026-08-04
---

# iso13485-qms-audit

## Zweck

Spezialisiert den gemeinsamen Compliance-Review-Kern für QMS-Audits und hält Audit Evidence getrennt von CAPA Root Cause und Managemententscheidungen.

## Trigger

Verwenden für internes ISO-13485-Audit, Mock-/Certification-Readiness, Process Audit, Follow-up oder Finding Review.

## Gemeinsame Regulated-Engineering-Regeln

- Aussagen mit regulatorischer Wirkung trennen `regulation/law`, `standard`, `guidance`, `organizational-policy` und `interpretation`.
- Zeitabhängige regulatorische Fakten benötigen `asOf` und eine nachvollziehbare Source-Referenz; fehlt sie, bleibt der Punkt `unknown`.
- Volltexte urheberrechtlich geschützter Standards werden nicht reproduziert. Verwende zugängliche autoritative Quellen und organisationslizenzierte Normtexte nur als Evidenz.
- Fehlende Evidenz ist kein positiver Compliance-Nachweis.
- Bei High-Impact-Klassifikation, Zulassung, Zertifizierung, Freigabe oder Legal Interpretation wird die erforderliche menschliche/behördliche Autorität nicht simuliert.

## Fachregeln

- Audit Purpose, Scope, Criteria, Auditor Independence und asOf werden vor Evidenzsammlung fixiert.
- Audit Frequency und Sampling folgen Risiko, Prozessleistung, Änderungen, Previous Findings und organisationsdefinierter Auditmethodik; keine universelle Zahl wird erfunden.
- Jeder Finding-Kandidat trennt Requirement, Objective Evidence und Gap/Conclusion.
- Finding Classification wird gegen die anwendbare Audit-/Certification-/Organisationsmethodik begründet, nicht aus einer universellen Major/Minor-Tabelle.
- CAPA Root Cause wird nicht im Audit erfunden; Findings werden an medical-device-capa/evidence-based-causal-investigation übergeben.
- Missing evidence kann selbst ein Gap sein, aber fehlende Stichprobe beweist nicht automatisch Prozessversagen.

## Workflow

1. Audit Scope/Criteria/Independence und Risk Inputs bestimmen.
2. Audit Plan und evidenzbasierte Sample-Rationale erstellen.
3. Requirement Coverage und Evidence Effectiveness prüfen.
4. Findings mit Objective Evidence und Traceability dokumentieren.
5. Follow-up/CAPA-Verifikation und offene Evidence Requests planen.

## Wayfinder-kompatible Übergabe

Wenn der nächste sichere Schritt durch Unsicherheit blockiert ist, gib eine begrenzte Übergabe mit diesen Feldern aus: `facts, assumptions, hypotheses, unknowns, blockers, decisions, investigations, risks`. Investigations müssen eine einzelne Frage, benötigte Evidenz, Stop Condition und Nicht-Ziele enthalten.

## Compliance Traceability

Verknüpfe relevante Ergebnisse mit `compliance-traceability-v1` als `obligation -> product-requirement -> risk/rationale -> implementation/control -> verification -> evidence -> status`. Quellenbezogene regulatorische Claims folgen `regulatory-source-evidence-v1`.

## Grenzen

- Keine Zertifiziererentscheidung simulieren.
- Keine fixe jährliche/vierteljährliche Frequenz als Norm.
- Keine Root Cause aus dem Finding ableiten.

## Qualitätsgate

Pass nur, wenn Facts/Interpretations getrennt, Freshness sichtbar, zentrale Claims rückverfolgbar, Unknowns nicht positiv umgedeutet, Cross-Skill-Grenzen respektiert und die nächste Aktion ohne versteckte Regulatory-Annahme ausführbar ist.
