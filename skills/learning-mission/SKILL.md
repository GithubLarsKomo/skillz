---
name: learning-mission
description: Definiert oder revidiert ein einzelnes kohärentes Lernziel als portablen Vertrag mit Warum, beobachtbaren Erfolgskriterien, Constraints und Out-of-Scope. Verwenden, wenn ein Teach-Lernworkspace gestartet, geschärft oder aufgrund neuer Realität bewusst geändert wird; nicht zum Bewerten von Kompetenz oder Planen einzelner Übungen.
userFacing: false
implicitInvocation: true
version: 0.1.0
status: draft
owners:
  - GithubLarsKomo
requires: []
outputs:
  - learning-mission.json
---

# Learning Mission

## Zweck

Dieser Skill verwandelt einen Lernwunsch in **eine überprüfbare Mission**. Die Mission beantwortet, warum gelernt wird und welche reale Fähigkeit am Ende beobachtbar sein soll. Sie ist kein Lehrplan und kein Kompetenznachweis.

## Kernprinzip

**Eine Mission beschreibt einen kohärenten Outcome, nicht eine Themenliste.** Wenn mehrere unabhängige Outcomes vorliegen, trenne sie in mehrere Missionen oder priorisiere eine aktive Mission.

## Eingaben

Mindestens:

- Thema oder Zielbereich,
- beabsichtigter realer Nutzen,
- bekannte Constraints.

Optional:

- vorhandene Mission,
- Frist oder Prüfungskontext,
- vorhandenes Vorwissen,
- ausdrücklich ausgeschlossene Inhalte,
- Quellen- oder Skill-Referenzen.

## Ablauf

### 1. Warum konkretisieren

Formuliere den realen Zweck in einem Satz. Vermeide Formulierungen wie „mehr über X wissen“, wenn stattdessen eine beobachtbare Handlung beschrieben werden kann.

### 2. Erfolg beobachtbar machen

Formuliere `successCriteria` als Fähigkeiten, die durch Verhalten, Lösung oder Transfer demonstriert werden können.

Gute Kriterien beginnen sinngemäß mit:

- unterscheiden,
- erklären ohne Hilfsmittel,
- anwenden,
- beurteilen,
- entwerfen,
- einen neuen Fall lösen.

Bloße Stoffabdeckung ist kein Erfolgskriterium.

### 3. Constraints erfassen

Nur Constraints aufnehmen, die die Lernstrategie tatsächlich verändern, zum Beispiel Zeit, erlaubte Quellen, Prüfungstyp, verfügbares Tooling oder Sicherheitsgrenzen.

### 4. Out-of-Scope explizit machen

Grenze interessante Nebenthemen aus, wenn sie den Kernpfad verwässern würden.

### 5. Mission stabil identifizieren

Erzeuge eine stabile `id`. Eine semantisch neue Mission erhält eine neue Identität. Kleine Präzisierungen können dieselbe Mission versionieren.

### 6. Änderungen bewusst behandeln

Eine vorhandene Mission darf nicht stillschweigend umgeschrieben werden. Wenn neue Informationen das Ziel verändern, dokumentiere den Änderungsgrund und gib einen expliziten Revisionsstatus aus.

## Ausgabe

`learning-mission.json`:

```json
{
  "schemaVersion": 1,
  "id": "mission-id",
  "version": 1,
  "topic": "...",
  "why": "...",
  "successCriteria": ["observable capability"],
  "constraints": [],
  "outOfScope": [],
  "sourceRefs": [],
  "state": "active",
  "revisionReason": null
}
```

## Qualitätsregeln

- `why` beschreibt einen konkreten Nutzen.
- Jedes Erfolgskriterium ist beobachtbar.
- Erfolgskriterien beschreiben Kompetenz, nicht Unterrichtsaktivität.
- Constraints und Out-of-Scope sind getrennt.
- Eine Revision ist nachvollziehbar und nicht retroaktiv unsichtbar.
- Die Mission enthält keine behauptete Kompetenz.

## Fehlerbehandlung

Wenn der Nutzer nur ein sehr breites Gebiet nennt, erzeuge keine künstlich vollständige Curriculum-Mission. Schneide den zuerst relevanten Outcome oder markiere offene Zielklärung.

Wenn ein gewünschtes Erfolgskriterium nicht beobachtbar ist, formuliere es nicht als erledigt, sondern als offene Missionseigenschaft.

## Datenschutz

Die Mission speichert nur für den Lernzweck notwendige Informationen. Private Rohdaten, Credentials und unnötige personenbezogene Details gehören nicht in den Vertrag.

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn genau eine kohärente Mission mit konkretem Warum, beobachtbaren Erfolgskriterien, relevanten Constraints, Out-of-Scope und stabiler Identität vorliegt und jede Änderung gegenüber einer vorhandenen Mission sichtbar bleibt.
