---
name: story-bible-continuity
description: Verwaltet Fiction-Canon und prüft Szenen, Kapitel und Bände gegen Weltwahrheit, Figurenwissen/-glauben, Leserwissen, Timeline, Beziehungen, Arc-Zustände und Setup/Payoff-Verträge. Verwenden für Serienkontinuität, Canon Freeze und Retcon-Impact-Analyse; Project Second Brain bleibt getrennt und publizierter Hard Canon wird nicht still umgeschrieben.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.2.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - speculative-worldbuilding
  - ensemble-character-architecture
  - series-architecture
  - structured-knowledge-artifact
consumes:
  - world-model.json
  - character-ensemble.json
  - series-architecture.json
  - setup-payoff-ledger.json
outputs:
  - story-bible-index.json
  - knowledge-state.json
  - continuity-review.json
  - canon-impact-analysis.json
lastEvaluated: 2026-09-06
---

# Story Bible Continuity

## Zweck

Die Story Bible ist die kanonische Wahrheitsschicht des fiktionalen Universums. Sie ist **nicht** die Chronik des Schreibprojekts.

## Drei Wahrheiten

### World Truth

Was ist im Universum tatsächlich wahr?

### Character Knowledge/Belief

Für jede Figur und jeden relevanten Zeitpunkt:

- knows;
- believes;
- suspects;
- misunderstands;
- does-not-know.

### Reader Knowledge

Für Publikations-/Szenenpunkte:

- disclosed;
- strongly implied;
- weakly implied;
- concealed;
- contradicted by apparent evidence.

**World Truth, Character State und Reader State dürfen nicht kollabieren.**

## Reveal Timing

Reader Knowledge besitzt nicht nur einen Zustand, sondern auch einen **zulässigen Zeitpunkt und eine Stärke**.

Für wichtige Fakten/Mysterien nach Möglichkeit modellieren:

- `earliestAllowed`;
- `targetWindow`;
- `latestUseful`;
- `actualFirstDisclosure`;
- `actualStrength`.

Eine wahre Aussage kann ein Continuity-Fehler sein, wenn sie dem Leser zu früh als gesicherte Wahrheit präsentiert wird.

Prüfe insbesondere:

- versehentliche Bestätigung eines späteren Reveals;
- wiederholte schwache Hinweise, die kumulativ bereits starke Gewissheit erzeugen;
- Figurenwissen, das indirekt zu viel Leserwissen verrät;
- Metaphern/Dialoge, die Mystery-Fakten unbeabsichtigt benennen.

## Zeitmodell

Jede Szene besitzt nach Möglichkeit:

- in-world timestamp/order;
- POV character;
- location;
- active relationship states;
- entering knowledge state;
- new observations/reveals;
- exiting knowledge state;
- reader disclosures.

## Canon Lifecycle

- idea;
- planned;
- draft-canon;
- approved-canon;
- published-hard-canon.

Ein `published-hard-canon`-Element wird nicht still verändert.

## Continuity Review

Prüfe mindestens:

- Timeline und Alter;
- räumliche Erreichbarkeit;
- Verletzungen/Ressourcen/Objekte;
- Beziehungen;
- Fähigkeiten und Weltregeln;
- wer was wann weiß;
- was der Leser wann wissen darf;
- Arc State;
- offene Setups/Payoffs.

Findings klassifizieren:

- `critical`: publizierter oder zentraler Widerspruch;
- `major`: wahrscheinlich wahrnehmbarer Kontinuitätsbruch;
- `minor`: lokaler Inkonsistenz-/Klarheitsfehler;
- `intentional`: dokumentierte Täuschung, unreliable narration oder Mystery.

## Retcon

Eine Änderung publizierten Hard Canons erzeugt zuerst `canon-impact-analysis.json` mit:

- affected entities;
- affected scenes/volumes;
- knowledge-state impacts;
- setup/payoff impacts;
- downstream arc impacts;
- repair options;
- residual contradictions.

**Kein Retcon ohne Impact Analysis.**

## Sequel Reserves

Fakten, Setups und Mysterien für spätere Bände werden explizit klassifiziert.

Mindestens dokumentieren:

- stabile ID;
- aktueller Canon State;
- `openPurpose` oder gleichwertig (`sequel-reserve`, `later-volume`, `intentional-unresolved`);
- beabsichtigter Horizont;
- maximale Offenlegungsstärke im aktuellen Band;
- abhängige spätere Arcs/Fakten, soweit bekannt.

Vor Veröffentlichung eines Bandes prüfen:

- Wurde ein späterer Fakt versehentlich geschlossen oder widersprochen?
- Erzeugt aktueller Hard Canon unnötige Retcon-Pflicht für einen geplanten Folgeband?
- Ist die aktuelle Geschichte trotzdem lokal geschlossen?
- Wird ein zentrales Versprechen fälschlich nur in die Fortsetzung verschoben?

## Whole-Manuscript Continuity Audit

Vor Publication Freeze muss ein vollständiger Audit über den Band laufen:

- Timeline/Alter;
- Geographie/Reisezeit/Jahreszeit;
- Verletzungen, Ressourcen, Geld, Objekte;
- Namen, Titel, Familienbeziehungen;
- Weltregeln/Magie/Fähigkeiten;
- Institutionen/Politik/Recht;
- Character Knowledge/Belief;
- Reader Knowledge und Reveal Timing;
- Beziehungen und Arc States;
- alle Setups/Payoffs;
- Sequel Reserves.

Major/Critical Findings blockieren Publication Freeze.

## Story Bible versus Project Second Brain

Story Bible: Wahrheit innerhalb der Fiktion.  
Project Second Brain: Entscheidungen, Evidenz, Versionen und Workflowhistorie des Projekts.

Beide dürfen aufeinander verweisen, aber nicht dieselben Zustände besitzen.

## Qualitätsgate

- **Drei Wahrheitsschichten bleiben getrennt.**
- Published Hard Canon ist standardmäßig unveränderlich.
- Intentional deception wird nicht als Kontinuitätsfehler gewertet, wenn sie modelliert ist.
- Jeder Major/Critical Finding verweist auf betroffene Canon-/Scene-IDs.
- Neue Draft-Ideen überschreiben keinen freigegebenen Canon.
- Zu frühe oder zu starke Offenlegung gilt als Continuity Finding, selbst wenn die Aussage faktisch wahr ist.
- Jeder offene Faden vor Publication Freeze ist als aktueller Payoff, bewusste offene Frage oder Sequel Reserve klassifiziert.

## Abschluss

Abgeschlossen, wenn Story Bible, Knowledge States und Continuity Findings referenziell konsistent sind und ein nachgelagerter Schreibprozess erkennen kann, was geändert werden darf und was nicht.
