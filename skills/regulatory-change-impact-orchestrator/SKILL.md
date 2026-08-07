---
name: regulatory-change-impact-orchestrator
description: Orchestriert bestätigte Regulatory-/Lifecycle-Change-Events über Design, Risk, V&V, QMS, Evidence, Labeling, PMS und Markt-Spezialisten, ohne deren Fachentscheidungen zu duplizieren.
userFacing: true
implicitInvocation: true
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - regulated-product-context
  - regulatory-evidence-traceability
  - decision-record
outputs:
  - regulatory-change-route-map.json
  - lifecycle-impact-gates.json
  - change-integration-status.json
lastEvaluated: 2026-08-07
---

# Regulatory Change Impact Orchestrator

## Zweck und Grenze

Dieser Skill koordiniert bestätigte Regulatory-/Lifecycle-Change-Events über bestehende Fach-Skills. Er normalisiert das Ereignis, identifiziert betroffene Lifecycle-Domains, erzeugt Routing-Aufträge, sammelt die resultierenden Fachentscheidungen und macht offene Gates sichtbar.

Er ist **kein** zweiter Design-Change-, Risk-, QMS-, PMS-, Clinical-/Performance- oder Submission-Assessor. Eine fachliche Entscheidung bleibt beim jeweiligen Owner-Skill; der Orchestrator darf sie weder vorwegnehmen noch umformulieren, um ein gewünschtes Release-Ergebnis zu erzeugen.

## Kernprinzipien

- **Router, not assessor:** der Skill besitzt Routing- und Integrationslogik, keine zweite Fachbewertung.
- **Event before routing:** Art, Quelle, Baseline, Zeitpunkt, betroffene Produkte/Märkte und Evidence müssen vor dem Routing ausreichend fixiert sein.
- **Specialist ownership is preserved:** jede Design-, Risk-, V&V-, QMS-, Evidence-, Labeling-, PMS- oder marktbezogene Entscheidung bleibt bei ihrem Fach-Skill.
- **Evidence-only events are valid change events:** neue externe Evidenz, Guidance oder Post-Market-Signale können Lifecycle-Impact auslösen, ohne dass bereits eine technische Produktänderung existiert.
- **Gate aggregation is not gate closure:** der Orchestrator zeigt Status und Blocker; er schließt kein Gate nur durch Routing oder Dokumentation.
- **Markets stay separate:** FDA-, EU-/IVDR-/MDR- und andere Marktentscheidungen werden nicht zu einer universellen Regulatory Decision verdichtet.

## Workflow

### 1. Change Event normalisieren

Erfasse Event ID, Quelle, `asOf`, Current Baseline, Proposed/Observed Delta, betroffene Produkte/Varianten, Märkte, Timing, bekannte Evidence und Unknowns. Event-Typ mindestens `design-or-product-change|supplier-or-process-change|software-or-cyber-change|label-or-claim-change|new-clinical-evidence|pms-signal|regulatory-or-guidance-change|other|uncertain`.

### 2. Lifecycle-Domains klassifizieren

Bestimme nur den Routing-Bedarf:

- technische Design-/Produktänderung → `design-change-regulatory-impact`
- Risk-Frage → `medical-device-risk-management-iso14971`
- Software-Lifecycle → `iec62304-software-lifecycle`
- Cybersecurity → `medical-device-cybersecurity-lifecycle`
- Usability → `iec62366-usability-engineering`
- Supplier/Process/QMS → passende Supplier-/Process-Validation-/QMS-Skills
- neue klinische/wissenschaftliche Evidenz → `clinical-evidence-update-impact`
- Performance Evaluation → bestehende IVDR-/Clinical-Performance-Skills
- Label/Claim → `medical-device-labeling-ifu` / `regulatory-claims-consistency`
- PMS/Postmarket → `medical-device-pms-system` plus marktbezogene Vigilance-/Complaint-/Field-Action-Skills
- aktuelle regulatorische Änderung → EU/FDA Front Door, MDCG-/Guidance-Navigator oder zuständiger Regulatory-Spezialist.

Ein Domain-Routing ist noch keine Impact-Entscheidung.

### 3. Specialist Work Orders erzeugen

Für jeden benötigten Fach-Skill dokumentiere Input References, konkrete Frage, benötigte Baseline/Evidence, Dringlichkeit, Owner und erwarteten Output. Kopiere keine vollständigen Quelldokumente in den Routing-Record.

### 4. Fachentscheidungen integrieren

Verknüpfe die tatsächlichen Outputs der Spezialisten über stabile References. Übernimm Decision State, Evidence, Rationale, Gaps und Re-evaluation Trigger, ohne die Fachentscheidung neu zu interpretieren.

### 5. Lifecycle Gates aggregieren

Führe pro Gate `satisfied|open|blocked|external-pending|not-applicable|unknown`. Gates können Design/V&V, Risk, QMS, Supplier/Process, Clinical/Performance, Labeling, PMS, Regulatory Submission/Notification und externe Human-/Authority-Schritte umfassen.

Ein Gate ist nur `satisfied`, wenn der zuständige Owner nachvollziehbare Completion Evidence liefert.

### 6. Cross-market und Release Status bilden

`change-integration-status.json` zeigt je Produkt/Markt offene Decisions, Blocker, externe Abhängigkeiten und Next Actions. Der Orchestrator gibt **keine** universelle Freigabeentscheidung aus und simuliert weder FDA-, NB- noch Authority-Akzeptanz.

### 7. Re-evaluation Trigger definieren

Trigger umfassen neue Evidenz, geänderte Change-Baseline, neue Risk-/PMS-Signale, Guidance-/Regeländerungen, fehlgeschlagene V&V, Supplier-/Process-Abweichungen oder externe Regulatory Feedbacks.

## Output-Verträge

`regulatory-change-route-map.json` enthält Event/Baseline, Domain Classification, Specialist Work Orders, Input/Output References, Owner, Priority und `asOf`.

`lifecycle-impact-gates.json` enthält Gate, zuständigen Fach-Owner, State, Completion Evidence, Blocker, External Dependency und Re-evaluation Trigger.

`change-integration-status.json` enthält pro Produkt/Markt die integrierten Specialist Decisions, offene Gaps, Release-/Market Constraints und Next Actions, ohne selbst Regulatory Approval zu behaupten.

## Memory Path

Persistenzwürdig sind validierte Routing-Heuristiken, stabile produktfamilienbezogene Lifecycle-Dependency-Muster und wiederverwendbare Gate-Strukturen. Konkrete unreleased Changes, aktuelle Design-/Risk-/V&V-Ergebnisse, Submission-/NB-/Authority-States, momentane Guidance-Snapshots und offene Blocker bleiben run-only bzw. Project/Quality/Decision Records. Regulatory Memory Candidates benötigen `sourceRefs`, `asOf` und `reviewAfter`; übergib ausschließlich abstrahierte `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`.

## Qualitätsgate

Bestanden nur wenn:

- Change Event und Baseline ausreichend fixiert oder Unknowns explizit sind,
- Routing und Fachentscheidung klar getrennt bleiben,
- Specialist ownership für alle betroffenen Domains erhalten bleibt,
- Evidence-only Events nicht künstlich als Design Change umgedeutet werden,
- offene Gates nicht durch Routing als geschlossen erscheinen,
- Marktentscheidungen separat bleiben,
- externe Regulatory/Authority States nicht simuliert werden,
- konkrete Change-/Submission-/Design-Zustände nicht in globales dauerhaftes Memory gelangen.
