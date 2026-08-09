---
name: ivdr-economic-operator-postmarket-propagation
description: Strukturiert und evidenziert die eigenständigen IVDR-Postmarket-Pflichten von Importeuren und Distributoren bei Complaints, Nonconformity, Serious Risk, Withdrawal, Recall und FSCA und propagiert kontrollierte Actions durch die Lieferkette, ohne Manufacturer-, Vigilance- oder Communication-Ownership zu duplizieren.
---

# IVDR Economic Operator Postmarket Propagation

## Zweck und Grenze

Dieser Skill besitzt die **rollen- und evidenzgebundene Propagation von IVDR-Postmarket-Pflichten über Importeur- und Distributor-Ebenen**. Er wird verwendet, wenn Complaint-/Incident-/Nonconformity-/Recall-/Withdrawal-/FSCA-Fakten durch eine EU-Lieferkette laufen und pro Economic Operator geklärt werden muss, welche Information, Registerführung, Kooperation, Corrective Action oder Serious-Risk-Eskalation tatsächlich erforderlich, ausgelöst und evidenziert ist.

Er ersetzt weder den Manufacturer als FSCA-/Vigilance-Owner, `ivdr-pms-vigilance`, `ivdr-field-safety-corrective-action`, `medical-device-field-action-communication` noch `medical-device-field-action-physical-execution`. Er sendet keine Kundenkommunikation autonom, führt keine physische Rückholung aus und behauptet keine behördliche Meldung ohne externe Evidence.

Aktuelle IVDR-Anforderungen werden aus autoritativen Quellen auf den relevanten Zeitpunkt bezogen. Insbesondere sind die General Obligations von Importers und Distributors, ihre Register-/Forwarding-/Cooperation-Pflichten sowie Serious-Risk-Eskalationen source-bound zu bewerten und nicht aus Erinnerung als statische Checkliste zu behandeln.

## Kernprinzipien

- **Economic-operator role is a legal fact, not a contact label:** Manufacturer, Authorised Representative, Importer, Distributor, Servicepartner und Customer werden nicht aufgrund von CRM-/Vertriebsbezeichnungen gleichgesetzt.
- **Own duty is not delegated away:** eine Manufacturer-Anweisung oder zentrale Konzernprozedur kann die Ausführung koordinieren, ersetzt aber keine eigenständige gesetzliche Pflicht eines Importeurs/Distributors, soweit eine solche anwendbar ist.
- **Complaint forwarding is not complaint closure:** weitergeleitete Complaint-/Incident-Information bleibt ein Evidence Event; der Distributor/Importer entscheidet dadurch weder Investigation noch Vigilance Reportability.
- **Own register remains own evidence:** erforderliche Register zu Complaints, Nonconforming Devices, Recalls und Withdrawals bleiben operator-spezifische Records; ein Manufacturer-Master-Record darf sie nicht still ersetzen.
- **Serious risk bypasses manufacturer response:** wenn die aktuelle IVDR-Pflicht eine unmittelbare Behördeninformation des Economic Operators verlangt, darf diese nicht bis zur Antwort/Freigabe des Manufacturers warten.
- **Cooperation ≠ completion:** die Bitte des Manufacturers um Recall-/Withdrawal-/Corrective-Action-Kooperation beweist nicht, dass der Operator sie umgesetzt hat.
- **Forwarded ≠ propagated:** eine Nachricht an einen Distributor beweist nicht, dass betroffene Downstream-Recipients oder Inventory kontrolliert wurden.
- **Operator inventory is part of action scope:** betroffene Ware unter Verantwortung eines Importeurs/Distributors wird als eigener Inventory-/Custody-State geführt und bei Bedarf an Physical Execution übergeben.
- **Market scope is operator-specific:** Member States, Sites, Downstream Customers und Device Scope je Operator werden versioniert; Scope Gaps bleiben sichtbar.
- **No role collapse across group companies:** rechtlich getrennte Importer-/Distributor-Gesellschaften behalten getrennte Pflichten/Evidence, auch bei gemeinsamem ERP oder Konzernzugehörigkeit.
- **Article-16-type activity is a role-change trigger:** Relabeling, Repackaging, Translation oder Modification durch Importer/Distributor wird bei möglicher regulatorischer Rollen-/Compliance-Auswirkung an den Regulatory Owner geroutet; dieser Skill erfindet keine Rollenklassifikation.
- **New safety facts return upstream immediately:** neue Complaints/Incidents/Serious-Risk-Fakten aus Operator-Netzwerken gehen ohne Warten auf Supply-Chain-Closure an Manufacturer/Vigilance/FSCA-/MDR-Owner.

## Zulässige Source Types

Der Skill kann kontrollierte Inputs aus mehreren Postmarket-Pfaden konsumieren:

- Complaint/Incident Intake,
- Distributor-/Importer-eigene Complaint-/Nonconformity-Records,
- `ivdr-pms-vigilance`,
- `ivdr-field-safety-corrective-action`,
- Recall/Withdrawal/Corrective-Action-Plan,
- `medical-device-field-action-communication`,
- `medical-device-field-action-physical-execution`,
- Competent-Authority Request oder andere kontrollierte IVDR-Postmarket-Evidence.

Kein künstlicher FSCA- oder Complaint-State wird erzeugt, nur um den Workflow auszulösen.

## Workflow

### 1. Economic-Operator-Netz und Rollen fixieren

Erfasse pro Organisation/Site:

- legal entity/reference,
- Role `importer|distributor|authorised-representative|manufacturer|other`,
- Market/Member-State Scope,
- Device/Product Scope,
- upstream/downstream relation,
- Distribution/Inventory Data Sources,
- aktuelle authoritative Requirement References + `asOf`,
- bekannte Role-/Activity Conflicts.

Unklare Rolle bleibt `role-unresolved` und wird nicht aus Handelsnamen oder Konzernstruktur abgeleitet.

### 2. Trigger und Obligation Map ableiten

Bewerte pro Operator und Evidence Snapshot getrennt mindestens folgende Triggerklassen:

- Complaint oder suspected incident received,
- Device believed nonconforming,
- Device presents or may present serious risk,
- Recall/Withdrawal/Corrective Action/FSCA initiated,
- Competent Authority information/sample/action request,
- storage/transport or inventory condition relevant,
- operator activity with possible Article-16-/role impact.

`ivdr-economic-operator-obligation-map.json` enthält pro Trigger Requirement Source, Fact Basis, Operator, Obligation Type, Time Criticality, Human/External Owner, Evidence Needed und State `not-triggered|possible|required|performed-unverified|verified|blocked|unknown`.

### 3. Complaint-/Incident-Forwarding evidenzieren

Wenn ein Importeur/Distributor Complaint- oder suspected-incident-Information erhält:

- Original receipt/provenance erhalten,
- Weiterleitung an die nach aktuell anwendbarem IVDR erforderlichen Parteien als separates Event führen,
- Receipt/Forwarding Timestamp und Evidence referenzieren,
- operator-eigenen Register State aktualisieren,
- neue Safety Facts unverzüglich an Complaint/Vigilance Owner routen.

Weiterleitung erzeugt keine automatische `complaint-investigated`, `not-reportable` oder `closed`-Entscheidung.

### 4. Nonconformity / Recall / Withdrawal Cooperation steuern

Wenn der Operator von Nonconformity ausgeht oder eine Field Action/Recall/Withdrawal läuft:

- Manufacturer/AR/Importer/Distributor Cooperation Requirements current-source-basiert bestimmen,
- betroffene Market-/Device-/Inventory-/Downstream-Scope-Version führen,
- benötigte Communication-Aktionen an `medical-device-field-action-communication` geben,
- Inventory Hold/Return/Quarantine/Correction/Disposition an `medical-device-field-action-physical-execution` geben,
- eigene Register-/Evidence-States fortschreiben.

Eine zentrale Manufacturer-Task-ID ist nur Referenz; sie ersetzt nicht den operator-eigenen Evidence State.

### 5. Serious-Risk-Eskalation separat führen

Wenn aktuelle Evidence einen `serious-risk-possible|required`-Trigger für den jeweiligen Economic Operator erzeugt:

- aktuelle zuständige Authority/Member-State Requirement Source bestimmen,
- External Action Owner und Required Content/Gaps sichtbar machen,
- Hersteller-/AR-/NB-/Authority-Informationspfade getrennt führen,
- erforderliche sofortige Eskalation nicht auf Complaint Closure, Root Cause, Manufacturer Approval oder vollständige Recall-Reconciliation verschieben.

`authorityNotified=true` wird nur mit verifizierter externer Evidence gesetzt.

### 6. Operator-spezifische Register kontrollieren

Führe, soweit anwendbar und gefordert, operator-spezifische Records für:

- complaints,
- suspected incidents / forwarded reports,
- nonconforming devices,
- recalls,
- withdrawals,
- corrective-action cooperation,
- serious-risk escalations,
- authority requests/responses.

Cross-References zu Manufacturer-/AR-/Field-Action-Records sind erlaubt; stilles Ersetzen eigener Pflichtrecords durch einen zentralen Konzernrecord ist nicht erlaubt.

### 7. Downstream Propagation und Distribution Scope prüfen

Pro Distributor/Importer erfasse:

- affected inventory under own responsibility,
- downstream recipient population known/unknown,
- direct notification/forwarding state,
- downstream forwarding evidence,
- returned/quarantined/corrected inventory state,
- no-response/unreachable downstream entities,
- scope extensions/new Member States.

`forwardedToDistributor=true` ist kein Beweis für vollständige Downstream-Propagation.

### 8. Role-/Activity-Conflict erkennen

Wenn ein Importeur/Distributor Tätigkeiten wie Relabeling, Repackaging, Translation, Modification oder andere Eingriffe ausführt, die die regulatorische Rolle oder Responsibility verändern können:

- Fakten und Tätigkeit fixieren,
- current-source Regulatory Assessment triggern,
- keine automatische `still-distributor`, `manufacturer`, `Article-16-compliant` oder vergleichbare Schlussfolgerung erzeugen,
- Field-Action-Evidence unter der bisherigen Rolle nicht still auf eine neue Rolle übertragen.

### 9. New Facts und Non-Response zurückrouten

Neue Complaint-/Incident-/Serious-Risk-/Scope-Fakten aus Economic Operators werden sofort an die zuständigen Upstream-Owner zurückgegeben. Fehlende Antwort eines Importeurs/Distributors wird als `unresolved/blocked` geführt und nicht als `no affected product` oder `no serious risk` interpretiert.

### 10. Propagation State erzeugen

`ivdr-economic-operator-propagation-state.json` enthält pro Operator:

- Role/Market/Device Scope Version,
- triggered obligations,
- own register states,
- required forwarding/cooperation actions,
- communication/physical-execution references,
- authority escalation state,
- downstream coverage,
- unresolved gaps,
- new safety facts,
- reassessment triggers.

Der State ist Input für FSCA/Vigilance, Field-Action-Communication, Physical Execution und Effectiveness, aber keine Authority-/Manufacturer-Closure.

## Output-Verträge

`ivdr-economic-operator-obligation-map.json` enthält Operator/Role, Trigger Facts, authoritative requirement refs, obligation type, time-criticality, evidence requirement, owner und state.

`ivdr-economic-operator-propagation-state.json` enthält operator-spezifische Register-, Forwarding-, Cooperation-, Inventory-, Downstream-, Communication- und Physical-Execution-States sowie unresolved scope.

`ivdr-economic-operator-escalation-log.json` enthält append-only Complaint-/Incident-/Serious-Risk-/Authority-/Manufacturer-/AR-Eskalationsereignisse mit Evidence, Status und offenen Gaps.

## Memory Path

Persistenzwürdig sind abstrahierte Economic-Operator-Role-/Obligation-Muster, sichere Propagation-State-Machines und robuste Register-/Downstream-Reconciliation-Heuristiken. Konkrete Distributor-/Importer-/Customer-/Device-/Complaint-/Recall-/Authority-/Inventory-Daten bleiben kontrollierte Regulatory/Quality Records und run-only.

Regulatorische Memory Candidates benötigen `sourceRefs`, `asOf` und `reviewAfter`; nur abstrahierte nicht-sensitive `memory-candidate-handoff-v1`-Kandidaten gehen an `communication-memory-governance`.

## Qualitätsgate

Bestanden nur wenn:

- Economic-Operator-Rollen evidenzgebunden statt aus Kontakt-/Konzernlabels abgeleitet sind,
- eigene Importer-/Distributor-Pflichten nicht still an den Manufacturer delegiert werden,
- Complaint Forwarding nicht als Complaint Investigation oder Closure gilt,
- operator-spezifische Register/Evidence States erhalten bleiben,
- Serious-Risk-Eskalation nicht auf Manufacturer Response, Root Cause oder Action Closure wartet,
- externe Authority Actions nicht ohne Evidence als erfolgt markiert werden,
- Recall/Withdrawal/FSCA Cooperation nicht mit vollständiger Ausführung gleichgesetzt wird,
- Downstream Propagation nicht aus einer einzelnen Distributor-Bestätigung abgeleitet wird,
- betroffene Operator Inventory States an den Physical-Execution-Layer anschlussfähig sind,
- Role-/Article-16-relevante Tätigkeiten eine Regulatory Reassessment auslösen statt Rollen zu erfinden,
- neue Safety Facts unverzüglich an Vigilance/Complaint/FSCA Owner zurückfließen,
- konkrete Economic-Operator-/Customer-/Authority-Daten nicht in globales dauerhaftes Memory gelangen.
