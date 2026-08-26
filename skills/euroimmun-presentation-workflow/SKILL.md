---
name: euroimmun-presentation-workflow
description: Erstellt oder überarbeitet EUROIMMUN-/Revvity-Präsentationen auf Basis des bestätigten EUROIMMUN-Corporate-PowerPoint-Templates und einer managementtauglichen Storyline. Verwenden, wenn der Nutzer eine EUROIMMUN-Präsentation, Board-/Management-Deck, R&D-/Innovation-Deck oder eine bestehende Präsentation im EUROIMMUN-Stil verlangt. Nicht für allgemeine Revvity- oder fremde Corporate-Decks verwenden.
userFacing: true
implicitInvocation: false
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - precision-writing-revision
outputs:
  - euroimmun-presentation.pptx
  - presentation-qa.md
lastEvaluated: 2026-08-26
---

# EUROIMMUN Presentation Workflow

Dieser Skill verwandelt freigegebenen fachlichen Inhalt in eine editierbare EUROIMMUN-Präsentation, die das bestätigte EUROIMMUN-PowerPoint-Template nutzt und nach visueller QA abgeschlossen wird.

## Verbindliche Designquelle

Die Referenz ist die vom Nutzer bestätigte Datei `260610 Innovation Topics.pptx`, SHA-256 `a85871bbe60a795436982e08bfce4a7efbc85b57471cb0c837062362844395e2`.

Die Originaldatei wird **nicht** im Skill-Repository gespeichert, weil sie proprietäre/vertrauliche Inhalte enthält. Stattdessen hält `references/euroimmun-template-spec.md` ausschließlich die daraus abgeleiteten Design- und Layoutregeln fest. Ist die bestätigte Referenzdatei im Arbeitskontext verfügbar, hat sie Vorrang vor der textuellen Spezifikation.

## Workflow

1. **Source of truth bestimmen**
   - Liegt die bestätigte EUROIMMUN-Template-Datei vor, verwende sie direkt als PowerPoint-Basis und erhalte Master, Layouts, Theme, Logos, Footer und Seitenformat.
   - Liegt sie nicht vor, rekonstruiere ausschließlich aus `references/euroimmun-template-spec.md` und kennzeichne das Ergebnis als template-compatible, nicht template-derived.

2. **Inhalt verdichten**
   - Trenne Fakten, Interpretation, Annahmen und Entscheidungen.
   - Formuliere Slides als Management-Storyline: `why now -> evidence -> strategic choice -> economics -> risks -> decision`.
   - Eine Slide hat eine Hauptbotschaft. Titel sollen die Aussage transportieren, nicht nur das Thema nennen.

3. **Slide-Typ wählen**
   - Cover: Corporate title layout.
   - Kapiteltrenner: farbiger Section Header.
   - Standardanalyse: weißer Content-Slide mit Titel, Logo/Footer und 1-2 visuellen Informationsblöcken.
   - Tabellen nur für echte Vergleiche; Tabelleninhalt auf entscheidungsrelevante Zeilen beschränken.
   - Timeline, Portfolio und Financials bevorzugt als Diagramm/Visual statt Fließtext.

4. **Corporate Design anwenden**
   - 16:9 widescreen.
   - Primäre Schrift: Hanken Grotesk; SemiBold für starke Hierarchie. Fallback nur wenn technisch nötig.
   - EUROIMMUN-Grün für Tabellenheader und ausgewählte Akzente; Revvity-Farbflächen für Abschnittstrenner nur passend zum Themenkontext.
   - EUROIMMUN-Logo links oben bzw. gemäß Master; Revvity-Branding/Footer gemäß Template.
   - Footer-/Confidentiality-Logik des Templates beibehalten.
   - Keine frei erfundene 'EUROIMMUN Branding'-Variante verwenden, wenn das echte Template verfügbar ist.

5. **Visualisierung**
   - Zahlen als Charts, Waterfalls, Portfolio-Matrizen, Roadmaps oder Stage-Gate-Diagramme visualisieren.
   - Maximal etwa 6 Kernaussagen pro Slide.
   - Diagramme und Tabellen bevorzugt auf weißen Flächen; starke Vollflächen für Section Header und wenige Key Messages reservieren.
   - Quellen klein, aber lesbar am unteren Rand; proprietäre Information nicht mit öffentlichen Quellen vermischen.

6. **Narrative QA**
   Prüfe vor Export:
   - Ist die zentrale Entscheidung nach 3-4 Slides verständlich?
   - Sind Fakten und Modellannahmen erkennbar getrennt?
   - Sind alle Zahlen über Slides hinweg konsistent?
   - Werden Investment, Timing, Risiken und Decision Gates explizit?
   - Kann die Präsentation ohne Begleitreport verstanden werden?

7. **Visual QA**
   - Gesamtes Deck rendern und Montage prüfen.
   - Keine überlappenden Objekte, abgeschnittene Texte, uneinheitliche Titelpositionen oder abweichende Footer.
   - Tabellen und Diagramme in normaler Präsentationsansicht lesbar.
   - Corporate Master/Layout möglichst wiederverwenden statt manuell nachzubauen.

## Nicht-Ziele

- Keine fachliche Regulatory-, Clinical-, IP- oder Finanzanalyse erfinden; dafür vorgelagerte Fach-Skills nutzen.
- Keine vertraulichen Inhalte aus der Referenzpräsentation in neue Decks übernehmen, sofern sie nicht Teil der aktuellen Aufgabenbasis sind.
- Keine proprietäre Referenz-PPTX ins öffentliche/zentral synchronisierte Skill-Repository einchecken.

## Abschlusskriterien

Die Aufgabe ist abgeschlossen, wenn:

- das Deck auf dem bestätigten Template oder der dokumentierten Fallback-Spezifikation basiert,
- die Management-Storyline schlüssig ist,
- Corporate Master/Footer/Branding konsistent sind,
- Fakten und Annahmen getrennt sind,
- das PPTX editierbar ist,
- ein visueller Render-QA ohne kritische Layoutfehler durchgeführt wurde.
