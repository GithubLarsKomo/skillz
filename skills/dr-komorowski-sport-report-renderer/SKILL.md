---
name: dr-komorowski-sport-report-renderer
description: Legacy-Direkt-PDF-Renderer für bestehende Dr.-Komorowski-Sportdiagnostik- und Trainingsreports auf ReportLab-Basis. Bleibt zur reproduzierbaren Ausgabe älterer Report-Specs mit Vektorlogo und Vektor-Charts erhalten; neue Reports sollen über den kanonischen DOCX- und den daraus abgeleiteten PDF-Renderer laufen.
userFacing: true
implicitInvocation: false
category: workflow
version: 0.3.0
status: candidate
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

1. **Inhalt einfrieren.** Der Legacy-Renderer verändert keine Schwellen, Lasten, Diagnosen, Trainingswerte oder medizinischen Aussagen.
2. Report-Spec mit den vom vorhandenen `scripts/render_report.py` unterstützten Blöcken validieren.
3. Direkt-PDF mit dem bestehenden ReportLab-Renderer erzeugen.
4. Kopf-/Fußzeilen, Tabellen, Callouts und Charts kontrollieren.
5. **Visuell verifizieren.** PDF in Seitenbilder rendern und auf Clipping, Überlauf, Glyphenfehler, Achsen/Legenden und Seitenumbrüche prüfen.
6. Bei Layoutfehlern nur Layoutparameter/Blockstruktur korrigieren, keine Fachwerte.

Beispiel:

```bash
python scripts/render_report.py assets/report-spec.example.json /tmp/dr-komorowski-legacy.pdf
python scripts/render_report.py assets/report-spec.lactate-chart.example.json /tmp/dr-komorowski-legacy-lactate.pdf
```

## Chart-Kompatibilität

Der bestehende `lactate_hr_power`-Block bleibt für historische Specs erhalten. Leistung, Laktat, Herzfrequenz sowie übergebene LT1-/LT2-Bänder werden als ReportLab-Vektorinhalt gerendert. Der Renderer berechnet oder verschiebt LT1/LT2 nicht.

## Designstandard

Historisches Referenzdesign:

- Navy `#173652`,
- Dark `#1C2B3A` / Body `#24313E`,
- Teal `#2B8884` / Teal Text `#246F6C`,
- Border `#D6E0E6`, Table Fill `#EDF3F6`, Callout Fill `#F6F8F9`,
- Warning Fill `#FFF4D6` / Warning Border `#9A6500`,
- A4, Vektorlogo und ReportLab-Vektor-Charts.

## Fehlerbehandlung

- **ReportLab fehlt:** Abhängigkeit explizit melden; keine Ersatzdatei als PDF ausgeben.
- **Font nicht vorhanden:** DejaVu Sans über Systempfade suchen, andernfalls Helvetica-Fallback; keine Fontdatei kopieren.
- **Zu breite Tabelle:** Spaltenbreiten/Umbruch anpassen oder logisch teilen; niemals horizontal aus A4 laufen lassen.
- **Ungültiger Chart:** bei fehlenden/nichtnumerischen Punkten, nicht aufsteigender Leistung oder ungültigen LT-Bändern abbrechen; keine Werte erraten oder sortieren.
- **Seitenüberlauf:** ReportLab-Flowables/PageBreaks verwenden, keine manuellen Leerzeichen-Tricks.

## Übergabe

Primärer Output bleibt `dr-komorowski-report.pdf`. Bei neuen Reportaufträgen stattdessen auf die DOCX-first-Pipeline routen und DOCX sowie daraus abgeleitetes PDF gemeinsam ausgeben.

## Abschlusskriterien

Der Legacy-Skill ist abgeschlossen, wenn das PDF im historischen Design gerendert, visuell geprüft und inhaltlich identisch zum freigegebenen Spec ist. Er ist **kein** zweiter kanonischer Layoutpfad für neue Dokumente.
