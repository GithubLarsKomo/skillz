---
name: fiction-series-writing-workflow
description: Orchestriert langfristige Science-Fiction- und Fantasy-Projekte von Craft-Modell, Welt, Ensemble und Serienarchitektur über Drafting, Schreibwerkstatt und kreative Revision bis zum Canon-/Continuity-Recheck. Verwenden für Romane und mehrbändige Reihen; keine Story-Bible-Logik duplizieren und keinen Entwurf als Canon oder publiziert behandeln, bevor die entsprechenden Gates passiert sind.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - mentor-text-craft-analysis
  - speculative-worldbuilding
  - ensemble-character-architecture
  - series-architecture
  - story-bible-continuity
  - creative-writing-workshop
  - creative-prose-revision
  - project-second-brain
consumes:
  - world-model.json
  - character-ensemble.json
  - series-architecture.json
  - continuity-review.json
  - creative-workshop-review.json
  - final-creative-text
outputs:
  - fiction-manuscript.md
  - fiction-series-run.json
  - story-bible-handoff.json
lastEvaluated: 2026-09-06
---

# Fiction Series Writing Workflow

## Zweck

Schreibe Fiction als iterativen Langformprozess, der über viele Kapitel und Bände konsistent fortsetzbar bleibt.

## Vorbedingungen

Aus dem übergeordneten Grilling/Handoff müssen mindestens bekannt sein:

- Genre und Zielpublikum;
- Einzelroman oder Reihe;
- Autor-Modus `coach|coauthor|writer|editor`;
- gewünschte Planungstiefe `discovery|hybrid|architected`;
- POV-/Ensemble-Grundidee;
- Sprache und gewünschte Ausgabe;
- Tabus/Nicht-Ziele.

## Ablauf

### 1. Craft Context

Optional `mentor-text-craft-analysis` ausführen. Übernommen werden Mechanismen, nicht Stimmenkopien.

### 2. Story System

Je nach Projektstand erzeugen/aktualisieren:

- `world-model.json`;
- `character-ensemble.json`;
- `series-architecture.json`;
- Story Bible/Knowledge States.

### 3. Draft Contract

Für die nächste Schreibeinheit fixieren:

- scene/chapter ID;
- POV;
- zeitliche Position;
- entering character knowledge;
- active relationships;
- scene objective;
- required setup/payoff movement;
- allowed reveals;
- canon constraints;
- desired reader effect.

### 4. Draft

Entsprechend dem Autor-Modus:

- `coach`: Übungen, Fragen, Diagnose; Nutzer schreibt.
- `coauthor`: gemeinsame Szenen-/Textentwicklung.
- `writer`: vollständiger Entwurf erlaubt.
- `editor`: Nutzertext bleibt Ausgangspunkt.

### 5. Workshop

`creative-writing-workshop` auf der abgeschlossenen Einheit ausführen.

### 6. Revision

`creative-prose-revision` ausführen.

### 7. Continuity Gate

Revidierte Fassung gegen `story-bible-continuity` prüfen:

- World Truth;
- Character Knowledge/Belief;
- Reader Knowledge;
- Timeline;
- Relation/Arc State;
- Setup/Payoff.

Bei Major/Critical Finding keine Canon-Promotion.

### 8. Canon Promotion

Nur bestätigte neue Tatsachen und Zustände aus dem Manuskript gezielt in die Story Bible übernehmen. Prosa selbst wird nicht zur Wahrheitsschicht.

Mögliche Promotion:

`draft-canon -> approved-canon -> published-hard-canon`.

### 9. Project Memory

Wesentliche Projektentscheidung, Canon Freeze, abgeschlossener Band oder wichtiger Richtungswechsel kann als Project-Second-Brain-Event verankert werden. Story Bible und Project Memory bleiben getrennt.

## Qualitätsgate

- **Manuskript ist nicht Story Bible.**
- **Workshop vor Revision; Continuity nach Revision.**
- POV-Figur besitzt nur den zulässigen Knowledge State.
- Neue Weltregeln werden nicht beiläufig ohne Canon-Entscheidung eingeführt.
- Discovery-Writing darf Architektur verändern, aber nicht rückwirkend Hard Canon löschen.
- Ein Band kann erst als publication-ready markiert werden, wenn offene Major/Critical Continuity Findings geschlossen sind.

## Output

`story-bible-handoff.json` enthält neue/änderte Canon-Kandidaten, Knowledge-State-Änderungen, Setup/Payoff-Bewegungen und noch nicht freigegebene Vorschläge.

`fiction-series-run.json` enthält Projekt-/Band-/Kapitelstand, Workshop-/Revision-/Continuity-Status und nächste Schreibeinheit.

## Abschluss

Ein Schreibinkrement ist abgeschlossen, wenn Manuskript, Workshop, Revision und Continuity Gate konsistent sind und Canon-Kandidaten getrennt übergeben wurden. Ein Gesamtprojekt endet erst nach dem vereinbarten Publikations-/Delivery-Schritt.
