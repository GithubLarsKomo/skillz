---
name: fiction-award-jury-review
description: Bewertet abgeschlossene Fiction-Einheiten mit getrennten, adversarialen Hugo-, Nebula- und World-Fantasy-inspirierten Kammern, bewahrt Dissens, erzeugt evidenzgebundene Award-Blocker/Protect-Findings und übersetzt sie in einen risiko-kontrollierten Revisionsloop. Verwenden für Acts oder vollständige speculative-fiction-Manuskripte nach normalem Workshop/Continuity-Pass; keine reale Award-Eligibility, offizielle Juryentscheidung oder Gewinnwahrscheinlichkeit behaupten.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.2.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - creative-writing-workshop
  - story-bible-continuity
  - creative-revision-regression
consumes:
  - fiction-manuscript.md
  - creative-workshop-review.json
  - continuity-review.json
  - creative-revision-regression.json
outputs:
  - fiction-award-jury-review.json
  - fiction-award-jury-review.md
  - fiction-award-critique-ledger.json
  - fiction-award-revision-plan.md
  - fiction-award-regression-review.json
lastEvaluated: 2026-09-10
---

# Fiction Award Jury Review

## Zweck

Erzeuge einen reproduzierbaren, adversarialen Literaturreview für Science Fiction und Fantasy, der drei institutionell unterschiedliche Award-Perspektiven simuliert:

- **Hugo Chamber:** breite, erfahrene Genreleserschaft; Empfehlungsstärke, Begeisterung, Figurenbindung, Momentum, Ideen und Erinnerungswert;
- **Nebula Chamber:** professionelle Autor:innenperspektive; Handwerk, Figurenpsychologie, Struktur, Sprache, Originalität, thematische Kontrolle und unsichtbare Autorarbeit;
- **World Fantasy Chamber:** kleine literarisch orientierte Jury; imaginative Eigenständigkeit, Atmosphäre, Stimme, Ambiguität, mythic resonance und emotionaler Nachhall.

Die Simulation bildet **Entscheidungslogiken und Perspektivkonflikte** nach, nicht geheime oder offizielle Bewertungsmaßstäbe der realen Awards.

## Scope

reviewScope:

- act: größere abgeschlossene Einheit; diagnostisch, bevor strukturelle Probleme in den nächsten Akt fortgeschrieben werden;
- full-manuscript: vollständiger Roman vor Publication Freeze;
- regression: gezielter Re-Review nach einer materiellen Revision.

Nicht für einzelne unfertige Szenen verwenden; dafür zuerst creative-writing-workshop.

## Eingaben

Mindestens:

- zu prüfende Manuskriptfassung(en);
- Genre/Subgenre;
- Zielpublikum;
- Scope;
- bekannte Review-/Continuity-Artefakte.

Optional für den **zweiten** Pass:

- Character-/World-/Series-Architecture;
- Reveal Budget;
- Setup/Payoff Ledger;
- Autorintention.

### Blind-First-Regel

Der erste Jury-Pass erhält keine Story-Bible-Erklärung, die das Manuskript nachträglich rettet.

Wenn etwas auf der Seite nicht verständlich, glaubwürdig oder wirksam ist, wird es zunächst als Leserproblem erfasst. Erst danach darf ein intentReconciliation-Pass prüfen, ob ein Finding:

- echter Manuskriptfehler;
- bewusstes Mysterium;
- Sequel Reserve;
- absichtlich ambivalente Wirkung;
- oder Fehlinterpretation der Jury

ist.

## Verbindliches Phasenmodell

Für Full-Manuscript-Reviews und andere Reviews mit Blind-Anspruch gilt strikt:

```text
Phase A  unabhängige Blind Chambers
         -> FREEZE A
Phase B  Blind Deliberation nur aus Manuskript + eingefrorenen Chamber Reads
         -> FREEZE B
Phase C  Intent Reconciliation mit Architektur
Phase D  gezielte kleinste ausreichende Revision
Phase E  Regression gegen Findings + Protect + Gate-Invalidierung
```

### Freeze A

Jede Chamber wird in einem isolierten Kontext abgeschlossen und unveränderlich referenziert, bevor sie Ergebnisse anderer Chambers sehen darf.

### Freeze B

Die Blind Deliberation darf ausschließlich erhalten:

- dasselbe Clean-Manuscript-Paket;
- das Blind-Protokoll;
- exakt die eingefrorenen Chamber Reports.

Story Bible, Plot-/Series-Architektur, frühere nichtblinde Reviews und Autorintention bleiben bis zum Deliberation-Freeze gesperrt.

Wenn Phase A oder B kontaminiert wurde, darf der Lauf nicht als valider Blind-Jury-Review ausgewiesen werden.

## Jurymodell

### Hugo Chamber — 9 Rollen

1. plot/momentum;
2. character attachment;
3. worldbuilding;
4. big ideas / sense of wonder;
5. politics / moral complexity;
6. accessibility;
7. emotional payoff;
8. experienced genre reader / derivative detection;
9. demanding general speculative-fiction reader.

Jeder Juror entscheidet unabhängig:

- nominate|maybe|no;
- aboveNoAward|belowNoAward;
- stärkster Grund für Nominierung;
- stärkster Grund gegen Nominierung.

### Nebula Chamber — 7 Rollen

Schwerpunkte:

- Figurenpsychologie und Agency;
- narrative Kontrolle;
- Struktur und Szenenfunktion;
- Prosa und Dialog;
- Originalität;
- thematische Tiefe;
- speculative premise.

Zusatzfrage: **Wo wird die Arbeit des Autors sichtbar?**

Typische Warnsignale:

- Exposition klingt nach Exposition;
- Figuren handeln für den Plot;
- Dialog transportiert sichtbar Informationen;
- Foreshadowing ist mechanisch;
- Themen werden erklärt statt dramatisch verkörpert;
- Cliffhanger oder POV-Wechsel wirken konstruiert.

### World Fantasy Chamber — 5 Rollen

Schwerpunkte:

- Atmosphäre;
- imaginative originality;
- Stimme;
- Mehrdeutigkeit;
- symbolische Kohärenz;
- mythic resonance;
- literarische Eigenständigkeit;
- emotionaler Nachhall.

Die fünf Rollen diskutieren nach dem unabhängigen Read gemeinsam. Konsens ist nicht erzwungen.

## Gemeinsame Core-Craft-Matrix

Bewerte soweit relevant:

- Character;
- Voice;
- Agency;
- Plot causality;
- Structure;
- Stakes;
- Pacing;
- Worldbuilding;
- Originality;
- Theme;
- Emotional impact;
- Ending/payoff;
- Mystery;
- Reveal control;
- Prose;
- Dialogue;
- Immersion;
- Memorability.

Scores sind nur Diagnosehilfen und dürfen nie die begründete Kritik ersetzen.

## Ablauf

### Phase A — Independent Blind Read

Alle Rollen lesen unabhängig. Keine Rolle sieht Scores oder Kommentare der anderen.

Jeder Juror liefert zwingend:

- bestThing;
- biggestReasonNotToWin;
- sceneToDefend;
- sceneToCutOrRadicallyRewrite;
- 3–7 evidenzgebundene Findings;
- Verdict gemäß eigener Kammer.

Findings müssen eine konkrete Stelle, Beobachtung und Leserwirkung enthalten.

### Phase B — Blind Deliberation

Erst nach Abschluss der Einzelreviews werden die Positionen gegenseitig sichtbar.

Jeder wesentliche Dissens wird diskutiert:

- Was genau wird unterschiedlich erlebt?
- Liegt die Differenz an Leserpriorität, Genreerwartung oder tatsächlich widersprüchlicher Textwirkung?
- Welche Revision könnte die Schwäche beheben, ohne die Stärke der Gegenseite zu zerstören?

Kein Mittelwert darf einen relevanten Minderheitenbefund auslöschen.

Nach Abschluss werden Deliberation, Konsens-/Dissensbefunde, Kill Reasons, Protect List und Minority Report **vor jedem Architekturzugriff eingefroren**.

### 3. Kill Reasons

Jede Kammer benennt maximal drei killReasons.

Ein Kill Reason ist der stärkste konkrete Grund, warum die Kammer das Werk **nicht** in die nächste Award-Diskussionsstufe heben würde.

### 4. Protect List

Erzeuge verpflichtend protect[].

protect enthält Stellen, Figurenmechaniken, Ambiguitäten, Rhythmen, Bilder oder strukturelle Entscheidungen, die eine Revision nicht beschädigen darf.

### 5. Cross-Jury Tribunal

Ein Chair synthetisiert ohne eigene Geschmackswertung.

Für jedes Finding:

- id;
- location;
- observation;
- evidence;
- readerEffect;
- rootCause;
- chambers;
- agreementLevel;
- severity;
- revisionHypothesis;
- protectedStrengthsAtRisk;
- status.

agreementLevel:

- consensus;
- cross-chamber-majority;
- single-chamber;
- minority-report;
- design-conflict.

### 6. Severity

Nur vier Stufen:

- S0-protect: außergewöhnlich wirksam; schützen;
- S1-polish: lokales Problem;
- S2-structural: betrifft mehrere Szenen/Kapitel oder zentrale Wirkung;
- S3-award-blocker: expliziter Nominierungs-/Finalisten-Blocker für mindestens eine Kammer.

Ein S3 darf nicht stillschweigend weitergetragen werden. Vor dem nächsten Hardening muss es entweder:

1. revidiert;
2. als bewusster Design-Trade-off akzeptiert;
3. oder mit klarer Begründung und geplantem späteren Gate deferred

werden.

### 7. Minority Report

Jeder substantielle Minderheitenbefund bleibt erhalten, insbesondere wenn:

- eine Kammer etwas liebt, das eine andere für schädlich hält;
- eine ungewöhnliche Entscheidung polarisiert;
- eine Revision die Eigenart des Textes glätten könnte.

### 8. Forgotten Book Test

Simuliere nach inhaltlicher Distanz:

- welche fünf Dinge bleiben erinnerlich;
- welche wichtigen Figuren/Setups/Regeln sollten erinnerlich sein, sind es aber nicht;
- welche Elemente überproportional viel kognitive Last erzeugen.

Dies ist keine echte zeitversetzte Messung, sondern eine strukturierte Memorability-Heuristik und muss so gekennzeichnet werden.

### Phase C — Intent Reconciliation

Erst jetzt Story Bible, Reveal Budget und Architektur öffnen.

Für jedes Major-Finding prüfen:

- passt die Leserreaktion zur beabsichtigten Wirkung?
- wurde eine spätere Enthüllung versehentlich vorweggenommen?
- wird ein bewusst offenes Rätsel fälschlich als Lücke behandelt?
- ist die beabsichtigte Information tatsächlich auf der Seite vorhanden?

Intent darf kein Leserproblem einfach wegdefinieren.

### Phase D — Targeted Revision Architecture

Nicht automatisch umschreiben.

Reihenfolge für priorisierte Findings:

finding → root cause → revision hypothesis → affected units → protected strengths at risk → **smallest sufficient intervention** → targeted reread → regression check

Maximal 3–7 priorisierte Interventionen pro Loop.

### Phase E — Regression Review

Nach materieller Revision `creative-revision-regression` ausführen. Die Award-Projektion liest:

- Baseline;
- Candidate;
- ursprüngliches Finding.

Sie bewertet:

- resolved;
- improved;
- unchanged;
- worse;
- newProblemIntroduced.

Zusätzlich collateralDamage[].

Ein Problem gilt erst als geschlossen, wenn seine Ursache verbessert wurde **und** keine S0-Stärke oder bereits geschlossene Major-Funktion wesentlich beschädigt wurde.

Zusätzlich muss die Revision nach Funktionswirkung klassifiziert werden. Hat sie Motivation, Reveal, POV, Beziehung, Ereigniskausalität oder Architektur materiell verändert, werden dadurch berührte frühere Gates invalidiert und vor Publication Freeze wiederhergestellt.

## Verdict-Skala

Keine Prozentwahrscheinlichkeit.

Je Kammer und Gesamttribunal:

- below-consideration;
- publishable;
- notable;
- nomination-conversation;
- finalist-strength;
- winner-conversation.

winner-conversation bedeutet nur, dass das Werk in dieser Simulation harte Gegenargumente übersteht. Es ist keine Aussage über reale Jurys, Nominierungen oder künftige Ergebnisse.

## Output Contract

### fiction-award-jury-review.json

Enthält mindestens:

- schemaVersion;
- projectId;
- scope;
- sourceManuscripts;
- blindRead;
- chambers.hugo;
- chambers.nebula;
- chambers.worldFantasy;
- deliberation;
- killReasons;
- protect;
- minorityReport;
- forgottenBookTest;
- intentReconciliation;
- verdicts;
- nextGate.

### fiction-award-critique-ledger.json

Jedes Ledger-Item besitzt:

- id;
- location;
- observation;
- evidence;
- rootCause;
- readerEffect;
- severity;
- chambers;
- agreementLevel;
- revisionHypothesis;
- protectedStrengthsAtRisk;
- status.

### fiction-award-revision-plan.md

Nur die nächste Revision, mit 3–7 priorisierten Interventionen, Abhängigkeiten, Risiken und konkreten Regression-Checks.

### fiction-award-regression-review.json

Vergleicht Baseline und Candidate ausschließlich gegen die zuvor akzeptierten Findings und Protect-Constraints.

## Qualitätsregeln

- Blind Read vor Story Bible.
- Phase A wird vor Cross-Chamber-Zugriff eingefroren.
- Phase B wird vor Intent/Architektur eingefroren.
- Einzelurteil vor Deliberation.
- Dissens nicht mitteln.
- Evidence vor abstrakter Meinung.
- Ursache vor Reparatur.
- Kleinste ausreichende Intervention vor breitem Rewrite.
- Protect List ist verbindlich.
- Materielle Revisionen werden über `creative-revision-regression` gegen Collateral Damage und Gate-Invalidierung geprüft.
- Maximal drei Kill Reasons je Kammer.
- Keine automatische Vollumschreibung.
- Keine behauptete offizielle Award-Rubrik.
- Keine reale Award-Eligibility oder Gewinnprognose ableiten.
- Reale Award-Regeln können sich ändern; institutionelle Fakten bei externer Nutzung aktuell verifizieren.
- Ein Werk kann literarisch stark sein, obwohl reale Award-Eligibility aus anderen Gründen fehlt.

## Abschluss

Ein Review-Loop ist abgeschlossen, wenn:

1. alle drei Kammern unabhängig gelesen haben;
2. Deliberation und Minority Report vorliegen;
3. Kill Reasons und Protect List fixiert sind;
4. Critique Ledger Ursachen statt Symptome enthält;
5. 3–7 priorisierte Revisionshypothesen freigegeben sind;
6. jeder S3-Befund eine explizite Disposition hat.

Ein Regression-Loop endet erst nach Collateral-Damage-Check und Wiederherstellung aller durch die Revision invalidierten blockierenden Gates.
