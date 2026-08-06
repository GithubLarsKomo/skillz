---
name: medical-device-regulatory-strategy
description: Orchestriert evidenzbasierte Multi-Market-Regulatory-Strategie für Medical Devices und IVDs aus bestätigtem Produktkontext und spezialisierten EU/FDA-Assessments, ohne deren Fachanalyse oder Wayfinder zu duplizieren.
userFacing: true
implicitInvocation: true
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires: 
  - regulated-product-context
  - eu-mdr-ivdr-regulatory-specialist
  - fda-medical-device-ivd-regulatory-specialist
  - medical-device-risk-management-iso14971
  - large-work-wayfinder
outputs: 
  - regulatory-strategy.json
  - regulatory-strategy.md
  - regulatory-wayfinding-handoff.json
lastEvaluated: 2026-08-04
---

# medical-device-regulatory-strategy

## Zweck

Ersetzt eine breite Head-of-RA-Persona durch einen dünnen strategischen Orchestrator für Markets, Sequencing, Evidence Reuse, Dependencies, Decisions und Investigations.

## Trigger

Verwenden für regulatorische Gesamtstrategie über mehrere Märkte, Market Sequencing, Submission-/Evidence Roadmap, cross-functional Regulatory Dependencies oder Executive Regulatory Decision Preparation.

## Gemeinsame Regulated-Engineering-Regeln

- Aussagen mit regulatorischer Wirkung trennen `regulation/law`, `standard`, `guidance`, `organizational-policy` und `interpretation`.
- Zeitabhängige regulatorische Fakten benötigen `asOf` und eine nachvollziehbare Source-Referenz; fehlt sie, bleibt der Punkt `unknown`.
- Volltexte urheberrechtlich geschützter Standards werden nicht reproduziert. Verwende zugängliche autoritative Quellen und organisationslizenzierte Normtexte nur als Evidenz.
- Fehlende Evidenz ist kein positiver Compliance-Nachweis.
- Bei High-Impact-Klassifikation, Zulassung, Zertifizierung, Freigabe oder Legal Interpretation wird die erforderliche menschliche/behördliche Autorität nicht simuliert.

## Fachregeln

- Der Skill konsumiert Specialist Assessments; er klassifiziert MDR/IVDR/FDA nicht noch einmal unabhängig.
- Market Priorities, Sequencing, Evidence Reuse, Dependencies, Resource Needs und Irreversible Decisions werden explizit getrennt.
- Fees, Authority Review Times, Guidance-Versionen, NB Capacity und Übergangsregeln sind volatile Planning Inputs und benötigen aktuelles asOf/Source Evidence.
- Strategieoptionen enthalten Preconditions, Regulatory Risk, Evidence Gaps, Reversibility und Decision Owner/Authority Status.
- Bei kritischer Unsicherheit wird ein begrenztes Investigation Backlog an large-work-wayfinder übergeben statt eine scheinpräzise Roadmap erfunden.
- Approval/Clearance/CE/Submission Accepted werden nur aus externer bestätigter Evidenz als Status übernommen.

## Workflow

1. Produktkontext und Zielmärkte fixieren.
2. EU/FDA/weitere bestätigte Specialist Assessments konsolidieren.
3. Evidence Reuse, kritische Pfade, QMS/Risk/Clinical-Performance/Technical-Documentation Dependencies modellieren.
4. Strategieoptionen und Decision Points mit Freshness/Risiko vergleichen.
5. Wayfinder-Investigations für ungelöste kritische Unsicherheit erzeugen.
6. Executive Strategy und nächste sichere Aktion ausgeben.

## Wayfinder-kompatible Übergabe

Wenn der nächste sichere Schritt durch Unsicherheit blockiert ist, gib eine begrenzte Übergabe mit diesen Feldern aus: `facts, assumptions, hypotheses, unknowns, blockers, decisions, investigations, risks`. Investigations müssen eine einzelne Frage, benötigte Evidenz, Stop Condition und Nicht-Ziele enthalten.

## Compliance Traceability

Verknüpfe relevante Ergebnisse mit `compliance-traceability-v1` als `obligation -> product-requirement -> risk/rationale -> implementation/control -> verification -> evidence -> status`. Quellenbezogene regulatorische Claims folgen `regulatory-source-evidence-v1`.

## Grenzen

- Keine zweite Specialist-Klassifikation.
- Keine statischen Kosten/Reviewzeiten.
- Keine behauptete Regulatory Approval ohne Authority Evidence.

## Qualitätsgate

Pass nur, wenn Facts/Interpretations getrennt, Freshness sichtbar, zentrale Claims rückverfolgbar, Unknowns nicht positiv umgedeutet, Cross-Skill-Grenzen respektiert und die nächste Aktion ohne versteckte Regulatory-Annahme ausführbar ist.

## Memory Path

At completion, extract only confirmed, reusable, non-sensitive learnings that remain useful beyond the current run. Current task state, open follow-ups, tool snapshots, speculative hypotheses, secrets, sensitive personal data and raw connector payloads remain run-only. Encode eligible candidates using `memory-candidate-handoff-v1` from `docs/MEMORY-PATH-CONTRACT.md`, preserve provenance and freshness, and pass the ephemeral handoff to `communication-memory-governance`. The producing skill does not persist memory and never claims persistence succeeded without confirmation from the memory layer.

