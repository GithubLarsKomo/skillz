---
name: learning-state
description: Pflegt einen portablen semantischen Lernzustand aus nachgewiesenen Kompetenzen, relevantem Vorwissen, Fehlvorstellungen, Lücken und kurzen Learning Records. Verwenden, wenn Lern- oder Prüfungsevidenz in dauerhaften Kompetenzzustand überführt oder ein bestehender Zustand nachvollziehbar revidiert werden soll; nicht als Roh-Eventlog oder Scheduler.
userFacing: false
implicitInvocation: true
category: productivity
version: 0.1.0
status: draft
owners:
  - GithubLarsKomo
requires: []
outputs:
  - learning-state.json
  - learning-record.md
---

# Learning State

## Zweck

`learning-state` ist die semantische Langzeitansicht einer aktiven Lernmission. Er speichert **was tatsächlich nachgewiesen wurde**, welche Fehlvorstellungen relevant sind, welches Vorwissen die Lehre verändert und welche Lücken offen bleiben.

Der Skill ist kein Scheduler, kein vollständiges Sessionlog und kein Ersatz für ETF-ReviewEvents.

## Normative Zustände

Kompetenzlevel:

- `introduced` — Begriff/Inhalt wurde eingeführt; noch kein Kompetenznachweis.
- `retrieval-demonstrated` — ohne unmittelbare Hilfe korrekt abgerufen oder erklärt.
- `application-demonstrated` — in einer repräsentativen Aufgabe korrekt angewendet.
- `transfer-demonstrated` — in einem ausreichend neuen Kontext erfolgreich übertragen.

**Exposition allein erzeugt keinen Kompetenzsprung.**

## Eingaben

Mindestens:

- `missionId`,
- vorhandener Lernzustand oder leerer Ausgangszustand,
- neue Evidenzreferenzen oder explizit bestätigtes Vorwissen.

Mögliche Evidenz:

- `learning-assessment.json`,
- referenzierte ETF ReviewEvents oder Assessment-Zusammenfassungen,
- reale Arbeitsprodukte,
- beobachtete Antworten/Aufgaben,
- explizit bestätigtes und für die Lehre relevantes Vorwissen.

## Kernworkflow

### 1. Evidenz klassifizieren

Ordne neue Information einem Typ zu:

- Kompetenznachweis,
- Vorwissen,
- Fehlvorstellung,
- Korrektur einer Fehlvorstellung,
- offene Lücke,
- Missionsänderung.

Bloße Unterrichtsaktivität ist keine Lernzustandsänderung.

### 2. Kompetenzübergang prüfen

Ein Level darf nur erreicht werden, wenn die Evidenz zum geforderten Niveau passt. Ein Recall-Test rechtfertigt keinen Transferstatus.

Bei widersprüchlicher Evidenz behalte die stärkeren und neueren Evidenzreferenzen sichtbar; setze den Zustand nicht durch Mittelwertbildung künstlich hoch.

### 3. Vorwissen getrennt halten

`priorKnowledge` verändert Sequenzierung und Schwierigkeit, ist aber nicht automatisch gleichbedeutend mit aktuell demonstrierter Kompetenz. Wenn Vorwissen ausreichend demonstriert wurde, kann daraus reguläre Kompetenzevidenz entstehen.

### 4. Fehlvorstellungen versionieren

Eine korrigierte Fehlvorstellung wird nicht aus der Historie gelöscht. Markiere sie als `corrected`, verweise auf die Korrekturevidenz und bewahre den ursprünglichen Befund.

### 5. Learning Record nur bei substantieller Änderung erzeugen

Ein kurzer `learning-record.md` entsteht nur, wenn mindestens eines gilt:

- nicht-triviale Kompetenz wurde demonstriert,
- relevantes Vorwissen wurde belastbar festgestellt,
- eine Fehlvorstellung wurde korrigiert,
- die Mission änderte sich aufgrund neuen Lernens.

**Coverage is not learning.** Eine behandelte Seite, Lesson oder Karte allein erzeugt keinen Record.

## Ausgabe

`learning-state.json`:

```json
{
  "schemaVersion": 1,
  "missionId": "...",
  "version": 1,
  "competencies": [
    {
      "id": "...",
      "statement": "...",
      "level": "introduced|retrieval-demonstrated|application-demonstrated|transfer-demonstrated",
      "evidenceRefs": ["..."],
      "lastDemonstratedAt": "...",
      "state": "active"
    }
  ],
  "misconceptions": [
    {
      "id": "...",
      "statement": "...",
      "state": "active|corrected",
      "evidenceRefs": [],
      "correctionEvidenceRefs": []
    }
  ],
  "priorKnowledge": [],
  "openGaps": [],
  "nextCandidateCompetencies": []
}
```

`learning-record.md` bleibt kurz und enthält nur Änderung, Evidenzreferenzen und pädagogische Konsequenz. Es ist kein Sitzungsprotokoll.

## Evidenz- und Provenance-Regeln

- Jeder Kompetenzsprung braucht mindestens eine nachvollziehbare Evidenzreferenz.
- Roh-ETF-Events werden nicht redundant in jeden Record kopiert; referenziere sie stabil.
- Unsichere Evidenz darf als offene Lücke erhalten bleiben.
- Ein späterer stärkerer Nachweis darf einen früheren Zustand superseden, aber nicht die Provenance löschen.

## Formale Trainingsgrenze

`learning-state` beschreibt pädagogische Evidenz. Er bestätigt **keine formale Qualifikation, Zertifizierung, QMS-Schulung oder Autorisierung**.

## Datenschutz

Persistiere nur mission-relevante semantische Informationen. Private Rohantworten aus Connectoren, Credentials und unnötige personenbezogene Daten bleiben außerhalb des Lernzustands.

## Fehlerbehandlung

- Fehlt eine Evidenzreferenz für einen beanspruchten Kompetenzsprung, lehne den Übergang ab.
- Passt Evidenz nur zu Retrieval, darf `application-demonstrated` oder `transfer-demonstrated` nicht gesetzt werden.
- Bei Konflikten markiere Unsicherheit oder Regression, statt den höchsten jemals erreichten Zustand blind beizubehalten.

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn jede persistierte Kompetenz nach Evidenzniveau begründet ist, Vorwissen und aktuelle Kompetenz getrennt bleiben, Fehlvorstellungen nachvollziehbar versioniert sind, Learning Records nur substanzielle Änderungen dokumentieren und keine formale Qualifikation behauptet wird.
