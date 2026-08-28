---
name: euroimmun-presentation-workflow
description: Erstellt oder überarbeitet EUROIMMUN-/Revvity-Präsentationen auf Basis der bevorzugten aktuellen bestätigten EUROIMMUN-Corporate-PowerPoint-Referenz und delegiert Storyline, präsentationsspezifische Sprachoptimierung sowie Layout-/Render-QA an den generischen Template-Presentation-Workflow. Verwenden für EUROIMMUN Board-, Management-, R&D-, Innovation- oder bestehende Corporate-Decks; nicht für fremde Corporate Templates.
---

# EUROIMMUN Presentation Workflow

Dieser Skill ist ein dünner Corporate Wrapper um `template-presentation-workflow`. Er enthält ausschließlich EUROIMMUN-/Revvity-spezifische Design-, Governance- und Template-Regeln und dupliziert keine generische Storyline-, Sprach- oder QA-Logik.

## Verbindlicher Corporate Design Contract

Für jede EUROIMMUN-Firmenpräsentation MUSS vor der Bearbeitung `docs/corporate/euroimmun/DESIGN.md` gelesen und als normativer Design Contract angewendet werden. Zusätzlich MUSS `docs/corporate/euroimmun/ACTIVE_PRESENTATION_REFERENCE.md` für die aktuell bevorzugte Referenz und `docs/corporate/euroimmun/GOLDEN_REFERENCE.md` für die Level-1-/Level-2-Verifikation berücksichtigt werden.

- Ist `docs/corporate/euroimmun/DESIGN.md` nicht verfügbar, den Corporate Workflow abbrechen statt Designregeln zu improvisieren.
- Ein konkret für die Aufgabe geliefertes freigegebenes Corporate Template hat immer Vorrang vor der allgemeinen Referenz.
- Das verwendete Binärtemplate bleibt Source of Truth für Master, Layouts, Theme, Logo, Footer, Seitennummern und kontrollierte Template-Elemente.
- `presentation-qa.md` MUSS Design-Contract, Template-Identität/Status, SHA-256 bei Binärquelle, Brand-/Theme-Verhalten, Render-Coverage, Findings und finalen Corporate Design Gate dokumentieren.
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

## Referenz-Priorität

1. Für die konkrete Aufgabe geliefertes `approved-controlled` Template.
2. Verifizierte bevorzugte aktuelle Referenz `260828 NDD Review.pptx`.
3. Andere explizit gelieferte bestätigte Corporate-Binärreferenz mit dokumentierter Provenienz.
4. `references/euroimmun-template-spec.md` als `template-compatible` Fallback, wenn keine Binärreferenz verfügbar ist.
5. Historische Referenz `260610 Innovation Topics.pptx` nur bei explizitem Bedarf.

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

## EUROIMMUN-spezifische Slide-Präferenzen

- Cover: natives Corporate Title Layout.
- Kapiteltrenner: nativer Section Header.
- Standardanalyse: weißer Content-Slide mit Corporate Header/Footer und wenigen klaren Informationsblöcken.
- Tabellen nur für echte Vergleiche und auf entscheidungsrelevante Zeilen begrenzen.
- Timeline, Portfolio, Financials und Stage Gates bevorzugt visualisieren.
- Quellen klein, aber lesbar und klar von proprietären internen Informationen unterscheiden.

## Sprach- und QA-Regel

Präsentationstexte werden durch `presentation-language-rewriter` innerhalb des generischen Workflows optimiert, separat für Deutsch und Englisch und abhängig von Elementtyp und Zielgruppe.

Layout- und Box-Overflow-Prüfung erfolgt über `presentation-layout-qa`. Das finale visuelle Gate erfolgt über `presentation-render-verifier` einschließlich vollständigem Slide-Render, PDF-/Druckrender und erneutem Render nach Korrekturen. Bei verfügbarer Binärreferenz ist zusätzlich die Level-2-Prüfung aus `docs/corporate/euroimmun/GOLDEN_REFERENCE.md` anzuwenden.

## Nicht-Ziele

- Keine fachliche Regulatory-, Clinical-, IP- oder Finanzanalyse erfinden; dafür vorgelagerte Fach-Skills nutzen.
- Keine vertraulichen Inhalte der Referenzpräsentation in neue Decks übernehmen, sofern sie nicht Teil der aktuellen Aufgabenbasis sind.
- Keine proprietäre Referenz-PPTX in das öffentliche/zentral synchronisierte Skill-Repository einchecken.
- Keine generische Presentation-Logik hier duplizieren.

## Abschluss

Abgeschlossen, wenn der generische Template-Presentation-Workflow erfolgreich durchlaufen wurde, EUROIMMUN Corporate Master/Branding konsistent erhalten sind, die finale PPTX editierbar ist, eine geprüfte PDF vorliegt, der QA-Bericht keine ungeklärten Critical/Major Layout-, Sprach-, Brand- oder Renderfehler enthält und `Corporate Design Gate: PASS` dokumentiert ist. `template-derived` darf nur ausgegeben werden, wenn die relevante Level-2-Prüfung PASS ist.
