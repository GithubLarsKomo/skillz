---
name: ivdr-fsca-status-final-reporting
description: Finalisiert IVDR-Vigilance-/FSCA-Herstellerberichte und verfolgt zuständige-Behörden-Feedback, Follow-up- und Closure-Evidence aus kontrollierter Field-Action-Evidence, ohne einen Final Report mit Authority Acceptance oder Closure gleichzusetzen.
---

# IVDR FSCA Status and Final Reporting

## Zweck und Grenze

Dieser Skill besitzt die kontrollierte Herstellerseite der IVDR-Vigilance-/FSCA-Finalisierung: aktuelle Report-/Form-Anforderungen bestimmen, Final-/Follow-up-Pakete aus verifizierter Investigation-, Risk-, FSCA-, Communication-, Physical-Execution- und Effectiveness-Evidence erstellen, Authority Questions versioniert beantworten und den tatsächlichen externen Authority State separat führen.

Er entscheidet nicht neu über initiale Serious-Incident-/FSCA-Reportability und ersetzt weder `ivdr-pms-vigilance` noch `ivdr-field-safety-corrective-action`. Er simuliert keine zuständige-Behörden-Bewertung, Zustimmung oder Closure. Ein Hersteller-`final report submitted` ist ein Submission State, kein Authority-Closure-State.

## Current-source Baseline

IVDR Article 84 verlangt nach Meldung eines schwerwiegenden Vorkommnisses die unverzügliche erforderliche Investigation einschließlich Risk Assessment und FSCA-Bewertung sowie die Zusammenarbeit mit zuständigen Behörden und gegebenenfalls der Benannten Stelle. Änderungen am betroffenen Device/Sample, die eine spätere Ursachenbewertung beeinflussen könnten, dürfen nicht ohne vorherige Information der zuständigen Behörde erfolgen.

Die Europäische Kommission veröffentlicht die aktuellen PMSV Reporting Forms. Stand 8. August 2026 ist MIR 7.3.1 seit 1. Mai 2026 verpflichtend; die Kommissionsseite führt außerdem die aktuellen FSCA-, FSN-, Trend- und Periodic-Summary-Formate. Die konkrete für einen Fall erforderliche Form-/Channel-/Authority-Prozedur wird current-source-basiert geprüft und nicht aus einem alten Template fest verdrahtet.

Ein `Final (Non-reportable) incident` darf nicht als Shortcut verwendet werden, solange Root Cause bzw. Ursache/Contributing Factors nicht ausreichend finalisiert sind; aktuelle MDCG-Vigilance-Guidance bleibt dafür maßgeblich.

## Kernprinzipien

- **Current form before final package:** Formversion, XSD/Helptext, Authority/Channel und anwendbare Übergangsregel werden vor Finalisierung aktuell verifiziert.
- **Manufacturer final ≠ authority closed:** finaler Herstellerbericht, Submission, Authority Receipt, Authority Assessment und Authority Closure sind getrennte Zustände.
- **Investigation completeness is explicit:** ungeklärte Root Cause/Contributing Factors, offene Device-/Sample-Evidence oder materielle Contradictions bleiben sichtbar.
- **No non-reportable shortcut:** ein Fall wird nicht durch Final-Non-reportable-Label geschlossen, wenn die erforderliche Ursachenbasis fehlt.
- **FSCA execution evidence is consumed, not recomputed:** Effectiveness/Product Reconciliation werden aus dem bestehenden Worker übernommen.
- **Authority feedback is append-only:** Kommentare, Requests, Coordinating-/Evaluating-Authority-Feedback und geänderte Anforderungen erzeugen neue Events/Paketversionen statt History Rewrite.
- **Multi-state consistency:** Market-/Country-/FSN-/Scope-Versionen müssen über Final/Follow-up Reporting mit dem ausgeführten Field-Action-Scope reconciled bleiben.
- **New safety facts bypass finalization:** neue Serious Incidents, Correction Failures, Scope Drift oder neue Countries/Lots gehen sofort zurück an Vigilance/FSCA/Risk/CAPA/Communication; kein vorbereiteter Final Report blockiert Reassessment.
- **Authority silence is not acceptance:** fehlende Rückfrage oder verstrichene Zeit wird nicht als Approval/Closure interpretiert.
- **Notified Body and Authority states stay distinct:** sofern Benannte Stelle beteiligt ist, werden deren Review/Information States nicht mit Competent-Authority-States zusammengeführt.

## Workflow

### 1. Current Regulatory Reporting Context verifizieren

Bestimme zum Run-Zeitpunkt mindestens:

- applicable IVDR/Vigilance route,
- zuständige bzw. koordinierende/bewertende Authority soweit bekannt,
- aktuelle EU/MDCG Reporting Form/Version und Helptext,
- required report type / follow-up state,
- Submission Channel/System und bekannte Authority Instructions,
- vorherige MIR/FSCA/FSN/Authority References,
- Notified Body involvement soweit relevant.

Nicht verifizierte Form-/Channel-Annahmen werden als `unknown` oder `verification-required` geführt.

### 2. Evidence Baseline einfrieren

Konsumiere und referenziere, statt neu zu berechnen:

- Incident/Vigilance Decision History,
- Investigation/Root Cause/Contributing Factors,
- Risk Assessment,
- FSCA Scope/Versions,
- FSN/Communication Evidence,
- Physical Execution/Product Reconciliation,
- Field-Action Effectiveness,
- CAPA/PMS Links,
- offene Unknowns/Contradictions,
- neue Safety Facts seit letztem Report.

Jeder Final-/Follow-up-Snapshot besitzt Scope Version, Cut-off und SourceRefs.

### 3. Final-/Follow-up-Readiness prüfen

Vor einem Final Report prüfe mindestens:

- erforderlicher Report Type aktuell korrekt,
- Investigation für diesen Report Type ausreichend,
- Cause/Contributing Factors nicht ungerechtfertigt als bekannt dargestellt,
- Risk/FSCA/Corrective Action konsistent,
- Device/Lot/UDI/Market Scope reconciled,
- neue Safety Facts bewertet,
- erforderliche Attachments/FSN/Action Evidence vorhanden,
- offene Authority Questions adressiert oder explizit offen.

Ein administrativer Wunsch nach Closure ersetzt keine fachliche Readiness.

### 4. Hersteller-Finalpaket erstellen

`ivdr-vigilance-final-report-package.json` enthält mindestens:

- Case/Report/Authority References,
- current Form/Schema Version + verification date/source,
- Report Type,
- Incident/Device/Scope Version,
- Investigation Summary + known/unknown cause state,
- Risk Assessment Reference,
- FSCA/Corrective Action + Effectiveness Evidence,
- Product/Recipient Reconciliation Summary soweit relevant,
- CAPA/PMS Links,
- unresolved issues/limitations,
- Attachments/FSN References,
- Human Approval/Submission State.

### 5. Authority Follow-up führen

`ivdr-fsca-authority-followup.json` führt append-only:

- Authority Event ID,
- evaluating/coordinating authority where evidenced,
- received request/comment/date/reference,
- requested clarification/evidence/action,
- response package version,
- due date only if externally evidenced or explicitly internally governed,
- submission/receipt evidence,
- unresolved questions,
- impact on FSCA/FSN/Scope/Risk/CAPA.

### 6. External Submission/Receipt nicht simulieren

`prepared|approved-for-submission|submitted-evidenced|receipt-evidenced|authority-review-pending|more-information-required|authority-assessment-evidenced|authority-closed-verified` bleiben getrennt. Nur verifizierte externe Evidence kann Submission Receipt, Authority Assessment oder Closure setzen.

### 7. Authority State reconciliieren

`ivdr-authority-state.json` führt mindestens:

`report-preparation|final-report-ready|submitted-evidenced|authority-review-pending|more-information-required|authority-action-required|authority-assessment-evidenced|authority-closed-verified|reopened-or-scope-extended|unknown`.

Authority Closure wird nur aus tatsächlicher zuständiger Authority-/System-Evidence abgeleitet. Keine Rückfrage, interne Completion oder PMS-Update setzt diesen State automatisch.

### 8. Reopen / Scope Drift

Neue Länder, Lots, Software-Versionen, Incidents oder Correction Failures nach einem Final-/Follow-up-Snapshot erzeugen eine neue Scope-Version und unverzügliche Reassessment-Handoffs. Vorherige Report-/Submission-Versionen bleiben historische Evidence und werden nicht umgeschrieben.

## Output-Verträge

`ivdr-vigilance-final-report-package.json` enthält current-source-verifizierte Form-/Report-Provenance, Investigation/Risk/FSCA/Effectiveness-Evidence, offene Punkte und Human Submission State.

`ivdr-fsca-authority-followup.json` enthält append-only Authority Questions, Comments, Requested Actions, Response Packages, Submission/Receipt Evidence und Auswirkungen auf Scope/Risk/FSCA.

`ivdr-authority-state.json` enthält den separaten externen Authority State mit Evidence References, Supersession/Reopen-Historie und unterscheidet Hersteller-, Notified-Body- und Competent-Authority-Zustände.

## Memory Path

Persistenzwürdig sind abstrahierte IVDR Final-/Follow-up-State-Machines, Current-Form-Verification-Muster und sichere Authority-Reconciliation-Gates. Konkrete Incident-, Device-, Patient-, Customer-, FSCA-, Authority-, Submission-, NB- oder Case-Daten bleiben kontrollierte Records/run-only.

Nur abstrahierte `memory-candidate-handoff-v1`-Kandidaten werden an `communication-memory-governance` übergeben.

## Qualitätsgate

Bestanden nur wenn:

- aktuelle Form-/Schema-/Channel-Anforderungen vor Finalisierung verifiziert werden,
- jeder Report Scope Version/Cut-off/SourceRefs besitzt,
- Investigation-Unknowns und materielle Contradictions sichtbar bleiben,
- Final-Non-reportable nicht ohne ausreichende Ursachenbasis als Closure-Shortcut verwendet wird,
- FSCA-/Effectiveness-Evidence konsumiert statt als zweite Engine neu berechnet wird,
- Manufacturer Final, Submission, Authority Receipt, Assessment und Closure strikt getrennt sind,
- Authority Silence nicht als Acceptance gewertet wird,
- Authority Feedback append-only und versioniert verarbeitet wird,
- Notified-Body- und Competent-Authority-States getrennt bleiben,
- neue Safety Facts/Scope Drift Finalization sofort unterbrechen und Reassessment triggern,
- Authority Closure nur mit verifizierter externer Evidence behauptet wird,
- konkrete Case-/Authority-Daten nicht in globales dauerhaftes Memory gelangen.
