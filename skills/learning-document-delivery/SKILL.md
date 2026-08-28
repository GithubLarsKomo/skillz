---
name: learning-document-delivery
description: Überführt ein kanonisches Learning-Content-Modell und seine Visuals DESIGN.md-konform in ein editierbares Lern-DOCX und daraus in ein geprüftes PDF, mit Corporate-Renderer-Routing wenn ein verbindlicher Firmenkontext vorliegt. Verwenden für Lernhandouts, SOP-Drafts und Video-Study-Guides; nicht zum inhaltlichen Re-Authoring beim Rendering.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - learning-content-design-system
outputs:
  - learning-handout.docx
  - learning-handout.pdf
  - learning-document-qa.json
lastEvaluated: 2026-08-28
---

# Learning Document Delivery

## Grundarchitektur

`learning-content-model.json -> canonical DOCX -> full-page QA -> PDF -> parity QA`

DOCX und PDF werden nicht unabhängig neu geschrieben.

## Renderer-Routing

1. explizit bereitgestelltes Nutzer-/Corporate-DOCX-Template;
2. anwendbarer bestätigter Corporate Renderer;
3. EUROIMMUN: `euroimmun-docx-report-renderer` und anschließend `euroimmun-pdf-report-renderer`, inklusive `docs/corporate/euroimmun/DESIGN.md`;
4. sonst neutraler professioneller A4-Lernreport auf Basis des aktiven Learning-DESIGN.md.

Kein stilles Corporate-Fallback oder erfundene Unternehmensfreigabe.

## Inhaltliche Struktur

Je nach Content-Modell:

- Titel/Source block;
- Lernziele;
- Key Takeaways;
- Mental Model;
- erklärende Kapitel;
- Visuals mit Caption;
- optional derived SOP;
- Critical details / Common mistakes;
- Self-check / FAQ;
- Source Map / Timestamp references;
- offene Evidenzlücken.

## Fidelity

Beim Rendering müssen erhalten bleiben:

- Claim-Inhalt und Confidence;
- `observed/derived/recommended`;
- Zahlen, Einheiten und Negationen;
- Warnungen;
- Schrittfolge;
- Timestamp-Referenzen;
- Visual-ID/Caption/Provenance;
- Quellen.

## DOCX QA

Komplettes Dokument seitenweise rendern und prüfen:

- Seitenformat/Margins;
- Heading-Hierarchie;
- Tabellen;
- Visual-Clipping;
- Captions;
- Header/Footer;
- Seitenumbrüche;
- Font-/Glyph-Probleme;
- Quellen/Timestamp-Lesbarkeit.

## PDF QA

Nach DOCX-PASS:

- jede PDF-Seite rendern;
- Seitenzahl/Inhaltsreihenfolge vergleichen;
- keine Reflow-/Glyph-/Bildfehler;
- sichtbare Parität zum kanonischen DOCX;
- Corporate Design Gate zusätzlich PASS, wenn anwendbar.

## Abschluss

Abgeschlossen, wenn DOCX editierbar, PDF visuell vollständig geprüft und beide inhaltlich identisch zur kanonischen Learning-Basis sind.
