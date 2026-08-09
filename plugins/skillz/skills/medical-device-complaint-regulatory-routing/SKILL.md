---
name: medical-device-complaint-regulatory-routing
description: Überführt Medical-Device-/IVD-Complaint-Fakten, Customer-Follow-up und Awareness-Evidence frühzeitig in jurisdiction-spezifische Reportability-/Vigilance-Assessments, ohne selbst FDA-MDR-, EU-Vigilance- oder andere Behördenentscheidungen zu treffen.
---

# Medical Device Complaint Regulatory Routing

## Zweck und Grenze

Dieser Skill besitzt die kontrollierte **Schwelle vom Complaint Handling in jurisdiction-spezifische Vigilance-/Reportability-Assessments**. Er normalisiert Markets, Rollen, Awareness-Evidence, Customer-Follow-up-Deltas, Safety-/Performance-Fakten und Unknowns und orchestriert parallele Handoffs an die vorhandenen Regulatory-Spezialisten.

Er entscheidet ausdrücklich **nicht** `reportable|not-reportable`, berechnet keine finale gesetzliche Due Date und übermittelt keine Behördenmeldung. FDA-MDR bleibt bei `fda-complaint-mdr-reportability`; IVDR-Vigilance bleibt bei `ivdr-pms-vigilance`. Weitere Jurisdiktionen werden als `specialist-required` geroutet, bis ein eigener Owner existiert.

Der Router ist der **Complaint-origin Orchestrator**: Er ruft die zuständigen Markt-Spezialisten auf und verfolgt deren Acknowledgement-/Assessment-State. Umgekehrt dürfen diese Spezialisten nicht technisch vom Complaint-Router abhängig sein, weil sie auch aus anderen zulässigen Quellen wie PMS, Literatur, Field Signals oder bereits kontrollierten Event Records aufgerufen werden können.

Customer Follow-up ist ein Evidence-Zulieferer des Routers, **kein Gate vor dem Initial-Routing**. Ein `planned|in-progress|no-response|device-return-pending`-Follow-up darf eine bereits mögliche zeitkritische Markt-Bewertung nicht verzögern; spätere materielle Antworten erzeugen stattdessen ein versioniertes Reassessment.

## Kernprinzipien

- **Routing precedes final investigation and follow-up:** mögliche regulatorische Relevanz wird aus verfügbaren Fakten und Unknowns geroutet, nicht erst nach Root Cause, Kundenantwort, Produkt-Rücklauf oder Complaint Closure.
- **Follow-up evidence enriches, never suppresses:** `customer-followup-evidence.json` kann Facts/Unknowns ergänzen und Reassessment auslösen; `no-response`, `customer satisfied`, `replacement completed` oder fehlender Return dürfen keine Specialist-Bewertung abschneiden.
- **One complaint, multiple jurisdiction decisions:** ein Complaint kann mehrere Markt-Assessments auslösen; Source Facts werden referenziert statt dupliziert oder gegeneinander überschrieben.
- **Awareness evidence is not awareness conclusion:** Empfangs-, Transfer-, Follow-up- und Employee-/Function-Awareness-Fakten werden chronologisch bewahrt; die rechtliche Awareness-/Clock-Entscheidung trifft der zuständige Market-Skill.
- **No favorable backdating or forward-dating:** Timeline-Fakten werden nicht auf Complaint-Eröffnung, QA-Eingang oder Regulatory-Review verschoben, nur weil diese Zeitpunkte prozessual bequemer sind.
- **Potential seriousness bypasses completeness:** mögliche Death/Serious-Injury/Serious-Incident-/Malfunction-/False-Result-/Public-Health-Fakten werden sofort weitergereicht, auch wenn Device, Lot, Outcome, Customer Follow-up oder Causality unvollständig sind.
- **Prior decisions are historical, not immunity:** ein früheres `not-reportable`, `assessment-complete`, `complaint-closed` oder `no-action` bleibt als versionierte Entscheidung erhalten, verhindert aber keine erneute Specialist-Bewertung bei neuen materiellen Fakten.
- **Material new information triggers reassessment:** neue Safety-, Outcome-, Malfunction-, False-Result-, Market-, Role-, Follow-up- oder Remedial-Action-Fakten erzeugen pro betroffener Jurisdiktion einen neuen `reassessment-required`-State mit Referenz auf die frühere Entscheidung.
- **Non-reportability is a specialist decision:** Customer Service, Customer Follow-up, Complaint Handling und dieser Router dürfen eine potenziell relevante Meldung nicht durch `not-a-complaint`, `known issue`, `user error`, `no device returned`, `customer satisfied`, `no response` oder `root cause unknown` abschneiden.
- **Specialists stay reusable:** FDA- und IVDR-Spezialisten dürfen außerhalb des Complaint-Flows mit anderen kontrollierten Postmarket-/Event-Quellen arbeiten; Complaint-Provenance wird nur verlangt, wenn der Ursprung tatsächlich ein Complaint ist.
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

### 2. Customer-Follow-up-State einbeziehen

Konsumiere vom `medical-device-complaint-customer-followup` soweit vorhanden:

- `customer-followup-plan.json`,
- `customer-followup-evidence.json`,
- Follow-up Attempt/Response References,
- `followupState: not-needed|planned|in-progress|no-response|completed|blocked|unknown`,
- New Facts/Unknowns,
- Evidence Delta Classification,
- Device/Return/Preservation State,
- Prior Decision References und Reassessment Trigger.

Wenn Follow-up noch nicht durchgeführt oder unbeantwortet ist, route aus den bereits verfügbaren Complaint-Fakten weiter. Der Router wartet nicht auf einen Fragebogen oder Device Return, wenn die vorhandenen Fakten bereits eine Specialist-Bewertung erfordern.

### 3. Jurisdiktionen und Rollen bestimmen

Erzeuge pro möglichem Markt einen getrennten Routing-State:

- `US-FDA-MDR-assessment`,
- `EU-IVDR-vigilance-assessment`,
- `other-jurisdiction-specialist-required`,
- `market-or-role-unknown`.

Verifiziere Hersteller-/Importer-/Distributor-/User-Facility-/Economic-Operator-Rolle soweit für die jeweilige Pflicht relevant. Ein Vertrieb in mehreren Märkten kann mehrere parallele Handoffs benötigen.

### 4. Awareness-Timeline normalisieren

`regulatory-awareness-timeline.json` bewahrt getrennt:

- Original Event/Customer Dates soweit bekannt,
- `customerContactReceivedAt`,
- Distributor/Field-Service/Sales Transfer Times,
- früheste belegte interne Employee-/Function-Receipt-Facts,
- Complaint-System Entry,
- QA/Regulatory Receipt,
- Customer-Follow-up Attempt/Response Receipt Times,
- spätere Safety-/Seriousness-/Malfunction-Erkenntnisse,
- Supplemental-/Follow-up-Receipt-Facts,
- Source References und Unsicherheit jeder Zeitangabe.

Keine dieser Tatsachen wird automatisch als finale regulatorische Awareness Date bezeichnet. Für FDA ist insbesondere zu beachten, dass aktuelle Part-803-Regeln Awareness nicht erst auf QA/Regulatory beschränken; die konkrete Rechtsanwendung bleibt beim FDA-Skill.

### 5. Escalation Threshold bestimmen

Setze `immediateSpecialistAssessmentRequired=true`, wenn die Informationen vernünftigerweise eine jurisdiction-spezifische Reportability/Vigilance-Frage auslösen können. Beispiele sind mögliche:

- Death/Serious Injury/Serious Incident,
- relevante Malfunction/Fehlfunktion,
- falsche oder fehlende IVD-Ergebnisse mit möglicher erheblicher Auswirkung,
- Field Safety/Remedial Action/Public-Health-Frage,
- wiederkehrende/trendbezogene Safety-Signale,
- unklare Causality bei gleichzeitig erheblichem Outcome.

Der Router verlangt keinen Beweis, dass das Event tatsächlich reportable ist, und keinen abgeschlossenen Customer Follow-up.

### 6. Reassessment Need bei neuer Information bestimmen

Wenn bereits eine Market-Entscheidung existiert, vergleiche neue Complaint- oder Customer-Follow-up-Fakten gegen deren Evidence Snapshot. Setze pro Jurisdiktion mindestens:

- `no-material-change`,
- `reassessment-required`,
- `reassessment-sent`,
- `reassessment-open`,
- `reassessment-complete`,
- `blocked|unknown`.

Ein `reassessment-required` entsteht, wenn neue Information die frühere Awareness-, Seriousness-, Malfunction-, Causality-, Remedial-Action-, Market-/Role- oder sonstige Reportability-/Vigilance-Bewertung materiell beeinflussen kann. Frühere Entscheidungen bleiben versioniert referenziert und werden nicht überschrieben.

### 7. Market-Spezialisten aufrufen

Für USA → rufe `fda-complaint-mdr-reportability` mit Complaint Reference, Product/Role Facts, Awareness Evidence, Event/Malfunction Facts, Investigation State, Customer-Follow-up Evidence Delta, Prior FDA Assessment Reference, New Material Facts und Unknowns auf.

Für EU-IVDR → rufe `ivdr-pms-vigilance` mit Complaint Reference, Product/Market Facts, Event/Seriousness/False-Result Facts, PMS Context Reference soweit vorhanden, Investigation State, Customer-Follow-up Evidence Delta, Prior IVDR Decision Reference, New Material Facts und Unknowns auf.

Für andere Märkte → benenne Regulatory Owner/Specialist Need, Current-Source Requirement und `human-review-required`; erfinde keine analoge FDA-/EU-Regel.

Die Spezialisten erhalten Complaint-Provenance als Input, bleiben aber eigenständige Owner ihrer Rechts-/Vigilance-Entscheidung. Der Router darf deren Output nicht umetikettieren oder in einen eigenen Reportability-State verdichten.

### 8. Specialist Acknowledgement verfolgen

`vigilance-entry-handoff.json` enthält pro Jurisdiktion:

- `handoffState: required|sent-to-specialist|acknowledged|assessment-open|assessment-complete|reassessment-required|reassessment-open|reassessment-complete|blocked|unknown`,
- zuständigen Specialist/Owner,
- immutable Complaint/Timeline/Follow-up References,
- Prior Assessment Reference,
- New Material Facts/Delta,
- Time-Criticality,
- Specialist Assessment/Decision Reference soweit vorhanden,
- offene Fakten/Folgeinformationen.

Complaint Closure darf bei einem erforderlichen, aber nicht bestätigten Regulatory-Handoff oder Reassessment nicht als vollständig gelten. Ein interner Router-State `sent-to-specialist` ist weder Specialist-Acknowledgement noch Assessment-Completion.

## Output-Verträge

`complaint-regulatory-routing.json` enthält Market/Role Scope, Routing Reason, Specialist Target, Immediate-Assessment-/Reassessment-Flag, Complaint-/Follow-up Facts/Unknowns, Prior Assessment Reference, New Material Facts, Current Source References/`asOf` und Handoff State. Es enthält keine finale Reportability.

`regulatory-awareness-timeline.json` enthält chronologische Evidence Events mit Source, Actor/Function soweit zulässig, Timestamp/Precision, Fact Type und Confidence, einschließlich Customer-Follow-up-/Supplemental-Evidence-Events, ohne diese automatisch zur gesetzlichen Awareness Date zu machen.

`vigilance-entry-handoff.json` ist der kontrollierte Übergabestatus vom Complaint-/Follow-up-Prozess an FDA-/EU-/weitere Regulatory-Spezialisten und liefert Initial-/Reassessment-Acknowledgement-/Assessment-State zurück an Complaint Handling.

## Memory Path

Persistenzwürdig sind abstrahierte Routing-/Reassessment-Heuristiken, stabile Timeline-Fact-Typen und validierte jurisdiction-neutrale Escalation-Muster. Konkrete Complaints, Kunden-/Patientendaten, Follow-up-Antworten, Employee-Awareness-Fälle, Zeitstempel, Reportability Assessments, Due Dates und Authority Submission States bleiben kontrollierte Records/run-only. Regulatory Learnings benötigen `sourceRefs`, `asOf` und `reviewAfter`; nur geeignete abstrahierte `memory-candidate-handoff-v1`-Kandidaten gehen an `communication-memory-governance`.

## Qualitätsgate

Bestanden nur wenn:

- Complaint-/Safety-Fakten frühzeitig in alle relevanten Jurisdiktionen geroutet werden,
- Investigation/Root Cause, Customer Follow-up oder Device Return die Reportability-Eskalation nicht verzögern,
- Customer-Follow-up-Evidence referenzgebunden konsumiert wird und `no-response` keine günstige Safety-/Reportability-Interpretation erzeugt,
- Awareness-Evidence chronologisch erhalten und nicht mit finaler Awareness-Rechtsentscheidung verwechselt wird,
- neue materielle Complaint-/Follow-up-Fakten frühere `not-reportable`-/Assessment-/Complaint-Closure-Zustände nicht als Sperre behandeln,
- Reassessment pro Jurisdiktion versioniert und mit Prior Decision/New Evidence referenziert wird,
- FDA-/EU-Spezialisten tatsächlich aufgerufen und deren Acknowledgement-/Assessment-State getrennt vom Router-State verfolgt wird,
- FDA-/EU-/weitere Marktentscheidungen getrennte Specialist Assessments bleiben,
- die Markt-Spezialisten außerhalb des Complaint-Flows weiterhin mit anderen kontrollierten Event-/PMS-Quellen verwendbar bleiben,
- `known issue`, `user error`, fehlender Rücklauf, fehlende Kundenantwort oder Kundenzufriedenheit keine mögliche regulatorische Bewertung abschneiden,
- ein Headline-Status wie `ticket closed` oder `complaint closed` keine Authority-/Reportability-Closure erzeugt,
- externe Meldung/Receipt/Acceptance niemals simuliert wird,
- konkrete Complaint-/Follow-up-/Awareness-Daten nicht global persistiert werden.
