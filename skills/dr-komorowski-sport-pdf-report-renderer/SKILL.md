---
name: dr-komorowski-sport-pdf-report-renderer
description: Erzeugt aus dem kanonischen Dr.-Komorowski-Sport-DOCX ein professionelles PDF mit identischem Styling. Nutzt den DOCX-Renderer als einzige Layoutquelle, führt keine fachliche oder gestalterische Neuerfindung durch und verlangt eine seitenweise visuelle Paritätsprüfung zwischen DOCX-Rendering und PDF.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - dr-komorowski-sport-docx-report-renderer
outputs:
  - dr-komorowski-sport-report.pdf
lastEvaluated: 2026-08-19
---

# Dr. Komorowski Sport PDF Report Renderer

Erzeuge neue Dr.-Komorowski-Sportreports als PDF **ausschließlich aus dem kanonischen DOCX** des `dr-komorowski-sport-docx-report-renderer`.

## Architekturregel

`Report-Spec -> Dr.-Komorowski-DOCX-Template -> DOCX -> PDF`

Dieser Skill besitzt keine unabhängige Layout-Engine. Er verändert weder Trainingswerte noch Text, Tabellenstruktur, Charts, Header/Footer oder Seitengestaltung. Sichtbare PDF-Probleme werden im DOCX-Spec, Template oder DOCX-Renderer behoben und anschließend neu konvertiert.

## Trigger

Nutze diesen Skill, wenn ein finalisierter Sportdiagnostik-, Trainings-, Reha-, Taper- oder Testreport als PDF benötigt wird. Existiert noch kein kanonisches DOCX, zuerst `dr-komorowski-sport-docx-report-renderer` ausführen.

Für die exakte Reproduktion älterer ReportLab-Dokumente darf weiterhin der explizite Legacy-Skill `dr-komorowski-sport-report-renderer` verwendet werden. Neue Reports sollen diesen Direkt-PDF-Pfad nicht nutzen.

## Ablauf

1. Verifizieren, dass die Eingabe ein vollständig gerendertes und visuell geprüftes `.docx` des kanonischen Sport-DOCX-Renderers ist.
2. Mit `python scripts/render_pdf.py INPUT.docx OUTPUT.pdf` über LibreOffice/soffice konvertieren.
3. PDF in Seitenbilder rendern.
4. Dasselbe kanonische DOCX in Seitenbilder rendern.
5. Seitenanzahl, Header/Footer, Tabellen, Charts, Seitenumbrüche, Glyphen und sichtbare Inhalte Seite für Seite vergleichen.
6. Bei Reflow oder Layoutabweichung **nicht** das PDF separat bearbeiten. Ursache im DOCX/Template beheben, DOCX neu erzeugen und erneut konvertieren.
7. Nur die visuell geprüfte PDF-Version ausgeben.

## Visuelle Parität

Mindestens prüfen:

- identische Seitenanzahl oder erklärbare Renderer-Differenz ohne Inhaltsverlust,
- keine neu getrennten Tabellenzeilen,
- wiederholte Tabellenköpfe bleiben erhalten,
- Charts haben identische Daten, Achsen und Schwellenbänder,
- keine abgeschnittenen Tabellen oder Callouts,
- keine Glyphen-/Fontsubstitutionsfehler,
- Header, Footer, Logo und Seitenränder bleiben konsistent.

Wenn die Toolchain identische DOCX- und PDF-Seitenbilder erzeugt, darf zusätzlich ein pixelweiser Vergleich dokumentiert werden. Pixelidentität ist ein starkes QA-Signal, aber kein Ersatz für die inhaltliche Prüfung.

## Fehlerbehandlung

- **Eingabe ist kein DOCX:** abbrechen.
- **DOCX fehlt:** abbrechen; keinen Inhalt aus Erinnerungen rekonstruieren.
- **LibreOffice/soffice fehlt:** Abhängigkeit melden; keine HTML- oder Bilddatei als PDF tarnen.
- **Konvertierung fehlschlägt:** stderr/stdout-Kontext melden und keine leere PDF ausgeben.
- **PDF-Reflow:** Ursache im DOCX-Pfad korrigieren, nicht separat im PDF.
- **Visuelle Abweichung:** als nicht freigegeben behandeln und neu rendern.

## Übergabe

Primärer Output ist `dr-komorowski-sport-report.pdf`. Für Reproduzierbarkeit soll das zugehörige kanonische DOCX erhalten bleiben und im übergeordneten Workflow gemeinsam mit dem PDF ausgegeben werden.

## Abschlusskriterien

Der Skill ist abgeschlossen, wenn die PDF-Datei erfolgreich aus dem finalen DOCX konvertiert wurde, keine eigenständige Inhalts- oder Layoutänderung erfolgte und die seitenweise visuelle Übereinstimmung zwischen DOCX-Rendering und PDF geprüft und dokumentiert ist.
