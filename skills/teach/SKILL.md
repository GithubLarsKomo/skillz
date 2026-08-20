---
name: teach
description: Orchestriert auf ausdrücklichen Wunsch einen zustandsbehafteten Lernprozess mit Lernmission, evidenzbasiertem Stoff, nachgewiesener Kompetenz, adaptivem nächsten Schritt und Übergaben an die Exam-Trainer-Lernruntime. Verwenden bei `/teach`, beim gezielten Erlernen eines Themas oder mit `/teach skill <skill-name>`; nicht für gewöhnliche Einzelerklärungen ohne Lernworkspace.
userFacing: true
implicitInvocation: false
category: productivity
version: 0.1.0
status: draft
owners:
  - GithubLarsKomo
requires:
  - learning-mission
  - learning-state
  - learning-next-step
  - learning-assessment-spec
  - learning-assessment
  - research-to-evidence-note
outputs:
  - learning-mission.json
  - learning-state.json
  - learning-next-step.json
  - learning-practice-request.json
---

# Teach

## Zweck und Grenze

`teach` ist der explizite pädagogische Orchestrator für dauerhaftes Lernen über mehrere Sitzungen. Er verbindet Lernziel, belastbare Evidenz, Erklärung, Retrieval, Anwendung, Transfer und dokumentierte Kompetenz, ohne Fachlogik oder Scheduling selbst zu duplizieren.

Der Skill wird **nur explizit gestartet**. Eine normale Bitte wie „erkläre mir X“ erzeugt keinen persistenten Lernworkspace. Typische Aufrufe sind:

```text
/teach <topic>
/teach skill <skill-name>
/teach status
/teach review
```

## Normative Eigentumsgrenzen

- Fachliche Wahrheit bleibt bei spezialisierten Skillz-Skills und belastbaren Quellen.
- `research-to-evidence-note` strukturiert strittige oder mehrquellige Evidenz.
- `learning-mission` bestimmt Warum, Erfolgskriterien, Grenzen und Scope.
- `learning-state` hält semantisch nachgewiesene Kompetenz, Vorwissen, Fehlvorstellungen und Lücken.
- `learning-next-step` wählt die nächste pädagogische Herausforderung.
- `learning-assessment-spec` definiert, welche Evidenz für einen Kompetenzsprung erforderlich ist.
- `learning-assessment` interpretiert tatsächliche Lern-/Prüfungsevidenz.
- `exam-trainer-framework` (ETF) bleibt externe Runtime für Spaced Retrieval, adaptive Lernsitzungen, ReviewEvents und Prüfungen.

**Coverage ist kein Lernen.** Material darf nicht als beherrscht markiert werden, nur weil es erklärt, gelesen oder einmal gezeigt wurde.

## Kernworkflow

### 1. Lernmission herstellen oder laden

Nutze `learning-mission`, um ein beobachtbares Ziel festzulegen. Eine Mission muss mindestens beantworten:

- Warum soll das gelernt werden?
- Was kann der Lernende danach konkret tun?
- Welche Constraints gelten?
- Was ist ausdrücklich außerhalb des Scopes?

Ist bereits eine aktive Mission vorhanden, ändere sie nicht stillschweigend.

### 2. Vorwissen und belastbare Wissensbasis trennen

Erfasse vorhandenes Wissen zunächst als `priorKnowledge`, bis es ausreichend belegt ist. Für fachliche Claims nutze vorhandene Spezialskills oder, bei Recherchebedarf, `research-to-evidence-note`.

Parametrisches Modellwissen allein ist bei zeitabhängigen, regulierten oder strittigen Inhalten keine ausreichende Autorität.

### 3. Kompetenzpfad bilden

Zerlege das Ziel in beobachtbare Kompetenzen und Voraussetzungen. Bevorzuge wenige stabile Kompetenzen gegenüber vielen Kartenfragmenten.

Für `/teach skill <skill-name>` verwende den kanonischen Skillz-Index und die aktuelle `SKILL.md` des Zielskills. Berücksichtige deklarierte Abhängigkeiten, Outputs und Evaluationsfälle als Kandidaten für Anwendungs- und Transferaufgaben.

### 4. Nächsten Schritt wählen

Delegiere die Auswahl an `learning-next-step`. Zulässige nächste Schritte sind unter anderem:

- Erklärung,
- Worked Example,
- geführte Übung,
- Retrieval,
- Anwendung,
- Transfer,
- ETF-Lernsitzung,
- ETF-Prüfung,
- reale/praktische Aufgabe.

Die Schwierigkeit soll in der Zone der nächsten erreichbaren Herausforderung liegen: nicht trivial, aber mit dem vorhandenen Zustand plausibel lösbar.

### 5. Übung an ETF übergeben, wenn sinnvoll

Teach beschreibt **was** geübt beziehungsweise geprüft werden soll. ETF entscheidet **wann und wie** einzelne QuestionVariants wiederholt werden.

Für eine ETF-Übergabe erzeuge zunächst einen provider-neutralen `learning-practice-request.json` mit:

```json
{
  "schemaVersion": 1,
  "missionId": "...",
  "competencyIds": ["..."],
  "mode": "retrieval|application|transfer|exam",
  "assessmentSpecRef": "...",
  "sourceRefs": [],
  "runtime": "exam-trainer-framework"
}
```

Phase 1 definiert nur diesen semantischen Request. ETF-spezifische Katalog-/ReviewEvent-Adapter gehören in die Interoperabilitätsphase.

### 6. Evidenz bewerten

Wenn der Lernende eine Übung, Aufgabe oder Prüfung abgeschlossen hat, nutze `learning-assessment`. Eine Prozentzahl allein darf keinen Kompetenzzustand bestimmen.

Unterscheide mindestens:

- `introduced`,
- `retrieval-demonstrated`,
- `application-demonstrated`,
- `transfer-demonstrated`.

### 7. Lernzustand aktualisieren

`learning-state` übernimmt nur belegte Änderungen. Lernrecords entstehen bei tatsächlich nachgewiesenem Verständnis, relevantem Vorwissen, korrigierter Fehlvorstellung oder einer begründeten Missionsänderung.

### 8. Schleife fortsetzen oder sauber beenden

Nach jedem substantiellen Schritt:

1. Zustand aktualisieren,
2. offene Lücken bestimmen,
3. nächsten Schritt berechnen,
4. Mission gegen Erfolgskriterien prüfen.

Beende eine Mission nicht aufgrund bloßer Stoffabdeckung.

## Status- und Review-Modus

### `/teach status`

Zeige knapp:

- aktive Mission,
- nachgewiesene Kompetenzen nach Level,
- offene Fehlvorstellungen/Lücken,
- zuletzt belegte Entwicklung,
- vorgeschlagenen nächsten Schritt.

### `/teach review`

Nutze fällige oder schwach belegte Kompetenzen als semantischen Review-Fokus. ETF bleibt Scheduler einzelner Retrieval-Items; Teach darf keine zweite Fälligkeitslogik etablieren.

## Datenschutz und Persistenz

- Missions- und Kompetenzzustand darf im Lernworkspace persistent sein.
- Rohdaten privater Connectoren, Zugangsdaten und unnötige personenbezogene Daten bleiben laufzeitgebunden.
- Dauerhafte globale Kommunikationspräferenzen gehören zu `communication-memory-governance`, nicht in den Kompetenzzustand.
- ETF-Lernerhistorie bleibt standardmäßig lokal in ETF; Teach referenziert nur die für semantische Bewertungen benötigte Evidenz.

## Formale Trainingsgrenze

Ein Teach-/ETF-Ergebnis darf nicht eigenständig als formale Qualifikation, QMS-Schulung, Autorisierung oder Zertifizierung ausgegeben werden. Dafür ist ein separat kontrollierter Trainingsrecord-Workflow mit zuständiger Autorität erforderlich.

## Fehlerbehandlung

- Fehlt belastbare Evidenz, kennzeichne die Lücke und lehre die Aussage nicht als gesicherte Tatsache.
- Widerspricht neue Evidenz dem bisherigen Lernzustand, bewahre die Provenance und korrigiere den Zustand explizit.
- Ist ETF nicht verfügbar, kann Teach mit dialogischen Retrieval-/Transferaufgaben fortfahren, darf aber keine ETF-ReviewEvents erfinden.
- Ist die Mission zu breit, schneide ein kohärentes Lernziel statt beliebig viele Themen parallel zu verfolgen.

## Abschlusskriterien

Ein Teach-Zyklus ist abgeschlossen, wenn die aktive Mission dokumentiert ist, verwendete fachliche Claims nachvollziehbar sind, der aktuelle Kompetenzzustand nur nachgewiesene Fähigkeiten enthält, der nächste Schritt begründet ist und jede Runtime-Übergabe einen expliziten portablen Vertrag besitzt.
