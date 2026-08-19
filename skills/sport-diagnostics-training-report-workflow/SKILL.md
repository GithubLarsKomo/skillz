---
name: sport-diagnostics-training-report-workflow
description: Orchestriert den vollständigen Dr.-Komorowski-Sportdiagnostik-Workflow von Test-/Athletendaten über nachvollziehbare Leistungsinterpretation und periodisierte Trainingsplanung bis zum kanonischen DOCX und dem daraus abgeleiteten, visuell abgeglichenen PDF. Fachlogik bleibt in den spezialisierten Skills.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.2.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - sport-performance-diagnostics
  - sport-training-programming
  - dr-komorowski-sport-docx-report-renderer
  - dr-komorowski-sport-pdf-report-renderer
outputs:
  - sport-report-package
lastEvaluated: 2026-08-19
---

# Sport Diagnostics to Training Report Workflow

Koordiniere die spezialisierten Sport-Skills, ohne deren Fachlogik zu duplizieren. Ziel ist ein reproduzierbarer Ablauf von Eingangsdaten über fachliche Arbeitsartefakte bis zum **editierbaren kanonischen DOCX und dem daraus abgeleiteten PDF**.

## Trigger

Nutze diesen Orchestrator bei Aufträgen wie:

- „Werte diesen Laktattest aus, leite einen Trainingsplan ab und erstelle DOCX und PDF im Dr.-Komorowski-Stil.“
- „Überführe meinen aktuellen Kraftblock in einen Taperplan und generiere den professionellen Report.“
- „Erstelle aus Befund/Leistungsdaten und Trainingsziel einen vollständigen Sportdiagnostik- und Trainingsreport.“

Bei reiner Testauswertung, reiner Trainingsplanung oder reinem Dokumentsatz direkt den jeweiligen Fach- oder Renderer-Skill verwenden.

## Voraussetzungen

- Eingabedaten und Ziel sind ausreichend klar oder Unsicherheiten werden explizit dokumentiert.
- Für medizinische Befunde liegt der Originaltext oder eine verlässliche Quelle vor; keine Diagnose aus bloßer Erinnerung rekonstruieren.
- Für Trainingsplanung stehen Termin, Sportart, Verfügbarkeit und relevante Last-/Zoneninformationen soweit möglich bereit.
- Vor dem Rendering ist der fachliche Inhalt eingefroren.

## Ablauf

1. **Auftrag zerlegen.** Feststellen, welche Eingangsdaten vorhanden sind und ob Diagnostik, Trainingsprogrammierung und Rendering tatsächlich alle benötigt werden.
2. **Diagnostik ausführen.** Falls erforderlich Testdaten an `sport-performance-diagnostics` übergeben. Ergebnis als `sport-diagnostics.json` sichern.
3. **Trainingsplan ableiten.** Falls erforderlich Arbeitswerte, Zieltermin und Belastungsgrenzen an `sport-training-programming` übergeben. Ergebnis als `sport-training-plan.json` sichern.
4. **Konsistenz-Gate.** Trainingszonen, 1RM/e1RM, Termine, Übungsnamen, RIR/RPE, Dauer/Kadenz und Sicherheitsgrenzen zwischen Diagnose und Plan widerspruchsfrei halten.
5. **Report-Spec bauen.** Nur freigegebene Inhalte in Metadaten, Abschnitte, Tabellen, Callouts, Charts und Seitenumbrüche des DOCX-Renderer-Schemas transformieren.
6. **Kanonisches DOCX rendern.** `dr-komorowski-sport-docx-report-renderer` aufrufen und jede Seite visuell prüfen. Mehrseitige Tabellen müssen ungeteilte Datenzeilen und wiederholte Kopfzeilen behalten.
7. **PDF ableiten.** Das freigegebene DOCX an `dr-komorowski-sport-pdf-report-renderer` übergeben; keine zweite Layoutlogik verwenden.
8. **Paritäts-Gate.** DOCX- und PDF-Seitenbilder auf Reflow, Tabellen, Charts, Header/Footer, Glyphen und sichtbare Inhalte vergleichen. Bei Abweichung zurück zum DOCX-Pfad.
9. **Paket abschließen.** DOCX, PDF und benötigte strukturierte Zwischenartefakte/Quellenreferenzen gemeinsam ausgeben.

## Renderer-Routing

Für neue Reports gilt zwingend:

`Report-Spec -> dr-komorowski-sport-docx-report-renderer -> DOCX -> dr-komorowski-sport-pdf-report-renderer -> PDF`

`dr-komorowski-sport-report-renderer` ist ein Legacy-Direkt-PDF-Pfad für die Reproduktion älterer ReportLab-Dokumente und wird von diesem Orchestrator **nicht automatisch** für neue Reports aufgerufen.

## Prüfungen

- Wurde jeder fachliche Wert nur an einer Stelle interpretiert und danach referenziert?
- Stimmen Testmodalität und Trainingsmodalität zusammen oder ist die Übertragung ausdrücklich begründet?
- Sind Plan, Report-Spec, DOCX und PDF numerisch identisch?
- Sind medizinische Quellenbefunde von sportwissenschaftlichen Ableitungen getrennt?
- Sind Warn-/Abbruchregeln vollständig erhalten?
- Wurde jede DOCX-Seite visuell geprüft?
- Wurde das PDF ausschließlich aus dem finalen DOCX erzeugt?
- Wurde die visuelle DOCX/PDF-Parität geprüft?

## Fehlerbehandlung

- **Diagnostik nicht auflösbar:** keine Trainingszone erzwingen; konservative Ersatzsteuerung oder Klärungsbedarf erhalten.
- **Trainingskonflikt:** vor dem Rendering korrigieren; Renderer sind kein Ort für fachliche Änderungen.
- **Quellbefund widersprüchlich:** Widerspruch sichtbar erhalten und gezielte Bestätigung/medizinische Klärung verlangen.
- **DOCX-Layoutfehler:** nur Layout an den DOCX-Renderer zurückgeben; Fachartefakte unverändert lassen.
- **PDF-Reflow:** nicht im PDF reparieren; DOCX-Quelle korrigieren und neu konvertieren.
- **Tool-/Dateifehler:** zuletzt verifiziertes Zwischenartefakt erhalten und genau dort wiederaufnehmen.

## Übergabe

`sport-report-package` enthält mindestens:

```json
{
  "diagnostics": "sport-diagnostics.json|not_required",
  "training_plan": "sport-training-plan.json|not_required",
  "report_spec": "report-spec.json",
  "docx": "dr-komorowski-sport-report.docx",
  "pdf": "dr-komorowski-sport-report.pdf",
  "verification": {
    "content_consistency": true,
    "visual_docx_check": true,
    "visual_pdf_check": true,
    "docx_pdf_parity": true
  }
}
```

Die strukturierten Fachartefakte sind die fachliche Wahrheit; das DOCX ist die kanonische Layoutquelle; das PDF ist deren abgeleitete Präsentationsform.

## Abschlusskriterien

Der Workflow ist abgeschlossen, wenn alle benötigten Fach-Skills beendet wurden, Diagnose und Trainingsplan konsistent sind, der Report-Spec keine stillen Inhaltsänderungen enthält, das DOCX visuell geprüft wurde, das PDF ausschließlich daraus konvertiert wurde und die visuelle DOCX/PDF-Übereinstimmung bestätigt ist.
