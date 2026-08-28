---
name: sport-training-programming
description: Deprecated Compatibility-Fassade für frühere Aufrufe des monolithischen Sport-Trainingsprogrammierers. Übersetzt Legacy-Inputs in den kanonischen sport-training-plan-workflow und referenziert dessen sport-training-plan.json, ohne Kraft-, Ausdauer- oder Periodisierungslogik erneut zu besitzen.
implicitInvocation: false
version: 0.2.0
status: deprecated
discoverability: compatibility
deprecatedSince: 2026-08-28
replacedBy: sport-training-plan-workflow
owners:
  - GithubLarsKomo
requires:
  - sport-training-plan-workflow
outputs:
  - sport-training-programming-compatibility-run.json
lastEvaluated: 2026-08-28
---

# Sport Training Programming — Compatibility Facade

## Zweck

Dieser Skill erhält alte explizite Aufrufe von `sport-training-programming`, ist aber **keine zweite Trainingsplan-Engine** mehr. Neue Aufträge verwenden `sport-training-plan-workflow`.

Die Compatibility-Fassade darf Legacy-Eingaben normalisieren und den Nachfolger aufrufen. Das kanonische `sport-training-plan.json` bleibt ausschließlich Output und Ownership von `sport-training-plan-workflow`.

## Trigger

Nur explizit verwenden, wenn ein bestehender Prompt, eine gespeicherte Automation oder ein externer Consumer weiterhin den alten Skillnamen `sport-training-programming` referenziert.

Nicht implizit auswählen und nicht für neue Trainingsplan-Aufträge empfehlen.

## Voraussetzungen

- ursprüngliche Legacy-Inputs soweit verfügbar;
- Ziel/Sportart/Zeitfenster und reale Trainingsverfügbarkeit;
- bekannte Diagnostik-/Leistungsreferenzen und Health Constraints;
- Zugriff auf `sport-training-plan-workflow`.

Fehlende Legacy-Felder werden nicht erfunden. Sie werden entweder auf das aktuelle Eingabemodell abgebildet, als unbekannt weitergereicht oder lösen gezielte Klärung im Nachfolger aus.

## Ablauf

1. **Legacy-Aufruf erkennen.** Sicherstellen, dass die Compatibility-Fassade explizit angefordert wurde.
2. **Inputs normalisieren.** Frühere Ziel-, Termin-, Trainingshistorie-, Diagnostik-, Equipment- und Constraint-Felder auf die Eingaben des `sport-training-plan-workflow` abbilden.
3. **Keine Fachlogik ausführen.** Keine eigene Periodisierung, Kraft-/Power-Dosierung, Ausdauerzonen, Progression oder Taperlogik berechnen.
4. **Nachfolger aufrufen.** `sport-training-plan-workflow` mit den normalisierten Inputs ausführen.
5. **Plan referenzieren.** Das vom Nachfolger erzeugte `sport-training-plan.json` unverändert referenzieren; nicht kopieren und nicht als eigenen Output deklarieren.
6. **Compatibility-Manifest schreiben.** `sport-training-programming-compatibility-run.json` dokumentiert Legacy-Input-Mapping, Nachfolger, Plan-Referenz, Warnings und Migrationshinweis.

## Compatibility-Vertrag

Minimaler Output:

```json
{
  "legacySkill": "sport-training-programming",
  "replacementSkill": "sport-training-plan-workflow",
  "mappedInputs": [],
  "unmappedInputs": [],
  "trainingPlanRef": "sport-training-plan.json",
  "warnings": [],
  "migrationRequired": true
}
```

## Prüfungen

- Wurde die Fassade explizit statt implizit ausgewählt?
- Wird `sport-training-plan-workflow` als einziger fachlicher Nachfolger aufgerufen?
- Bleibt `sport-training-plan.json` ausschließlich beim Nachfolger in Ownership?
- Sind unmapped/unknown Legacy-Felder sichtbar statt erfunden?
- Enthält das Manifest einen klaren Migrationshinweis?
- Wurde keine alte monolithische Kraft-/Ausdauer-/Taperlogik reaktiviert?

## Fehlerbehandlung

- **Neuer normaler Trainingsplan-Auftrag:** direkt an `sport-training-plan-workflow` routen; Compatibility-Fassade nicht verwenden.
- **Unbekanntes Legacy-Feld:** dokumentieren und nur dann klären, wenn es die fachliche Planung beeinflusst.
- **Nachfolger nicht verfügbar:** keinen Legacy-Plan improvisieren; Fail mit Replacement-Hinweis.
- **Nachfolger meldet Safety/Health Review:** unverändert weiterreichen; keine Legacy-Override-Regel anwenden.

## Übergabe

Primärer Output dieser Fassade ist ausschließlich `sport-training-programming-compatibility-run.json`. Darin wird das vom Nachfolger erzeugte `sport-training-plan.json` referenziert. Aktive Consumer sollen auf `sport-training-plan-workflow` migriert werden.

## Abschlusskriterien

Die Fassade ist abgeschlossen, wenn der Legacy-Aufruf transparent auf den Nachfolger abgebildet wurde, das kanonische Trainingsplan-Artefakt unverändert referenziert wird, keine Fachlogik oder Output-Ownership dupliziert wurde und der Consumer einen eindeutigen Migrationspfad erhält.
