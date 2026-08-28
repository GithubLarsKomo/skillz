---
name: learning-activity-generator
description: Erzeugt evidenzgebundene Lernaktivitäten, Übungen und Wissenchecks aus Lernzielen und Course-Concept-Graph, mit Antwortbegründung, Distraktorlogik und klarer Trennung zwischen Recall, Verständnis und Anwendung. Verwenden innerhalb des Course Builders; nicht zur psychometrischen Kalibrierung oder Zertifizierungsprüfung.
userFacing: false
implicitInvocation: true
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - learning-path-planner
outputs:
  - course-activities.json
  - course-knowledge-checks.json
lastEvaluated: 2026-08-28
---

# Learning Activity Generator

## Ziel

Jedes Modul erhält geeignete aktive Lernschritte. Die Aktivitäten prüfen definierte Lernziele und führen keine neuen fachlichen Claims ein.

## Aktivitätstypen

- `recall-check` — Begriffe/Fakten wiedergeben;
- `concept-check` — Zusammenhänge erklären oder unterscheiden;
- `sequence-task` — Prozessschritte ordnen;
- `diagnostic-case` — Fehler/Ursache identifizieren;
- `parameter-interpretation` — vorhandene Zahlen/Parameter im richtigen Kontext deuten;
- `compare-variants` — Varianten und Scope unterscheiden;
- `application-task` — Konzept auf neuen, aber evidenzverträglichen Fall anwenden;
- `teach-back` — Mental Model in eigenen Worten erklären;
- `source-critique` — Konflikt/Quellenstärke beurteilen.

## Knowledge Checks

Jede Frage enthält:

- `questionId`, Modul/Lernziel;
- Fragetyp und Schwierigkeit;
- Frage;
- korrekte Antwort / erwartete Elemente;
- Begründung;
- Evidenz-/Claim-IDs;
- Feedback für typische Fehlannahmen;
- bei MC optional Distraktoren mit Fehlergrund.

Distraktoren dürfen plausibel sein, aber keine neue Falschinformation ohne Korrektur in das Lernartefakt tragen.

## Bloom-orientierte Staffelung

Verwende pragmatisch:

`remember -> understand -> apply -> analyze`

`evaluate/create` nur, wenn Kursziel und Material das tatsächlich tragen.

## Assessment-Grenzen

- Keine Behauptung psychometrischer Validität.
- Keine automatische Zertifizierung oder Kompetenzfreigabe.
- Ein Knowledge Check ist formative Lernkontrolle, sofern kein separat validierter Prüfungsworkflow eingesetzt wird.
- In sicherheits-/regulierten Kontexten dürfen Bestehensgrenzen nicht erfunden werden.

## Spaced Retrieval

Wichtige Kernkonzepte können in späteren Modulen erneut abgefragt werden. Wiederholungsfragen sollen einen neuen Kontext oder höhere Verarbeitungstiefe haben statt identisch wiederholt zu werden.

## Output

`course-activities.json` enthält Aktivitäten je Lektion/Modul.
`course-knowledge-checks.json` enthält Entry Checks, Modul-Checkpoints und einen optionalen Abschlusscheck.

## Qualitätsfälle

**Happy Path:** PCR-Zyklus wird erst erkannt, dann erklärt, später auf eine Fehlersituation angewendet.

**Edge Case:** Ein Claim ist konfliktbehaftet -> Frage prüft die Qualifikation/Varianten, nicht eine fälschlich eindeutige Antwort.

**Failure Case:** Antwort setzt einen Parameter voraus, der in keiner Quelle belegt ist -> Frage verwerfen oder als Open Question kennzeichnen.
