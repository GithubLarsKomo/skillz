---
name: leadership-reflection
description: Analysiert reale Führungssituationen als strukturierte Reflexion und trennt Beobachtung, eigenes Verhalten, Wirkung, Interpretation, Alternativerklärungen und Lernhypothesen. Verwenden nach relevanten Führungsereignissen; nicht zur Persönlichkeitsdiagnose anderer Personen.
---

# Leadership Reflection

## Zweck

Macht reale Führungssituationen lernbar, ohne Beobachtung und Interpretation zu vermischen.

## Ablauf

1. Situation, Ziel und Kontext festhalten.
2. beobachtbare Ereignisse und eigenes Verhalten extrahieren.
3. Verhalten anderer nur als beobachtete Handlungen erfassen.
4. Interpretationen separat markieren.
5. mindestens eine plausible Alternativerklärung prüfen, wenn die Interpretation handlungsrelevant ist.
6. Wirkung und Ergebnis von der vermuteten Absicht trennen.
7. Learning Hypotheses und wenige Candidate Experiments ableiten.
8. Safety Flags an `coaching-safety-routing` übergeben.

## Output

`leadership-reflection.json` enthält mindestens `schemaVersion`, `reflectionId`, `coachingCaseId`, `developmentGoalRefs`, `situation`, `observations`, `ownActions`, `otherPartyObservedActions`, `interpretations`, `alternativeInterpretations`, `effects`, `whatWorked`, `whatDidNotWork`, `learningHypotheses`, `candidateExperiments`, `confidence`, `safetyFlags` und `createdAt`.

## Harte Regeln

- „war defensiv“, „ist toxisch“ oder „will sabotieren“ sind Interpretationen, solange keine beobachtbare Definition und ausreichende Evidenz vorliegt.
- Keine Diagnose, Persönlichkeitsklassifikation oder spekulative Motivzuschreibung.
- Selbstkritik und Selbstbestätigung werden gleich behandelt: beide brauchen beobachtbare Anker.
- Drittinformationen nur soweit nötig persistieren.

## Übergabe

Validierte Lernhypothese → `leadership-behavior-experiment`; neue Zielstruktur → `leadership-development-model`; Safety-Signal → `coaching-safety-routing`.

## Abschlusskriterien

Die Situation ist so getrennt, dass Beobachtung, Interpretation und Lernhypothese nachvollziehbar sind und mindestens ein testbarer nächster Schritt möglich ist.
