---
name: fda-corrections-removals
description: Bewertet Medical-Device-Korrekturen und -Entfernungen nach 21 CFR 806/Part 7 auf Reportability, 10-Arbeitstage-Frist, Recall-/Recordkeeping-Pfad und verknüpft Risk, MDR, CAPA und externe FDA-Aktionen ohne diese zu duplizieren.
userFacing: true
implicitInvocation: false
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - medical-device-risk-management-iso14971
  - medical-device-capa
  - fda-complaint-mdr-reportability
  - decision-record
outputs:
  - correction-removal-assessment.json
  - correction-removal-action-plan.json
  - correction-removal-reporting-state.json
lastEvaluated: 2026-08-08
---

# FDA Corrections and Removals

## Zweck und Grenze

Dieser Skill bewertet eine tatsächlich initiierte oder geplante Medical-Device-Correction/Removal gegen aktuelle FDA-Anforderungen aus 21 CFR Part 806 sowie den Recall-Kontext aus 21 CFR Part 7. Er entscheidet Reportability und Recordkeeping auf Basis von Risk-to-Health, Violation Context, Action Type und vorhandener FDA-Berichterstattung.

Er ist **kein Recall-Execution-System**, kein CAPA-System und kein MDR-Ersatz. Externe FDA-Einreichung, Consignee Outreach, Produktbewegung und Effectiveness Checks bleiben verifizierte Human-/External-Actions. Die regulierte Customer-/Consignee-Kommunikation wird nach der Regulatory-Entscheidung kontrolliert an `medical-device-field-action-communication` übergeben; deren verifizierte Execution Evidence kann anschließend von `medical-device-field-action-effectiveness` bewertet werden.

## Kernprinzipien

- **Action facts first:** Initiation Date, Initiator, Device Scope, Correction vs Removal und Reason müssen belegt sein.
- **806 reportability is separate from recall class:** Reportability wird nach 21 CFR 806 bewertet; Recall Classification ist ein eigener FDA/recall-process state.
- **Ten-working-day clock is explicit:** bei reportable Correction/Removal wird die 10-Arbeitstage-Frist aus der Initiation abgeleitet und nicht aus Complaint-/MDR-Awareness-Daten übernommen.
- **MDR overlap is checked:** wenn dieselbe Information bereits nach 21 CFR 803 oder einschlägigen Ausnahmen berichtet wurde, wird die 806-Ausnahme evidenzgebunden geprüft statt doppelt zu melden.
- **Non-reportable still means records:** nicht reportable Corrections/Removals können weiterhin Recordkeeping-Pflichten haben.
- **Regulatory decision ≠ execution success:** ein `806-reportable`, `record-only` oder interner Recall-Strategy-State beweist weder Consignee Notification noch Product Correction/Removal noch Effectiveness.
- **FDA classification/termination stay external:** interne Risk-/Recall-Einschätzung wird nicht als FDA Recall Classification oder FDA `terminated`-State ausgegeben.
- **Execution cannot delay the 806 clock:** Recipient-Listen, Recall Letter, Root Cause, CAPA oder Effectiveness-Planung dürfen einen laufenden Part-806-Reporting-Clock nicht blockieren.

## Workflow

### 1. Action Scope fixieren

Erfasse Initiator, Initiation Date, Device/UDI/Listing/Submission Context, Lots/Serials, Distribution Scope, Correction/Removal/Stock Recovery/Routine Servicing/Market Withdrawal Context und konkrete Risk-/Violation-Begründung.

### 2. Risk-to-Health und Violation Evidence referenzieren

Nutze vorhandene Risk-, Complaint-, Investigation- und CAPA-Evidence. Keine zweite Hazard-/CAPA-Analyse erzeugen. Unklare Gesundheitsrisiken bleiben `unknown` und werden nicht automatisch als non-reportable behandelt.

### 3. 806 Reportability bestimmen

Klassifiziere als `806-reportable|record-only|exempt/duplicate-reporting-evidence|outside-806|uncertain`. Reportable ist insbesondere eine vom Manufacturer/Importer initiierte Correction/Removal zur Reduktion eines Risk to Health oder zur Behebung einer Act-Verletzung, die Risk to Health darstellen kann, sofern keine belegte Ausnahme greift.

### 4. Frist und Inhalt ableiten

Für `806-reportable` wird Due Date = 10 working days ab Initiation Date geführt. Mappe die aktuellen §806.10(c)-Informationsfelder, bekannte/fehlende Daten, Amendments/Extensions und empfohlenen aktuellen Submission-Kanal/Form-State ohne Einreichung zu simulieren.

Eine Scope-Erweiterung auf zusätzliche Lots/Batches/Devices wird current-source-basiert auf Amendment-/neue Initiation-/Reporting-Auswirkungen geprüft und versioniert; sie überschreibt nicht den ursprünglichen Action-/Reporting-Snapshot.

### 5. Recall-/Postmarket-Routing

- Recall Strategy/Communications → `medical-device-field-action-communication` mit `correction-removal-action-plan.json`, kontrollierter Action/Scope Version, Recipient/Distribution Basis, Required Action und Release Preconditions. Der Communication Worker entscheidet keine 806-Reportability oder Recall Classification.
- Communication-/Product-Execution-Evidence → `medical-device-field-action-effectiveness` für Strategy-basierte Effectiveness Checks, Product Reconciliation und Closure-Readiness. Interne Closure-Readiness ist keine FDA Recall Termination.
- MDR Event Reportability → `fda-complaint-mdr-reportability`.
- CAPA/Investigation → `medical-device-capa` bzw. bestehende Investigation Owner.
- Design/Labeling/Software Change → `design-change-regulatory-impact`, `medical-device-labeling-ifu`, ggf. Software/Cybersecurity-Skills.
- Registration/Listing/UDI Master Data → `fda-registration-listing-udi`.
- Externe FDA Submission/Recall-/Termination-Aktion → autorisierte Regulatory-Funktion bzw. `human-procedure-wizard`; Erfolg erst nach externer Evidence.

### 6. Execution Feedback und Scope Drift

Neue Consignee-/Distribution-/Product-/Safety-Evidence aus Communication/Effectiveness kann:

- Action Scope erweitern,
- ein Part-806-Amendment/erneute Reporting-Prüfung auslösen,
- MDR-Reassessment triggern,
- Recall Strategy/Effectiveness Check verändern,
- Risk/CAPA/PMS aktualisieren.

Eine hohe Communication-/Effectiveness-Quote oder ein interner `completed`-State immunisiert die Regulatory-Entscheidung nicht gegen neue materielle Fakten.

## Output-Verträge

`correction-removal-assessment.json` enthält Action Facts, Device Scope, Risk/Violation Evidence, 806 Decision, Exemption/Overlap Evidence, Rationale, Current Sources/`asOf` und Decision Owner.

`correction-removal-action-plan.json` enthält affected scope/version, containment/correction/removal actions, communication/effectiveness-check dependencies, Recipient/Distribution Basis soweit vorhanden, CAPA/Risk/Design Links, Execution Handoff State und stop conditions. Es enthält keinen erfundenen Consignee-Notification- oder Effectiveness-Erfolg.

`correction-removal-reporting-state.json` enthält reportability, Initiation Date, computed due-date basis, required information/gaps, external-submission state, amendment triggers, Recall/FDA external state und verification evidence.

## Memory Path

Persistenzwürdig sind nur abstrahierte validierte 806-Entscheidungs- und Recall-Dependency-Muster. Konkrete Complaint-/Patient-/Consignee-Daten, Lot/Serial/UDI, Initiation-/Due-Dates, Recall-/806-Nummern, aktuelle FDA-Kommunikation und offene CAPA-/Risk-/Execution-Zustände bleiben run-only oder kontrollierte Quality/Regulatory Records. Geeignete Memory Candidates gehen ausschließlich an `communication-memory-governance`.

## Qualitätsgate

Bestanden nur wenn:

- Initiation Date und Action Type belegt oder als fehlend markiert sind,
- Risk-to-Health/Violation-Logik evidenzgebunden ist,
- 806 Reportability nicht mit Recall Classification oder MDR gleichgesetzt wird,
- die 10-Arbeitstage-Frist aus der richtigen Initiation abgeleitet wird,
- Ausnahmen/Doppelberichterstattung nur mit belegter Evidence angewendet werden,
- record-only nicht mit „keine Dokumentation“ verwechselt wird,
- Recipient-/Communication-/Effectiveness-Arbeit den Part-806-Clock nicht verzögert,
- `medical-device-field-action-communication` und `medical-device-field-action-effectiveness` keine 806-/Recall-Authority-Entscheidung zurückerfinden,
- externe FDA-/Recall-/Termination-Aktionen nicht simuliert werden,
- interne Operational Completion nicht als FDA `terminated` ausgegeben wird,
- Scope-Erweiterungen und neue Safety Facts Amendment/MDR/Risk/CAPA-Reassessment auslösen können,
- konkrete Case-/Recall-/Due-Date-/Consignee-Daten nicht in globales dauerhaftes Memory gelangen.
