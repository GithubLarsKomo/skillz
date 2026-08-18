---
name: sport-diagnostics-training-report-workflow
description: Orchestriert den vollständigen Dr.-Komorowski-Sportdiagnostik-Workflow von Test-/Athletendaten über nachvollziehbare Leistungsinterpretation und periodisierte Trainingsplanung bis zum visuell geprüften Marken-PDF. Verwenden, wenn Analyse, Trainingsableitung und professioneller Dr.-Komorowski-Report gemeinsam als ein durchgängiger Auftrag gewünscht sind; Fachlogik bleibt in den spezialisierten Skills.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - sport-performance-diagnostics
  - sport-training-programming
  - dr-komorowski-sport-report-renderer
outputs:
  - sport-report-package
lastEvaluated: 2026-08-18
---

# Sport Diagnostics to Training Report Workflow

Koordiniere die drei spezialisierten Skills, ohne deren Fachlogik zu duplizieren. Ziel ist ein reproduzierbarer Ablauf von Eingabedaten über fachliche Arbeitsartefakte bis zum finalen Dr.-Komorowski-PDF.

## Trigger

Nutze diesen Orchestrator bei Aufträgen wie:

- „Werte diesen Laktattest aus und erstelle daraus einen Trainingsplan als Dr.-Komorowski-PDF.“
- „Überführe meinen aktuellen Kraftblock in einen Taperplan und generiere den professionellen Report.“
- „Erstelle aus Befund/Leistungsdaten und Trainingsziel einen vollständigen Sportdiagnostik- und Trainingsreport.“

Bei reiner Testauswertung, reiner Trainingsplanung oder reinem PDF-Satz direkt den jeweiligen Fach-Skill verwenden.

## Voraussetzungen

- Eingabedaten und Ziel sind ausreichend klar oder Unsicherheiten können explizit dokumentiert werden.
- Für medizinische Befunde liegt der Originaltext oder eine verlässliche Quelle vor; keine Diagnose aus einer bloßen Erinnerung rekonstruieren.
- Für Trainingsplanung stehen Termin, Sportart, Verfügbarkeit und relevante Last-/Zoneninformationen soweit möglich bereit.
- Für den PDF-Schritt ist der fachliche Inhalt bereits freigegeben.

## Ablauf

1. **Auftrag zerlegen.** Feststellen, welche Eingangsdaten vorhanden sind und ob Diagnostik, Trainingsprogrammierung und PDF-Rendering tatsächlich alle benötigt werden.
2. **Diagnostik ausführen.** Testdaten an `sport-performance-diagnostics` übergeben. Ergebnis als `sport-diagnostics.json` sichern.
3. **Trainingsplan ableiten.** Relevante Arbeitswerte, Zieltermin und Belastungsgrenzen zusammen mit dem Nutzerziel an `sport-training-programming` übergeben. Ergebnis als `sport-training-plan.json` sichern.
4. **Konsistenz-Gate.** Prüfen, ob Trainingszonen, 1RM/e1RM, Termine, Übungsnamen und Sicherheitsgrenzen zwischen Diagnose und Plan widerspruchsfrei sind.
5. **Report-Spec bauen.** Nur freigegebene Inhalte in Cover, Metadaten, Abschnitte, Tabellen und Callouts des Renderer-Schemas transformieren.
6. **PDF rendern.** `dr-komorowski-sport-report-renderer` aufrufen und visuelle Qualitätsprüfung durchführen.
7. **Paket abschließen.** `sport-report-package` mit finalem PDF sowie den strukturierten Zwischenartefakten/Quellenreferenzen ausgeben, soweit sie für Reproduzierbarkeit benötigt werden.

## Prüfungen

- Wurde jeder fachliche Wert nur an einer Stelle interpretiert und danach referenziert?
- Stimmen Testmodalität und Trainingsmodalität zusammen oder ist die Übertragung ausdrücklich begründet?
- Sind Plan und PDF numerisch identisch?
- Sind medizinische Quellenbefunde von sportwissenschaftlichen Ableitungen getrennt?
- Sind alle Warn-/Abbruchregeln aus dem Plan im Report erhalten?
- Wurde das finale PDF gerendert und visuell geprüft?

## Fehlerbehandlung

- **Diagnostik nicht auflösbar:** keine Trainingszone erzwingen; Plan mit konservativer Ersatzsteuerung oder Klärungsbedarf fortsetzen.
- **Trainingskonflikt:** vor dem PDF-Schritt korrigieren; der Renderer ist kein Ort für fachliche Änderungen.
- **Quellbefund widersprüchlich:** Widerspruch sichtbar erhalten und gezielte Bestätigung anfordern bzw. medizinisch klären.
- **PDF-Layoutfehler:** nur Layout an den Renderer zurückgeben; Fachartefakte unverändert lassen.
- **Tool-/Dateifehler:** zuletzt verifiziertes Zwischenartefakt erhalten und genau dort wiederaufnehmen.

## Übergabe

`sport-report-package` enthält mindestens:

```json
{
  "diagnostics": "sport-diagnostics.json|not_required",
  "training_plan": "sport-training-plan.json|not_required",
  "report_spec": "report-spec.json",
  "pdf": "dr-komorowski-report.pdf",
  "verification": {
    "content_consistency": true,
    "visual_pdf_check": true
  }
}
```

Die strukturierten Artefakte sind die fachliche Wahrheit; das PDF ist deren Präsentationsform.

## Abschlusskriterien

Der Workflow ist abgeschlossen, wenn alle benötigten Fach-Skills erfolgreich beendet wurden, Diagnose und Trainingsplan konsistent sind, der Report-Spec keine stillen Inhaltsänderungen enthält und das finale Dr.-Komorowski-PDF visuell geprüft zusammen mit einem nachvollziehbaren `sport-report-package` vorliegt.
