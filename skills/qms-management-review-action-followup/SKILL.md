---
name: qms-management-review-action-followup
description: Verfolgt Management-Review-Actions evidenzbasiert über Routing, Implementierung, Wirksamkeit und Closure bis zum Folgereview.
userFacing: true
implicitInvocation: true
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - qms-management-review-governance
  - decision-and-follow-up-tracker
  - deferred-external-action-verification
outputs:
  - management-review-follow-up-status.json
  - management-review-effectiveness-gaps.json
  - management-review-return-input.json
lastEvaluated: 2026-08-08
---

# QMS Management Review Action Follow-up

## Zweck und Grenze

Dieser Skill schließt die zeitliche Schleife nach einem QMS Management Review. Er übernimmt ausschließlich **bestätigte** `management-review-actions.json`, verfolgt deren Routing, Implementierungs-, Effectiveness- und gegebenenfalls externe Closure-Evidenz und erzeugt den belegten Rückgabestatus für den nächsten Management Review.

Er ist **kein** zweiter CAPA-, Risk-, PMS-, Regulatory-Change-, Audit- oder Task-Manager. Die fachliche Entscheidung und Wirksamkeitsbewertung bleibt beim jeweiligen Owner-Skill. Dieser Skill besitzt den übergreifenden Governance-Status der Management-Review-Action und verhindert, dass „beschlossen“, „zugewiesen“, „umgesetzt“, „wirksam“ und „geschlossen“ vermischt werden.

## Temporal Feedback Contract

Der Lifecycle ist bewusst zeitlich und wird nicht als zyklische harte Skill-Dependency modelliert:

`Management Review -> management-review-actions.json -> qms-management-review-action-followup -> management-review-return-input.json -> nächster Management Review`

`qms-management-review-action-followup` benötigt den erzeugenden Management-Review-Skill. Der nächste `qms-management-review-governance`-Lauf konsumiert den Return Input als Vorperioden-Evidenz, sobald frühere Actions existieren. Dadurch bleibt der Capability-Graph azyklisch, während der fachliche Feedback-Loop explizit und testbar ist.

## Kernprinzipien

- **Decision is not action completion:** eine bestätigte Managemententscheidung erzeugt eine Action, aber keine Implementierung.
- **Routing is not implementation:** Übergabe an CAPA, Risk, PMS, Change oder andere Owner ändert den Status höchstens zu `routed|in-progress`.
- **Implementation is not effectiveness:** Completion Evidence einer Maßnahme beweist noch nicht, dass ihr beabsichtigter Effekt erreicht wurde.
- **Effectiveness is not always closure:** wenn externe Regulatory-/Authority-/Customer-/Certification-Closure erforderlich ist, bleibt der Management-Review-Punkt bis zur verifizierten externen Evidenz `external-pending`.
- **Specialist ownership remains intact:** Root Cause, CAPA Effectiveness, Risk Acceptability, PMS Signal State, Design/Regulatory Change Impact oder Authority State werden nicht neu entschieden.
- **No silent ageing:** überfällige, blockierte, ineffektive oder high-impact Actions bleiben sichtbar und gehen zwingend in den Return Input.
- **Re-open on failed effectiveness:** fehlgeschlagene Effectiveness Verification führt nicht zu kosmetischer Closure, sondern zu Re-open/Routing an den zuständigen Fachprozess.

## Action-State-Modell

Zulässige Governance-Zustände:

`pending|routed|in-progress|implemented|effectiveness-pending|effective|ineffective|blocked|external-pending|closed|cancelled|superseded|unknown`

Regeln:

- `implemented` benötigt objektive Completion Evidence des Fach-Owners.
- `effective` benötigt die vorab definierte oder fachlich bestätigte Effectiveness Evidence; reine Aktivitäts-/Terminbestätigung genügt nicht.
- `closed` ist nur zulässig, wenn alle für die Action erforderlichen Completion-, Effectiveness-, Risk/QMS/Document-Update- und externen Closure-Gates erfüllt sind.
- `cancelled|superseded` benötigt bestätigte Autorität, Begründung, Datum und gegebenenfalls Ersatz-Action.
- `overdue` ist ein Zeit-/Governance-Merkmal, kein Beweis für Ineffektivität oder Noncompliance.
- Fehlende Owner-, Due-Date- oder Status-Evidenz bleibt `unknown`; der Skill erfindet sie nicht aus Organigramm oder Kontext.

## Workflow

### 1. Management-Review-Actions normalisieren

Übernimm Action ID, Source Review ID/Datum, bestätigte Decision Reference, Beschreibung, Owner/Due Date soweit bestätigt, Target Skill/System, erforderliche Completion-/Effectiveness-Evidence, externe Abhängigkeiten, Priorität/High-Impact-State und Follow-up Trigger.

### 2. Generic Follow-up State konsolidieren

Nutze `decision-and-follow-up-tracker` für bestätigte Ownership-, Due-, Waiting-, Delegation- und Statusinformationen. Ein Produktivitätsstatus wie `done` wird nicht automatisch zum QMS-Zustand `effective|closed` hochgestuft.

### 3. Specialist Evidence referenzieren

Ordne die Action dem tatsächlichen Fach-Owner zu, beispielsweise:

- CAPA/Investigation → `medical-device-capa` / `evidence-based-causal-investigation`
- Risk → `medical-device-risk-management-iso14971`
- PMS/Postmarket → `medical-device-pms-system`
- Regulatory-/Design Change → `regulatory-change-impact-orchestrator` / `design-change-regulatory-impact`
- Labeling/Claims → `medical-device-labeling-ifu` / `regulatory-claims-consistency`
- Audit Finding → `audit-inspection-finding-response`
- Controlled Documents → `controlled-quality-documentation`

Übernimm nur belegte Status-/Evidence-References; der Follow-up-Skill rechnet deren Fachentscheidung nicht neu.

### 4. Completion und Effectiveness getrennt bewerten

Prüfe pro Action:

- wurde die geplante Maßnahme tatsächlich implementiert?
- liegt die geforderte Completion Evidence vor?
- ist ein Effectiveness Criterion definiert?
- ist das Beobachtungsfenster/der Trigger bereits erreicht?
- liegt geeignete Effectiveness Evidence vor?
- hat die Fachbewertung `effective|ineffective|unknown` ergeben?
- sind erforderliche Risk/QMS/Document/PMS/Regulatory-Updates abgeschlossen?

Wenn das Beobachtungsfenster noch läuft, bleibt `effectiveness-pending`; eine erledigte Task-Liste ist kein Ersatz.

### 5. Externe Closure separat verifizieren

Wenn eine Action externe Meldung, Authority-/NB-/AO-/Customer-Bestätigung oder anderen asynchronen Endzustand benötigt, nutze `deferred-external-action-verification`. Interne Implementierung oder Managementbestätigung darf einen `external-pending`-Status nicht in `closed` umwandeln.

### 6. Ineffektive oder blockierte Actions routen

Bei `ineffective|blocked|unknown` dokumentiere Ursache/Gaps und route an den zuständigen Owner. Eine ineffektive CAPA kann neue Investigation/CAPA/Risk/PMS-/Change-Arbeit auslösen; der Follow-up-Skill entscheidet diese Folgearbeit nicht selbst.

### 7. Return Input für den nächsten Management Review erzeugen

`management-review-return-input.json` enthält mindestens:

- offene/überfällige/blockierte Actions,
- `implemented` aber noch nicht `effective` bewertete Actions,
- ineffektive/re-opened Actions,
- `external-pending` States,
- High-Impact-Ausnahmen,
- seit dem letzten Review verifiziert geschlossene Actions mit Evidence References,
- cancelled/superseded Actions mit Autorität und Begründung,
- Effectiveness/Data Gaps,
- Entscheidungen/Ressourcenfragen für Top Management.

Geschlossene Punkte dürfen für Trend-/Wirksamkeitsbewertung sichtbar bleiben; sie werden nicht einfach aus der Historie gelöscht.

## Output-Verträge

`management-review-follow-up-status.json` enthält pro Action Source Review, Decision Reference, Owner/Due soweit bestätigt, Target Owner, Governance State, Completion Evidence, Effectiveness State/Evidence, External State/Evidence, Overdue/High-Impact Flags, Blocker, Re-open State und `lastConfirmedAt`.

`management-review-effectiveness-gaps.json` enthält fehlende/ungeeignete Completion- oder Effectiveness-Evidence, nicht erreichte Beobachtungsfenster, ungeklärte Ownership, externe Pending States und den jeweils nächsten evidenzbeschaffenden Schritt.

`management-review-return-input.json` ist der aggregierte, datensparsame Vorperioden-Input für den nächsten `qms-management-review-governance`-Lauf. Es referenziert Spezialisten-Evidenz statt Rohdaten zu duplizieren.

## Memory Path

Persistenzwürdig sind nur abstrahierte, validierte Action-State-/Effectiveness-/Escalation-Muster. Konkrete Managemententscheidungen, Owner/Due Dates, aktuelle CAPA-/Risk-/PMS-/Regulatory-Zustände, Audit Findings, externe Authority States und aktuelle Effectiveness-Ergebnisse bleiben kontrollierte QMS-/Project-/Regulatory Records und nicht globales Memory. Geeignete Kandidaten werden als `memory-candidate-handoff-v1` an `communication-memory-governance` übergeben; dieser Skill persistiert nichts selbst.

## Grenzen

- Keine Managemententscheidung, Root Cause, Risk Acceptance oder CAPA Effectiveness erfinden.
- Kein `closed` aus Meeting-Minutes, Task-Checkbox oder Owner-Aussage ohne erforderliche Evidenz ableiten.
- Keine externe Authority-/NB-/AO-/Customer-Closure ohne verifizierten externen Endzustand behaupten.
- Keine personenbezogenen Rohfälle oder unnötigen Complaint-/Patientendaten in Follow-up- oder Return-Inputs kopieren.

## Qualitätsgate

Bestanden nur wenn:

- jede Action auf eine bestätigte Managemententscheidung und Source Review zurückgeführt wird,
- Routing, Implementierung, Effectiveness und Closure getrennte Zustände bleiben,
- Completion-/Effectiveness-Evidence vom zuständigen Fach-Owner referenziert wird,
- `implemented` ohne Effectiveness Evidence nicht als `effective|closed` erscheint,
- erforderliche externe Closure separat verifiziert wird,
- ineffektive/blockierte/high-impact Actions sichtbar bleiben und korrekt re-routed werden,
- der nächste Management Review einen vollständigen Return Input zu Vorperioden-Actions erhält,
- aktuelle QMS-/Regulatory-Zustände nicht in globales dauerhaftes Memory gelangen.
