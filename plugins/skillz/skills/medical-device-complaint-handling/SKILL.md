---
name: medical-device-complaint-handling
description: Führt Medical-Device-/IVD-Complaints als kontrollierten QMS-Prozess von Intake über Evaluation und Investigation bis zu evidenzbasierter Closure, ohne MDR-/Vigilance-Reportability, CAPA oder Risk Management zu duplizieren.
---

# Medical Device Complaint Handling

## Zweck und Grenze

Dieser Skill besitzt den **QMS-Complaint-Prozess** für Medical Devices und IVDs zwischen kontrolliertem Customer-/Field-Intake und regulatorischer Reportability/Vigilance. Er bewertet, dokumentiert und untersucht Complaints, bewahrt Individual Records und entscheidet evidenzbasiert über Investigation und Closure.

Er entscheidet **nicht** über FDA MDR, EU Serious-Incident-/Vigilance-Reportability, CAPA-Notwendigkeit oder finale Risk-Akzeptanz. Diese Fachentscheidungen bleiben bei den jeweiligen Spezialisten.

Aktuelle regulatorische Basis wird source-bound geführt. Für die USA gilt seit 2. Februar 2026 QMSR; FDA weist ausdrücklich darauf hin, dass Complaint Handling fortbesteht und Complaint Records unter 21 CFR 820.35 sowie den inkorporierten QMS-Anforderungen geführt werden. Für EU MDR/IVDR sind Complaints/Feedback relevante PMS-Datenquellen und dürfen nicht aus dem Post-Market-System herausfallen.

## Kernprinzipien

- **Every complaint keeps its own record:** ähnliche oder duplizierte Complaints dürfen auf eine bestehende Investigation verweisen, aber der einzelne Complaint-Record wird nicht gelöscht oder zusammengelegt.
- **Investigation decision is explicit:** `not-yet-evaluated|investigation-required|investigation-not-required-with-justification|under-investigation|complete|blocked|reopened`.
- **No-investigation needs evidence:** ein Verzicht auf neue Investigation benötigt nachvollziehbare Begründung und Verweis auf ausreichende bestehende Untersuchung/Evidenz; Convenience, geringe Kosten oder bereits geleisteter Ersatz reichen nicht.
- **Regulatory routing is early:** mögliche Reportability/Vigilance wird beim Intake/Evaluation geroutet und nicht bis zum Complaint-Abschluss oder finaler Root Cause aufgeschoben.
- **Reporting and investigation run in parallel:** regulatorische Meldung/Assessment kann vor finaler Ursachenklärung erforderlich sein; Investigation läuft danach weiter.
- **Closure is not immunity:** `closed` ist ein historischer Complaint-Zustand, keine Sperre gegen spätere neue Fakten. Materielle Folgeinformationen können Complaint Evaluation, Investigation, Risk/CAPA/PMS-Routing und regulatorischen Handoff erneut öffnen.
- **Supplemental evidence is versioned:** spätere Kunden-/Service-/Distributor-/Feldinformationen werden mit eigener Source Reference und Empfangszeit als Delta zum bisherigen Complaint-Stand geführt; frühere Entscheidungen und Closure-Rationale bleiben nachvollziehbar erhalten.
- **Evidence preservation before destructive handling:** rückgesandtes Device, Probe, Lotmaterial, Logs, Screenshots, Rohdaten oder sonstige potenziell relevante Evidenz werden vor destruktiver Veränderung kontrolliert behandelt.
- **Customer response ≠ complaint closure:** Antwort, Austausch, Gutschrift oder technische Lösung sind eigenständige Zustände.
- **Closure is evidence-based:** Closure setzt nachvollziehbare Evaluation, erforderliche Investigation, regulatorischen Handoff-Status, relevante Risk/CAPA/PMS-Links und dokumentierte Restpunkte voraus.

## Workflow

### 1. Complaint Intake übernehmen

Konsumiere `complaint-intake-handoff.json` und verifiziere:

- Original Source Reference und Intake-/Transfer-Zeitlinie,
- Device/Variant/UDI/Lot soweit bekannt,
- Reporter-/Nutzungskontext soweit erforderlich,
- Problem-/Failure-/Performance-/Labeling-/Packaging-/Safety-Fakten,
- Customer Impact und bekannte medizinische/operative Folgen,
- bereits erfolgte Service-/Commercial-Actions,
- Safety-/Regulatory Flags und Unknowns,
- Related Prior Complaint/Contact sowie `newMaterialFacts` bei Folgeinformationen.

Fehlende Felder bleiben offen; der Record wird nicht durch Annahmen „vervollständigt“.

### 2. Complaint Scope bestätigen

Klassifiziere `possible|confirmed|not-a-complaint-with-rationale|unknown|reopened`. Eine mögliche Nichtkonformität/Fehlfunktion eines Device, Labelings, Packagings oder relevanter Performance-/Safety-Erwartung wird nicht wegen freundlicher Kundenformulierung, fehlender Rückgabe oder erfolgreicher Soforthilfe ausgeschlossen.

Wenn die Complaint-Klassifikation unsicher bleibt, behandle sie bis zur begründeten Entscheidung als `possible`; Safety-/Regulatory-Routing läuft unabhängig davon weiter.

### 3. Investigation Need entscheiden

Bewerte, ob eine neue oder wiederaufzunehmende Investigation erforderlich ist. Dokumentiere:

- Decision State,
- Entscheidungsgrund,
- vorhandene ähnliche/gleiche Investigation-Evidence,
- Relevanz/Gleichwertigkeit zum aktuellen Complaint,
- neue materielle Fakten seit letzter Evaluation/Closure,
- notwendige Device-/Log-/Sample-/Record-Prüfungen,
- Verantwortliche und Verifikationsschritte.

Bei Bezug auf frühere Investigation muss ausdrücklich belegt sein, warum diese den aktuellen Sachverhalt ausreichend abdeckt. Ein „known issue“-Label allein genügt nicht.

### 4. Investigation kontrolliert durchführen

Wenn Investigation erforderlich:

- Ereignis-/Failure-Fakten rekonstruieren,
- Device-/Batch-/Software-/Label-/Use-/Service-/Distribution-Kontext prüfen,
- relevante Evidenz vor Veränderung sichern,
- Hypothesen und verifizierte Befunde trennen,
- bei kausaler Unsicherheit `evidence-based-causal-investigation` verwenden,
- neue/erhöhte Risiken an `medical-device-risk-management-iso14971` routen,
- systemische Nonconformity/CAPA-Fragen an `medical-device-capa` routen,
- Design-/Process-/Supplier-/Labeling-Themen an vorhandene Spezialisten übergeben.

Root Cause darf `confirmed|probable|possible|not-established|not-applicable` sein. `not-established` verhindert nicht automatisch regulatorische Reportability.

### 5. Supplemental Information und Reopen prüfen

Bei Folgeinformation nach früherer Evaluation oder Closure:

1. erhalte die frühere Decision-/Closure-Version unverändert im Audit Trail,
2. erfasse neue Fakten als separates Evidence Delta mit Source/ReceivedAt,
3. prüfe, ob Complaint Scope, Investigation Need, Root-Cause Confidence, Risk, CAPA, PMS oder Regulatory Relevance materiell betroffen sind,
4. setze `complaintClosureState=reopened` und/oder `investigationState=reopened`, wenn eine erforderliche Neubewertung besteht,
5. erzeuge einen aktualisierten `complaint-regulatory-handoff.json`, sobald neue regulatorisch relevante Fakten vorliegen.

Ein früheres `investigation-complete`, `complaint-closed` oder `not-reportable` wird nicht gelöscht, aber auch nicht als dauerhafte Immunität gegen neue Evidenz verwendet.

### 6. Regulatory Handoff fortschreiben

Erzeuge `complaint-regulatory-handoff.json` **früh** und aktualisiere ihn, sobald relevante Fakten hinzukommen. Enthalten sind:

- Complaint/Contact References,
- Intake-/Awareness-Evidence-Timeline ohne finale Rechtsinterpretation,
- Markets/Roles soweit bekannt,
- Safety/Seriousness/Malfunction/False-Result-Fakten,
- Investigation State,
- Device Availability/Evidence State,
- Unknowns,
- neue Fakten seit letztem Handoff,
- Prior Decision/Assessment References und `reassessmentTrigger` soweit zutreffend.

Der Handoff entscheidet nicht `reportable|not-reportable`.

### 7. Kundenkommunikation getrennt führen

Dokumentiere Customer Response, technische Lösung, Ersatz/Gutschrift und offene Rückfragen. Eine externe Antwort darf Fakten-/Regulatory-Uncertainty nicht als bewiesene Root Cause oder finale Safety-Aussage darstellen.

### 8. Closure Readiness prüfen

`complaint-closure-readiness.json` trennt mindestens:

- `customerResponseComplete`,
- `investigationCompleteOrJustified`,
- `regulatoryHandoffAcknowledged`,
- `riskRoutingCompleteOrNotRequired`,
- `capaRoutingCompleteOrNotRequired`,
- `pmsHandoffCompleteOrNotRequired`,
- `requiredExternalActionsVerifiedOrPending`,
- `openUnknowns`,
- `residualRisks`,
- `complaintClosureState: open|ready|closed|reopened|blocked|unknown`.

Ein Complaint darf nicht allein deshalb geschlossen werden, weil das Ticket geschlossen, das Produkt ersetzt, die Untersuchung „similar to prior“ genannt oder eine Meldung abgeschickt wurde. Neue materielle Information nach Closure setzt die relevanten Gates wieder auf offen, statt die historische Closure zu überschreiben.

## Output-Verträge

`complaint-record.json` enthält unveränderliche Intake-Referenzen, Klassifikation, Device/Reporter/Market Facts, Problem/Impact, Service Actions, Investigation Decision/State, Evidence/Root-Cause State, Supplemental-Evidence-/Reopen-Historie, Risk/CAPA/PMS/Regulatory Links, Customer Response und Audit Trail.

`complaint-investigation-plan.json` enthält Investigation Need, Begründung, Scope, zu sichernde Evidenz, Tests/Analysen, bekannte ähnliche Investigations, Reopen-/Delta-Scope soweit zutreffend, Stop/Preservation Conditions, Verantwortliche und Completion Evidence.

`complaint-regulatory-handoff.json` enthält normalisierte Fakten und Timeline für jurisdiction-spezifische Regulatory Assessment ohne finale Reportability, einschließlich neuer materieller Fakten und früherer Assessment-References für Reassessment.

`complaint-closure-readiness.json` enthält die getrennten Completion-Gates, Reopen State und verhindert administrative Closure bei ungeklärten erforderlichen Quality-/Regulatory-Aktionen.

## Memory Path

Persistenzwürdig sind abstrahierte Complaint-Kategorien, validierte Investigation-/Reopen-Entscheidungsmuster, Evidence-Preservation-Regeln und wiederverwendbare Closure-Gates. Konkrete Complaints, Kunden-/Patienten-/Reporter-Daten, UDI/Lot/Seriennummern, Investigation Findings, Root Causes, Reportability States und aktuelle CAPA/Risk/Regulatory-Verknüpfungen bleiben kontrollierte Records/run-only. Übergib nur geeignete abstrahierte `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`.

## Qualitätsgate

Bestanden nur wenn:

- jeder Complaint einen eigenen nachvollziehbaren Record behält,
- Investigation-Verzicht konkret und evidenzbasiert begründet ist,
- regulatorischer Handoff nicht auf Root Cause oder Complaint Closure wartet,
- spätere materielle Evidenz eine frühere Closure/Investigation/Assessment nachvollziehbar reopenen kann,
- frühere Entscheidungen erhalten bleiben und durch neue Versionen ergänzt statt überschrieben werden,
- Device-/Sample-/Log-Evidenz vor destruktiver Behandlung geschützt wird,
- Customer Resolution, Investigation Completion, Reportability, CAPA und Complaint Closure getrennte Zustände bleiben,
- ähnliche Complaints nicht ohne individuellen Record/Assessment zusammengelegt werden,
- fehlende Fakten und nicht etablierte Root Cause ehrlich erhalten bleiben,
- personenbezogene und konkrete Complaint-Daten nicht in globales Memory gelangen.
