---
name: euroimmun-presentation-workflow
description: Erstellt oder überarbeitet EUROIMMUN-/Revvity-Präsentationen auf Basis der bevorzugten aktuellen bestätigten EUROIMMUN-Corporate-PowerPoint-Referenz, optional ergänzt um die bestätigte Corporate-Storytelling-Grammatik und das freigegebene Icon-System, und delegiert Storyline, präsentationsspezifische Sprachoptimierung sowie Layout-/Render-QA an den generischen Template-Presentation-Workflow. Verwenden für EUROIMMUN Board-, Management-, R&D-, Innovation-, Town-Hall-, Leadership- oder bestehende Corporate-Decks; nicht für fremde Corporate Templates.
userFacing: true
implicitInvocation: false
category: workflow
version: 0.4.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - template-presentation-workflow
outputs:
  - euroimmun-presentation.pptx
  - euroimmun-presentation.pdf
  - presentation-qa.md
  - presentation-template-profile.json
lastEvaluated: 2026-08-28
---

# EUROIMMUN Presentation Workflow

Dieser Skill ist ein dünner Corporate Wrapper um `template-presentation-workflow`. Er enthält ausschließlich EUROIMMUN-/Revvity-spezifische Design-, Governance-, Template-, Storytelling- und Asset-Regeln und dupliziert keine generische Storyline-, Sprach- oder QA-Logik.

## Verbindlicher Corporate Design Contract

Für jede EUROIMMUN-Firmenpräsentation MUSS vor der Bearbeitung `docs/corporate/euroimmun/DESIGN.md` gelesen und als normativer Design Contract angewendet werden. Zusätzlich MUSS `docs/corporate/euroimmun/ACTIVE_PRESENTATION_REFERENCE.md` für die aktuell bevorzugte Referenz und `docs/corporate/euroimmun/GOLDEN_REFERENCE.md` für die Level-1-/Level-2-Verifikation berücksichtigt werden.

Wenn Corporate-Storytelling oder freigegebene Icons für die Aufgabe relevant sind, zusätzlich lesen:

- `docs/corporate/euroimmun/PRESENTATION_STORYTELLING_REFERENCE.md`
- `docs/corporate/euroimmun/ICON_SYSTEM.md`

- Ist `docs/corporate/euroimmun/DESIGN.md` nicht verfügbar, den Corporate Workflow abbrechen statt Designregeln zu improvisieren.
- Ein konkret für die Aufgabe geliefertes freigegebenes Corporate Template hat immer Vorrang vor der allgemeinen Referenz.
- Das verwendete Binärtemplate bleibt Source of Truth für Master, Layouts, Theme, Logo, Footer, Seitennummern und kontrollierte Template-Elemente.
- Storytelling-Referenz und Icon-System dürfen die aktive Binärquelle ergänzen, aber nicht deren Master-/Theme-Vertrag überschreiben.
- `presentation-qa.md` MUSS Design-Contract, Template-Identität/Status, SHA-256 bei Binärquelle, Brand-/Theme-Verhalten, verwendeten Storytelling-Modus, Icon-Asset-Provenienz soweit angewendet, Render-Coverage, Findings und finalen Corporate Design Gate dokumentieren.
- Eine `template-derived`- oder Master-Paritätsaussage ist nur nach Level-2-Verifikation zulässig.

## Bevorzugte aktuelle Designquelle

Die bevorzugte aktuelle bestätigte Binärreferenz ist:

- `260828 NDD Review.pptx`
- SHA-256 `349e5599ee0c1876a474057ec659244e0f37dd39d65636d2042b7eee46bab02e`
- Status: `confirmed-reference-binary`
- Golden Reference: `LEVEL_2_PASS` am 2026-08-28
- 16:9, 13.333 × 7.5 in
- 3 Slide-Master, 51 sichtbare PowerPoint-Layouts, 4 Themes
- Primärtheme: `Hanken Grotesk Light` / `Hanken Grotesk`
- aktiver grüner Theme-Akzent: `#208528`

Die Originaldatei wird nicht im Skill-Repository gespeichert. Wenn eine Datei mit dieser Referenz im Arbeitskontext verfügbar ist, MUSS vor einer Level-2-Aussage ihr SHA-256 gegen die dokumentierte Identität geprüft werden.

`260610 Innovation Topics.pptx`, SHA-256 `a85871bbe60a795436982e08bfce4a7efbc85b57471cb0c837062362844395e2`, ist ab 2026-08-28 eine **historische bestätigte Referenz**. Sie darf weiterhin für historische Kompatibilität oder explizit darauf basierende Aufgaben genutzt werden, darf die aktuelle Referenz aber nicht stillschweigend verdrängen.

## Bestätigte Corporate-Storytelling-Referenz

Für interne Kommunikation, Town Hall, Leadership Briefing, Change/Transformation, Alignment, People/Organization und vergleichbare erzählerische Firmenpräsentationen ist zusätzlich bestätigt:

- `Town Hall_BL Meeting_180826.pptx`
- SHA-256 `72a082c769abe5f18f53079ccfa7c59dc73ed53e285e4107f096ff587043bfb9`
- 57 Slides, 1 Master, 44 Layouts, 3 Themes
- Primärtheme der Binärquelle: Arial; clover `#73C054`, forest `#218529`
- Rolle: **secondary style reference**, nicht Ersatz der aktiven Template-/Masterquelle

Die daraus abgeleitete visuelle Grammatik steht in `docs/corporate/euroimmun/PRESENTATION_STORYTELLING_REFERENCE.md`.

## Referenz-Priorität

1. Für die konkrete Aufgabe geliefertes `approved-controlled` Template.
2. Verifizierte bevorzugte aktuelle Referenz `260828 NDD Review.pptx`.
3. Andere explizit gelieferte bestätigte Corporate-Binärreferenz mit dokumentierter Provenienz.
4. `references/euroimmun-template-spec.md` als `template-compatible` Fallback, wenn keine Binärreferenz verfügbar ist.
5. Historische Referenz `260610 Innovation Topics.pptx` nur bei explizitem Bedarf.

Die Corporate-Storytelling-Referenz ist **orthogonal** zu dieser Priorität: Sie steuert Archetypen, Bildsprache, Informationsarchitektur und visuelle Erzählweise, soweit diese mit der aktiven Master-/Templatequelle vereinbar sind.

## Corporate Context für den generischen Workflow

An `template-presentation-workflow` übergeben:

- Source of Truth gemäß obiger Priorität,
- Fallback ohne Binärmaster stets als `template-compatible`, nicht `template-derived`, kennzeichnen,
- Seitenformat 16:9 widescreen gemäß aktivem Template,
- Theme-Schriften aus dem aktiven Template verwenden; beim aktuellen Referenzdeck `Hanken Grotesk Light` / `Hanken Grotesk`,
- template-eigene Farbwerte haben für template-derived Elemente Vorrang vor formatübergreifenden Palette-Tokens; beim aktuellen Referenzdeck ist der aktive grüne Theme-Akzent `#208528`,
- das Brand-Profil `euroimmun-corporate` bleibt autoritativ für neue Corporate-Farben, soweit das aktive Template die betreffende Rolle nicht definiert,
- EUROIMMUN-/Revvity-Logo, Footer, Proprietary/Confidential-Kennzeichnung und Seitennummern aus Master/Layout erben, nicht rekonstruieren,
- Corporate Layouts und Platzhalter bevorzugt wiederverwenden,
- keine vertraulichen fachlichen Inhalte einer Referenzpräsentation übernehmen, sofern sie nicht Teil der aktuellen Aufgabenbasis sind.

## Präsentationsmodus bestimmen

Vor der Storyline einen Modus festlegen:

- `scientific` — Evidenz, Studien, Performance, Quellen, Regulatory/Clinical.
- `executive` — Entscheidung, Optionen, Business Case, Risiken, Gates, Roadmap.
- `technical` — Architektur, Prozess, Technologie, Implementierung.
- `corporate-storytelling` — Town Hall, Leadership, Transformation, People/Organization, Alignment, Rollout.
- `hybrid` — z. B. scientific/executive Kern mit Corporate-Storytelling für Cover, Agenda, Section Divider, Roadmap, Decision und Next Steps.

Der Modus ist in `presentation-qa.md` zu dokumentieren. `corporate-storytelling` darf wissenschaftliche Einschränkungen, Quellen oder Unsicherheit nicht visuell verdecken.

## EUROIMMUN-spezifische Slide-Präferenzen

### Allgemein

- Cover: natives Corporate Title Layout.
- Kapiteltrenner: nativer Section Header.
- Standardanalyse: weißer Content-Slide mit Corporate Header/Footer und wenigen klaren Informationsblöcken.
- Tabellen nur für echte Vergleiche und auf entscheidungsrelevante Zeilen begrenzen.
- Timeline, Portfolio, Financials und Stage Gates bevorzugt visualisieren.
- Quellen klein, aber lesbar und klar von proprietären internen Informationen unterscheiden.

### Corporate-Storytelling

Wenn der Modus anwendbar ist, zusätzlich die Archetypen aus `PRESENTATION_STORYTELLING_REFERENCE.md` nutzen:

- Hero/Cover mit einem starken visuellen Anker statt Objekt-Mosaik.
- Agenda/Orientierung mit maximal 3–5 klaren Punkten und optional einer großen Bildhälfte.
- Section Divider mit klarer Farb-/Bilddramaturgie; organische/gerundete Bildgrenzen sind erlaubt.
- Prozess-, Rollen- und Übergabefolien als wiederholte, große Geometrien mit eindeutiger Richtung.
- Do/Avoid, Current/Future und Before/After in klar gepaarten Strukturen.
- Summary/Next Steps mit expliziter Handlung oder Führungsimplikation.
- Große Weißräume bewusst beibehalten; nicht jede Fläche füllen.

## Corporate Icon System

Wenn `Icons.zip` oder eine später revidierte freigegebene EUROIMMUN-Icon-Bibliothek im Arbeitskontext vorliegt, `docs/corporate/euroimmun/ICON_SYSTEM.md` anwenden.

Für die analysierte Referenz gilt:

- `Icons.zip` SHA-256 `533f9adda32bb5746ab061a95b8e392be7511071a18d23e2c56e819b89ae8fde`
- ca. 196 wiederkehrende semantische Motive / 1,019 SVG-Dateien
- Familien: Essential, Portfolio & Indication, Technique, Project
- dominantes Square-Icon-Format: `viewBox 0 0 256 256`
- Standardvarianten: black, clover, white, white-black, white-clover

Regeln:

- supplied SVG variant vor eigenem Recoloring verwenden;
- auf weißem Grund vorzugsweise clover oder black;
- auf dunklem/Foto-Grund white oder geeignete supplied circle variant;
- ein Icon pro Message-Block; wiederholte Strukturen mit derselben Familie/Variante;
- indikations- und technologiespezifische Icons vor generischen Symbolen bevorzugen;
- Project Icons nur für das tatsächlich benannte Projekt verwenden;
- Icons sind semantische Orientierung, kein Ersatz für Labels, Quellen oder Claims.

## Sprach- und QA-Regel

Präsentationstexte werden durch `presentation-language-rewriter` innerhalb des generischen Workflows optimiert, separat für Deutsch und Englisch und abhängig von Elementtyp und Zielgruppe.

Layout- und Box-Overflow-Prüfung erfolgt über `presentation-layout-qa`. Das finale visuelle Gate erfolgt über `presentation-render-verifier` einschließlich vollständigem Slide-Render, PDF-/Druckrender und erneutem Render nach Korrekturen. Bei verfügbarer Binärreferenz ist zusätzlich die Level-2-Prüfung aus `docs/corporate/euroimmun/GOLDEN_REFERENCE.md` anzuwenden.

Zusätzliche visuelle QA bei Storytelling/Icon-Nutzung:

- pro Slide eine dominante Botschaft;
- Bilder haben eine narrative/inhaltliche Funktion und sind keine Stock-Dekoration;
- wiederholte Karten, Pfeile und Icons besitzen konsistente Geometrie, Abstände und optische Größe;
- Icon-Farbvariante passt zum Hintergrund und stammt möglichst aus dem supplied Asset;
- keine gemischten Fremd-Icon-Stile ohne dokumentierte Ausnahme;
- Sektionstrenner sind von Analyse-/Evidence-Slides klar unterscheidbar;
- Storytelling-Layout reduziert keine Quellen, Limitierungen oder regulatorischen Hinweise unter die notwendige Lesbarkeit.

## Nicht-Ziele

- Keine fachliche Regulatory-, Clinical-, IP- oder Finanzanalyse erfinden; dafür vorgelagerte Fach-Skills nutzen.
- Keine vertraulichen Inhalte der Referenzpräsentation in neue Decks übernehmen, sofern sie nicht Teil der aktuellen Aufgabenbasis sind.
- Keine proprietäre Referenz-PPTX oder Corporate-Icon-Binärbibliothek in das öffentliche/zentral synchronisierte Skill-Repository einchecken.
- Keine generische Presentation-Logik hier duplizieren.
- Corporate Storytelling nicht als Vorwand nutzen, wissenschaftliche oder regulatorische Inhalte dekorativ zu vereinfachen.

## Abschluss

Abgeschlossen, wenn der generische Template-Presentation-Workflow erfolgreich durchlaufen wurde, EUROIMMUN Corporate Master/Branding konsistent erhalten sind, der gewählte Präsentationsmodus nachvollziehbar angewendet wurde, verwendete Icons/Assets provenance- und kontrastgerecht eingesetzt wurden, die finale PPTX editierbar ist, eine geprüfte PDF vorliegt, der QA-Bericht keine ungeklärten Critical/Major Layout-, Sprach-, Brand-, Asset- oder Renderfehler enthält und `Corporate Design Gate: PASS` dokumentiert ist. `template-derived` darf nur ausgegeben werden, wenn die relevante Level-2-Prüfung PASS ist.
