---
name: fiction-series-writing-workflow
description: Orchestriert langfristige Science-Fiction- und Fantasy-Projekte von Craft-Modell, Welt, Ensemble und Serienarchitektur über Drafting, Schreibwerkstatt und kreative Revision bis zum Canon-/Continuity-Recheck. Verwenden für Romane und mehrbändige Reihen; keine Story-Bible-Logik duplizieren und keinen Entwurf als Canon oder publiziert behandeln, bevor die entsprechenden Gates passiert sind.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.3.0
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
  - fiction-award-jury-review
  - project-second-brain
consumes:
  - world-model.json
  - character-ensemble.json
  - series-architecture.json
  - continuity-review.json
  - creative-workshop-review.json
  - final-creative-text
  - fiction-award-jury-review.json
  - fiction-award-critique-ledger.json
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

### 9. Act-Level Editorial & Consistency Gate

Nach Abschluss eines Aktes oder einer vergleichbaren größeren Einheit:

- Developmental Lektorat über den gesamten Akt;
- POV-/Rhythmus-/Wiederholungsprüfung;
- Cross-Chapter-Continuity;
- Reveal-Timing gegen Reader Knowledge und Architektur;
- Setup/Payoff-Fortschritt;
- Prüfung auf zu frühe Offenlegung;
- Prüfung von Fakten, die erst in späteren Akten/Bänden Bedeutung erhalten sollen.

**Wichtig:** Eine Aussage kann mit World Truth vereinbar und trotzdem falsch platziert sein, wenn sie dem Leser zu früh zu viel Sicherheit gibt.

Für wichtige Wahrheiten/Mysterien nach Möglichkeit ein Reveal-Budget führen:

- `earliestAllowed`;
- `targetWindow`;
- `latestUseful`;
- `actualFirstDisclosure`;
- `actualStrength` (`concealed|weakly-implied|strongly-implied|disclosed|confirmed`).

Bei offenen Major/Critical Findings nicht einfach in den nächsten Akt fortschreiben.

### 9a. Act-Level Award Jury Diagnostic

Für ambitionierte Science-Fiction-/Fantasy-Projekte nach dem Act-Level Editorial & Consistency Gate fiction-award-jury-review mit scope act ausführen.

Dabei:

- Manuskript zuerst blind gegen drei getrennte Perspektiven lesen lassen;
- Hugo-, Nebula- und World-Fantasy-inspirierte Kammern nicht vorzeitig gegenseitig beeinflussen;
- Kill Reasons, Protect List, Minority Report und Critique Ledger erzeugen;
- S3-Award-Blocker vor weiterem Hardening explizit disponieren;
- maximal 3–7 Revisionshypothesen in den nächsten Loop übernehmen;
- kein S0-Protect-Element durch eine vermeintliche Glättung beschädigen.

Ein Act-Level Award Diagnostic ersetzt weder Continuity noch normales Developmental Editing. Er prüft, ob der bereits technisch konsistente Text als speculative fiction außergewöhnlich genug wirkt und wo unterschiedliche Leser-/Autor-/Literaturperspektiven miteinander kollidieren.

### 10. Full-Manuscript Editorial & Series Continuity Gate

Nach vollständigem Manuskript und vor `publication-ready`:

- globales Developmental Lektorat;
- vollständige Timeline-/Geographie-/Objekt-/Verletzungs-/Ressourcenprüfung;
- Namen, Titel, Familienbeziehungen, Institutionen und Terminologie;
- Magie-/Fähigkeits-/Kostenkonsistenz;
- Character-/Reader-Knowledge über alle Kapitel;
- Relationship-/Arc-State-Konsistenz;
- vollständige Setup/Payoff-Schließung;
- Reveal-/Mystery-Integrität;
- Voice-/Line-/Audio-Lektorat;
- **Sequel-Reserve-Audit**.

Danach fiction-award-jury-review mit scope full-manuscript ausführen. Vor Publication Freeze müssen:

- Cross-Jury Tribunal und Minority Report vorliegen;
- alle S3-Award-Blocker revidiert, bewusst akzeptiert oder begründet deferred sein;
- Protect List gegen Line-/Voice-/Audio-Polish gesichert sein;
- ein priorisierter Award-Revisionsloop abgeschlossen oder explizit als Design-Trade-off geschlossen sein;
- nach materieller Revision ein Regression Review auf Collateral Damage erfolgen.

Jeder offene Setup-Faden muss vor Publikation entweder:

1. im aktuellen Band bezahlt sein;
2. ausdrücklich `sequel-reserve`/späterer Horizont sein;
3. bewusst ungelöst sein und als solcher dokumentiert sein.

Fakten, die spätere Romane vorbereiten, müssen stabil referenzierbar sein und dürfen im aktuellen Band weder versehentlich widersprochen noch zu früh erklärt werden.

### 11. Project Memory

Wesentliche Projektentscheidung, Canon Freeze, abgeschlossener Band oder wichtiger Richtungswechsel kann als Project-Second-Brain-Event verankert werden. Story Bible und Project Memory bleiben getrennt.

## Qualitätsgate

- **Manuskript ist nicht Story Bible.**
- **Workshop vor Revision; Continuity nach Revision.**
- POV-Figur besitzt nur den zulässigen Knowledge State.
- Neue Weltregeln werden nicht beiläufig ohne Canon-Entscheidung eingeführt.
- Discovery-Writing darf Architektur verändern, aber nicht rückwirkend Hard Canon löschen.
- Ein Akt darf nicht ohne bewusste Entscheidung über offene Major/Critical Act-Level-Findings verhärtet werden.
- Für ambitionierte speculative fiction dürfen offene S3-Findings aus dem Act-Level Award Jury Diagnostic nicht stillschweigend in den nächsten Akt fortgeschrieben werden.
- Ein Band kann erst als publication-ready markiert werden, wenn offene Major/Critical Chapter-, Act- und Full-Manuscript-Continuity Findings geschlossen sind.
- Publication-ready verlangt zusätzlich eine klassifizierte Setup/Payoff- und Sequel-Reserve-Bilanz.
- Publication-ready verlangt bei speculative fiction außerdem den Full-Manuscript Award Jury Review inklusive Protect List, Minority Report und Regression-Check nach materiellen Revisionsschritten.
- Offenlegungszeitpunkt und -stärke sind Teil der Continuity, nicht nur faktische Widerspruchsfreiheit.

## Output

`story-bible-handoff.json` enthält neue/änderte Canon-Kandidaten, Knowledge-State-Änderungen, Setup/Payoff-Bewegungen und noch nicht freigegebene Vorschläge.

`fiction-series-run.json` enthält Projekt-/Band-/Kapitelstand, Workshop-/Revision-/Continuity-Status und nächste Schreibeinheit.

## Abschluss

Ein Schreibinkrement ist abgeschlossen, wenn Manuskript, Workshop, Revision und Continuity Gate konsistent sind und Canon-Kandidaten getrennt übergeben wurden.

Ein Akt ist erst abgeschlossen, wenn zusätzlich das Act-Level Editorial & Consistency Gate passiert ist. Bei einem aktivierten Award-Level-Ziel muss außerdem der Act-Level Award Jury Diagnostic gelaufen und jeder S3-Befund disponiert sein.

Ein Gesamtmanuskript ist erst publication-ready, wenn das Full-Manuscript Editorial & Series Continuity Gate inklusive Reveal- und Sequel-Reserve-Audit bestanden ist und der Full-Manuscript Award Jury Review keine undisponierten S3-Befunde mehr enthält.

Ein Gesamtprojekt endet erst nach dem vereinbarten Publikations-/Delivery-Schritt.
