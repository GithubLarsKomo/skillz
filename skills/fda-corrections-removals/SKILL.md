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
lastEvaluated: 2026-08-07
---

# FDA Corrections and Removals

## Zweck und Grenze

Dieser Skill bewertet eine tatsächlich initiierte oder geplante Medical-Device-Correction/Removal gegen aktuelle FDA-Anforderungen aus 21 CFR Part 806 sowie den Recall-Kontext aus 21 CFR Part 7. Er entscheidet Reportability und Recordkeeping auf Basis von Risk-to-Health, Violation Context, Action Type und vorhandener FDA-Berichterstattung.

Er ist **kein Recall-Execution-System**, kein CAPA-System und kein MDR-Ersatz. Kommunikation, FDA-Einreichung, Consignee Outreach, Produktbewegung und Wirksamkeitschecks bleiben verifizierte Human-/External-Actions.

## Kernprinzipien

- **Action facts first:** Initiation Date, Initiator, Device Scope, Correction vs Removal und Reason müssen belegt sein.
- **806 reportability is separate from recall class:** Reportability wird nach 21 CFR 806 bewertet; Recall Classification ist ein eigener FDA/recall-process state.
- **Ten-working-day clock is explicit:** bei reportable Correction/Removal wird die 10-Arbeitstage-Frist aus der Initiation abgeleitet und nicht aus Complaint-/MDR-Awareness-Daten übernommen.
- **MDR overlap is checked:** wenn dieselbe Information bereits nach 21 CFR 803 oder einschlägigen Ausnahmen berichtet wurde, wird die 806-Ausnahme evidenzgebunden geprüft statt doppelt zu melden.
- **Non-reportable still means records:** nicht reportable Corrections/Removals können weiterhin Recordkeeping-Pflichten haben.

## Workflow

### 1. Action Scope fixieren

Erfasse Initiator, Initiation Date, Device/UDI/Listing/Submission Context, Lots/Serials, Distribution Scope, Correction/Removal/Stock Recovery/Routine Servicing/Market Withdrawal Context und konkrete Risk-/Violation-Begründung.

### 2. Risk-to-Health und Violation Evidence referenzieren

Nutze vorhandene Risk-, Complaint-, Investigation- und CAPA-Evidence. Keine zweite Hazard-/CAPA-Analyse erzeugen. Unklare Gesundheitsrisiken bleiben `unknown` und werden nicht automatisch als non-reportable behandelt.

### 3. 806 Reportability bestimmen

Klassifiziere als `806-reportable|record-only|exempt/duplicate-reporting-evidence|outside-806|uncertain`. Reportable ist insbesondere eine vom Manufacturer/Importer initiierte Correction/Removal zur Reduktion eines Risk to Health oder zur Behebung einer Act-Verletzung, die Risk to Health darstellen kann, sofern keine belegte Ausnahme greift.

### 4. Frist und Inhalt ableiten

Für `806-reportable` wird Due Date = 10 working days ab Initiation Date geführt. Mappe die aktuellen §806.10(c)-Informationsfelder, bekannte/fehlende Daten, Amendments/Extensions und empfohlenen aktuellen Submission-Kanal/Form-State ohne Einreichung zu simulieren.

### 5. Recall-/Postmarket-Routing

- Recall Strategy/Communications/Effectiveness Check → autorisierter Recall-/Human-Action-Pfad.
- MDR Event Reportability → `fda-complaint-mdr-reportability`.
- CAPA/Investigation → `medical-device-capa` bzw. bestehende Investigation Owner.
- Design/Labeling/Software Change → `design-change-regulatory-impact`, `medical-device-labeling-ifu`, ggf. Software/Cybersecurity-Skills.
- Registration/Listing/UDI Master Data → `fda-registration-listing-udi`.

## Output-Verträge

`correction-removal-assessment.json` enthält Action Facts, Device Scope, Risk/Violation Evidence, 806 Decision, Exemption/Overlap Evidence, Rationale, Current Sources/`asOf` und Decision Owner.

`correction-removal-action-plan.json` enthält affected scope, containment/correction/removal actions, communication/effectiveness-check dependencies, CAPA/Risk/Design Links und stop conditions.

`correction-removal-reporting-state.json` enthält reportability, Initiation Date, computed due-date basis, required information/gaps, external-submission state, amendment triggers und verification evidence.

## Memory Path

Persistenzwürdig sind nur abstrahierte validierte 806-Entscheidungs- und Recall-Dependency-Muster. Konkrete Complaint-/Patient-/Consignee-Daten, Lot/Serial/UDI, Initiation-/Due-Dates, Recall-/806-Nummern, aktuelle FDA-Kommunikation und offene CAPA-/Risk-Zustände bleiben run-only oder kontrollierte Quality/Regulatory Records. Geeignete Memory Candidates gehen ausschließlich an `communication-memory-governance`.

## Qualitätsgate

Bestanden nur wenn:

- Initiation Date und Action Type belegt oder als fehlend markiert sind,
- Risk-to-Health/Violation-Logik evidenzgebunden ist,
- 806 Reportability nicht mit Recall Classification oder MDR gleichgesetzt wird,
- die 10-Arbeitstage-Frist aus der richtigen Initiation abgeleitet wird,
- Ausnahmen/Doppelberichterstattung nur mit belegter Evidence angewendet werden,
- record-only nicht mit „keine Dokumentation“ verwechselt wird,
- externe FDA-/Recall-Aktionen nicht simuliert werden,
- konkrete Case-/Recall-/Due-Date-Daten nicht in globales dauerhaftes Memory gelangen.
