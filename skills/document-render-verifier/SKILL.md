---
name: document-render-verifier
description: Rendert ein DOCX und die daraus erzeugte PDF-Version seitenweise und verifiziert sichtbare Parität, Clipping, Font-/Glyph-Substitution, Tabellen-/Bild-Reflow, Seitenumbrüche, Header/Footer, Felder und Druckstabilität. Verwenden nach struktureller Dokument-QA als finales visuelles Gate; nicht als Ersatz für editierbare DOCX-Prüfung.
userFacing: false
implicitInvocation: true
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - document-layout-qa
consumes:
  - document-layout-qa.json
outputs:
  - document-render-qa.json
  - document-render-qa.md
  - document-preview.pdf
lastEvaluated: 2026-08-28
---

# Document Render Verifier

## Zweck und Grenze

Dieser Skill prüft das sichtbare Endergebnis eines Word-Dokuments. Er ergänzt strukturelle DOCX-QA um echten Seitenrender und den Vergleich mit der daraus abgeleiteten PDF-Ausgabe.

## Trigger

Nach `document-layout-qa` und nach jeder relevanten Korrektur erneut verwenden, bevor ein Dokument als visuell geprüft, druckstabil oder PDF-paritätisch bezeichnet wird.

## Voraussetzungen

- aktuelles editierbares DOCX;
- struktureller QA-Status aus `document-layout-qa.json`;
- ein tatsächlich verfügbarer DOCX-Renderer/Office-Exportweg;
- bei gewünschter PDF-Ausgabe ein echter PDF-Export aus derselben DOCX-Version.

## Ablauf

1. DOCX vollständig seitenweise rendern.
2. Seitenfolge und Seitenanzahl dokumentieren.
3. Jede Seite auf Clipping, Umbrüche, Tabellen-/Bild-Reflow, Fonts/Glyphen, Header/Footer, Felder und Weißraum-Anomalien prüfen.
4. PDF aus exakt derselben DOCX-Version exportieren.
5. PDF ebenfalls seitenweise rendern.
6. DOCX- und PDF-Render auf Seitenzahl, Inhaltsreihenfolge, sichtbare Elemente und relevante Geometrieabweichungen vergleichen.
7. Findings korrigieren lassen und anschließend beide Render erneut prüfen.

## Visuelle Prüffelder

- abgeschnittene oder verschwundene Text-/Tabelleninhalte;
- ungewollte Einzelzeilen, Leer-/Fast-Leerseiten und harte Reflow-Sprünge;
- Font-Substitutionen, fehlende Glyphen und veränderte Laufweiten;
- Bilder, SVG-/Rasterassets, Captions und Seitenbreiten;
- Tabellenkopf-Wiederholung, Zellhöhe, Row-Splits und Spaltenbreiten;
- Header/Footer, Seitenzahlen, Felder und Section-Wechsel;
- Link-/Quellenlesbarkeit und Druckrand;
- PDF-Abweichungen gegenüber dem kanonischen DOCX-Render.

## Status

- `pass`: keine offenen Critical/Major Findings und Re-Render nach Korrekturen durchgeführt.
- `review`: nur begründete visuelle Review-Punkte verbleiben.
- `fail`: Critical/Major Finding, fehlender belastbarer Render oder relevante DOCX/PDF-Paritätsabweichung.

## Prüfungen

- `visually verified` nur ausgeben, wenn ein tatsächlicher Seitenrender geprüft wurde.
- PDF darf nicht unabhängig neu gesetzt oder inhaltlich korrigiert werden; DOCX bleibt Layoutquelle.
- Nach jeder Korrektur ist ein neuer Render erforderlich.
- Ein erfolgreicher DOCX-Render beweist nicht automatisch PDF-Parität.
- Fachliche Werte werden bei Layoutkorrekturen nicht verändert.

## Fehlerbehandlung

- **Renderer fehlt:** `fail|not-run`; keine textuelle Sichtprüfung simulieren.
- **PDF-Export scheitert:** DOCX-Status separat erhalten, PDF-Parität aber nicht als bestanden markieren.
- **Font fehlt:** Substitution sichtbar dokumentieren und bei relevanter Layoutwirkung blockieren.
- **Unklare visuelle Abweichung:** Seite/Region als Review-Finding erhalten statt still zu akzeptieren.

## Übergabe

Outputs sind `document-render-qa.json`, `document-render-qa.md` und optional `document-preview.pdf` als geprüfte Vorschau. Ein produktiver finaler PDF-Dateiname bleibt Eigentum des aufrufenden Dokumentworkflows.

## Abschlusskriterien

Abgeschlossen, wenn DOCX und – falls gefordert – PDF vollständig gerendert, seitenweise geprüft, relevante Findings korrigiert und erneut gerendert wurden und der finale Status auf tatsächlicher Render-/Paritätsevidenz statt auf struktureller Vermutung beruht.
