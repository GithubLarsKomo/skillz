---
name: medical-device-service-report-quality-routing
description: Überführt Medical-Device-/IVD-Service-, Repair- und Troubleshooting-Ereignisse evidenztreu in Quality-/Complaint-/Safety-Routing, ohne Serviceabschluss mit Qualitäts- oder regulatorischer Closure zu verwechseln.
userFacing: true
implicitInvocation: true
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - medical-device-customer-contact-intake
  - quality-record-integrity
outputs:
  - service-event-quality-record.json
  - service-quality-routing.json
  - service-complaint-handoff.json
lastEvaluated: 2026-08-08
---

# Medical Device Service Report Quality Routing

## Zweck und Grenze

Dieser Skill besitzt den kontrollierten Übergang von **Service, Repair, Field Service und Troubleshooting** in die Quality-/Complaint-Kette. Er verhindert, dass ein als Servicefall gestartetes Ereignis wegen erfolgreicher Reparatur, Ersatz, Kalibrierung, Reinigung, Software-Reset oder Ticketabschluss aus Complaint-/Safety-Betrachtung herausfällt.

Er ersetzt weder den allgemeinen Kundenkontakt-Intake noch Complaint Investigation, CAPA, Risk Management, PMS, FDA MDR oder EU/IVDR Vigilance. Er bewertet ausschließlich, welche Service-Evidenz erhalten werden muss und welche Quality-/Complaint-/Safety-Handoffs aus dem Serviceereignis entstehen.

## Kernprinzipien

- **Service label is not a quality conclusion:** Tickettyp, Servicecode oder kommerzielle Einstufung entscheiden nicht, ob eine Complaint oder ein Safety-Signal vorliegt.
- **Preserve before repair:** soweit praktikabel werden Vorzustand, Konfiguration, Fehlermeldungen, Logs, Fotos, Software-/Firmwarestand, Verbrauchsmaterial-/Lotbezug und relevante Mess-/QC-Daten vor Veränderung referenziert oder gesichert.
- **Repair success is not root cause:** eine erfolgreiche Reparatur oder ein Teiletausch beweist weder Ursache noch Nicht-Reportability.
- **No destructive convenience:** potenziell relevante Evidenz wird nicht allein zur schnelleren Wiederinbetriebnahme zerstört, überschrieben oder zurückgesetzt, ohne Preservation-/Decision-State.
- **Safety bypasses service SLA:** mögliche Death-/Serious-Injury-/Serious-Incident-/False-Result-/gefährliche Malfunction-Fakten werden unverzüglich in den bestehenden Complaint-/Regulatory-Pfad gegeben; Serviceanalyse darf diesen Pfad nicht blockieren.
- **One event, parallel tracks:** Kundenservice, Gerätewiederherstellung, Complaint Handling, Investigation und regulatorische Bewertung können gleichzeitig laufen.
- **Service completion ≠ complaint closure:** `serviceCompleted=true` oder `deviceOperational=true` hat keine automatische Wirkung auf Complaint-, Investigation-, CAPA-, Risk- oder Regulatory-State.
- **Follow-up is new evidence:** spätere Servicebesuche, Remote-Logs, Ersatzteilbefunde oder Werkstattberichte werden als neue Evidence Events mit eigener Source/ReceivedAt geführt.
- **Unknown remains unknown:** fehlende Pre-Service-Daten, fehlendes Gerät oder bereits veränderte Konfiguration werden als Evidence Gap dokumentiert, nicht rekonstruiert.

## Trigger

Nutze den Skill, wenn ein Kunden-/Distributor-/Field-Service-Kontakt technische Diagnose, Reparatur, Wartung, Austausch, Remote-Service, Software-/Firmwareeingriff oder vergleichbare Gerätebearbeitung enthält und ein möglicher Produkt-, Performance-, Labeling-, Safety- oder Complaint-Bezug nicht sicher ausgeschlossen ist.

## Voraussetzungen

- kontrollierter Kontakt- oder Service-Source-Record soweit vorhanden,
- nachvollziehbare Zeit-/Source-Referenzen,
- Serviceaktion und Produktbezug soweit bekannt,
- `quality-record-integrity` für unveränderliche Quellen, Ergänzungen und Korrekturen.

Fehlende Voraussetzungen blockieren keine zeitkritische Safety-Eskalation.

## Ablauf

### 1. Serviceevent fixieren

Erfasse mindestens:

- `serviceEventId`, Related Contact/Ticket/Complaint IDs,
- `receivedAt`, Service Start/End soweit bekannt,
- Produkt/Device/Variant/UDI/Serial/Lot soweit bekannt,
- Problemnarrativ und Original Source Reference,
- Pre-Service Condition und bekannte Auswirkungen,
- geplante und tatsächlich ausgeführte Service Actions,
- beteiligte Teile/Software/Consumables soweit relevant,
- bekannte Patient-/User-/Result-Auswirkungen,
- bereits vorhandene Safety-/Complaint-Flags und Unknowns.

### 2. Evidence-Preservation Gate setzen

Bestimme vor verändernden Eingriffen `preservationState: not-needed|requested|preserved|partially-preserved|not-possible-with-rationale|unknown`.

Besonders schützenswert sind soweit fallrelevant:

- Error-/Audit-/Application-/Instrument-Logs,
- Screenshots/Fotos,
- Software-/Firmware-/Konfigurationsstände,
- QC-/Kalibrations-/Messdaten,
- Gerät, Modul oder ausgetauschtes Teil,
- Reagenz-/Lot-/Consumable-Bezug,
- Service-Messwerte und reproduzierbare Fehlersymptome.

Wenn eine sofortige Intervention aus Safety- oder Versorgungsgründen erforderlich ist, dokumentiere Grund und vor der Veränderung tatsächlich gesicherte Evidenz; Preservation darf notwendige Safety-Maßnahmen nicht verhindern.

### 3. Quality-Relevanz multi-label klassifizieren

Erlaube parallel:

- `routine-service`,
- `service-support`,
- `possible-complaint`,
- `confirmed-complaint`,
- `potential-safety-event`,
- `possible-nonconformity`,
- `supplemental-evidence`,
- `reopen-candidate`,
- `unknown`.

Ein Event kann technisch erfolgreich abgeschlossen und trotzdem `possible-complaint` oder `potential-safety-event` sein.

### 4. Service-zu-Complaint-Handoff erzeugen

Erzeuge `service-complaint-handoff.json`, sobald der Servicebericht Tatsachen enthält, die eine mögliche Unzufriedenheit, Fehlfunktion, Nichtkonformität, Performanceabweichung, falsches/fehlendes IVD-Ergebnis oder Safety-Auswirkung betreffen können.

Der Handoff enthält nur notwendige Facts/Unknowns/Source References, einschließlich Pre-/Post-Service State und durch die Serviceaktion veränderter Evidenz. Die finale Complaint-Klassifikation bleibt bei `medical-device-complaint-handling`.

### 5. Safety-Bypass auslösen

Setze `immediateQualitySafetyEscalation=true`, sobald verfügbare Fakten vernünftigerweise eine zeitkritische Reportability-/Vigilance-Frage auslösen können. Der Skill wartet dafür nicht auf:

- Abschluss der Reparatur,
- reproduzierten Fehler,
- Root Cause,
- Rücksendung des Geräts,
- vollständige Lot-/UDI-Daten,
- Freigabe des Serviceberichts.

Nutze den bestehenden Complaint-/Regulatory-Routing-Pfad; erfinde keine eigene Reportability-Entscheidung.

### 6. Post-Service Evidence Delta dokumentieren

Trenne:

- beobachteten Ausgangszustand,
- ausgeführte Intervention,
- danach beobachteten Zustand,
- Hypothese zur Ursache,
- verifizierte Ursache, falls tatsächlich belegt,
- neue materielle Informationen,
- durch Intervention nicht mehr verfügbare Evidenz.

`problemResolvedAfterAction` ist eine Beobachtung, keine automatische Kausalitätsbestätigung.

### 7. Folgeinformationen routen

Spätere Werkstatt-/Supplier-/Field-Service-Befunde werden als neue Evidence Events referenziert. Materielle neue Fakten können Complaint Investigation, Risk/CAPA/PMS und regulatorische Reassessment-Pfade erneut öffnen.

## Prüfungen

Prüfe vor Abschluss des Service-Quality-Routings:

- wurden Originalquelle und Pre-Service-Fakten von späterer Interpretation getrennt,
- ist jeder verändernde Eingriff nachvollziehbar,
- ist Evidence Loss explizit statt unsichtbar,
- wurden Complaint-/Safety-Trigger unabhängig vom Serviceerfolg bewertet,
- wurde ein notwendiger zeitkritischer Handoff nicht auf Serviceabschluss verschoben,
- sind `serviceCompleted`, `customerResolved`, `complaintClosed` und Regulatory State getrennt.

## Fehlerbehandlung

- Bereits repariert/reset ohne Preservice-Evidenz → `evidenceGap=true`; keine nachträgliche Rekonstruktion als Fakt.
- Gerät nicht verfügbar → Investigation-/Evidence Gap dokumentieren; Complaint-/Safety-Routing läuft weiter.
- Servicebericht widerspricht Kundenangabe → beide Quellen erhalten, Konflikt markieren, nicht zusammenrechnen.
- Known Service Bulletin → Referenz als Evidence nutzen, aber nicht automatisch Root Cause oder Non-Reportability ableiten.
- Ticket bereits geschlossen → neue materielle Serviceevidenz als Supplemental Event/Reopen Candidate routen.

## Übergabe

- Complaint-/Investigation-Relevanz → `medical-device-complaint-handling` über `service-complaint-handoff.json`.
- mögliche zeitkritische regulatorische Relevanz → bestehender Complaint-/Regulatory-Routing-Pfad unverzüglich parallel.
- systemische Ursache → nachgelagert `medical-device-capa` / `evidence-based-causal-investigation`.
- neue/erhöhte Risiken → `medical-device-risk-management-iso14971`.
- aggregierbare Servicequalität → `medical-device-pms-system`; dieser Skill behauptet selbst keinen Trend.

## Output-Verträge

`service-event-quality-record.json` enthält Source-/Timeline-Referenzen, Product/Service Context, Pre-Service State, Service Actions, Post-Service State, Preservation State, Evidence Gaps, Facts/Unknowns und Related Case References.

`service-quality-routing.json` enthält Quality Labels, Complaint/Safety Flags, `immediateQualitySafetyEscalation`, Evidence-Preservation-/Loss-State, New Material Facts und Owner/Handoff States.

`service-complaint-handoff.json` enthält den für Complaint Handling notwendigen Service-Evidence-Snapshot ohne finale Complaint-/Reportability-Entscheidung.

## Memory Path

Persistenzwürdig sind abstrahierte Service-zu-Quality-Trigger, validierte Preservation-Muster und wiederverwendbare Service-Evidence-Kategorien. Konkrete Kunden-/Geräte-/Serien-/Lotdaten, Serviceberichte, Logs, Ereignisse, Safety-Signale und laufende Complaint-/Regulatory-Zustände bleiben run-only bzw. in kontrollierten Service-/Quality-Records. Nur geeignete abstrahierte `memory-candidate-handoff-v1`-Kandidaten gehen an `communication-memory-governance`.

## Abschlusskriterien

Bestanden nur wenn:

- ein Servicecode oder erfolgreicher Repair niemals selbst Complaint-/Safety-Relevanz ausschließt,
- Pre-Service-Evidenz soweit praktikabel vor verändernden Eingriffen geschützt wird,
- Evidence Loss sichtbar und begründet bleibt,
- Repair Success nicht als Root Cause oder Non-Reportability ausgegeben wird,
- mögliche Safety-Fakten den Serviceprozess zeitkritisch umgehen können,
- Service Completion, Customer Resolution, Complaint Closure und Regulatory Closure getrennt bleiben,
- spätere Serviceevidenz als neues Evidence Event Reassessment auslösen kann,
- der Skill keinen eigenen Complaint-, CAPA-, Trend- oder Vigilance-Entscheidungsprozess dupliziert.
