---
name: medical-device-complaint-regulatory-routing
description: Überführt Medical-Device-/IVD-Complaint-Fakten und Awareness-Evidence frühzeitig in jurisdiction-spezifische Reportability-/Vigilance-Assessments, ohne selbst FDA-MDR-, EU-Vigilance- oder andere Behördenentscheidungen zu treffen.
userFacing: true
implicitInvocation: false
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - medical-device-complaint-handling
  - regulated-product-context
  - regulatory-evidence-traceability
outputs:
  - complaint-regulatory-routing.json
  - regulatory-awareness-timeline.json
  - vigilance-entry-handoff.json
lastEvaluated: 2026-08-08
---

# Medical Device Complaint Regulatory Routing

## Zweck und Grenze

Dieser Skill besitzt die kontrollierte **Schwelle vom Complaint Handling in jurisdiction-spezifische Vigilance-/Reportability-Assessments**. Er normalisiert Markets, Rollen, Awareness-Evidence, Safety-/Performance-Fakten und Unknowns und erzeugt parallele Handoffs an die vorhandenen Regulatory-Spezialisten.

Er entscheidet ausdrücklich **nicht** `reportable|not-reportable`, berechnet keine finale gesetzliche Due Date und übermittelt keine Behördenmeldung. FDA-MDR bleibt bei `fda-complaint-mdr-reportability`; IVDR-Vigilance bleibt bei `ivdr-pms-vigilance`. Weitere Jurisdiktionen werden als `specialist-required` geroutet, bis ein eigener Owner existiert.

## Kernprinzipien

- **Routing precedes final investigation:** mögliche regulatorische Relevanz wird aus verfügbaren Fakten und Unknowns geroutet, nicht erst nach Root Cause, Produkt-Rücklauf oder Complaint Closure.
- **One complaint, multiple jurisdiction decisions:** ein Complaint kann mehrere Markt-Assessments auslösen; Source Facts werden referenziert statt dupliziert oder gegeneinander überschrieben.
- **Awareness evidence is not awareness conclusion:** Empfangs-, Transfer- und Employee-/Function-Awareness-Fakten werden chronologisch bewahrt; die rechtliche Awareness-/Clock-Entscheidung trifft der zuständige Market-Skill.
- **No favorable backdating or forward-dating:** Timeline-Fakten werden nicht auf Complaint-Eröffnung, QA-Eingang oder Regulatory-Review verschoben, nur weil diese Zeitpunkte prozessual bequemer sind.
- **Potential seriousness bypasses completeness:** mögliche Death/Serious-Injury/Serious-Incident-/Malfunction-/False-Result-/Public-Health-Fakten werden sofort weitergereicht, auch wenn Device, Lot, Outcome oder Causality unvollständig sind.
- **Prior decisions are historical, not immunity:** ein früheres `not-reportable`, `assessment-complete`, `complaint-closed` oder `no-action` bleibt als versionierte Entscheidung erhalten, verhindert aber keine erneute Specialist-Bewertung bei neuen materiellen Fakten.
- **Material new information triggers reassessment:** neue Safety-, Outcome-, Malfunction-, False-Result-, Market-, Role- oder Remedial-Action-Fakten erzeugen pro betroffener Jurisdiktion einen neuen `reassessment-required`-State mit Referenz auf die frühere Entscheidung.
- **Non-reportability is a specialist decision:** Customer Service, Complaint Handling und dieser Router dürfen eine potenziell relevante Meldung nicht durch `not-a-complaint`, `known issue`, `user error`, `no device returned`, `customer satisfied` oder `root cause unknown` abschneiden.
- **External action remains external:** Routing/Assessment/Approval ≠ submitted/received/accepted by authority.

## Workflow

### 1. Complaint Regulatory Handoff konsumieren

Übernimm `complaint-regulatory-handoff.json` mit:

- Complaint/Contact References,
- Source-/Intake-/Transfer-Timeline,
- Device/Variant/UDI/Lot soweit bekannt,
- Markets/Distribution/Legal-Manufacturer-/Importer-/User-Facility-Kontext soweit bekannt,
- Safety/Outcome/Malfunction/False-Result-/Performance-Fakten,
- Investigation State und neue Erkenntnisse,
- Device/Evidence Availability,
- Unknowns,
- Prior Assessment/Decision References und `reassessmentTrigger` soweit vorhanden.

Der Original-Complaint-Record bleibt Source of Truth; Handoffs kopieren keine unnötigen personenbezogenen Daten.

### 2. Jurisdiktionen und Rollen bestimmen

Erzeuge pro möglichem Markt einen getrennten Routing-State:

- `US-FDA-MDR-assessment`,
- `EU-IVDR-vigilance-assessment`,
- `other-jurisdiction-specialist-required`,
- `market-or-role-unknown`.

Verifiziere Hersteller-/Importer-/Distributor-/User-Facility-/Economic-Operator-Rolle soweit für die jeweilige Pflicht relevant. Ein Vertrieb in mehreren Märkten kann mehrere parallele Handoffs benötigen.

### 3. Awareness-Timeline normalisieren

`regulatory-awareness-timeline.json` bewahrt getrennt:

- Original Event/Customer Dates soweit bekannt,
- `customerContactReceivedAt`,
- Distributor/Field-Service/Sales Transfer Times,
- früheste belegte interne Employee-/Function-Receipt-Facts,
- Complaint-System Entry,
- QA/Regulatory Receipt,
- spätere Safety-/Seriousness-/Malfunction-Erkenntnisse,
- Supplemental-/Follow-up-Receipt-Facts,
- Source References und Unsicherheit jeder Zeitangabe.

Keine dieser Tatsachen wird automatisch als finale regulatorische Awareness Date bezeichnet. Für FDA ist insbesondere zu beachten, dass aktuelle Part-803-Regeln Awareness nicht erst auf QA/Regulatory beschränken; die konkrete Rechtsanwendung bleibt beim FDA-Skill.

### 4. Escalation Threshold bestimmen

Setze `immediateSpecialistAssessmentRequired=true`, wenn die Informationen vernünftigerweise eine jurisdiction-spezifische Reportability/Vigilance-Frage auslösen können. Beispiele sind mögliche:

- Death/Serious Injury/Serious Incident,
- relevante Malfunction/Fehlfunktion,
- falsche oder fehlende IVD-Ergebnisse mit möglicher erheblicher Auswirkung,
- Field Safety/Remedial Action/Public-Health-Frage,
- wiederkehrende/trendbezogene Safety-Signale,
- unklare Causality bei gleichzeitig erheblichem Outcome.

Der Router verlangt keinen Beweis, dass das Event tatsächlich reportable ist.

### 5. Reassessment Need bei neuer Information bestimmen

Wenn bereits eine Market-Entscheidung existiert, vergleiche neue Fakten gegen deren Evidence Snapshot. Setze pro Jurisdiktion mindestens:

- `no-material-change`,
- `reassessment-required`,
- `reassessment-sent`,
- `reassessment-open`,
- `reassessment-complete`,
- `blocked|unknown`.

Ein `reassessment-required` entsteht, wenn neue Information die frühere Awareness-, Seriousness-, Malfunction-, Causality-, Remedial-Action-, Market-/Role- oder sonstige Reportability-/Vigilance-Bewertung materiell beeinflussen kann. Frühere Entscheidungen bleiben versioniert referenziert und werden nicht überschrieben.

### 6. Market-Handoffs erzeugen

Für USA → `fda-complaint-mdr-reportability` mit Complaint Reference, Product/Role Facts, Awareness Evidence, Event/Malfunction Facts, Investigation State, Prior FDA Assessment Reference, New Material Facts und Unknowns.

Für EU-IVDR → `ivdr-pms-vigilance` mit Complaint Reference, Product/Market Facts, Event/Seriousness/False-Result Facts, PMS Context Reference soweit vorhanden, Investigation State, Prior IVDR Decision Reference, New Material Facts und Unknowns.

Für andere Märkte → benenne Regulatory Owner/Specialist Need, Current-Source Requirement und `human-review-required`; erfinde keine analoge FDA-/EU-Regel.

### 7. Routing Acknowledgement verfolgen

`vigilance-entry-handoff.json` enthält pro Jurisdiktion:

- `handoffState: required|sent-to-specialist|acknowledged|assessment-open|assessment-complete|reassessment-required|reassessment-open|reassessment-complete|blocked|unknown`,
- zuständigen Specialist/Owner,
- immutable Complaint/Timeline References,
- Prior Assessment Reference,
- New Material Facts/Delta,
- Time-Criticality,
- offene Fakten/Folgeinformationen.

Complaint Closure darf bei einem erforderlichen, aber nicht bestätigten Regulatory-Handoff oder Reassessment nicht als vollständig gelten.

## Output-Verträge

`complaint-regulatory-routing.json` enthält Market/Role Scope, Routing Reason, Specialist Target, Immediate-Assessment-/Reassessment-Flag, Facts/Unknowns, Prior Assessment Reference, New Material Facts, Current Source References/`asOf` und Handoff State. Es enthält keine finale Reportability.

`regulatory-awareness-timeline.json` enthält chronologische Evidence Events mit Source, Actor/Function soweit zulässig, Timestamp/Precision, Fact Type und Confidence, einschließlich Supplemental-Evidence-Events, ohne diese automatisch zur gesetzlichen Awareness Date zu machen.

`vigilance-entry-handoff.json` ist der kontrollierte Übergabestatus vom Complaint-Prozess an FDA-/EU-/weitere Regulatory-Spezialisten und liefert Initial-/Reassessment-Acknowledgement-/Assessment-State zurück an Complaint Handling.

## Memory Path

Persistenzwürdig sind abstrahierte Routing-/Reassessment-Heuristiken, stabile Timeline-Fact-Typen und validierte jurisdiction-neutrale Escalation-Muster. Konkrete Complaints, Kunden-/Patientendaten, Employee-Awareness-Fälle, Zeitstempel, Reportability Assessments, Due Dates und Authority Submission States bleiben kontrollierte Records/run-only. Regulatory Learnings benötigen `sourceRefs`, `asOf` und `reviewAfter`; nur geeignete abstrahierte `memory-candidate-handoff-v1`-Kandidaten gehen an `communication-memory-governance`.

## Qualitätsgate

Bestanden nur wenn:

- Complaint-/Safety-Fakten frühzeitig in alle relevanten Jurisdiktionen geroutet werden,
- Investigation/Root Cause die Reportability-Eskalation nicht verzögert,
- Awareness-Evidence chronologisch erhalten und nicht mit finaler Awareness-Rechtsentscheidung verwechselt wird,
- neue materielle Fakten frühere `not-reportable`-/Assessment-/Complaint-Closure-Zustände nicht als Sperre behandeln,
- Reassessment pro Jurisdiktion versioniert und mit Prior Decision/New Evidence referenziert wird,
- FDA-/EU-/weitere Marktentscheidungen getrennte Specialist Assessments bleiben,
- `known issue`, `user error`, fehlender Rücklauf oder Kundenzufriedenheit keine mögliche regulatorische Bewertung abschneiden,
- ein Headline-Status wie `ticket closed` oder `complaint closed` keine Authority-/Reportability-Closure erzeugt,
- externe Meldung/Receipt/Acceptance niemals simuliert wird,
- konkrete Complaint-/Awareness-Daten nicht global persistiert werden.
