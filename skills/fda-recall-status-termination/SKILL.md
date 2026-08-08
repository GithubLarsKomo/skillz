---
name: fda-recall-status-termination
description: Erstellt und verfolgt FDA-Recall-Statusberichte, Termination-Request-Pakete und verifizierte FDA-Authority-States aus kontrollierter Field-Action-Evidence, ohne interne Completion als FDA Termination zu simulieren.
userFacing: true
implicitInvocation: false
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - fda-corrections-removals
  - medical-device-field-action-effectiveness
  - regulatory-evidence-traceability
  - quality-record-integrity
outputs:
  - fda-recall-status-report.json
  - fda-recall-termination-request.json
  - fda-recall-authority-state.json
lastEvaluated: 2026-08-08
---

# FDA Recall Status and Termination

## Zweck und Grenze

Dieser Skill besitzt den kontrollierten Übergang von laufender FDA-Recall-Execution zu periodischem Recall-Status-Reporting, Termination-Request-Readiness und verifizierter FDA-Termination. Er konsumiert die regulatorische Ausgangslage aus `fda-corrections-removals` und die operative Evidence aus `medical-device-field-action-effectiveness`.

Er entscheidet weder rückwirkend über Part-806-Reportability noch über Recall Classification, Recall Strategy oder Effectiveness-Check-Level. Er kann FDA-Entscheidungen vorbereiten und dokumentieren, aber nicht simulieren. Insbesondere sind `operationally-complete`, `termination-requested`, `FDA-review-pending` und `FDA-terminated` getrennte Zustände.

## Current-source Baseline

Für freiwillige Recalls nach 21 CFR Part 7 fordert FDA periodische Recall-Statusberichte an, damit die Agency den Fortschritt bewerten kann. Die Frequenz wird fallbezogen durch FDA bestimmt; als allgemeiner Richtwert nennt FDA 2–4 Wochen. Der Statusbericht enthält, sofern nicht anders spezifiziert oder unpassend, insbesondere Consignee Notification, Responses/Non-Responses, zurückgeführte oder korrigierte Mengen, accounted-for quantities, Anzahl/Ergebnisse der Effectiveness Checks und eine Completion-Schätzung. Statusberichte werden erst beendet, wenn FDA den Recall terminiert.

FDA-Termination liegt erst vor, wenn FDA bestimmt, dass alle angemessenen Bemühungen entsprechend Recall Strategy durchgeführt wurden und Produktentfernung sowie angemessene Correction/Disposition hinreichend erfolgt sind. Ein Unternehmen kann Termination schriftlich beantragen; dazu gehören der aktuelle Recall-Statusbericht und die Beschreibung der Disposition des recalled product.

## Kernprinzipien

- **FDA cadence is an external case state:** keine feste 2-/4-Wochen-Frist erfinden, wenn FDA für den konkreten Recall eine andere Frequenz festgelegt hat.
- **Status report is a snapshot, not history rewrite:** jeder Report trägt Scope/Population/Cut-off und bleibt historisch erhalten.
- **Unknowns remain reportable facts:** Non-Responder, not-located units und ungeklärte Mengen werden nicht aus dem nächsten Bericht entfernt.
- **Effectiveness evidence is consumed, not recomputed:** der Skill übernimmt verifizierte Effectiveness-/Reconciliation-Evidence und baut keine zweite Effectiveness Engine.
- **Completed ≠ terminated:** interner oder öffentlicher `completed` State ist nicht FDA `terminated`.
- **Request ≠ decision:** `termination-requested` oder ein eingereichtes Paket beweist keine FDA-Termination.
- **FDA state needs FDA evidence:** `FDA-terminated` nur mit verifizierbarer Agency Notification/Authority Evidence.
- **Agency questions reopen the package, not history:** Rückfragen, zusätzliche Anforderungen oder abweichende Agency-Einschätzungen erzeugen neue Authority Events und neue Paketversionen.
- **New safety facts bypass termination:** neue serious events, Correction Failures oder Scope Extensions gehen sofort an MDR/806/Recall/Risk/CAPA Owner; ein vorbereiteter Termination Request wird dadurch nicht immun.
- **806 amendment stays separate:** Scope-Erweiterungen, die eine Part-806-Amendment-Pflicht auslösen können, werden zurück an `fda-corrections-removals` geroutet statt nur im Recall-Statusbericht versteckt.

## Workflow

### 1. FDA Recall Authority Baseline übernehmen

Erfasse Recall/Event Identifier, aktuelle FDA Classification/Strategy soweit evidenziert, DRC/Authority Reference, angeforderte Reporting Frequency, Recall Depth/Effectiveness Strategy, Scope Version, letzte FDA-/Firm-Communication und offene Agency Requests.

Unbekannte oder nicht belegte Agency States bleiben `unknown|pending`; sie werden nicht aus internen Annahmen ergänzt.

### 2. Status-Reporting Clock ableiten

Nutze zuerst die konkrete FDA-Anforderung. Nur wenn keine recall-spezifische Frequenz vorliegt, darf der aktuelle FDA-General-Guidance-Richtwert als Planungsannahme mit expliziter Provenance verwendet werden. Ein Planning Default wird niemals als behördlich bestätigte Deadline ausgegeben.

### 3. Status Snapshot erzeugen

`fda-recall-status-report.json` enthält mindestens:

- Recall/Scope/Population Version + Cut-off,
- Consignees notified + date/method summary,
- responding consignees + quantities on hand,
- nonresponding consignees,
- returned/corrected quantities and accounted-for quantity,
- Effectiveness Check count/results per authorized strategy,
- unresolved downstream/product states,
- estimated completion timeframe,
- new safety facts/scope changes,
- prior report reference,
- current Agency Requests/Questions,
- sourceRefs and evidence gaps.

Statuszahlen müssen mit den zugrunde liegenden Communication-/Physical-/Effectiveness-Records reconciled sein.

### 4. Agency Feedback versioniert verarbeiten

Jede FDA-Rückfrage, Strategieänderung, Classification-/Status-Mitteilung oder zusätzliche Evidence-Anforderung wird als append-only Authority Event erfasst. Eine neue Agency Instruction supersediert nur den betroffenen aktuellen Planungsstate, nicht historische Berichte oder frühere Agency-Evidence.

### 5. Termination-Readiness prüfen

Ein Termination Request wird nur vorbereitet, wenn die aktuell autorisierte Recall Strategy, Effectiveness-/Product-Reconciliation-Evidence und verbleibenden Unknowns einen belastbaren Antrag tragen. Interne Zielquoten oder `operationally-complete` allein reichen nicht.

`fda-recall-termination-request.json` enthält mindestens:

- Recall Identifier/Authority Reference,
- aktuelle Status-Report-Version,
- Recall Strategy/Classification Evidence,
- Effectiveness Summary,
- Product Disposition Description,
- unresolved items + rationale,
- new safety facts check,
- requested action `termination-review`,
- human approval/submission state.

### 6. External Submission nicht simulieren

Vorbereitung, Approval, Submission, FDA Receipt, FDA Review und FDA Decision bleiben getrennte Zustände. Externe irreversible Aktion erfolgt über den vorgesehenen Human/External-Action-Pfad; ohne Evidence wird kein `submitted`, `received` oder `terminated` gesetzt.

### 7. FDA-Termination reconciliieren

`fda-recall-authority-state.json` führt mindestens:

`ongoing|firm-completed-not-terminated|termination-request-ready|termination-requested|FDA-review-pending|FDA-more-information-required|FDA-terminated-verified|reopened-or-scope-extended|unknown`.

`FDA-terminated-verified` benötigt verifizierte FDA-Evidence. Öffentliche Datenbank-/Enforcement-States können zusätzliche Evidence sein, ersetzen aber nicht automatisch die kontrollierte Case Evidence, wenn diese widersprüchlich oder zeitlich unklar ist.

### 8. Reopen / Amendment

Neue Lots/Batches, Scope Extensions, wiederholte Safety Events oder FDA-Nachforderungen können den vorherigen Readiness-State supersedieren. Historische Termination-Request-Versionen und Reports bleiben unverändert; der aktuelle State wird neu bewertet und an 806/MDR/Risk/CAPA/Communication/Execution geroutet.

## Output-Verträge

`fda-recall-status-report.json` enthält periodischen, versionierten FDA-Recall-Fortschritt mit den durch FDA erwarteten Statusdimensionen, Scope/Cut-off, Evidence und offenen Punkten.

`fda-recall-termination-request.json` enthält die evidenzgebundene Termination-Request-Vorbereitung einschließlich aktuellem Statusbericht und Product-Disposition-Beschreibung, aber keinen simulierten Submission-/Decision-State.

`fda-recall-authority-state.json` enthält append-only FDA Authority Events, angeforderte Reporting Frequency, Agency Questions, Submission/Receipt/Review/Termination Evidence, superseded states und reopen triggers.

## Memory Path

Persistenzwürdig sind abstrahierte FDA-Recall-Status-State-Machines, sichere Report-Snapshot-/Authority-Reconciliation-Muster und wiederverwendbare Termination-Gates. Konkrete Recall-, Customer-, Device-, Quantity-, FDA-Case-, DRC-, Submission- oder Authority-Communication-Daten bleiben kontrollierte Records/run-only.

Nur abstrahierte `memory-candidate-handoff-v1`-Kandidaten werden an `communication-memory-governance` übergeben.

## Qualitätsgate

Bestanden nur wenn:

- recall-spezifische FDA-Frequenz vor einem generischen 2–4-Wochen-Richtwert priorisiert wird,
- jeder Statusbericht Version/Cut-off und nachvollziehbare Source Evidence besitzt,
- Notification/Response/Non-Response, Product Return/Correction/Accounting und Effectiveness Checks getrennt berichtet werden,
- Unknowns und Non-Responder nicht aus späteren Reports verschwinden,
- Effectiveness nicht doppelt berechnet wird,
- `completed`, `termination-requested` und `FDA-terminated` strikt getrennte Zustände bleiben,
- FDA-Termination nur mit externer FDA-Evidence behauptet wird,
- Agency Questions/Changes als neue Authority Events statt History Rewrite geführt werden,
- neue Safety Facts oder Scope Extensions Termination-Readiness unterbrechen und notwendige 806/MDR-Reassessment-Pfade auslösen,
- konkrete Recall-/Authority-Daten nicht in globales dauerhaftes Memory gelangen.
