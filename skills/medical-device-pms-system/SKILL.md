---
name: medical-device-pms-system
description: Steuert ein marktübergreifendes Medical-Device-PMS-System aus Plan, Datenquellen, Review-Zyklen, Signalrouting und Lifecycle-Rückkopplung, ohne Vigilance, Complaint, CAPA oder PMPF zu duplizieren.
userFacing: true
implicitInvocation: true
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - regulated-product-context
  - medical-device-risk-management-iso14971
  - regulatory-evidence-traceability
  - decision-record
outputs:
  - pms-system-plan.json
  - pms-source-register.json
  - pms-review-status.json
lastEvaluated: 2026-08-07
---

# Medical Device PMS System

## Zweck und Grenze

Dieser Skill steuert das Post-Market-Surveillance-System eines Medical Device oder IVD über Märkte hinweg. Er verbindet PMS-Planung, Datenquellen, Review-Zyklen, Signal-/Trend-Intake und Lifecycle-Routing zu einem nachvollziehbaren Systemzustand.

Er ist **kein** Complaint-Handling-, Vigilance-/MDR-Reportability-, CAPA-, Recall/Correction-, PMPF/PMCF- oder Risk-Management-Skill. Fallbezogene oder marktbezogene Entscheidungen bleiben bei den vorhandenen Spezialisten. PMS aggregiert und routet Evidence; es ersetzt deren Fachlogik nicht.

## Kernprinzipien

- **System, not case processor:** PMS besitzt Plan, Source Coverage, Review und Routing; einzelne Fälle bleiben bei Complaint/Vigilance/Field-Action-Ownern.
- **Risk- and evidence-driven planning:** Sources, Frequenzen und Review-Trigger werden aus Product Context, Risk, Claims, Performance und Marktpflichten abgeleitet, nicht aus einer statischen Checkliste.
- **Source completeness before trend claims:** Datenherkunft, Coverage, Denominator und Zeitbezug werden geprüft, bevor ein Trend oder Signal behauptet wird.
- **A count is not a rate:** steigende absolute Fallzahlen sind ohne Exposure-/Denominator-/Coverage-Kontext nicht automatisch ein statistischer Trend.
- **Market-specific reportability stays specialist-owned:** EU-/IVDR-Vigilance, FDA MDR/806 oder andere Marktentscheidungen werden nicht vom PMS-System selbst getroffen.
- **PMS closes the lifecycle loop:** relevante Signale müssen Risk, Performance/Clinical Evidence, Labeling/Claims, CAPA, Change Impact oder Regulatory Strategy erreichen.

## Current-source discipline

Resolve aktuelle regulatorische PMS-/Vigilance-Anforderungen pro Markt bei jedem wesentlichen Scope-/Plan-Review. Für EU MDR/IVDR ist als Stand 2026-08-07 insbesondere die aktuelle MDCG-PMS-Guidance einschließlich MDCG 2025-10 relevant; Versionen, Forms, Fristen und marktbezogene Detailregeln werden jedoch nicht als zeitloses Wissen konserviert. Für FDA wird der aktuelle Total-Product-Lifecycle-/Postmarket-/QMS-Kontext verwendet; konkrete Reportability bleibt bei den FDA-Spezialisten.

## Workflow

### 1. PMS Scope fixieren

Erfasse Produkt/Produktfamilie, Varianten/Baselines, Intended Use, Claims, Risikoprofil, Märkte, Lifecycle State, PMS-Verantwortung und `asOf`. Marktpflichten werden separat geführt.

### 2. PMS Source Architecture aufbauen

Führe relevante Datenquellen mit Owner, Provenance, Coverage, Periodizität/Event Trigger, Denominator/Exposure soweit anwendbar und Data-Quality-State. Typische Quellen können umfassen:

- Complaints/Feedback,
- Service/Returns/Repairs,
- Distributor-/Importer-/Field Feedback,
- Nonconformity/CAPA,
- Vigilance/MDR/Field Actions/Recalls,
- Literatur und neue externe Evidenz,
- PMPF/PMCF bzw. gezielte Follow-up-Aktivitäten,
- Cybersecurity/Vulnerability Information,
- Production-/Process-/Supplier Quality,
- Register/RWE/Market Data soweit geeignet.

Eine Source im Register ist noch kein Signal.

### 3. Review- und Decision Rules definieren

Definiere pro Source bzw. aggregiert Review-Cadence/Event Trigger, Baseline, mögliche Signalindikatoren, Data-Quality-Prüfung, Escalation Owner und Re-evaluation Trigger. Schwellenwerte werden nur verwendet, wenn fachlich/statistisch/regulatorisch begründet; der Skill erfindet keine universellen Complaint-Rates oder Trend-Grenzen.

### 4. PMS Review durchführen

Klassifiziere Source-/System-State mindestens `adequate-no-signal|signal-to-triage|trend-hypothesis|evidence-gap|coverage-gap|action-open|external-pending|unknown`. Trenne beobachtete Daten, Signalhypothese und regulatorische Interpretation.

### 5. Specialist Routing

- EU-/IVDR Signal/Vigilance → `ivdr-pms-vigilance`
- FDA Complaint/MDR → `fda-complaint-mdr-reportability`
- FDA Correction/Removal → `fda-corrections-removals`
- Performance/Clinical Evidence → `clinical-evidence-update-impact`, `ivdr-performance-evaluation` oder `ivdr-pmpf` soweit passend
- neue/geänderte Risiken → `medical-device-risk-management-iso14971`
- systemische Nonconformity → `medical-device-capa` / `evidence-based-causal-investigation`
- Label/Claim Impact → `regulatory-claims-consistency` / `medical-device-labeling-ifu`
- produkt-/prozessbezogene Änderung → `regulatory-change-impact-orchestrator` bzw. `design-change-regulatory-impact`
- Management-/QMS-Review → zuständiger QMS-Management-Review-Owner.

### 6. Lifecycle Closure verfolgen

Ein PMS Signal gilt nicht dadurch als erledigt, dass es geroutet wurde. `pms-review-status.json` hält Specialist Decision References, offene Actions, Completion Evidence, External States und Re-evaluation Trigger.

### 7. Plan und Source Coverage aktualisieren

Neue Produkte, Märkte, Claims, Risikokontrollen, Field Signals, Regulatory Changes oder geänderte Exposure-/Source-Strukturen triggern eine PMS-System-Neubewertung.

## Output-Verträge

`pms-system-plan.json` enthält Scope, Märkte, Risk-/Claim-/Performance-Links, Sources, Review-Cadence/Event Trigger, Decision Rules, Owners, Current-Requirement References und Re-evaluation Trigger.

`pms-source-register.json` enthält Source, Provenance, Coverage, Denominator/Exposure soweit anwendbar, Data Quality, Zeitbezug, Owner und bekannte Gaps.

`pms-review-status.json` enthält Review Period/Event, Beobachtungen, Signal-/Trend-Hypothesen, Specialist Routing, Decision References, Actions, Completion Evidence, External State und offene Gaps.

## Memory Path

Persistenzwürdig sind validierte PMS-Source-Architekturen, stabile produktspezifische Surveillance-Fragen und abstrahierte Signal-/Routing-Heuristiken. Einzelne Complaints/Incidents, Patienten-/Anwenderdaten, aktuelle Fallzahlen/Rates, laufende Reportability-/Recall-/CAPA-Fälle, momentane Trendhypothesen und volatile Guidance-/Form-/Frist-Snapshots bleiben run-only bzw. kontrollierte Quality/Regulatory Records. Regulatory Candidates benötigen `sourceRefs`, `asOf` und `reviewAfter`; übergib nur abstrahierte `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`.

## Qualitätsgate

Bestanden nur wenn:

- PMS Scope und marktbezogene Pflichten getrennt nachvollziehbar sind,
- Source Coverage/Data Quality vor Trendbehauptungen geprüft wird,
- Counts nicht ohne geeigneten Exposure-/Denominator-Kontext als Rate/Trend interpretiert werden,
- Complaint/Vigilance/MDR/806/CAPA/PMPF nicht dupliziert werden,
- marktbezogene Reportability bei den jeweiligen Spezialisten bleibt,
- relevante Signale in Risk/Performance/Clinical Evidence/Labeling/CAPA/Change zurückgeführt werden,
- Routing nicht mit Closure verwechselt wird,
- einzelne Fälle und personenbezogene Daten nicht in dauerhaftes globales Memory gelangen.
