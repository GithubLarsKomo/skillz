---
name: leadership-development-model
description: Übersetzt einen bestätigten Leadership-Coaching-Auftrag in wenige beobachtbare Entwicklungsziele mit Situation, aktuellem Verhalten, Zielverhalten, erwarteter Wirkung und Messsignalen. Verwenden, bevor konkrete Verhaltensexperimente geplant werden.
---

# Leadership Development Model

## Zweck

Operationalisiert Leadership-Entwicklung. Der Skill modelliert keine Persönlichkeit, sondern beobachtbare Situationen, Verhaltensmuster und gewünschte Veränderungen.

## Ablauf

1. Coaching-Zweck und relevante Rollenanforderungen fixieren.
2. Herausforderung als Situation plus beobachtbares Verhalten formulieren.
3. Interpretation und Eigenschaftszuschreibung entfernen oder als Hypothese markieren.
4. Zielverhalten beschreiben, das in realen Situationen erkennbar ist.
5. wenige Observable Signals definieren.
6. erwartete Wirkung getrennt vom Verhalten festhalten.
7. Unsicherheit und konkurrierende Erklärungen sichtbar lassen.

## Output

`leadership-development-model.json` enthält mindestens `schemaVersion`, `developmentModelId`, `coachingCaseId`, `roleContextRefs`, `developmentGoals`, `assumptions`, `unknowns` und `updatedAt`.

Jedes Development Goal enthält `id`, `challenge`, `contexts`, `currentBehavior`, `targetBehavior`, `observableSignals`, `expectedEffect`, `evidenceStatus`, `confidence` und `status`.

## Regeln

- `currentBehavior` darf Selbstbeobachtung oder Fremdfeedback enthalten, aber Provenance bleibt sichtbar.
- Ein Ziel wie „charismatischer werden“ ist nicht ausreichend operationalisiert.
- Keine geschützten oder sachfremden Merkmale als Leadership-Defizit verwenden.
- Nicht mehr als wenige aktive Entwicklungsziele parallel priorisieren.

## Übergabe

Aktives Ziel → `leadership-behavior-experiment`; neue reale Situation → `leadership-reflection`.

## Abschlusskriterien

Mindestens ein priorisiertes Ziel ist als beobachtbare Verhaltensänderung mit Situation und Messsignal operationalisiert.
