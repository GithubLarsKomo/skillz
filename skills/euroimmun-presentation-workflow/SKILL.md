---
name: euroimmun-presentation-workflow
description: Erstellt oder überarbeitet EUROIMMUN-/Revvity-Präsentationen auf Basis des bestätigten EUROIMMUN-Corporate-PowerPoint-Templates und delegiert Storyline, präsentationsspezifische Sprachoptimierung sowie Layout-/Render-QA an den generischen Template-Presentation-Workflow. Verwenden für EUROIMMUN Board-, Management-, R&D-, Innovation- oder bestehende Corporate-Decks; nicht für fremde Corporate Templates.
userFacing: true
implicitInvocation: false
category: workflow
version: 0.2.0
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
lastEvaluated: 2026-08-26
---

# EUROIMMUN Presentation Workflow

Dieser Skill ist ein dünner Corporate Wrapper um `template-presentation-workflow`. Er enthält ausschließlich EUROIMMUN-/Revvity-spezifische Design-, Governance- und Template-Regeln und dupliziert keine generische Storyline-, Sprach- oder QA-Logik.

## Verbindliche Designquelle

Die bestätigte Referenz ist `260610 Innovation Topics.pptx`, SHA-256 `a85871bbe60a795436982e08bfce4a7efbc85b57471cb0c837062362844395e2`.

Die Originaldatei wird nicht im Skill-Repository gespeichert. `references/euroimmun-template-spec.md` enthält ausschließlich abgeleitete Design- und Layoutregeln. Ist die bestätigte Referenzdatei im Arbeitskontext verfügbar, hat sie Vorrang vor der textuellen Spezifikation.

## Corporate Context für den generischen Workflow

An `template-presentation-workflow` übergeben:

- bevorzugte Source of Truth: bestätigte EUROIMMUN-PPTX,
- Fallback: `references/euroimmun-template-spec.md`, dann als `template-compatible`, nicht `template-derived`, kennzeichnen,
- Seitenformat: 16:9 widescreen gemäß Template,
- Primärschrift: Hanken Grotesk; SemiBold für starke Hierarchie, Fallback nur wenn technisch nötig,
- EUROIMMUN-Grün für Tabellenheader und ausgewählte Akzente,
- Revvity-Farbflächen für Section Header nur entsprechend dem bestätigten Corporate Template,
- EUROIMMUN-Logo, Revvity-Branding, Footer, Confidentiality und Seitennummern gemäß Master beibehalten,
- Corporate Layouts und Platzhalter bevorzugt wiederverwenden,
- keine frei erfundene EUROIMMUN-Branding-Variante, wenn das echte Template verfügbar ist.

## EUROIMMUN-spezifische Slide-Präferenzen

- Cover: Corporate Title Layout.
- Kapiteltrenner: bestätigter Section Header.
- Standardanalyse: weißer Content-Slide mit Corporate Header/Footer und wenigen klaren Informationsblöcken.
- Tabellen nur für echte Vergleiche und auf entscheidungsrelevante Zeilen begrenzen.
- Timeline, Portfolio, Financials und Stage Gates bevorzugt visualisieren.
- Quellen klein, aber lesbar und klar von proprietären internen Informationen unterscheiden.

## Sprach- und QA-Regel

Präsentationstexte werden nicht mehr über `precision-writing-revision` wie Reports behandelt. Die Sprachoptimierung erfolgt durch `presentation-language-rewriter` innerhalb des generischen Workflows, separat für Deutsch und Englisch und abhängig von Elementtyp und Zielgruppe.

Layout- und Box-Overflow-Prüfung erfolgt über `presentation-layout-qa`. Das finale visuelle Gate erfolgt über `presentation-render-verifier` einschließlich PDF-/Druckrender und erneutem Render nach Korrekturen.

## Nicht-Ziele

- Keine fachliche Regulatory-, Clinical-, IP- oder Finanzanalyse erfinden; dafür vorgelagerte Fach-Skills nutzen.
- Keine vertraulichen Inhalte der Referenzpräsentation in neue Decks übernehmen, sofern sie nicht Teil der aktuellen Aufgabenbasis sind.
- Keine proprietäre Referenz-PPTX in das öffentliche/zentral synchronisierte Skill-Repository einchecken.
- Keine generische Presentation-Logik hier duplizieren.

## Abschluss

Abgeschlossen, wenn der generische Template-Presentation-Workflow erfolgreich durchlaufen wurde, EUROIMMUN Corporate Master/Branding konsistent erhalten sind, die finale PPTX editierbar ist, eine geprüfte PDF vorliegt und der QA-Bericht keine ungeklärten kritischen Layout- oder Renderfehler enthält.
