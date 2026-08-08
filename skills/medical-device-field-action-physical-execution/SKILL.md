---
name: medical-device-field-action-physical-execution
description: Steuert und evidenziert die physische Ausführung autorisierter Medical-Device-/IVD-Feldmaßnahmen von RMA, Transport und Chain-of-Custody über Quarantine und Correction bis Verification, Destruction oder anderer Disposition, ohne MRB, Effectiveness oder Authority Closure zu duplizieren.
userFacing: true
implicitInvocation: false
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - medical-device-field-action-communication
  - quality-record-integrity
  - controlled-quality-documentation
outputs:
  - field-action-physical-execution-plan.json
  - field-action-unit-custody-ledger.json
  - field-action-disposition-evidence.json
lastEvaluated: 2026-08-08
---

# Medical Device Field Action Physical Execution

## Zweck und Grenze

Dieser Skill besitzt den **physischen Execution- und Evidence-Lifecycle einer bereits autorisierten Medical-Device-/IVD-Feldmaßnahme**. Er verbindet Recipient-/Action-State aus `medical-device-field-action-communication` mit RMA/Return, Transport, Receipt, Quarantine, Correction/Repair/Software Update, Reinspection/Verification, Destruction, Return-to-Supplier oder anderer autorisierter Disposition und erzeugt eine belastbare Chain-of-Custody bis zum Übergang an `medical-device-field-action-effectiveness`.

Er entscheidet **nicht**, ob eine FSCA, ein FDA Recall, eine Correction/Removal oder eine andere Feldmaßnahme erforderlich ist. Er ersetzt weder `nonconformance-mrb-disposition`, `medical-device-service-report-quality-routing`, CAPA, Complaint Investigation, Risk Management noch Effectiveness/Authority Closure. MRB/NC bleibt Owner interner Nichtkonformitäts-Dispositionen; dieser Skill besitzt den feldaktionsspezifischen physischen Nachweis der betroffenen Einheiten und Mengen.

## Kernprinzipien

- **Action source before physical execution:** jede produktive Aktion referenziert Field Action ID, Scope Version, Required Action und freigegebene Instructions.
- **RMA ≠ return:** eine erteilte Return Authorization beweist weder Versand noch Eingang.
- **Shipped ≠ received:** Carrier-/Shipping-Evidence und physischer Receipt sind getrennte Events.
- **Received ≠ quarantined:** Eingang allein beweist keine wirksame Segregation oder Stop-Use-Kontrolle.
- **Quarantine ≠ disposition:** gesicherte Einheiten bleiben offen, bis eine autorisierte finale oder korrigierende Disposition evidenziert ist.
- **Correction performed ≠ correction verified:** Repair, Rework, Software/Firmware Update, Relabeling oder Configuration Change benötigen die im Action Plan festgelegte Verifikation vor `verified-complete`.
- **Replacement does not erase the affected unit:** Ersatzlieferung löst den Kundenbedarf, aber nicht automatisch Return, Quarantine, Correction oder Disposition der betroffenen Einheit.
- **Chain of custody is append-only:** Custody-, Location-, Quantity- und Identity-Transitions werden nicht rückwirkend überschrieben.
- **Identity before disposition:** Unit/Lot/Serial/UDI/Software-Version oder kontrollierte Quantity-Basis muss mit dem Field-Action-Scope reconciled sein; unklare Identität bleibt `unresolved`.
- **Evidence preservation precedes destructive action:** wenn Complaint-/Investigation-/Legal-/Regulatory-Evidence benötigt werden kann, darf Destruction oder evidence-destroying Repair nicht still vor Evidence Capture erfolgen.
- **No re-release by convenience:** korrigierte Einheiten kehren nur mit autorisierten Acceptance Criteria und erforderlicher Verification/Release Evidence in nutzbaren Bestand zurück.
- **Third-party custody is still custody:** 3PL, Distributor, Servicepartner, Repair Vendor oder Waste Contractor benötigen nachvollziehbare Handoffs und Scope-Bezug.
- **Physical completion ≠ field-action effectiveness:** vollständig bearbeitete Einheiten sind Input für Effectiveness; sie schließen weder Recipient Population noch Authority State.
- **New safety facts bypass execution cadence:** neue Incidents, unerwartete Schäden, Correction Failure oder zusätzliche betroffene Units gehen sofort zurück an Complaint/Vigilance/MDR/Risk/Action Owner.

## Zulässige Action Types

Der Skill kann je nach kontrolliertem Action Plan insbesondere folgende physische Pfade ausführen/evidenzieren:

- `stop-use-and-hold`,
- `return/removal`,
- `on-site-correction`,
- `repair/rework`,
- `software-or-firmware-update`,
- `configuration-change`,
- `inspection/screening`,
- `relabel/repackage` nur bei separat geklärter regulatorischer Zulässigkeit,
- `destroy/scrap`,
- `return-to-supplier`,
- `controlled-release-after-correction`,
- `other-authorized-disposition`.

Der Skill erfindet keine Disposition, wenn der Field-Action-/MRB-/Regulatory-Owner sie nicht autorisiert hat.

## Workflow

### 1. Execution Source und Unit Scope übernehmen

Erfasse mindestens:

- `fieldActionId`, Jurisdiction und Action Source Reference,
- Action/Scope Version,
- Recipient/Site Reference,
- Required Action und Instructions Version,
- betroffene Unit-/Lot-/Quantity-Identität,
- erwarteter Ausgangszustand,
- Evidence-/Investigation-Preservation Needs,
- Due-/Escalation Conditions,
- autorisierte Disposition Options.

Widersprechen Unit Identity, Notice Scope und Execution Instruction einander, wird die physische Aktion auf `scope-conflict` gesetzt und an den Action Owner zurückgegeben; fehlende Identität wird nicht passend geraten.

### 2. RMA/Return-Plan aufbauen

Wenn Return/Removal gefordert ist, trenne:

- Return Authorization/RMA issued,
- Packaging/Transport Instructions,
- Pickup/Shipment booked,
- handed-to-carrier,
- in-transit,
- delivered-to-receiving-site,
- physically received and reconciled.

Pro Event werden Zeit, Actor/Organisation, Location, Unit/Quantity, Source Evidence und Exception State geführt.

### 3. Chain-of-Custody führen

`field-action-unit-custody-ledger.json` ist append-only und enthält pro Unit/Quantity-Batch mindestens:

- scope/identity reference,
- custody holder,
- physical location,
- timestamp/event type,
- quantity in/out,
- seal/package/condition soweit relevant,
- handoff-from/to,
- evidence reference,
- discrepancy/unknown state.

Quantity- oder Identity-Differenzen werden als Reconciliation Gap geführt und nicht durch pauschale Korrekturbuchungen versteckt.

### 4. Receipt, Quarantine und Stop-Use verifizieren

Receipt wird erst nach tatsächlicher Eingangs-/Bestands-Evidence gesetzt. Quarantine/Stop-Use benötigt eine kontrollierte Segregations-/Usage-Control-Evidence, z. B. physische Sperrzone, Inventory Hold, System Lock, Label/Tag oder andere geeignete organisationsdefinierte Kontrolle.

`received=true` setzt nicht automatisch `quarantined=true`.

### 5. Evidence Preservation Gate

Vor Repair, Disassembly, Software Update, Data Wipe, Destruction oder anderer potenziell evidence-destroying Aktion prüfe:

- offene Complaint/Incident Investigation,
- benötigte Logs/Configuration/Samples/Photos,
- mögliche Authority/Legal/Supplier Evidence,
- bestehende Preservation Instruction.

Wenn Preservation erforderlich und noch nicht erfüllt ist, wird die destruktive Aktion blockiert oder nur über einen explizit autorisierten Safety-/Evidence-Tradeoff durchgeführt. Der Tradeoff und verlorene Evidence werden sichtbar dokumentiert.

### 6. Correction/Repair/Update ausführen und evidenzieren

Für jede Correction:

- verwendete kontrollierte Instruction/Software/Firmware/Tool-Version,
- ausführende Person/Organisation und Qualification soweit erforderlich,
- Unit/Quantity,
- Start/Ende,
- performed actions,
- deviations/exceptions,
- result state,
- benötigte Post-Action Verification.

Bei Service-/Repair-Fakten mit Quality-Relevanz route an `medical-device-service-report-quality-routing`; bei interner NC/MRB-Entscheidung an `nonconformance-mrb-disposition` statt diese Logik nachzubauen.

### 7. Verification und Release Gate

`performed` darf nur auf `verified-complete` wechseln, wenn die für diese Action definierte Evidence vorliegt. Dies kann Reinspection, Functional Test, Software-/Configuration Verification, Label Check, Validation Evidence oder andere spezifizierte Acceptance Criteria umfassen.

Eine korrigierte Einheit darf nur dann `released-for-use` oder `returned-to-customer` werden, wenn erforderliche Verification und autorisierter Release State vorliegen. Administrative Ticket-Closure oder Customer Pressure ersetzen kein Release Gate.

### 8. Destruction/Scrap/Final Disposition evidenzieren

Für finale Disposition dokumentiere soweit anwendbar:

- autorisierte Disposition,
- Unit/Quantity Identity,
- executing organisation/location,
- date/time,
- method/category,
- witness/certificate state soweit vorgesehen,
- evidence reference,
- quantity reconciliation,
- residual/exception state.

Ein Destruction Certificate beweist nur den darin tatsächlich identifizierten Scope. Nicht identifizierte oder nicht reconciled Units werden nicht als destroyed gezählt.

### 9. New Safety Facts und Scope Drift sofort zurückrouten

Neue Schäden, wiederholte Failure nach Correction, unerwartete Service Findings, zusätzliche betroffene Serial/Lot/Version oder beschädigte Returns erzeugen ein neues Evidence Event und gehen unmittelbar an:

- Complaint/Vigilance/MDR Owner,
- FSCA/Recall/Correction-Removal Owner,
- Risk/CAPA/Investigation Owner soweit relevant,
- Communication Scope Owner bei Populationserweiterung.

Physical Execution darf diese Reassessment-Linie nicht bis zum Ende der Logistics-Kette verzögern.

### 10. Handoff an Effectiveness

Übergebe an `medical-device-field-action-effectiveness` ausschließlich verifizierte, versionierte Evidence:

- Unit/Quantity Scope,
- RMA/Return State,
- Custody/Location State,
- Quarantine/Stop-Use State,
- Correction performed/verified State,
- Destruction/Disposition State,
- Release State,
- discrepancies/unknowns,
- new safety facts/scope extensions.

Effectiveness bleibt Owner der populationsbezogenen Wirksamkeits- und Closure-Readiness-Bewertung.

## Output-Verträge

`field-action-physical-execution-plan.json` enthält Action/Scope/Instruction Version, Unit/Quantity Scope, Return/Custody/Quarantine/Correction/Verification/Disposition Steps, Owners, Preservation Gates, Stop Conditions und Evidence Requirements.

`field-action-unit-custody-ledger.json` enthält append-only Custody-/Location-/Quantity-/Identity-Events, Handoffs, discrepancies und source references.

`field-action-disposition-evidence.json` enthält pro Unit/Quantity den autorisierten und evidenzierten Zustand `returned|quarantined|corrected|verified|released|destroyed|supplier-returned|unknown`, Evidence References, Verification/Release State und unresolved gaps.

## Memory Path

Persistenzwürdig sind nur abstrahierte Chain-of-Custody-State-Machines, sichere Evidence-Preservation-/Quarantine-/Release-Gates und robuste Reconciliation-Patterns. Konkrete RMA-, Customer-, Device-, Lot/Serial-, Location-, Repair-, Destruction-, Carrier- oder Custody-Daten bleiben kontrollierte Quality/Field-Action Records und run-only.

Nur abstrahierte nicht-sensitive `memory-candidate-handoff-v1`-Kandidaten werden an `communication-memory-governance` übergeben.

## Qualitätsgate

Bestanden nur wenn:

- Field Action/Scope/Instruction Source vor produktiver Ausführung eindeutig ist,
- RMA, Shipment, Receipt, Quarantine, Correction, Verification und Disposition getrennte Evidence States bleiben,
- Unit-/Quantity-Identität und Chain-of-Custody nachvollziehbar sind,
- Quantity-/Identity-Differenzen als Gaps sichtbar bleiben,
- Destruction/Repair keine benötigte Investigation Evidence still zerstört,
- Replacement die betroffene Original-Unit nicht aus der Reconciliation entfernt,
- Correction/Update ohne erforderliche Verification nicht als `verified-complete` gilt,
- Re-Release nur mit erforderlicher Verification/Release Evidence erfolgt,
- Third-Party-Handoffs nachvollziehbar bleiben,
- neue Safety Facts unverzüglich Reassessment triggern,
- MRB/NC, Service Quality, CAPA und Effectiveness nicht dupliziert werden,
- physische Completion weder Recipient-/Field-Action-Effectiveness noch Authority Closure simuliert,
- konkrete Unit-/Customer-/Custody-Daten nicht in globales dauerhaftes Memory gelangen.
