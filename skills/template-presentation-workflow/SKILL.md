---
name: template-presentation-workflow
description: Orchestriert die Erstellung oder Überarbeitung editierbarer Präsentationen auf Basis eines vorhandenen PowerPoint-Templates oder einer Referenzpräsentation. Übernimmt Look & Feel, kuratiert Storyline und Slide-Architektur, optimiert Deutsch/Englisch präsentationsspezifisch und erzwingt strukturelle sowie Render-/PDF-QA. Verwenden für template-basierte Management-, wissenschaftliche, technische, Sales- oder Educational-Decks; Corporate-Spezialregeln bleiben in dünnen Wrapper-Skills.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - presentation-template-profiler
  - presentation-language-rewriter
  - presentation-layout-qa
  - presentation-render-verifier
outputs:
  - presentation.pptx
  - presentation.pdf
  - presentation-qa.md
lastEvaluated: 2026-08-26
---

# Template Presentation Workflow

Dieser Skill ist der generische Orchestrator für template-basierte Präsentationen. Er koordiniert Fach-Skills, dupliziert deren Detailregeln aber nicht.

## Artifact Ownership

`presentation-template-profiler` ist der kanonische Producer von `presentation-template-profile.json`. Dieser Workflow konsumiert und referenziert das Profil, beansprucht aber nicht selbst dessen Ownership. Der Workflow besitzt dagegen die final orchestrierten Präsentationsartefakte `presentation.pptx`, `presentation.pdf` sowie den aggregierten Workflow-Bericht `presentation-qa.md`.

## Inputs

Mindestens:

- freigegebener Inhalt, Daten, Report, Research, Notes oder bestehendes Deck,
- Ziel und gewünschte Entscheidung/Wirkung der Präsentation,
- Zielgruppe,
- Sprache `de|en`, bei Englisch optional Zielvariante,
- vorhandenes Template oder bestätigte Referenzpräsentation, sofern verfügbar.

Optional:

- Corporate-spezifischer Wrapper mit Brand-Regeln,
- Terminologieliste,
- Author Voice,
- Evidence/Fidelity Lock,
- gewünschter Presentation Style: `executive|scientific|technical|sales|educational`.

## Workflow

### 1. Source of truth und Template fixieren

`presentation-template-profiler` ausführen. Liegt das echte Template vor, hat es Vorrang vor rekonstruierten Regeln. Master, Layouts, Theme, Footer, Logos, Platzhalter und Seitenformat erhalten.

### 2. Inhalt kuratieren

Fakten, Evidenz, Interpretation, Annahmen, Optionen, Empfehlungen und Entscheidungen trennen. Keine fachlichen Claims erfinden.

### 3. Storyline bauen

Eine nachvollziehbare Argumentationsfolge entwickeln. Für Executive/Management als Default:

`context -> why now -> evidence -> options -> recommendation -> economics/resources -> risks -> roadmap -> decision`

Die Reihenfolge an Präsentationstyp und Ziel anpassen. Die Kernentscheidung beziehungsweise Hauptaussage muss früh erkennbar sein.

### 4. Slide-Architektur kuratieren

Pro Slide genau eine primäre Botschaft definieren. Danach die geeignetste Darstellungsform wählen:

- Aussage + unterstützende Visualisierung,
- Chart,
- Tabelle nur für echte Vergleiche,
- Timeline/Roadmap,
- Prozess-/Stage-Gate-Diagramm,
- Portfolio-/2x2-Matrix,
- KPI/Scorecard,
- Bild mit analytischer Annotation,
- Section Header.

Textwände, dekorative Grafiken ohne Informationswert, überlange Tabellen und redundante Titel/Key Messages vermeiden. Wenn mehrere unabhängige Botschaften vorliegen, Slide teilen statt Schrift zu verkleinern.

### 5. Präsentationssprache optimieren

Alle sichtbaren Texte mit `presentation-language-rewriter` elementbezogen überarbeiten. Deutsch und Englisch separat idiomatisch optimieren. Report-Sätze nicht unverändert auf Slides übernehmen. Claims und Terminologie über Fidelity-Verifikation schützen.

### 6. Deck im Template erzeugen

Vorhandene Master/Layout-Platzhalter bevorzugt verwenden. Keine frei erfundene Corporate-Variante bauen, wenn ein echtes Template verfügbar ist. Grafiken, Tabellen und Charts an Theme, Raster, Typografie und Farblogik des Profils ausrichten.

### 7. Narrative QA

Prüfen:

- Hat jede Slide eine Hauptbotschaft?
- Ist die zentrale Aussage/Entscheidung früh verständlich?
- Sind Fakten, Annahmen und Empfehlungen getrennt?
- Sind Zahlen und Terminologie deckweit konsistent?
- Unterstützt jeder Visual die Aussage?
- Kann das Deck ohne begleitenden Report verstanden werden?

### 8. Strukturelle Layout-QA

`presentation-layout-qa` ausführen. Critical/Major Findings beheben. Textprobleme zuerst redaktionell oder strukturell lösen, bevor Schriftgrößen reduziert werden.

### 9. Render- und PDF-QA

`presentation-render-verifier` ausführen: Slides rendern, Deck-Level prüfen, PDF-/Druckversion exportieren und separat bewerten. Nach Korrekturen zwingend erneut rendern und verifizieren.

### 10. Finalisieren

Finale PPTX editierbar halten. PDF als geprüfte Druck-/Share-Version bereitstellen. `presentation-qa.md` aggregiert narrative, strukturelle und visuelle QA sowie verbleibende Warnungen und begründete Abweichungen. Das von `presentation-template-profiler` erzeugte `presentation-template-profile.json` bleibt als referenziertes Worker-Artefakt erhalten.

## Corporate Wrapper

Marken- oder unternehmensspezifische Skills sollen dünne Wrapper bleiben. Sie liefern Template-Referenz, Brand-Regeln, Pflichtfooter, Terminologie oder Governance und delegieren den eigentlichen Ablauf an diesen Skill. Wrapper sollen die generischen Artefakte dieses Workflows referenzieren statt sie erneut als eigene Outputs zu deklarieren; eigene Outputs sind nur echte Corporate-/Domain-Artefakte.

## Nicht-Ziele

- Keine fachliche Regulatory-, Medical-, Legal-, IP- oder Finanzanalyse erfinden.
- Kein neues Corporate Design entwickeln, wenn die Aufgabe Template-Treue verlangt.
- Keine Behauptung erfolgreicher visueller QA ohne tatsächlichen Render.
- Kein PDF-only Ergebnis, wenn eine editierbare PPTX verlangt ist.

## Abschlusskriterien

Abgeschlossen, wenn:

- Template/Look & Feel nachvollziehbar übernommen wurde,
- Storyline und Slide-Architektur schlüssig sind,
- deutsche oder englische Sprache präsentationsspezifisch optimiert wurde,
- PPTX editierbar ist,
- strukturelle Layout-QA bestanden ist,
- PPTX- und PDF-Render geprüft wurden,
- Korrekturen erneut gerendert wurden,
- finale PPTX, PDF, referenziertes Template-Profil und aggregierter QA-Bericht vorliegen.
