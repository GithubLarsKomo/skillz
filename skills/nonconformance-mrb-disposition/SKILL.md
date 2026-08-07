---
name: nonconformance-mrb-disposition
description: Strukturiert Medical-Device-Nichtkonformitäten von Containment und Impact Assessment bis risikobasierter MRB-Disposition, Rework-Evidenz und CAPA-Routing.
userFacing: true
implicitInvocation: true
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - medical-device-qms-iso13485
  - medical-device-risk-management-iso14971
  - two-axis-compliance-review
outputs:
  - nonconformance-assessment.json
  - mrb-disposition-decision.json
  - containment-actions.json
lastEvaluated: 2026-08-07
---

# Nonconformance and MRB Disposition for Medical Devices

## Zweck und Grenze

Dieser Skill strukturiert Medical-Device-/IVD-Nichtkonformitäten von Identifikation und Containment über Product-/Process-/Risk-/Regulatory-Impact bis zur nachvollziehbaren Material-Review-/Disposition-Entscheidung und notwendiger Rework-/Verification-Evidenz. Er ersetzt weder `medical-device-capa` noch Root Cause Investigation, Design Change, Complaint/Vigilance oder autorisierte Freigaben.

Der Skill erzeugt **keine retroaktive Akzeptanz**. Eine dokumentierte MRB-Empfehlung ist keine simulierte Genehmigung; Use-as-is/Concession, Rework, Repair, Scrap, Return oder andere Dispositionen benötigen die organisationsseitig vorgesehenen Rollen, Controls und Evidence.

## Kernprinzipien

- **Contain before disposition:** betroffene Einheiten/Lots/Records/Downstream-States werden identifiziert und kontrolliert, bevor eine Disposition als abgeschlossen gilt.
- **Scope and impact first:** Quantity, Lots, Products, Sites, Distribution/Release State und verwandte Nonconformities werden abgegrenzt; unbekannter Umfang bleibt sichtbar.
- **Risk and regulatory impact:** Product Safety/Performance, Claims, released product, complaint/vigilance/recall und market-authorization impact werden bei Bedarf an vorhandene Specialist Skills geroutet.
- **Disposition needs evidence:** Approval-Status oder MRB-Eintrag allein belegt nicht, dass Rework/Repair/Use-as-is technisch und regulatorisch vertretbar ist.
- **Rework must be reverified:** Rework/Repair benötigt definierte Instructions, Acceptance Criteria und geeignete Reinspection/Verification/Validation; keine automatische Rückkehr in Accepted State.
- **NC ≠ CAPA:** einzelne Nichtkonformität und systemisches CAPA-Signal bleiben getrennte States; CAPA wird anhand Significance/Recurrence/Systemic Evidence getriggert, nicht automatisch dupliziert.
- **No post-hoc specification:** bestehende Requirements/Acceptance Criteria werden nicht nachträglich geändert, um fehlerhafte Einheiten passend zu machen.

## Workflow

### 1. Nonconformance fixieren

Erfasse NC ID, Source/Detection Point, Date, Product/Part/Material/Process/Software/Record, Lot/Serial/Batch soweit relevant, observed condition, requirement/specification/reference, detected quantity und Known Scope. Trenne Fakt von Hypothese.

### 2. Immediate Containment

Bestimme betroffene physische/digitale Einheiten und Downstream-States. Mögliche Controls: Segregation/Hold, Stop-Ship/Stop-Use, zusätzliche Identifikation, Record Lock/Access Control, targeted screening oder andere organisationsseitig definierte Maßnahmen. Durchführung wird nur nach Evidence als erfolgt markiert.

### 3. Impact Assessment

Bewerte:
- Product Safety/Performance/Essential Characteristics,
- Risk Controls/Residual Risk,
- released/distributed product,
- related Lots/Products/Processes/Suppliers,
- Measurement-/Process-Validation-Reliability,
- Complaint/PMS/Vigilance/Reporting/Recall Relevance,
- Design-/Regulatory-Change-Fragen,
- möglicher systemischer Trend.

### 4. Disposition Options bewerten

Bewerte nur technisch und regulatorisch zulässige Optionen, z. B.:
- `rework-to-original-requirements`,
- `repair-with-evaluated-impact`,
- `use-as-is/concession-with-rationale`,
- `scrap/destroy`,
- `return-to-supplier`,
- `reclassify/alternate-controlled-use` soweit zulässig,
- `pending-investigation|unknown`.

Für jede Option dokumentiere Rationale, Risk/Requirement Impact, Needed Approval, Needed Verification/Validation, Record/Traceability Impact und Stop Conditions.

### 5. Rework/Repair Evidence

Vor Wiederfreigabe müssen genehmigte Instructions, identifizierte betroffene Units, geeignete Reinspection/Verification/Validation, Acceptance Criteria und Result Evidence vorliegen. Wenn Rework/Repair Design, Process, Software, Labeling oder Supplier Control verändert, route an `design-change-regulatory-impact` bzw. `process-validation-iq-oq-pq`.

### 6. Systemic/CAPA Trigger

Bewerte Recurrence, Severity, Detection/System Escape, common cause indicators, supplier/process trend und vorhandene ähnliche NCs. Bei systemischem Verdacht → `medical-device-capa` / `evidence-based-causal-investigation`. MRB-Disposition schließt eine notwendige CAPA nicht automatisch.

### 7. External/Lifecycle Routing

- released product / complaint / vigilance / reportability → zuständige PMS/FDA/EU-Skills
- Supplier NC → `supplier-quality-medical-device`
- Measurement System Issue → `measurement-system-validation`
- Process Validation Gap → `process-validation-iq-oq-pq`
- Design/Regulatory Change → `design-change-regulatory-impact`
- kontrollierte Records → `controlled-quality-documentation`.

## Output-Verträge

`nonconformance-assessment.json` enthält NC Facts, Requirement Reference, Scope, Containment State, Product/Process/Risk/Regulatory Impact, Related Signals und Open Questions.

`mrb-disposition-decision.json` enthält geprüfte Disposition Options, Selected/Recommended State, Rationale, Needed Approval, Rework/Repair/Verification Requirements, CAPA/Regulatory Routing und Human Decision State.

`containment-actions.json` enthält betroffene Scope-Objekte, geplante/ausgeführte Controls, Evidence References, Owner und Completion State.

## Memory Path

Persistenzwürdig sind validierte NC-Triage-/Disposition-Heuristiken, wiederverwendbare Containment-/Rework-Evidence-Patterns und abstrahierte CAPA-Trigger-Muster. Konkrete NCs, Lots/Serials, Product Defects, Supplier Details, Investigation Hypotheses, MRB Decisions, offene CAPA, Complaint/Vigilance-States und vertrauliche Manufacturing Records bleiben run-only bzw. in kontrollierten QMS/NC Records. Kandidaten benötigen `sourceRefs`; lifecycleabhängige Learnings zusätzlich `asOf`/`reviewAfter`. Übergib nur abstrahierte geeignete `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- Nonconformance Facts, Requirement und Scope nachvollziehbar fixiert sind,
- Containment vor abgeschlossener Disposition berücksichtigt wird,
- Disposition risikobasiert und evidenzgebunden statt nur administrativ gewählt wird,
- Rework/Repair vor Wiederfreigabe geeignete Verifikation/Validierung besitzt,
- Specifications/Acceptance Criteria nicht post-hoc passend gemacht werden,
- NC/MRB und CAPA getrennte Lifecycle States bleiben,
- Freigabe/Disposition/Human Approval nicht simuliert werden,
- konkrete NC-/MRB-Zustände nicht in globales dauerhaftes Memory gelangen.
