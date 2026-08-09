---
name: supplier-quality-medical-device
description: Steuert Medical-Device-Lieferanten risikobasiert von Auswahl und Qualifizierung über Qualitätsvereinbarung, Monitoring und Change Notification bis SCAR/CAPA-Routing.
---

# Supplier Quality for Medical Devices

## Zweck und Grenze

Dieser Skill bewertet und steuert externe Provider/Lieferanten für Medical-Device-/IVD-Produkte risikobasiert über Auswahl, Qualifizierung, festgelegte Controls, Qualitätsvereinbarungen, Monitoring, Change Notifications, Re-evaluation und Supplier-Issue-Routing. Er ersetzt weder Einkauf/Vertragsrecht noch `medical-device-capa`, führt kein paralleles Risk Register und simuliert keine Supplier-Audit-Freigabe.

QMSR-/ISO-13485-Anforderungen werden aus aktuellen autoritativen bzw. organisationsseitig autorisierten Quellen referenziert. Normtexte werden nicht reproduziert.

## Kernprinzipien

- **Risk-based supplier control:** Tiefe und Frequenz der Controls folgen Einfluss auf Produktqualität, Sicherheit, Performance, Compliance und Prozessverifizierbarkeit.
- **Criticality ≠ spend:** hoher Einkaufswert ist kein Ersatz für regulatorische/technische Supplier Criticality.
- **Evidence before approval:** Supplier Status benötigt nachvollziehbare Qualification-/Monitoring-Evidenz; ein Name auf einer Approved Supplier List allein reicht nicht.
- **Change notification is a control:** vereinbarte Änderungen bei Material, Prozess, Site, Equipment, Software, Subsupplier oder Specification müssen auf Produkt-/Risk-/Validation-/Regulatory-Impact geroutet werden.
- **Supplier CAPA stays CAPA:** Supplier Findings können SCAR/CAPA triggern, aber dieser Skill erzeugt keinen zweiten CAPA-Workflow.
- **Acceptance controls are linked:** Incoming-/Certificate-/Process-/Release-Controls werden referenziert und auf Supplier Risk/History abgestimmt.

## Workflow

### 1. Supplier Scope und Criticality fixieren

Erfasse Supplier/Service, gelieferte Produkte/Prozesse/Software/Services, betroffene Produkte/Sites, Single-Source-/Subsupplier-Abhängigkeiten, Patient-/Performance-/Compliance-Impact und vorhandene Risk Links.

### 2. Qualification Evidence erfassen

Indexiere je nach Risiko z. B. QMS-/Certification Evidence, Audit-/Assessment Evidence, Capability-/Process-/Validation Evidence, Sample/First Article/Incoming Evidence, technische Vereinbarungen, Regulatory-/Change-Notification-Fähigkeit und historische Performance. Ein Zertifikat ersetzt keine risikogerechte Qualifizierung.

### 3. Supplier Control Plan ableiten

Lege risikobasiert Controls fest, z. B.:
- Approval Scope und Bedingungen,
- Incoming-/Release-/Certificate Controls,
- Audit-/Review-/Re-evaluation-Frequenz,
- Quality Agreement / Change Notification,
- KPI/Trend/Complaint/NC Monitoring,
- Escalation/SCAR/CAPA Trigger,
- Contingency/Second Source soweit relevant.

### 4. Monitoring und Signals

Erfasse Supplier Performance Signals wie NC/Defects, Incoming Rejections, Complaints, CAPA/SCAR, Delivery-/Continuity-Risiken soweit qualitätsrelevant, Audit Findings, unautorisierte Changes und Trendverschlechterung. Trenne Einzelereignis von bestätigtem systemischem Signal.

### 5. Supplier Change Impact

Jede relevante Supplier Change Notification wird auf Design-/Material-/Process-/Software-/Validation-/Risk-/Regulatory-Impact geprüft und bei Bedarf an `design-change-regulatory-impact`, `process-validation-iq-oq-pq`, Risk Management oder Controlled Documentation geroutet.

### 6. Issue Routing

- systemische Ursache/CAPA → `medical-device-capa` / `evidence-based-causal-investigation`
- Produkt-/Risk-Impact → `medical-device-risk-management-iso14971`
- QMS-/Supplier-Control-Gap → `medical-device-qms-iso13485`
- Prozessvalidierung → `process-validation-iq-oq-pq`
- Design-/Regulatory Change → `design-change-regulatory-impact`
- kontrollierte Supplier Records/Agreements → `controlled-quality-documentation`.

## Output-Verträge

`supplier-quality-assessment.json` enthält Supplier Scope, Criticality Rationale, Qualification Evidence, Current Approval State, Coverage/Evidence Status, Gaps und Source References.

`supplier-control-plan.json` enthält risikobasierte Qualification-/Monitoring-/Audit-/Incoming-/Agreement-/Change-Notification-/Escalation-Controls, Owner, Frequenz/Trigger und Evidence Expectations.

`supplier-signal-set.json` enthält relevante Supplier Signals, Trend/Severity, Product/Risk Links, Needed Investigation/Action und Routing.

## Memory Path

Persistenzwürdig sind validierte Supplier-Criticality-Heuristiken, wiederverwendbare Qualification-/Monitoring-Muster und abstrahierte Change-Notification-/Escalation-Patterns. Konkrete Supplier Performance, Preise/Verträge, vertrauliche Audit Findings, offene SCAR/CAPA, aktuelle Approval States und firmenspezifische Quality Agreements bleiben run-only bzw. in kontrollierten Supplier/Quality Records. Kandidaten benötigen `sourceRefs`; volatile Learnings zusätzlich `asOf`/`reviewAfter`. Übergib nur abstrahierte geeignete `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- Supplier Controls aus Quality/Risk/Criticality statt Spend allein abgeleitet werden,
- Approval/Qualification auf Evidenz statt nur Listenstatus beruht,
- Change Notifications auf Risk/Validation/Regulatory Impact geroutet werden,
- Supplier Findings nicht in einem zweiten CAPA-System verarbeitet werden,
- Monitoring Trends und einzelne Events unterscheidet,
- konkrete Supplier-/Audit-/Agreement-Zustände nicht in globales dauerhaftes Memory gelangen.
