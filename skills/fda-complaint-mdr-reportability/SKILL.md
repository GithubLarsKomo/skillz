---
name: fda-complaint-mdr-reportability
description: Bewertet Medical-Device-Complaints auf FDA-MDR-Reportability, Timing und Folgeaktionen ohne Complaint- oder CAPA-System zu duplizieren.
userFacing: true
implicitInvocation: false
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - regulated-product-context
  - medical-device-risk-management-iso14971
  - regulatory-evidence-traceability
  - quality-record-integrity
outputs:
  - mdr-reportability-assessment.json
  - complaint-regulatory-actions.json
lastEvaluated: 2026-08-07
---

# FDA Complaint MDR Reportability

## Zweck und Grenze

Dieser Skill bewertet vorhandene Medical-Device-/IVD-Complaint- oder Adverse-Event-Fakten auf FDA Medical Device Reporting (MDR) Reportability und regulatorische Folgeaktionen. Er **ist kein Complaint-Management-System**, führt keine CAPA eigenständig und übermittelt keine eMDRs.

## Kernprinzipien

- **Actual awareness evidence:** Awareness Date/Source und vorhandene Event-Fakten werden aus dem realen Complaint-/Event-Record übernommen; keine Frist wird aus einem erfundenen Datum berechnet.
- **Reportability ≠ causality proven:** MDR kann auf Informationen beruhen, die reasonably suggest, dass ein Device verursacht/beigetragen haben könnte oder ein relevanter Malfunction vorliegt; endgültige Root Cause ist nicht Voraussetzung für die initiale Bewertung.
- **Current rule clock:** Report Type und Timing werden aus aktuellen offiziellen FDA/21-CFR-803-Quellen und tatsächlichem Awareness Context bestimmt.
- **30-day and 5-day stay distinct:** reguläre reportable Death/Serious-Injury/Malfunction-Fälle und 5-Day-Fälle werden nicht vermischt; 5-Day setzt die aktuelle spezifische Regulatory-Bedingung voraus.
- **Investigation continues:** Reporting beendet Investigation, Risk Update, CAPA/PMS oder Follow-up nicht.
- **External submission is verified:** Draft/Assessment ≠ eMDR submitted/received/accepted.

## Workflow

### 1. Complaint/Event Context fixieren

Erfasse Complaint/Event ID, Device/Variant, Market, Reporter/Source, Awareness Date und Awareness Role soweit relevant, Event Description, Outcome, Device Availability, Malfunction/Failure Information, Initial Risk/Seriousness Information und Record Integrity Status.

### 2. Record Reliability prüfen

Nutze `quality-record-integrity`, um Source/Attribution/Timing/Completeness zu bewerten. Fehlende Information bleibt `unknown`; sie wird nicht erfunden. Dokumentiere reasonable follow-up information, die noch beschafft werden kann.

### 3. MDR Criteria bewerten

Prüfe current-source-basiert mindestens:
- Death,
- Serious Injury,
- Device may have caused or contributed,
- Malfunction und Wahrscheinlichkeit einer Death/Serious Injury bei Wiederholung,
- 5-Day Trigger/Request bzw. remedial-action/public-health context,
- bekannte Exemption/Special Reporting Program soweit tatsächlich anwendbar,
- Supplemental Information nach bereits erfolgtem Report.

### 4. Timing ableiten

Klassifiziere `30-day|5-day|supplemental|not-reportable|insufficient-information|special-program-review`. Berechne Due/Clock nur aus tatsächlichem Awareness Context und current official rule source. Ein erinnerter Standardtermin ohne Source/Case Context ist unzulässig.

### 5. Cross-Lifecycle Routing

- Complaint Investigation/System Cause → `evidence-based-causal-investigation`
- Risk Update/Trend → `medical-device-risk-management-iso14971`
- CAPA Trigger → `medical-device-capa`
- IVD/EU PMS/Vigilance → `ivdr-pms-vigilance` soweit im Scope
- Claim/Use/Labeling Conflict → `regulatory-claims-consistency` / `medical-device-labeling-ifu`
- Design/Process/Supplier Change → jeweiliger bestehender Specialist
- eMDR Submission/Receipt Verification → `human-procedure-wizard` bzw. verifizierter externer Action Path.

### 6. Decision und External Boundary

Dokumentiere Reportability State, Rationale, Source References, Awareness/Clock Inputs, Missing Information, Investigation/Risk/CAPA Links, Human Regulatory Review State und External Submission State getrennt. Nur verifizierte externe Evidenz darf `submitted`/`received` setzen.

## Output-Verträge

`mdr-reportability-assessment.json` enthält Event Context, Awareness Evidence, Current Rule Sources/`asOf`, Criteria Assessment, Reportability State, Timing Class, Due/Clock Inputs, Rationale, Missing Information und Human Review State.

`complaint-regulatory-actions.json` enthält Required/Recommended Actions, Owner, Due Source, Investigation/Risk/CAPA/PMS Links, eMDR External State, Follow-up/Supplemental Need und Completion Evidence.

## Memory Path

Persistenzwürdig sind validierte MDR-Decision-Heuristiken, wiederverwendbare Event-Fact-Checklisten und abstrahierte Routing-Muster. Konkrete Complaints, Patient-/Reporter-Daten, Device IDs, Awareness Dates, aktuelle Due Dates, Reportability Decisions, eMDR IDs und Investigation Findings bleiben run-only bzw. in kontrollierten Complaint/Quality/Regulatory Records. Regulatory Candidates benötigen `sourceRefs`, `asOf` und `reviewAfter`. Übergib nur abstrahierte geeignete `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- **Actual awareness evidence** statt erfundener Clock-Inputs verwendet wird,
- Reportability nicht mit final bewiesener Causality verwechselt wird,
- **30-day and 5-day stay distinct** und current-source-basiert bewertet werden,
- fehlende Complaint-Fakten als unknown/follow-up statt erfunden behandelt werden,
- Reporting Investigation/Risk/CAPA/PMS nicht still beendet,
- eMDR Submission/Receipt nicht simuliert wird,
- konkrete Complaint-/Due-/Reportability-Zustände nicht in globales dauerhaftes Memory gelangen.
