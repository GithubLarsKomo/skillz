---
name: ivdr-pms-vigilance
description: Bewertet IVDR-Post-Market-Signale und Vigilance-Fragen evidenzgebunden, zeitkritisch und mit klarer Rückkopplung in PMS, Risk, CAPA, PMPF, Performance Evaluation und Management-Attention.
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
  - medical-device-pms-system
  - medical-device-risk-management-iso14971
  - two-axis-compliance-review
  - regulatory-evidence-traceability
  - mdcg-guidance-navigator
outputs:
  - ivdr-pms-assessment.json
  - vigilance-decision-log.json
  - trend-signal-set.json
lastEvaluated: 2026-08-08
---

# IVDR PMS and Vigilance

## Zweck und Grenze

Dieser Skill strukturiert IVDR-Post-Market-Surveillance-Signale und Vigilance-/Reportability-Fragen. Er verbindet Feldinformationen mit dem kontrollierten Complaint-Regulatory-Routing, Product Context, dem übergeordneten PMS-System, Risk Management, regulatorischer Evidenz und aktuellen Melde-/Guidance-Anforderungen und erzeugt nachvollziehbare Entscheidungen, Gaps und Eskalationen.

Er führt **keine externe Behördenmeldung autonom aus**, ersetzt keine Complaint Investigation, CAPA/Ursachenanalyse und ist kein generischer Complaint-Handling-Skill. Wegen potenziell zeitkritischer regulatorischer Entscheidungen ist die automatische implizite Invocation deaktiviert. Ein fehlender oder unvollständiger PMS-Systemkontext ist ein System-Gap, darf aber eine zeitkritische Vigilance-Bewertung nicht blockieren.

## Kernprinzipien

- **Complaint provenance enters vigilance intact:** `complaint-regulatory-routing.json`, `regulatory-awareness-timeline.json` und `vigilance-entry-handoff.json` werden als referenzierte Intake-/Awareness-Evidence übernommen; Original-Complaint und personenbezogene Rohdaten werden nicht unnötig dupliziert.
- **Routing evidence ≠ IVDR conclusion:** der Router löst die Bewertung aus, entscheidet aber weder Serious Incident noch Reportability; diese Entscheidung bleibt current-source-basiert in diesem Skill.
- Melde-/Vigilance-Fragen werden fallbezogen gegen aktuelle offizielle Anforderungen geprüft; Fristen und Definitionen werden nicht als statische Zahlen im Skill konserviert.
- Unvollständige Fakten sind kein Grund, potenziell zeitkritische regulatorische Bewertung aufzuschieben: Unsicherheit und nächste sichere Aktion werden explizit dokumentiert.
- **Time-critical vigilance bypasses complaint and management cadence:** Reportability-/Authority-/Field-Action-Eskalationen warten weder auf Complaint Closure/finale Root Cause noch auf periodischen PMS Review oder Management Review.
- Complaint, Incident, Serious-Incident-Hypothese, Trend, FSCA-/Field-Action-Frage, Nonconformity und Performance Signal bleiben getrennte Klassifikationen, bis Evidenz eine Verbindung trägt.
- `known issue`, `user error`, fehlender Device-Rücklauf, Kundenzufriedenheit oder nicht etablierte Causality sind für sich allein keine Vigilance-Non-Reportability-Entscheidung.
- PMS aggregiert Datenquellen; Complaint Handling, Risk Management, PMPF, Performance Evaluation und CAPA behalten ihre jeweilige Fachlogik.
- **Material signals return to PMS:** nach der Fall-/Signalbewertung wird ein referenzgebundener Handoff an `medical-device-pms-system` erzeugt, damit der Systemzustand und der Management-Review-Input aktualisiert werden können. Routing ist keine Closure.
- **Management attention is not case duplication:** bei höher-riskanten, systemischen, trendbezogenen oder regulatorisch wesentlichen Zuständen werden `managementAttention` und Grund markiert; der Management Review erhält später den aggregierten PMS-Status statt unnötiger Patient-/Fallrohdatenduplikate.
- Jede regulatorisch relevante Entscheidung besitzt Source/Requirement References, `asOf`, Facts/Unknowns und eine Authority/Human Boundary.

## Workflow

### 1. Complaint-/Signal-Intake normalisieren

Konsumiere soweit vorhanden `complaint-regulatory-routing.json`, `regulatory-awareness-timeline.json` und `vigilance-entry-handoff.json`. Erfasse/übernehme Quelle, Zeitpunkt/Transferchronologie, Produkt/Version/Lot soweit relevant, Markt, Nutzungskontext, Ereignisbeschreibung, Outcome/Impact, bekannte Patient-/User-Auswirkungen, technische Fakten, Complaint-Investigation-State und Unknowns.

Personenbezogene Daten werden minimiert und nicht unnötig in Vigilance-Artefakte kopiert. Übernimm soweit verfügbar den aktuellen PMS-Systemkontext/Source-State; fehlt er, markiere den Gap ohne zeitkritische Bewertung zu verzögern.

### 2. Current Requirements laden

Nutze `mdcg-guidance-navigator` und autoritative Rechtsquellen für die zum Fallzeitpunkt anwendbaren Definitionen, Meldewege, Fristen, Trend-/Vigilance-Regeln und Übergangsbedingungen. Historische Guidance wird nur verwendet, wenn sie für den Ereigniszeitpunkt relevant ist.

Aktuell relevante Referenzen umfassen insbesondere IVDR Chapter VII/Post-Market Surveillance/Vigilance, aktuelle Commission/MDCG-PMS-/Vigilance-Guidance und die tatsächlich anwendbaren elektronischen/behördlichen Reporting-Prozesse. Guidance-Finality und Rechtsquelle bleiben getrennt.

### 3. Signal klassifizieren

Bewerte getrennt:

- Complaint/Feedback,
- Performance- oder Safety-Signal,
- Incident-/Serious-Incident-Potenzial,
- Trend-Hypothese,
- Field-Safety-/Corrective-Action-Frage,
- bekannte Nonconformity/Systemursache,
- fehlende Fakten/Verification Need.

Status mindestens `not-indicated|possible|likely|confirmed|not-reportable-on-current-evidence|reportability-unresolved|human-authority-action-required`.

Eine Complaint-Klassifikation oder erfolgreiche Customer Resolution ist kein Ersatz für diese Vigilance-Klassifikation.

### 4. Zeitkritik und Stop Conditions bestimmen

Bei möglicher Meldepflicht oder anderer zeitkritischer Pflicht wird der relevante Human/Regulatory Owner sofort sichtbar gemacht. Fehlende Detailinformationen, offene Complaint Investigation oder nicht etablierte Root Cause dürfen notwendige Eskalation nicht still blockieren. Der Skill behauptet keine Meldung, solange externe Ausführung nicht verifiziert ist. Complaint Closure, Management Review oder periodischer PMS Review sind niemals Vorbedingungen für diese Aktion.

### 5. Evidence/Risk-Linkage

Verknüpfe die Entscheidung über `regulatory-evidence-traceability` mit aktuellen Requirements und aktualisiere bei Bedarf `medical-device-risk-management-iso14971`. Eine neue Gefahr/Risikohöhe oder ein neuer Failure Mode wird nicht nur im Vigilance-Log belassen. Complaint Investigation bleibt beim `medical-device-complaint-handling`; offene Ursachenarbeit wird referenziert, nicht dupliziert.

### 6. Management-Attention bestimmen

Setze `managementAttention=true`, wenn der Fall/das Signal z. B. einen höher-riskanten Safety-/Quality-Sachverhalt, systemisches Muster, wesentliche Trendhypothese, offene Field-Action-/FSCA-Frage, bedeutsame Risk-/Performance-Auswirkung oder länger offenbleibenden regulatorischen High-Impact-State erzeugt. Dokumentiere `managementAttentionReason`, ohne dadurch die operative Regulatory Action zu ersetzen oder zu verzögern.

### 7. Lifecycle-, Complaint- und PMS-Routing

- Complaint-Investigation-/Follow-up-State → referenzgebundener Rückkanal zu `medical-device-complaint-handling`; Reportability-Entscheidung darf dessen Investigation aber nicht blockieren
- PMS-Systemstatus/Management-Review-Handoff → `medical-device-pms-system` mit Decision/Signal Reference, State, Management-Attention, Data Limits und Follow-up Trigger
- Performance-Frage → `ivdr-performance-evaluation` / `ivdr-pmpf`
- Trend-/PMS-Überwachung → fortgesetztes PMS mit definiertem Trigger
- systemische Nonconformity → `medical-device-capa`
- unklare Ursache → `evidence-based-causal-investigation`
- externe Human-/Authority-Aktion → `human-procedure-wizard` bzw. verantwortliche Regulatory-Funktion
- kontrollierte Records → `controlled-quality-documentation`

Ein Management Review konsumiert die aggregierte PMS-Governance-Sicht; er ist kein zweites Fall- oder Reportability-Review.

## Output-Verträge

`ivdr-pms-assessment.json` enthält Scope, Complaint-/Routing-/PMS-References, Datenquellen, Signalübersicht, Product/PMS/Risk Context, Trend-/Performance-Bewertung, offene Gaps, Management-Attention, Re-evaluation Trigger und `asOf`.

`vigilance-decision-log.json` enthält pro Fall/Entscheidung Facts, Unknowns, Complaint/Timeline References, Current Requirement References, Klassifikation, Reportability State, Time-Criticality, Human Owner, Decision Evidence, externe Action State, `managementAttention`, `managementAttentionReason`, `pmsHandoffState` und Follow-up Trigger.

`trend-signal-set.json` enthält normalisierte Signaldefinition, Baseline/Denominator soweit verfügbar, Beobachtungen, Unsicherheit, Trigger/Threshold-Logik, Confidence, Management-Attention soweit relevant und Next Action. Ein statistischer Trend wird nicht behauptet, wenn Datenbasis oder Nenner unzureichend sind.

## Memory Path

Persistenzwürdig sind validierte produktspezifische Signaldefinitionen, stabile Surveillance-Grenzen und bestätigte wiederverwendbare Entscheidungsheuristiken. Einzelne Beschwerden, Patienten-/Anwenderdaten, Awareness-/Routing-Timelines, laufende Reportability-Fälle, aktuelle Meldefrist-Snapshots, momentane Trendwerte, Management-Attention einzelner Fälle und offene Investigation-Fakten bleiben run-only. Kandidaten benötigen `sourceRefs`; regulatorische Learnings zusätzlich `asOf` und `reviewAfter`. Übergib nur abstrahierte, nicht-sensitive `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- der kontrollierte Complaint-Regulatory-Routing-Handoff und seine Timeline-Provenance konsumiert werden,
- Router/Complaint-Status nicht als IVDR-Reportability-Entscheidung missverstanden wird,
- aktuelle Requirements statt erinnerter Fristen/Definitionen verwendet werden,
- Facts, Unknowns und regulatorische Interpretation getrennt sind,
- potenziell zeitkritische Fälle nicht auf Complaint Closure, vollständige Ursachenklärung, periodischen PMS Review oder Management Review warten,
- `known issue`, `user error`, fehlender Rücklauf oder Kundenzufriedenheit mögliche Vigilance-Bewertung nicht abschneiden,
- externe Meldung/Behördenaktion nicht simuliert wird,
- Risk/PMPF/Performance/CAPA-Rückkopplung korrekt geroutet ist,
- material relevante Vigilance-/Trend-/High-Impact-Zustände mit Decision Reference zurück in `medical-device-pms-system` gelangen und dort nicht still verloren gehen,
- Management-Attention nicht mit externer Meldung, Closure oder Managemententscheidung verwechselt wird,
- Trends ohne ausreichende Datenbasis nicht behauptet werden,
- unnötige einzelne Fall-/Patientendaten nicht in Management-Review-Handoffs oder dauerhaftes Memory gelangen.
