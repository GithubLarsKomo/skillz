---
name: learning-next-step
description: Wählt aus Lernmission, aktuellem Kompetenzzustand, offenen Lücken und verfügbarer Evidenz genau den nächsten pädagogischen Schritt mit kalibrierter Schwierigkeit. Verwenden, wenn zwischen Erklärung, Beispiel, Retrieval, Anwendung, Transfer, ETF-Lernsitzung, Prüfung oder realer Aufgabe entschieden werden soll; nicht als Scheduler einzelner Wiederholungskarten.
---

# Learning Next Step

## Zweck

Dieser Skill entscheidet **welche Lernhandlung als Nächstes den größten sinnvollen Kompetenzgewinn verspricht**. Er nutzt Mission, aktuellen Lernzustand, Voraussetzungen und offene Lücken. Er berechnet keine kartenbezogenen Fälligkeiten und ersetzt keinen ETF-Scheduler.

## Kernprinzip

**Die nächste Aufgabe soll gerade schwer genug sein, um neue Evidenz zu erzeugen.** Triviale Wiederholung erzeugt wenig Information; eine deutlich überfordernde Aufgabe erzeugt hauptsächlich Scheitern ohne saubere Diagnose.

## Eingaben

- `learning-mission.json`,
- `learning-state.json`,
- optional aktuelle Assessment-Ergebnisse,
- optional verfügbare Ressourcen oder Runtime-Fähigkeiten,
- optional zeitliche oder prüfungsbezogene Constraints.

## Zulässige Schrittarten

- `explanation`
- `worked-example`
- `guided-practice`
- `retrieval`
- `application`
- `transfer`
- `etf-learning-session`
- `etf-exam`
- `real-world-task`
- `evidence-gap-resolution`

## Entscheidungslogik

### 1. Blockierende Wissenslücken zuerst prüfen

Wenn eine notwendige fachliche Grundlage unklar oder unzureichend belegt ist, wähle `evidence-gap-resolution` oder eine gezielte Erklärung statt eine Prüfung auf unsicherer Basis zu bauen.

### 2. Einführung nicht mit Abruf verwechseln

Bei `introduced` ist meist ein erster Retrieval-Schritt sinnvoll, sobald genug Erklärung vorhanden ist. Mehr Erklärung ist nur dann vorzuziehen, wenn der Lernende die Aufgabe wegen fehlender konzeptueller Grundlage nicht sinnvoll versuchen kann.

### 3. Retrieval vor Anwendung

Wenn ein Kernkonzept noch nicht ohne unmittelbare Hilfe abrufbar ist, wähle Retrieval oder geführte Praxis, bevor repräsentative Anwendung als Kompetenznachweis erwartet wird.

### 4. Anwendung vor Transfer

Ein Transferfall soll erst dominieren, wenn repräsentative Anwendung bereits hinreichend demonstriert ist oder der Transferfall selbst diagnostisch sinnvoll bleibt.

### 5. Fehlerart berücksichtigen

- isolierter Fehler: gezielte Wiederholung oder erneuter Abruf,
- wiederholte Unsicherheit: Erklärung plus kontrastierendes Beispiel,
- stabile Fehlvorstellung: korrektive Intervention,
- gute Recall-Leistung, schwache Anwendung: repräsentative Fallaufgabe,
- gute Anwendung, ungeprüfter Transfer: neuer Kontext.

### 6. ETF nur für passende Runtime-Aufgaben wählen

Wähle eine ETF-Lernsitzung, wenn strukturierte oder wiederholte Retrieval-/Anwendungsvarianten sinnvoll sind. Wähle eine ETF-Prüfung, wenn ein zusammenhängender Assessment-Block benötigt wird.

Teach/Next-Step definiert die **semantische Absicht**. ETF bestimmt die konkrete Reihenfolge und Fälligkeit einzelner QuestionVariants.

### 7. Reale Praxis einbeziehen

Für Wisdom-/Praxisebene kann die beste nächste Evidenz aus einer realen Aufgabe, KOL-/Mentorengespräch, Review oder tatsächlichen Umsetzung stammen. Community- oder Praxisfeedback ersetzt bei fachlich regulierten Claims nicht die autoritative Evidenzbasis.

## Ausgabe

`learning-next-step.json`:

```json
{
  "schemaVersion": 1,
  "missionId": "...",
  "targetCompetencyId": "...",
  "action": "application",
  "reason": "retrieval-demonstrated; representative application not yet demonstrated",
  "difficulty": "lower|target|upper-zpd",
  "prerequisiteRefs": [],
  "evidenceNeeded": ["..."],
  "runtime": "dialog|exam-trainer-framework|real-world",
  "stopCondition": "..."
}
```

`difficulty=upper-zpd` darf nur gewählt werden, wenn die Aufgabe mit vorhandenem Zustand plausibel lösbar ist.

## Kein zweiter Scheduler

Dieser Skill darf keine individuellen Due Dates, FSRS-Stability-Werte oder Review-Intervalle berechnen. Wenn ein ETF-Katalog existiert, bleibt ETF für kartenbezogene Scheduling-Entscheidungen zuständig.

## Fehlerbehandlung

- Sind Mission oder Lernzustand inkonsistent, gib keinen scheinpräzisen nächsten Schritt aus; benenne die fehlende Klärung.
- Fehlt Evidenz für einen behaupteten Kompetenzstand, behandle den Status konservativ.
- Ist die vorgeschlagene Aufgabe nur eine Wiederholung ohne zusätzlichen Erkenntniswert, bevorzuge eine schwierigere Variante oder einen anderen Kompetenzknoten.
- Ist die Aufgabe erkennbar überfordernd, reduziere Scaffolding nicht vollständig, sondern wähle einen erreichbaren Zwischenschritt.

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn genau eine nächste Handlung mit Zielkompetenz, Begründung, kalibrierter Schwierigkeit, benötigter Evidenz, Runtime und Stop-Bedingung vorliegt und keine kartenbezogene Scheduling-Logik dupliziert wird.
