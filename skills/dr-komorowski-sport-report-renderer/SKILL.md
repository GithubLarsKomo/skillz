---
name: dr-komorowski-sport-report-renderer
description: Legacy-Direkt-PDF-Renderer für bestehende Dr.-Komorowski-Sportdiagnostik- und Trainingsreports auf ReportLab-Basis. Bleibt zur reproduzierbaren Ausgabe älterer Report-Specs mit Vektorlogo und Vektor-Charts erhalten; neue Reports sollen über den kanonischen DOCX- und den daraus abgeleiteten PDF-Renderer laufen.
implicitInvocation: false
version: 0.3.1
status: deprecated
discoverability: compatibility
deprecatedSince: 2026-08-28
replacedBy: dr-komorowski-sport-pdf-report-renderer
owners:
  - GithubLarsKomo
requires: []
outputs:
  - dr-komorowski-report.pdf
lastEvaluated: 2026-08-19
---

# Dr. Komorowski Sport Report Renderer — Legacy Direct PDF

Dieser Skill erhält den bisherigen **ReportLab-Direkt-PDF-Pfad** für die reproduzierbare Ausgabe älterer Dr.-Komorowski-Sportreports. Er wird nicht mehr automatisch ausgewählt.

## Migration

Für neue Reports gilt:

`Report-Spec -> dr-komorowski-sport-docx-report-renderer -> DOCX -> dr-komorowski-sport-pdf-report-renderer -> PDF`

Nutze diesen Legacy-Skill nur, wenn ein älterer Report exakt über den bisherigen ReportLab-Pfad reproduziert werden soll oder die historische vektorbasierte Chartausgabe benötigt wird. Der übergeordnete `sport-diagnostics-training-report-workflow` verwendet für neue Reports den DOCX-first-Pfad.

## Trigger

Explizit nutzen bei Aufträgen wie „rendere diesen vorhandenen alten Report-Spec mit dem Legacy-Renderer“ oder „reproduziere das frühere ReportLab-PDF“. Nicht als Standard für neue Reports verwenden.

## Voraussetzungen

- fachlich finalisierter Inhalt oder vorhandener kompatibler Report-Spec,
- lokale Python-Umgebung mit `reportlab`,
- PDF-Renderer für die visuelle Endprüfung.

Die historischen Designwerte stehen in `assets/report-theme.json`; das Vektorlogo liegt in `assets/dr-komorowski-logo.svg`. **Keine Fontdateien** in den Skill einbetten oder weitergeben.

## Ablauf

1. Bestehenden Legacy-Report-Spec validieren.
2. Historische ReportLab-Layoutlogik unverändert anwenden.
3. Vektorlogo und vorhandene Vektor-Charts verwenden; keine modernen DOCX-Template-Regeln einmischen.
4. PDF erzeugen und visuell seitenweise prüfen.
5. Abweichungen vom historischen Referenzpfad dokumentieren statt stillschweigend zu modernisieren.

## Prüfungen

- Wurde der Skill explizit als Legacy-Pfad ausgewählt?
- Ist der Input mit dem historischen ReportLab-Schema kompatibel?
- Sind Logo, Charts, Tabellen und Seitenumbrüche reproduzierbar?
- Wurde keine neue fachliche Interpretation im Renderer vorgenommen?
- Wird für neue Reports weiterhin der DOCX-first-Pfad empfohlen?

## Fehlerbehandlung

- **Nicht kompatibler neuer Report-Spec:** an `dr-komorowski-sport-docx-report-renderer` und anschließend `dr-komorowski-sport-pdf-report-renderer` routen.
- **Fehlende historische Assets:** nicht durch erfundene Corporate-/Brand-Assets ersetzen; fehlende Reproduzierbarkeit dokumentieren.
- **Renderfehler:** Legacy-PDF nicht als erfolgreich ausgeben, bis die visuelle Prüfung bestanden ist.

## Übergabe

Primärer Output bleibt `dr-komorowski-report.pdf` ausschließlich für explizite Legacy-Reproduktion. Neue Berichte verwenden den Nachfolgerpfad und erhalten kein zweites paralleles PDF-Layoutsystem.

## Abschlusskriterien

Der Skill ist abgeschlossen, wenn der explizit angeforderte historische Report reproduzierbar gerendert und visuell geprüft wurde oder der Fall als nicht kompatibel an den kanonischen DOCX-first-Pfad zurückgegeben wurde.
