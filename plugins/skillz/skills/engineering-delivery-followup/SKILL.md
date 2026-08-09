---
name: engineering-delivery-followup
description: Verfolgt eine reviewte Softwareänderung vom immutable Review-Head über externe CI-/Merge-Prüfung bis zu verifizierter Merge-, Issue- und Requirement-Closure, ohne Code Review, Implementierung oder Deployment zu duplizieren.
---

# Engineering Delivery Follow-up

## Zweck und Grenze

Dieser Skill besitzt die Delivery-/Closure-Schicht **nach** einem fachlich und technisch abgeschlossenen `two-axis-code-review`. Er verfolgt den exakt reviewten Head-SHA durch Required Checks, Mergefähigkeit, Merge, optionale Deployment-/Release-Zustände sowie Issue-/Requirement-Closure und erzeugt den verifizierten Rückkanal für die nächste Engineering-Iteration.

Er implementiert keinen Code, führt keinen zweiten Code Review durch, entscheidet keine neue Architektur und ersetzt weder GitHub-/CI-/Deployment-Systeme noch Issue-Tracker. Externe Zustände werden nur aus deren Evidenz übernommen und bei asynchronen Vorgängen über `deferred-external-action-verification` nachverfolgt.

## Kernprinzipien

- **Immutable review scope:** Review-Entscheidung und Evidence gelten nur für den exakt geprüften `reviewedHeadSha`.
- **Head change invalidates approval:** Jeder neue Commit nach dem Review setzt die Delivery auf `review-stale`, bis der neue Head erneut fachlich/technisch geprüft wurde.
- **Review-approved is not merge-ready:** Merge Readiness benötigt zusätzlich aktuelle Required Checks, Branch-Protection-/Review-Gates, Mergeability und keine bekannten blockierenden Zustände.
- **Merge is an external state:** Ein ausgelöster Merge gilt erst nach verifiziertem Merge-Ergebnis beziehungsweise Zielbranch-Evidenz als `merged`.
- **Merged is not deployed:** Deployment/Release ist eine eigene optionale externe Achse.
- **Merged is not issue-closed:** Issue-/Requirement-Closure benötigt den vereinbarten Closure-Nachweis; ein Merge allein schließt kein Issue automatisch.
- **Issue closed is not requirement verified:** Ein Tracker-Status `closed` ersetzt keine Traceability von Acceptance Criteria/Requirement IDs auf die tatsächlich gemergte Revision.
- **No silent follow-up loss:** Nicht-blockierende Review Notes, Residual Risks und vereinbarte Follow-ups bleiben bis zur expliziten Disposition sichtbar.

## Zustandsmodell

Verwende mindestens folgende getrennte Zustände:

`review-blocked|review-approved|review-stale|external-pending|merge-ready|merge-pending|merged|deployment-pending|deployed|issue-closure-pending|closed-with-followups|closed|unknown`

Statusübergänge erfolgen nur auf Evidenz. Ein späterer Zustand darf einen früheren fehlenden Nachweis nicht überdecken.

## Workflow

### 1. Review-Baseline fixieren

Übernimm aus `two-axis-code-review` mindestens Repository, Base, Branch, `reviewedHeadSha`, Achsenstatus, Review Decision, blockierende Findings, Residual Risks und noch ausstehende externe Prüfungen.

Bei `request-changes|insufficient-evidence` bleibt der Zustand `review-blocked` und die Arbeit wird an `implement-from-issue` beziehungsweise den benannten Diagnosepfad zurückgegeben. Keine Merge-Nachverfolgung beginnen.

### 2. Head-Freshness prüfen

Löse den aktuellen Branch-/PR-Head erneut auf und vergleiche ihn mit `reviewedHeadSha`.

- identisch: Review kann weiter als Baseline dienen;
- abweichend: `review-stale`; keine frühere Freigabe, CI oder Merge Readiness auf den neuen Head übertragen.

Auch ein Konfliktauflösungs-, Rebase-, Formatierungs- oder "nur kleiner" Commit ist ein neuer Head und benötigt die für den Scope erforderliche erneute Review-Evidenz.

### 3. Externe Checks verifizieren

Prüfe Required CI/Checks exakt für den reviewten Head. Trenne:

- `required-passed`,
- `required-failed`,
- `pending`,
- `missing`,
- `stale`,
- `not-applicable`,
- `unknown`.

Ältere grüne Läufe, Checks eines anderen SHA oder nur lokal erfolgreiche Tests sind keine aktuelle externe Merge-Evidenz. Asynchrone Checks an `deferred-external-action-verification` übergeben.

### 4. Merge Readiness bestimmen

`merge-ready` nur wenn:

- Review Decision für aktuellen Head freigabefähig ist,
- erforderliche Checks für exakt diesen Head grün sind,
- erforderliche Review-/Branch-Protection-Gates erfüllt sind,
- Mergeability aktuell positiv beziehungsweise ohne blockierende Unklarheit ist,
- keine bekannte offene Sicherheits-, Migrations- oder Betriebsbedingung das Merge verbietet.

Ein Merge-Button oder `mergeable=true` allein reicht nicht.

### 5. Merge extern verifizieren

Wenn der Merge ausgelöst wurde, zunächst `merge-pending`. `merged` erst bei belastbarer externer Evidenz, z. B. bestätigtem PR-Merge mit Merge-/Squash-SHA oder nachweisbarer Aufnahme der Änderung in den Zielbranch.

Ein geschlossener PR ohne Merge-Beleg ist **nicht** `merged`.

### 6. Deployment/Release separat verfolgen

Nur wenn Deployment oder Release Teil des vereinbarten Done-Kriteriums ist, separate Zustände und Evidenz führen. Ein Merge erzeugt niemals automatisch `deployed` oder `released`.

### 7. Issue- und Requirement-Closure prüfen

Für jedes Issue/Requirement dokumentiere:

- Source ID,
- Acceptance-/Closure-Kriterium,
- gemergte Revision,
- Evidence Reference,
- Tracker State,
- Closure State.

Tracker-`closed` ohne Evidence bleibt `unknown` oder Gap. Umgekehrt kann fachliche Acceptance verifiziert sein, während ein externes Issue technisch noch offen ist; diese Zustände nicht zusammenziehen.

### 8. Follow-ups und Residual Risks dispositionieren

Nicht-blockierende Notes, bekannte Restrisiken, Debt und spätere Follow-ups behalten Source Reference, Owner/Due nur wenn bestätigt sowie Status. Keine spätere Roadmap-Arbeit als Teil des abgeschlossenen Issues vortäuschen.

### 9. Rückkanal für nächste Iteration erzeugen

`engineering-iteration-return-input.json` enthält den verifizierten Delivery-Zustand der letzten Iteration. Die nächste Ausführung von `iterate-software-projects` muss diesen Zustand berücksichtigen, wenn er vorhanden ist. Ein fehlender Return Input trotz bekannter vorheriger reviewter Arbeit ist ein Continuity Gap und kein Beleg für Abschluss.

## Output-Verträge

`engineering-delivery-status.json` enthält Repository/PR, `reviewedHeadSha`, current Head, Review Decision, Check States, Merge Readiness, Merge State, Deployment/Release State soweit anwendbar, Issue-/Requirement-Closure sowie External Evidence References.

`engineering-closure-gaps.json` enthält stale Review, fehlende/rote/pending Checks, Merge Blocker, ungeprüfte Issue-/Requirement-Closure, offene Deployment-/Release-Bedingungen und undispositionierte Follow-ups.

`engineering-iteration-return-input.json` enthält mindestens letzte Iteration/Issue, Requirement IDs, reviewed/merged SHA, Status `closed|closed-with-followups|blocked|pending|unknown`, bestätigte Completion Evidence, offene Gaps/Risks, `doNotRepeat` sowie genau die früheste noch notwendige Aktion.

## Memory Path

Persistenzwürdig sind nur abstrahierte Delivery-Governance-Muster wie die Trennung Review/Merge/Deployment/Closure, stabile Freshness-Regeln und wiederverwendbare Failure-Mode-Heuristiken. Konkrete Repository-Namen, PR-/Issue-IDs, SHAs, aktuelle CI-/Deployment-Zustände, offene Findings und unveröffentlichte Änderungen bleiben Run-/Project-State. Übergib nur validierte, nicht-sensitive `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; dieser Skill persistiert nichts selbst.

## Grenzen

- Kein Code schreiben oder Review-Ergebnis fachlich neu entscheiden.
- Keine Merge-, Deployment-, Release- oder Issue-Closure simulieren.
- Keine Freigabe eines neuen Head-SHA aus einer Review-Evidenz des alten Heads ableiten.
- Keine externen Checks durch lokale Tests ersetzen, wenn sie explizit Required Gate sind.
- Keine automatischen Owner, Due Dates oder Tracker-Transitions erfinden.

## Qualitätsgate

Pass nur, wenn:

- Review-Evidenz exakt an `reviewedHeadSha` gebunden ist,
- jeder Head-Wechsel die alte Review-Freigabe stale macht,
- Review Approval, Merge Readiness, Merge, Deployment und Issue-/Requirement-Closure getrennte Evidenzzustände besitzen,
- Required Checks exakt dem relevanten Head zugeordnet sind,
- externe Aktionen nicht vor ihrem verifizierten Endzustand als erfolgreich gelten,
- Tracker-Status keine Requirement-Verifikation ersetzt,
- Restrisiken/Follow-ups nicht beim Merge verloren gehen,
- der Return Input die nächste Iteration ohne Wiederholung abgeschlossener Arbeit fortsetzbar macht.
