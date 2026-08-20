---
name: learning-assessment-spec
description: Definiert provider-neutral, welche beobachtbare Evidenz erforderlich ist, um eine Lernkompetenz von Einführung über Retrieval und Anwendung bis Transfer belastbar hochzustufen. Verwenden vor Quiz, Fallaufgabe, ETF-Prüfung oder realer Praxisbewertung; erzeugt selbst keine ETF-Karten und bewertet keine Antwort.
userFacing: false
implicitInvocation: true
category: productivity
version: 0.1.0
status: draft
owners:
  - GithubLarsKomo
requires:
  - learning-mission
  - learning-state
outputs:
  - learning-assessment-spec.json
---

# Learning Assessment Spec

## Zweck

Dieser Skill beschreibt **welcher Nachweis für eine konkrete Kompetenztransition benötigt wird**. Er trennt Assessment-Absicht von konkreter Runtime, Fragedarstellung und späterer Bewertung.

Er erzeugt keine ETF-Karten, führt keine Prüfung durch und entscheidet nicht nachträglich, ob der Nachweis bestanden wurde.

## Eingaben

- `learning-mission.json`,
- `learning-state.json`,
- Zielkompetenz,
- gewünschtes Zielniveau,
- verfügbare Evidenz- und Runtime-Grenzen.

## Kompetenzniveaus

- `introduced`
- `retrieval-demonstrated`
- `application-demonstrated`
- `transfer-demonstrated`

Ein Assessment muss zum beanspruchten Zielniveau passen. **Recall-Evidenz darf keinen Transferstatus begründen.**

## Ablauf

### 1. Zieltransition explizit machen

Beispiel:

```text
from: retrieval-demonstrated
to: application-demonstrated
```

Wenn der Ausgangszustand nicht belastbar ist, darf die Spec nicht so tun, als sei er gesichert.

### 2. Beobachtbare Evidenz formulieren

Definiere, was der Lernende tatsächlich tun muss. Vermeide Kriterien wie „hat die Lesson gelesen“ oder „hat 80 % der Inhalte gesehen“.

Beispiele:

- Konzept ohne Hilfestellung korrekt erklären,
- repräsentativen Fall mit begründeter Entscheidung lösen,
- neuen Fall mit veränderter Oberflächenstruktur korrekt übertragen,
- Fehler in einer fremden Lösung erkennen und korrigieren.

### 3. Unterstützungsgrad festlegen

Dokumentiere zulässige Hilfen:

- `none`,
- `limited`,
- `guided`.

Für einen echten Retrieval-Nachweis darf unmittelbare Antwortvorlage nicht verfügbar sein. Transfer verlangt ausreichend Neuheit gegenüber vorherigen Übungen.

### 4. Evidenzbreite festlegen

Ein einzelner Item-Treffer kann für triviale Fakten genügen, aber komplexe Kompetenzen benötigen häufig mehrere unabhängige Beobachtungen oder einen repräsentativen Fall.

Die Spec darf keine willkürliche Mindestzahl nur zur Scheingenauigkeit erfinden. Begründe die notwendige Breite aus Fehlerrisiko und Kompetenzkomplexität.

### 5. Bewertungsregel definieren

Lege fest:

- erforderliche Merkmale,
- kritische Fehler,
- Teilnachweise,
- wann Evidenz unzureichend statt „failed“ ist,
- ob Selbstbewertung nur Zusatzsignal oder zentrale Evidenz ist.

Ein Gesamtprozentsatz allein ist keine hinreichende Semantik.

### 6. Runtime neutral halten

Die Assessment-Spec kann später umgesetzt werden als:

- dialogische Aufgabe,
- ETF-Lernsitzung,
- ETF-Prüfung,
- reale Arbeitsaufgabe,
- Mentor-/KOL-Review.

Sie beschreibt die Evidenzanforderung, nicht das UI.

## Ausgabe

`learning-assessment-spec.json`:

```json
{
  "schemaVersion": 1,
  "missionId": "...",
  "competencyId": "...",
  "fromLevel": "retrieval-demonstrated",
  "targetLevel": "application-demonstrated",
  "assessmentClass": "retrieval|application|transfer",
  "taskIntent": "...",
  "allowedSupport": "none|limited|guided",
  "requiredEvidence": ["..."],
  "criticalErrors": ["..."],
  "minimumObservations": 1,
  "runtimeOptions": ["dialog", "exam-trainer-framework", "real-world"],
  "sourceRefs": []
}
```

`minimumObservations` muss begründet sein; es ist kein pauschaler Prüfungsstandard.

## ETF-Grenze

ETF-QuestionTypes, ExamBlueprints und QuestionVariants gehören in einen Adapter nach dieser Spec. Der Skill darf keine ETF-Implementierungsdetails zur Voraussetzung der fachlichen Assessment-Definition machen.

## Formale Trainingsgrenze

Die Spec kann Lernkompetenz operationalisieren, aber keine formale Zertifizierung, QMS-Qualifikation oder regulatorische Autorisierung definieren, sofern dafür nicht ein separater kontrollierter Prozess zuständig ist.

## Fehlerbehandlung

- Ist die Zielkompetenz selbst unklar, stoppe und präzisiere sie.
- Fehlt autoritative fachliche Grundlage für die erwartete Lösung, erzeuge keine scheinpräzise Assessment-Spec.
- Ist die Aufgabe zu ähnlich zu vorherigen Beispielen, darf sie nicht als starker Transfernachweis klassifiziert werden.
- Wenn das Assessment nur Aktivität misst, nicht beobachtbare Leistung, ist die Spec ungültig.

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn Zieltransition, beobachtbare Evidenz, Unterstützungsgrad, kritische Fehler, Evidenzbreite und zulässige Runtime klar sind, ohne ETF-spezifische Rendering-/Scheduling-Logik vorwegzunehmen.
