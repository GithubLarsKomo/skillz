---
name: medical-device-field-action-communication
description: Plant, kontrolliert und evidenziert Medical-Device-/IVD-Field-Action-, FSN- und Recall-Kommunikation über Kunden, Distributoren und Downstream-Empfänger, ohne Versand, Zustellung, Acknowledgement oder Maßnahmenabschluss zu simulieren.
userFacing: true
implicitInvocation: false
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - regulated-product-context
  - quality-record-integrity
  - controlled-quality-documentation
outputs:
  - field-action-recipient-scope.json
  - field-action-notice-package.json
  - field-action-communication-state.json
lastEvaluated: 2026-08-08
---

# Medical Device Field Action Communication

## Zweck und Grenze

Dieser Skill besitzt den **kontrollierten Kommunikationsübergang einer bereits fachlich/regulatorisch definierten Field Action** zu Kunden, Gesundheitseinrichtungen, Laboren, Distributoren, Importeuren, Servicepartnern oder anderen betroffenen Empfängern. Er ist jurisdiktionsübergreifend für EU-FSCA/FSN, FDA Recall/Correction/Removal und vergleichbare kontrollierte Field-Action-Pfade einsetzbar.

Er entscheidet **nicht**, ob eine FSCA, ein FDA-806-Report, ein Recall oder eine andere regulatorische Feldmaßnahme erforderlich ist. Diese Entscheidung muss aus einem autorisierten, versionierten Action Source Package stammen, z. B. `ivdr-field-safety-corrective-action` oder `fda-corrections-removals`. Der Skill sendet Kommunikation nicht autonom und ersetzt weder CRM/ERP/Distribution Records noch `human-procedure-wizard` für irreversible/externe Aktionen.

## Kernprinzipien

- **No action source, no release:** ohne kontrollierte Field-Action-ID, Scope-Version, Notice-/Instruction-Version und Release-/Authority-Preconditions gibt es keinen produktiven Kommunikations-Release.
- **Recipient scope is evidence, not a mailing list:** Sales-/CRM-Kontakte sind Quellen, aber kein Beweis vollständiger Distribution. Distribution-, Shipment-, Consignee-, Distributor-/Importer- und Downstream-Evidence werden reconciled.
- **One population, versioned:** die betroffene Recipient Population besitzt Version und Cut-off; spätere neue Empfänger erweitern den Scope statt die frühere Liste still umzuschreiben.
- **Sent ≠ delivered:** ein Send-/Dispatch-Event beweist nur die Übermittlung an einen Kanal.
- **Delivered ≠ acknowledged:** technische Zustellung beweist nicht, dass der verantwortliche Empfänger den Safety Content zur Kenntnis genommen hat.
- **Acknowledged ≠ action completed:** eine Antwort oder Empfangsbestätigung beweist nicht Quarantine, Stop-Use, Return, Correction, Destruction, Software Update oder andere geforderte Maßnahme.
- **Verbal contact needs a record:** Telefonat, Außendienst- oder Servicekontakt zählt nur mit nachvollziehbarer Identität, Zeitpunkt, kontrollierter Message Version und dokumentiertem Ergebnis.
- **Downstream distribution remains in scope:** ein Distributor-/Kunden-Acknowledgement beendet die Verantwortung nicht, wenn betroffene Produkte weiterverteilt wurden.
- **Translation cannot change safety meaning:** lokalisierte Inhalte müssen auf freigegebenen Master Content rückführbar sein; Risiko und Required Actions dürfen nicht abgeschwächt werden.
- **Commercial priority cannot reorder safety:** Umsatz, Account Tier oder Relationship Value bestimmen weder Empfängerpriorität noch Eskalation bei Safety Actions.
- **Communication evidence is immutable:** Korrekturen ergänzen den Verlauf; fehlgeschlagene Sendungen, Bounces, falsche Kontakte und Re-Sends werden nicht überschrieben.
- **No response remains unresolved:** Nichtantwort wird nicht als `no affected product`, `action completed` oder `customer informed` interpretiert.

## Zulässige Action Sources

Mindestens einer der folgenden kontrollierten Source Types muss referenziert sein:

- `EU-IVDR-FSCA`,
- `FDA-correction-removal`,
- `FDA-recall`,
- `other-authorized-field-action` mit klarer Owner-/Requirement-Provenance.

Der Skill erzeugt keine eigene Reportability-/Recall-/FSCA-Klassifikation, falls der Source State unklar ist. Er setzt dann `releaseBlocked=true` außer notwendige dringliche Safety-Kommunikation ist durch den fachlich/regulatorisch autorisierten Owner explizit freigegeben.

## Workflow

### 1. Field-Action-Source übernehmen

Erfasse:

- `fieldActionId`,
- Jurisdiction/Market,
- Decision/Action Source Reference,
- Action Scope Version,
- Device/UDI/Lot/Serial/Software Scope soweit relevant,
- Market/Country Scope,
- Master Notice/Instruction Version,
- Release-/Authority Preconditions,
- Urgency,
- Required Recipient Action,
- Requested Response/Acknowledgement,
- Due-/Escalation Conditions.

Widersprechen Source Package und aktuelle Notice Version einander, wird nicht versandt, sondern der Konflikt an den Action Owner zurückgegeben.

### 2. Recipient Population aufbauen

Nutze soweit vorhanden:

- Distribution-/Shipment Records,
- Consignee-/Sold-To-/Ship-To-Daten,
- Distributor-/Importer-Records,
- installierte Basis/Service Registry,
- RMA-/Replacement-/Loaner-Daten,
- relevante CRM-/Contact Records,
- bekannte Downstream-Distribution,
- bereits zurückgeholte/korrigierte Einheiten.

Erzeuge pro Population Version:

- Inclusion/Exclusion Rule,
- Data Sources,
- Cut-off,
- deduplizierte Recipient Entity,
- Device/Shipment Link soweit möglich,
- Contactability State,
- downstream-distribution status,
- unknown/unreconciled population.

Fehlende/inkonsistente Distribution Evidence wird als Scope Gap geführt und nicht durch CRM-Vollständigkeitsannahmen ersetzt.

### 3. Recipient und Contact Route normalisieren

Trenne mindestens:

- Legal/Operational Recipient Entity,
- Physical Site,
- Contact Person/Role,
- Primary/Backup Channel,
- Distributor/Importer/Direct User Role,
- Language,
- Country,
- downstream obligation,
- privacy/minimum-necessary context.

Personenbezogene Daten werden nur soweit für die Safety-Kommunikation erforderlich verarbeitet; keine unnötigen Patientendaten werden in Communication Records kopiert.

### 4. Notice Package kontrollieren

`field-action-notice-package.json` enthält:

- Field Action/Scope Version,
- Master Content Reference,
- freigegebene sprach-/landesspezifische Version,
- Recipient Role,
- Required Action,
- Acknowledgement/Reply Requirement,
- Downstream Forwarding Instruction,
- Attachments/Forms,
- Release Preconditions,
- Approval/Authority Comment References,
- valid-from/superseded state.

Eine superseded Notice Version darf nicht neu ausgesendet werden. Re-Sends referenzieren die tatsächlich verwendete kontrollierte Version.

### 5. Ausführung über Evidence States führen

Jeder Kommunikationsversuch besitzt einen append-only Event Record mit mindestens:

- `communicationEventId`,
- Recipient/Scope Version,
- Notice Version,
- Channel,
- `preparedAt`,
- `approvedAt` nur mit Approval Evidence,
- `sentAt` nur mit Dispatch Evidence,
- `deliveredAt` nur mit Delivery Evidence,
- `acknowledgedAt` nur mit Recipient Evidence,
- `responseRef`,
- `requiredActionState`,
- Failure/Bounce/Return Reason,
- Next Attempt/Escalation.

Statusmodell mindestens:

`planned|release-blocked|approved|sent-unverified|sent|delivery-confirmed|delivery-failed|acknowledged|response-received|action-reported|action-evidence-received|escalated|superseded`.

### 6. Non-Responder und Delivery Failure behandeln

Bei Bounce, unzustellbarer Post, falschem Kontakt, geschlossenem Standort, Nichtantwort oder unbekannter Zuständigkeit:

- Evidence erhalten,
- alternative kontrollierte Kontaktquelle suchen,
- erneute Kontaktaktion versionieren,
- ggf. Distributor/Importer/Service/Field Organization einbeziehen,
- Eskalationsregel aus dem Field Action Plan anwenden,
- unresolved status offen halten.

`attempted=true` ist kein Ersatz für `informed=true`.

### 7. Downstream Distribution erfassen

Wenn ein Empfänger weiterverteilt hat:

- Downstream Population referenzieren oder anfordern,
- Weiterleitungs-/Direct-Notification-State erfassen,
- Scope-Erweiterung an den Action Owner zurückgeben, wenn neue Empfänger/Regionen sichtbar werden,
- direkte und indirekte Communication Coverage getrennt halten.

Eine pauschale Distributor-Bestätigung ersetzt keinen erforderlichen Nachweis über betroffene Downstream-Empfänger.

### 8. Responses als kontrollierte Evidence übernehmen

Empfängerantworten werden nicht nur als Freitext abgelegt, sondern getrennt in:

- Receipt/Acknowledgement,
- affected-product possession,
- quantity/scope response,
- downstream distribution,
- action reported,
- action evidence,
- new incident/complaint/safety information,
- contradiction/unknown.

Neue Safety-/Incident-/Complaint-Fakten werden sofort an die zuständigen Complaint-/Vigilance-/MDR-Owner geroutet; Communication Follow-up darf diese Reassessment-Linie nicht blockieren.

### 9. Handoff an Effectiveness erzeugen

Übergebe an `medical-device-field-action-effectiveness`:

- versionierte Recipient Population,
- Communication Events,
- Delivery/Acknowledgement States,
- Required Action States,
- Downstream Population,
- unresolved recipients,
- evidence gaps,
- actual Notice Versions,
- scope extensions/new safety facts.

Der Effectiveness-Skill entscheidet nicht rückwirkend, ob ein Versand stattgefunden hat; er konsumiert nur verifizierte Communication Evidence.

## Output-Verträge

`field-action-recipient-scope.json` enthält Field Action/Scope Version, Population Rules, Data Sources/Cut-off, Recipients, Downstream State, Reconciliation Gaps und Scope Extension Candidates.

`field-action-notice-package.json` enthält kontrollierte Notice-/Instruction-Versionen, Sprache/Land, Release/Approval/Authority Preconditions, Required Action, Response/Forwarding Requirements und Supersession State.

`field-action-communication-state.json` enthält append-only Communication Events und getrennte States für prepared/approved/sent/delivered/acknowledged/action-reported/action-evidence, Failure/Escalation und New Safety Facts.

## Memory Path

Persistenzwürdig sind abstrahierte Recipient-Reconciliation-Patterns, sichere Communication-State-Machines, validierte Downstream-/Non-Responder-Eskalationsmuster und Translation-Control-Heuristiken. Konkrete Kunden-/Kontakt-/Adress-/Device-/Shipment-/Lot-/Communication-/Response-Daten und laufende Field Actions bleiben ausschließlich kontrollierte Records/run-only.

Nur abstrahierte `memory-candidate-handoff-v1`-Kandidaten ohne personen-/kundenbezogene Details werden an `communication-memory-governance` übergeben.

## Qualitätsgate

Bestanden nur wenn:

- eine kontrollierte Field-Action-/Notice-Quelle vor produktivem Release existiert,
- Recipient Scope aus Distribution-/Consignee-Evidence abgeleitet und versioniert ist,
- CRM/Sales-Daten nicht allein als vollständiger Distribution Proof gelten,
- `sent`, `delivered`, `acknowledged` und `action completed/evidenced` strikt getrennt bleiben,
- Bounces/Failures/Non-Responses nicht als erfolgreiche Information umgedeutet werden,
- Downstream Distribution nicht durch Distributor-Acknowledgement abgeschnitten wird,
- jede externe Communication Event Version/Evidence besitzt,
- superseded Notices nicht unkontrolliert weiterverwendet werden,
- Übersetzungen Risiko und Required Actions nicht abschwächen,
- kommerzielle Priorität Safety-Reihenfolge nicht beeinflusst,
- neue Safety Facts unverzüglich Reassessment triggern und nicht auf Communication Closure warten,
- der Skill weder FSCA/Recall/806-Reportability noch Effectiveness/Authority Closure selbst behauptet,
- konkrete Customer-/Recipient-Daten nicht in globales dauerhaftes Memory gelangen.
