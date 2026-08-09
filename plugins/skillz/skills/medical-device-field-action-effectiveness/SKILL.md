---
name: medical-device-field-action-effectiveness
description: Bewertet die tatsächliche Wirksamkeit und Closure-Readiness von Medical-Device-/IVD-Feldmaßnahmen anhand von Recipient-, Communication-, Action-, Product-Reconciliation- und Follow-up-Evidence, ohne CAPA-Effektivität oder Authority-Termination zu simulieren.
---

# Medical Device Field Action Effectiveness

## Zweck und Grenze

Dieser Skill besitzt den **operativen Effectiveness- und Closure-Readiness-Übergang** einer Medical-Device-/IVD-Feldmaßnahme. Er prüft, ob die definierte Recipient Population tatsächlich ausreichend erreicht wurde, ob geforderte Maßnahmen umgesetzt und evidenziert sind, ob betroffene Produkte/Installationen reconciled wurden und welche Gaps einer belastbaren Closure noch entgegenstehen. Verifizierte Unit-/Custody-/Quarantine-/Correction-/Disposition-Evidence wird aus `medical-device-field-action-physical-execution` konsumiert und hier nicht rückwirkend erfunden.

Er ersetzt weder jurisdiction-spezifische FSCA-/Recall-/806-Entscheidungen noch `medical-device-capa`-Effectiveness, Risk Management oder Authority Termination. Insbesondere gilt für FDA Recall States: interne `completed`-/`closure-ready`-Bewertung ist **nicht** gleichbedeutend mit einer von FDA erklärten `terminated` Recall. Für EU-FSCA werden Authority-/Final-Report-/Closure-Prozesse current-source-basiert und extern evidenziert geführt.

## Kernprinzipien

- **Effectiveness is outcome evidence, not activity count:** Anzahl gesendeter Notices oder Contact Attempts beweist keine Wirksamkeit.
- **Communication coverage ≠ action coverage:** Information des Empfängers und Durchführung der geforderten Correction/Removal/Stop-Use/Return-Aktion sind getrennte Nenner.
- **Action reported ≠ action verified:** eine Selbstauskunft kann ein Evidence Input sein, ersetzt aber nicht automatisch den vom Action Plan geforderten Nachweis.
- **Physical execution evidence is authoritative for unit state:** Return, Quarantine, Correction, Verification, Release und Destruction werden aus dem kontrollierten Physical-Execution-Ledger übernommen; Effectiveness darf diese Zustände nicht aus Communication-Antworten ableiten.
- **Denominator before percentage:** Prozentwerte sind nur belastbar, wenn Population/Recall Depth/Field-Action Scope ausreichend definiert und versioniert sind.
- **Jurisdiction strategy governs checking method:** FDA-Effectiveness-Check-Level, Sampling oder andere Marktanforderungen werden aus dem autorisierten aktuellen Recall/Field-Action-Plan übernommen; der Skill erfindet keine eigene Check-Stufe.
- **Sample adequacy must be justified:** ein Sample beweist nur das, was Sampling Design, Population und Response Bias tragen. Non-Responder werden nicht aus dem Nenner entfernt, um Effectiveness zu verbessern.
- **Downstream population cannot disappear:** weiterverteilte Devices/Recipients bleiben Teil der Reconciliation bis ihr State begründet aufgelöst ist.
- **Product reconciliation is separate from contact reconciliation:** Units shipped, on hand, returned, destroyed, corrected, quarantined, not located und unknown müssen nachvollziehbar auf Distribution Scope zurückgeführt werden.
- **No-new-complaints is not an effectiveness check:** fehlende neue Beschwerden beweisen weder Notification Receipt noch Corrective Action Completion.
- **CAPA effectiveness ≠ field-action effectiveness:** systemische Ursachenvermeidung und Feldmaßnahmen-Execution werden separat bewertet und später verknüpft.
- **New incidents bypass closure:** neue Safety Facts während der Aktion gehen sofort an Complaint/Vigilance/MDR/Risk; hohe Coverage oder fast fertige Closure blockiert kein Reassessment.
- **Closure readiness ≠ authority closure:** interne Readiness, Antrag/Final Report, Authority Review und tatsächliche Termination/Closure sind getrennte Evidenzzustände.
- **Residual unknowns are explicit:** `not located`, `no response`, `unknown disposition` und `unverified correction` werden nicht pauschal in completed umgedeutet.

## Workflow

### 1. Action Strategy und Population Snapshot übernehmen

Konsumiere:

- Field Action ID/Jurisdiction,
- Action/Recall/FSCA Scope Version,
- Recipient Population Version,
- Recall Depth/Target Population soweit anwendbar,
- Effectiveness Check Strategy/Level/Sampling Plan soweit vorgegeben,
- Required Recipient Actions,
- Communication Events,
- Physical Execution Plan/Unit Custody/Disposition Evidence,
- Downstream Distribution State,
- Product/Shipment/Installed Base Data,
- Due-/Status-Reporting-Anforderungen,
- Prior Effectiveness Assessments.

Wenn Strategy oder Population nach Start erweitert wurde, werden frühere Assessments historisch erhalten und gegen die neue Version neu gerechnet.

### 2. Effectiveness-Dimensionen definieren

Trenne mindestens:

1. `notificationReach` – relevante Empfänger erreicht,
2. `acknowledgement` – Kenntnisnahme/Response soweit erforderlich,
3. `requiredActionCompletion` – geforderte Maßnahme durchgeführt,
4. `actionVerification` – Maßnahme ausreichend belegt,
5. `downstreamCoverage` – Weiterverteilung aufgelöst,
6. `productReconciliation` – betroffene Units/Installationen dispositioniert/korrigiert,
7. `safetyOutcomeMonitoring` – neue relevante Safety Facts während Execution,
8. `regulatoryStatusReporting` – erforderliche Status-/Final-/Termination-Handoffs.

Keine Dimension darf durch eine andere implizit ersetzt werden.

### 3. Denominators versionieren

Erzeuge je Dimension:

- Population Definition,
- Scope Version,
- Numerator,
- Denominator,
- Unknown Count,
- Exclusion Count + Reason/Evidence,
- Cut-off Date,
- Data Sources,
- Confidence/Data Quality.

Ein veränderter Scope erzeugt neue Denominators; historische Kennzahlen bleiben nachvollziehbar.

### 4. Effectiveness Check durchführen/bewerten

Wenn der autorisierte Field-Action-/Recall-Plan ein bestimmtes Checking-Verfahren vorgibt, prüfe dessen Durchführung gegen den Plan.

Bei Sample-basierten Checks dokumentiere mindestens:

- Sampling Basis,
- Population/Strata,
- Sample Size,
- Selection Method,
- Non-Response,
- Ergebnis,
- erkennbare Bias-/Coverage-Grenzen.

Bei Census/100%-Tracking bleibt jeder unresolved Recipient/Device explizit. Eine intern gewünschte Zielquote ersetzt keine regulatorisch/strategisch festgelegte Methode.

### 5. Required Action Verification prüfen

Pro Recipient/Unit/Site je nach Action Plan:

- `not-applicable-with-evidence`,
- `not-started`,
- `reported-complete`,
- `evidence-received`,
- `verified-complete`,
- `partially-complete`,
- `failed`,
- `unknown`,
- `not-located`.

Geeignete Evidence kann z. B. Return/Destruction Records, Service-/Software-/Configuration Logs, Quarantine Confirmation, Inventory Reconciliation oder andere kontrollierte Nachweise umfassen. Physische Unit-/Disposition-Zustände stammen aus `medical-device-field-action-physical-execution`. Welche Evidence ausreichend ist, folgt dem Action Plan und anwendbaren Requirements, nicht einer pauschalen globalen Regel.

### 6. Product Reconciliation erstellen

`field-action-product-reconciliation.json` reconciled soweit anwendbar:

- distributed quantity/population,
- inventory/stock still under control,
- customer/site possession,
- returned,
- destroyed,
- corrected/updated/retrofitted,
- quarantined,
- transferred/downstream,
- not located,
- unknown disposition,
- duplicates/data conflicts.

Summenunterschiede bleiben Reconciliation Gaps und werden nicht durch Rundung oder pauschale `other`-Buckets unsichtbar gemacht.

### 7. New Safety Facts und Scope Drift überwachen

Neue Incidents/Complaints, unexpected failure after correction, zusätzliche betroffene Lots/Serials/Versions oder neue Länder lösen unverzüglich:

- Complaint-/MDR-/Vigilance-Reassessment,
- Risk Update,
- ggf. FSCA/Recall Scope Extension,
- Communication Population Update,
- CAPA/Investigation Feedback aus.

Der aktuelle Effectiveness-Prozentsatz darf diese Eskalation nicht verzögern.

### 8. Field-Action- vs CAPA-Effectiveness trennen

Dokumentiere getrennt:

- Feldmaßnahme erreicht/korrekt umgesetzt?
- Produkt-/Empfängerscope ausreichend bearbeitet?
- CAPA verhindert Wiederauftreten/systemische Ursache?

Eine wirksame Rückholung kann trotz unwirksamer CAPA vorliegen und umgekehrt. Closure-Readiness muss die jeweils erforderlichen offenen Cross-References sichtbar machen.

### 9. Closure-Readiness bestimmen

Status mindestens:

- `not-ready`,
- `progressing-with-gaps`,
- `operationally-complete-pending-regulatory-state`,
- `ready-for-final-status-report`,
- `ready-for-termination-or-closure-request`,
- `authority-review-pending`,
- `authority-closed-verified`.

`authority-closed-verified` darf nur gesetzt werden, wenn die zuständige externe Authority/Prozess-Evidence tatsächlich vorliegt. Für FDA wird ein interner Recall nicht als `terminated` bezeichnet, bevor FDA diesen State bestätigt hat.

### 10. Closure Package und Rückkopplung

`field-action-closure-readiness.json` enthält:

- Scope/Population Versions,
- Effectiveness Summary,
- unresolved Recipients/Units,
- Product Reconciliation,
- new Safety Facts,
- Risk/CAPA/PMS Links,
- required status/final reporting dependencies,
- Authority Action State,
- Closure Recommendation + Human Owner,
- Reopen Trigger.

Nach Abschluss fließen aggregierbare Lessons/Outcome-Daten in PMS/Risk/CAPA zurück. Konkrete Customer-/Recipient-Records werden nicht unnötig in Management Review oder dauerhaftes Memory kopiert.

## Output-Verträge

`field-action-effectiveness-assessment.json` enthält Strategy/Scope Version, Effectiveness Dimensions, Numerator/Denominator/Unknowns, Check Method/Sampling Evidence, Required Action Verification, Data Quality, New Safety Facts und Overall Operational Effectiveness State.

`field-action-product-reconciliation.json` enthält quantities/populations by disposition, reconciliation equations/gaps, downstream states, source refs und cut-off.

`field-action-closure-readiness.json` enthält operational completion, unresolved gaps, Risk/CAPA/PMS states, regulatory reporting/finalization dependencies, Authority State, Human Owner, recommendation und reopen triggers.

## Memory Path

Persistenzwürdig sind abstrahierte Effectiveness-Dimensionen, robuste Reconciliation-Muster, Sampling-/Non-Responder-Prüfheuristiken und Closure-State-Machines. Konkrete Recipient-/Customer-/Device-/Lot-/Quantity-/Recall-/FSCA-/Authority-Daten, laufende Quoten und offene Statusberichte bleiben kontrollierte Records/run-only.

Nur abstrahierte nicht-sensitive `memory-candidate-handoff-v1`-Kandidaten werden an `communication-memory-governance` übergeben.

## Qualitätsgate

Bestanden nur wenn:

- Activity Counts nicht als Effectiveness ausgegeben werden,
- Notification, Acknowledgement, Action Completion und Verification getrennt sind,
- physische Return/Quarantine/Correction/Verification/Disposition States aus kontrollierter Physical-Execution-Evidence stammen statt aus Communication-Selbstauskunft abgeleitet zu werden,
- Prozentwerte definierte versionierte Denominators besitzen,
- Non-Responder/Unknowns nicht aus Nennern entfernt werden, um Ergebnisse zu verbessern,
- Sampling/Check-Level aus autorisiertem Strategy State stammt und seine Grenzen sichtbar sind,
- Downstream Distribution vollständig in Reconciliation bleibt,
- Product Reconciliation und Contact Reconciliation getrennt aber verknüpft sind,
- `no new complaints` nicht als Effectiveness Proof verwendet wird,
- CAPA- und Field-Action-Effectiveness nicht gleichgesetzt werden,
- neue Safety Facts Closure sofort unterbrechen/reopen können,
- interne Operational Completion nicht als FDA Termination oder andere Authority Closure ausgegeben wird,
- Authority Closure nur mit verifizierter externer Evidence behauptet wird,
- unresolved material scope/disposition/action evidence eine belastbare Closure blockiert,
- konkrete Customer-/Device-/Authority-Daten nicht in globales dauerhaftes Memory gelangen.
