---
name: leadership-delegation
description: Plant wirksame Delegation über Outcome, Entscheidungsrechte, Grenzen, Ressourcen, Autonomie, Checkpoints und Eskalationsbedingungen. Verwenden, wenn Verantwortung übertragen werden soll, ohne Ownership oder Status zu erfinden.
---

# Leadership Delegation

## Zweck

Plant Delegation als expliziten Vertrag über Ergebnis, Entscheidungsraum, Grenzen, Ressourcen, Autonomie, Kontrollpunkte und Eskalation. Der Skill überträgt keine Verantwortung automatisch und ersetzt keine formelle Rollen- oder Organisationsentscheidung.

## Ablauf

1. Gewünschtes Outcome statt bloßer Aktivität definieren.
2. Prüfen, welche Accountability beim Manager verbleibt und welche Verantwortung übertragen werden darf.
3. Entscheidungsrechte und reservierte Entscheidungen konkretisieren.
4. Constraints, Ressourcen, Abhängigkeiten und Informationszugang erfassen.
5. Autonomiegrad und minimale Checkpoints festlegen.
6. Eskalationsbedingungen vorab definieren.
7. Erfolgsevidenz und gegebenenfalls Entwicklungsnutzen beschreiben.
8. Erst nach bestätigter Übergabe den Zustand als delegiert behandeln.

## Output

`leadership-delegation-plan.json` enthält mindestens `schemaVersion`, `delegationId`, `outcome`, `delegateeRef`, `authority`, `constraints`, `resources`, `dependencies`, `checkpoints`, `escalationConditions`, `successEvidence`, `managerRetainedAccountabilities`, `developmentOpportunity`, `status`, `sourceRefs`, `unknowns` und `updatedAt`.

## Authority Levels

Verwende nur explizit bestätigte Stufen, z. B. `recommend`, `decide-with-approval`, `decide-within-boundaries` oder `own-outcome`. Titel oder Hierarchie allein beweisen keinen Entscheidungsraum.

## Regeln

- Delegation von Arbeit ist nicht automatisch Delegation von Entscheidungskompetenz.
- Verantwortung ohne notwendige Ressourcen oder Informationen als Risiko markieren.
- Checkpoints dürfen nicht zu verstecktem Micromanagement werden; sie müssen zum Risiko und Reifegrad der Aufgabe passen.
- Status `briefed`, `active`, `completed` oder gleichwertig nur bei bestätigter Evidenz.
- Keine Leistungs- oder Persönlichkeitsdiagnose der delegierten Person aus Einzelereignissen ableiten.

## Übergaben

Bestätigte Delegation und offene Checkpoints können an `decision-and-follow-up-tracker` übergeben werden. Entwicklungsrelevante Beobachtungen können später `leadership-reflection` speisen.

## Abschlusskriterien

Outcome, Entscheidungsspielraum, Grenzen, Ressourcen, Checkpoints, Eskalation und retained Accountabilities sind explizit und widerspruchsfrei; geplanter und tatsächlich bestätigter Status bleiben getrennt.
