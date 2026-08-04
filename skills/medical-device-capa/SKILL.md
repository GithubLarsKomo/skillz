---
name: medical-device-capa
description: Strukturiert CAPA von Signal/Problem Statement über evidenzbasierte Kausalinvestigation, Action Plan und Effectiveness Verification bis zur kontrollierten Closure und Rückkopplung in Risk/QMS.
userFacing: true
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires: 
  - evidence-based-causal-investigation
  - medical-device-risk-management-iso14971
  - medical-device-qms-iso13485
outputs: 
  - capa-plan.json
  - capa-effectiveness-plan.json
  - capa-status.md
lastEvaluated: 2026-08-04
---

# medical-device-capa

## Zweck

Verhindert schematische CAPA-Routinen und koppelt Root Cause, Actions, Effectiveness und Risk/QMS-Updates nachweisbar.

## Trigger

Verwenden für CAPA-Bewertung und -Planung nach Complaint, Nonconformity, Audit Finding, Trend, Supplier-/Process-/Product-Problem oder Post-Market Signal.

## Gemeinsame Regulated-Engineering-Regeln

- Aussagen mit regulatorischer Wirkung trennen `regulation/law`, `standard`, `guidance`, `organizational-policy` und `interpretation`.
- Zeitabhängige regulatorische Fakten benötigen `asOf` und eine nachvollziehbare Source-Referenz; fehlt sie, bleibt der Punkt `unknown`.
- Volltexte urheberrechtlich geschützter Standards werden nicht reproduziert. Verwende zugängliche autoritative Quellen und organisationslizenzierte Normtexte nur als Evidenz.
- Fehlende Evidenz ist kein positiver Compliance-Nachweis.
- Bei High-Impact-Klassifikation, Zulassung, Zertifizierung, Freigabe oder Legal Interpretation wird die erforderliche menschliche/behördliche Autorität nicht simuliert.

## Fachregeln

- CAPA-Notwendigkeit folgt anwendbaren regulatorischen/QMS-Kriterien und risikobasierter Bewertung; eine feste Wiederholungsanzahl ist keine universelle Regel.
- Containment, Correction, Corrective Action, Preventive/Systemic Action und Risk Control sind getrennte Action Types.
- Root Cause wird aus evidence-based-causal-investigation übernommen und bleibt unverified, wenn die Evidenz nicht genügt.
- Jede Action nennt Ursache/Risiko-Bezug, Owner-Status, Due-Date-Status, Preconditions und objektive Completion Evidence.
- Effectiveness Criteria und Beobachtungsfenster werden vor Closure definiert und müssen zur behaupteten Ursache passen.
- Closed wird nur bei bestätigter Implementierung, ausreichender Effectiveness Evidence und erforderlicher Risk/QMS/Document-Update-Evidenz ausgegeben.

## Workflow

1. Signal, Scope, Risiko und CAPA-Kriterien bestimmen.
2. Containment/Correction von systemischer Investigation trennen.
3. Verifizierte/ungeklärte Ursachen übernehmen.
4. Actions mit Traceability und Effectiveness Criteria planen.
5. Implementierungs- und Effectiveness Evidence prüfen.
6. Closure Readiness sowie Risk/QMS/Document-Feedback ausgeben.

## Wayfinder-kompatible Übergabe

Wenn der nächste sichere Schritt durch Unsicherheit blockiert ist, gib eine begrenzte Übergabe mit diesen Feldern aus: `facts, assumptions, hypotheses, unknowns, blockers, decisions, investigations, risks`. Investigations müssen eine einzelne Frage, benötigte Evidenz, Stop Condition und Nicht-Ziele enthalten.

## Compliance Traceability

Verknüpfe relevante Ergebnisse mit `compliance-traceability-v1` als `obligation -> product-requirement -> risk/rationale -> implementation/control -> verification -> evidence -> status`. Quellenbezogene regulatorische Claims folgen `regulatory-source-evidence-v1`.

## Grenzen

- Keine automatische Closure.
- Keine universelle 3x-Wiederholungsregel.
- Keine Person als Root Cause ohne Systemanalyse.

## Qualitätsgate

Pass nur, wenn Facts/Interpretations getrennt, Freshness sichtbar, zentrale Claims rückverfolgbar, Unknowns nicht positiv umgedeutet, Cross-Skill-Grenzen respektiert und die nächste Aktion ohne versteckte Regulatory-Annahme ausführbar ist.
