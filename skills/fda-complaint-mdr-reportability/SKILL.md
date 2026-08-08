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
  - medical-device-complaint-regulatory-routing
  - regulated-product-context
  - medical-device-risk-management-iso14971
  - regulatory-evidence-traceability
  - quality-record-integrity
outputs:
  - mdr-reportability-assessment.json
  - complaint-regulatory-actions.json
lastEvaluated: 2026-08-08
---

# FDA Complaint MDR Reportability

## Zweck und Grenze

Dieser Skill bewertet vorhandene Medical-Device-/IVD-Complaint- oder Adverse-Event-Fakten auf FDA Medical Device Reporting (MDR) Reportability und regulatorische Folgeaktionen. Er **ist kein Complaint-Management-System**, führt keine CAPA eigenständig und übermittelt keine eMDRs.

Der Skill konsumiert den jurisdiction-neutralen Complaint-/Awareness-Handoff aus `medical-device-complaint-regulatory-routing`. Er übernimmt dessen Timeline-Fakten als Evidence, trifft die **FDA-spezifische Rechtsentscheidung über Awareness, Reportability und Timing aber selbst**. Ein Router- oder Complaint-Systemstatus darf diese Entscheidung weder vorwegnehmen noch verzögern.

## Kernprinzipien

- **Actual awareness evidence:** Awareness-Evidence, Source und vorhandene Event-Fakten werden aus dem realen Complaint-/Routing-Record übernommen; keine Frist wird aus einem erfundenen Datum berechnet.
- **Any-employee evidence is not discarded:** aktuelle Part-803-Awareness-Regeln dürfen nicht dadurch umgangen werden, dass nur QA-/Regulatory-Eingänge betrachtet werden. Frühere belegte Employee-/Function-Receipt-Fakten aus `regulatory-awareness-timeline.json` müssen in die FDA-Bewertung einfließen.
- **Router evidence ≠ legal conclusion:** die Timeline liefert Evidence Events; der FDA-Skill bestimmt daraus current-source-basiert die relevante Awareness-/Clock-Interpretation.
- **Prior not-reportable is not permanent:** eine frühere `not-reportable`-, `insufficient-information`- oder sonstige MDR-Entscheidung gilt nur für ihren dokumentierten Evidence Snapshot. Neue materielle Informationen lösen eine neue current-source-basierte Bewertung aus.
- **Supplemental information is versioned:** neue Safety-/Outcome-/Malfunction-/Remedial-Action-/Awareness-Fakten werden gegen die frühere Decision-Version bewertet; die frühere Entscheidung bleibt historisch erhalten und wird nicht still überschrieben.
- **Reportability ≠ causality proven:** MDR kann auf Informationen beruhen, die reasonably suggest, dass ein Device verursacht/beigetragen haben könnte oder ein relevanter Malfunction vorliegt; endgültige Root Cause ist nicht Voraussetzung für die initiale Bewertung.
- **Current rule clock:** Report Type und Timing werden aus aktuellen offiziellen FDA/21-CFR-803-Quellen und tatsächlichem Awareness Context bestimmt.
- **30-day and 5-day stay distinct:** reguläre reportable Death/Serious-Injury/Malfunction-Fälle und 5-Day-Fälle werden nicht vermischt; 5-Day setzt die aktuelle spezifische Regulatory-Bedingung voraus.
- **Investigation continues:** Reporting beendet Investigation, Risk Update, CAPA/PMS oder Follow-up nicht.
- **External submission is verified:** Draft/Assessment ≠ eMDR submitted/received/accepted.

## Workflow

### 1. Complaint/Event Context und Routing-Evidence fixieren

Konsumiere `complaint-regulatory-routing.json`, `regulatory-awareness-timeline.json` und `vigilance-entry-handoff.json`. Erfasse Complaint/Event ID, Device/Variant, Market, Reporter/Source, alle belegten relevanten Receipt-/Transfer-/Employee-/Function-Awareness-Fakten, Event Description, Outcome, Device Availability, Malfunction/Failure Information, Initial Risk/Seriousness Information, Prior FDA Assessment Reference, New Material Facts und Record Integrity Status.

Ein später QA-/Regulatory-Eingang überschreibt keine frühere belegte interne Information. Ein früher Customer-/Distributor-Zeitpunkt wird umgekehrt nicht ohne Manufacturer-Receipt-Evidence zur Hersteller-Awareness erklärt.

### 2. Record Reliability prüfen

Nutze `quality-record-integrity`, um Source/Attribution/Timing/Completeness zu bewerten. Fehlende Information bleibt `unknown`; sie wird nicht erfunden. Dokumentiere reasonable follow-up information, die noch beschafft werden kann.

### 3. FDA Awareness und MDR Criteria bewerten

Bestimme zuerst current-source-basiert aus den Routing-Evidence-Events den anwendbaren FDA-Awareness-Context. Prüfe anschließend mindestens:
- Death,
- Serious Injury,
- Device may have caused or contributed,
- Malfunction und Wahrscheinlichkeit einer Death/Serious Injury bei Wiederholung,
- 5-Day Trigger/Request bzw. remedial-action/public-health context,
- bekannte Exemption/Special Reporting Program soweit tatsächlich anwendbar,
- Supplemental Information nach bereits erfolgtem Report.

Complaint-Klassifikation, `known issue`, `user error`, Kundenzufriedenheit, fehlender Device-Rücklauf oder noch offene Root Cause sind für sich allein keine Non-Reportability-Entscheidung.

### 4. Reassessment bei neuer Information

Wenn ein früheres MDR Assessment existiert:

1. referenziere dessen Evidence Snapshot, Awareness Interpretation, Reportability State und externe Action State,
2. vergleiche `newMaterialFacts` gegen den früheren Stand,
3. führe eine neue Bewertung durch, wenn neue Information Awareness, Death/Serious Injury, Malfunction, Causality, Remedial Action/Public Health oder andere MDR-Kriterien materiell beeinflussen kann,
4. erhalte die frühere Entscheidung als historische Version,
5. bestimme current-source-basiert, ob daraus ein neuer Initial-/5-Day-/Supplemental-/sonstiger Follow-up-State entsteht.

Ein früheres `not-reportable` darf nicht unverändert kopiert werden, wenn der neue Evidence Snapshot materiell anders ist.

### 5. Timing ableiten

Klassifiziere `30-day|5-day|supplemental|not-reportable|insufficient-information|special-program-review`. Berechne Due/Clock nur aus der FDA-spezifisch bewerteten Awareness Evidence und current official rule source. Ein erinnerter Standardtermin oder bloßer Complaint-/QA-/Regulatory-System-Zeitpunkt ohne Rechts-/Case Context ist unzulässig.

### 6. Cross-Lifecycle Routing

- Complaint Investigation/System Cause → `medical-device-complaint-handling` / `evidence-based-causal-investigation`
- Risk Update/Trend → `medical-device-risk-management-iso14971`
- CAPA Trigger → `medical-device-capa`
- IVD/EU PMS/Vigilance → `ivdr-pms-vigilance` soweit im Scope
- Claim/Use/Labeling Conflict → `regulatory-claims-consistency` / `medical-device-labeling-ifu`
- Design/Process/Supplier Change → jeweiliger bestehender Specialist
- eMDR Submission/Receipt Verification → `human-procedure-wizard` bzw. verifizierter externer Action Path.

### 7. Decision, Routing Return und External Boundary

Dokumentiere Reportability State, Decision Version, Prior Assessment Reference, New Material Facts, Rationale, Source References, Awareness/Clock Inputs, Missing Information, Investigation/Risk/CAPA Links, Human Regulatory Review State und External Submission State getrennt. Aktualisiere den Complaint-/Routing-Follow-up-State referenzgebunden; nur verifizierte externe Evidenz darf `submitted`/`received` setzen.

## Output-Verträge

`mdr-reportability-assessment.json` enthält Event Context, Routing/Timeline References, Decision Version, Prior Assessment Reference, New Material Facts, FDA Awareness Evidence/Interpretation, Current Rule Sources/`asOf`, Criteria Assessment, Reportability State, Timing Class, Due/Clock Inputs, Rationale, Missing Information und Human Review State.

`complaint-regulatory-actions.json` enthält Required/Recommended Actions, Owner, Due Source, Reassessment/Supplemental Need, Investigation/Risk/CAPA/PMS Links, eMDR External State, Follow-up Need und Completion Evidence.

## Memory Path

Persistenzwürdig sind validierte MDR-Decision-/Reassessment-Heuristiken, wiederverwendbare Event-Fact-/Awareness-Checklisten und abstrahierte Routing-Muster. Konkrete Complaints, Patient-/Reporter-Daten, Device IDs, Awareness Dates, aktuelle Due Dates, Reportability Decisions, eMDR IDs und Investigation Findings bleiben run-only bzw. in kontrollierten Complaint/Quality/Regulatory Records. Regulatory Candidates benötigen `sourceRefs`, `asOf` und `reviewAfter`. Übergib nur abstrahierte geeignete `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- der kontrollierte Complaint-Regulatory-Routing-Handoff konsumiert und seine Provenance nicht verloren wird,
- **Actual awareness evidence** statt erfundener Clock-Inputs verwendet wird,
- frühere belegte Employee-/Function-Receipt-Fakten nicht zugunsten eines späteren QA-/Regulatory-Zeitpunkts verworfen werden,
- Awareness-Evidence und finale FDA-Rechtsinterpretation getrennt bleiben,
- neue materielle Informationen eine frühere `not-reportable`-/Assessment-Entscheidung erneut öffnen können,
- Reassessment frühere Decision-Version und neuen Evidence Snapshot getrennt erhält,
- Reportability nicht mit final bewiesener Causality verwechselt wird,
- **30-day and 5-day stay distinct** und current-source-basiert bewertet werden,
- fehlende Complaint-Fakten als unknown/follow-up statt erfunden behandelt werden,
- Reporting Investigation/Risk/CAPA/PMS nicht still beendet,
- eMDR Submission/Receipt nicht simuliert wird,
- konkrete Complaint-/Due-/Reportability-Zustände nicht in globales dauerhaftes Memory gelangen.
