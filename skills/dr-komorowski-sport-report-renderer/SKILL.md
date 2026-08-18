---
name: dr-komorowski-sport-report-renderer
description: Rendert strukturierte Sportdiagnostik- und Trainingsinhalte als professionellen A4-PDF-Report im etablierten Dr.-Komorowski-Diagnose-&-Training-Design mit Vektorlogo, Navy/Teal-Farbsystem, Tabellen, Callouts, Charts, Kopf-/Fußzeilen und visueller Qualitätskontrolle. Verwenden, wenn ein fertiger fachlicher Inhalt im wiederverwendbaren Dr.-Komorowski-Template ausgegeben werden soll; der Skill erfindet keine Diagnostik oder Trainingslogik.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.2.0
status: candidate
owners:
  - GithubLarsKomo
requires: []
outputs:
  - dr-komorowski-report.pdf
lastEvaluated: 2026-08-18
---

# Dr. Komorowski Sport Report Renderer

Setze bereits fachlich geklärten Inhalt in das etablierte Erscheinungsbild des **Dr. Komorowski Diagnose- und Trainingszentrums**. Der Renderer kapselt Logo, Farben, Typografie, Tabellen, Callouts, Charts, Kopf-/Fußzeilen und Seitenlogik, damit spätere Reports nicht jedes Mal neu gestaltet werden.

## Trigger

Nutze diesen Skill, wenn der Nutzer einen Sportdiagnostik-, Trainings-, Taper-, Test- oder Therapiearbeitsreport ausdrücklich im Dr.-Komorowski-Stil als PDF wünscht oder ein bestehender strukturierter Inhalt genau in dieses Template gesetzt werden soll.

Nicht nutzen, um ungeklärte Testdaten fachlich auszuwerten oder einen Trainingsplan neu zu entwickeln. Dafür zuerst `sport-performance-diagnostics` bzw. `sport-training-programming` verwenden.

## Voraussetzungen

- Ein fachlich freigegebener Report-Inhalt oder ein strukturiertes Report-Spec.
- Report-Titel, Datum, Dokumenttyp und optional Berichtsnummer.
- Optional Athleten-/Testmetadaten; personenbezogene Angaben nur übernehmen, wenn sie für das gewünschte Dokument erforderlich sind.
- Lokale Python-Umgebung mit `reportlab`.
- Für die visuelle Endprüfung ein PDF-Renderer wie Poppler/PDFium.

Die kanonischen Designwerte stehen in `assets/report-theme.json`; das Logo liegt als editierbares `assets/dr-komorowski-logo.svg` vor. Keine Fontdateien in den Skill einbetten oder weitergeben.

## Ablauf

1. **Inhalt einfrieren.** Fachtext, Tabellen und Zahlen vor dem Layout als Report-Spec strukturieren; der Renderer verändert keine Schwellen, Lasten, Diagnosen oder medizinische Aussagen.
2. **Template laden.** Farben, Maße und Textrollen aus `assets/report-theme.json` verwenden. Das Logo ist Vektorinhalt, kein Screenshot.
3. **Report-Spec validieren.** Pflichtfelder, unterstützte Blocktypen, Tabellenstruktur und Chart-Daten prüfen.
4. **PDF rendern.** `scripts/render_report.py INPUT.json OUTPUT.pdf` verwenden. Unterstützte Blöcke: `heading`, `subheading`, `paragraph`, `bullets`, `table`, `callout`, `chart`, `spacer`, `pagebreak`.
5. **Kopf-/Fußzeilen prüfen.** Oben rechts Dokumentkontext, unten Dokumenttyp/Datum sowie Seitennummer; Linien dezent in Border-Grau.
6. **Visuell verifizieren.** PDF mit mindestens einem Renderer in PNGs rendern und auf abgeschnittene Texte, überlaufende Tabellen, fehlerhafte Achsen/Legenden, Glyphenfehler, ungewollte Seitenumbrüche und inkonsistente Abstände prüfen.
7. **Bei Layoutfehlern korrigieren.** Nicht durch manuelle Leerzeichen oder hart codierte Zeilenumbrüche kaschieren; Spaltenbreiten, Absatzstile, Chart-Höhe oder Blockstruktur korrigieren und erneut rendern.
8. **Finale Datei benennen.** Aussagekräftiger ASCII-kompatibler Dateiname, PDF-Metadaten setzen und nur die finale Version ausgeben.

Beispiel:

```bash
python scripts/render_report.py assets/report-spec.example.json /tmp/dr-komorowski-report.pdf
python scripts/render_report.py assets/report-spec.lactate-chart.example.json /tmp/dr-komorowski-lactate-chart.pdf
```

## Chart-Block: Laktat + Herzfrequenz über Leistung

Der Renderer unterstützt einen echten Vektor-Chart mit `type: "chart"` und `chart_type: "lactate_hr_power"`. Er zeichnet:

- Leistung auf der x-Achse,
- Laktat auf der linken y-Achse,
- Herzfrequenz auf einer getrennten rechten y-Achse,
- Messpunkte und Verbindungslinien für beide Reihen,
- LT1-/LT2-Arbeitsbereiche als vertikale Bänder,
- optionale Arbeitswerte innerhalb der Bänder als gestrichelte Vertikalen,
- Titel, Legende, Achsenbeschriftungen und optionale Bildunterschrift.

Minimalbeispiel:

```json
{
  "type": "chart",
  "chart_type": "lactate_hr_power",
  "title": "Laktat und Herzfrequenz über Leistung",
  "data": [
    {"power_w": 100, "lactate_mmol_l": 1.0, "hr_bpm": 108},
    {"power_w": 125, "lactate_mmol_l": 1.0, "hr_bpm": 116}
  ],
  "threshold_bands": [
    {"label": "LT1", "kind": "lt1", "from_w": 175, "to_w": 185, "working_w": 180},
    {"label": "LT2", "kind": "lt2", "from_w": 220, "to_w": 230, "working_w": 225}
  ]
}
```

Für `data` sind mindestens zwei Messpunkte erforderlich. `power_w` muss streng aufsteigend sein; `power_w`, `lactate_mmol_l` und `hr_bpm` müssen endliche Zahlen sein. Für jedes Schwellenband muss `to_w > from_w` gelten. Wenn `working_w` angegeben wird, muss der Wert innerhalb des Bandes liegen. `height_mm` ist optional und muss zwischen 60 und 130 mm liegen.

Die Chart-Achsen werden aus den Daten automatisch auf sinnvolle Grenzen und Tick-Abstände skaliert. Die Laktatachse beginnt bei 0; die Herzfrequenzachse erhält eine eigene Skala. Die LT-Bänder sind **Darstellung bereits fachlich bestimmter Arbeitsbereiche**. Der Renderer berechnet oder verschiebt LT1/LT2 nicht.

Referenz: `assets/report-spec.lactate-chart.example.json`.

## Designstandard

Das aktuelle Referenzdesign verwendet:

- Navy `#173652` für Marke, Kopfzeile, Hauptüberschriften und Laktatkurve,
- Dark `#1C2B3A` / Body `#24313E` für Titel und Lesetext,
- Teal `#2B8884` für Linien, Akzente, Herzfrequenzkurve und LT1-Markierung,
- Teal Text `#246F6C` für Subheads,
- Border `#D6E0E6`, Table Fill `#EDF3F6`, Callout Fill `#F6F8F9`,
- Warning Fill `#FFF4D6` und Warning Border `#9A6500` für Warnboxen und LT2-Markierung,
- A4, großzügige Weißräume, serifenlose DejaVu-Sans/Helvetica-Fallbacks.

Weitere Details: `references/brand-guide.md`.

## Prüfungen

Vor Übergabe prüfen:

- Logo bleibt scharf und ist nicht gerastert.
- Alle Seiten tragen konsistente Kopf-/Fußzeilen.
- Überschriftenhierarchie ist klar, ohne dekorative Überladung.
- Tabellen sind auf A4 lesbar; kein Text läuft aus Zellen.
- Callouts verwenden nur definierte Info-/Warning-Rollen.
- Charts bleiben Vektorinhalt; Achsen, Messpunkte, Legende und LT-Bänder sind vollständig sichtbar.
- Bei Dual-Axis-Charts sind Laktat und Herzfrequenz eindeutig den jeweiligen Achsen zugeordnet; keine optische Gleichsetzung unterschiedlicher Einheiten.
- LT1/LT2-Bänder entsprechen exakt den im Report-Spec übergebenen fachlichen Arbeitsbereichen.
- Umlaute, Prozentzeichen, ×/x und Sonderzeichen rendern korrekt; bei Rendererproblemen ASCII-kompatible Zeichen bevorzugen.
- PDF-Metadaten enthalten Titel, Subject und Author ohne unbeabsichtigte personenbezogene Zusatzdaten.
- Visuelle PNG-Prüfung ist erfolgt.

## Fehlerbehandlung

- **ReportLab fehlt:** Abhängigkeit explizit melden; keine leere oder ersatzweise HTML-Datei als PDF ausgeben.
- **Font nicht vorhanden:** DejaVu Sans über Fontconfig/übliche Systempfade suchen, andernfalls Helvetica-Fallback verwenden; keine Fontdatei in den Skill kopieren.
- **Zu breite Tabelle:** Spaltenbreiten anpassen, Text umbrechen oder Tabelle in logisch getrennte Tabellen teilen; niemals horizontal aus A4 herauslaufen lassen.
- **Ungültiger Chart:** bei fehlenden/nichtnumerischen Messpunkten, nicht aufsteigender Leistung oder inkonsistenten LT-Bändern mit Blockindex abbrechen; keine Werte erraten oder sortierend verändern.
- **Chart zu hoch:** `height_mm` innerhalb 60–130 mm anpassen oder mit einem gezielten `pagebreak` platzieren; nicht aus dem Seitenrahmen skalieren.
- **Seitenüberlauf:** ReportLab-Flowables und PageBreaks verwenden, keine absolute Positionierung langer Fließtexte.
- **Ungültiges Blockformat:** mit verständlicher Fehlermeldung und Blockindex abbrechen.

## Übergabe

Primärer Output ist `dr-komorowski-report.pdf`. Zusätzlich kann die geprüfte Report-Spec zusammen mit einem Render-Preview als Audit-/Reproduktionsartefakt erhalten bleiben. Inhaltliche Änderungen müssen an den vorgelagerten Fach-Skill zurückgegeben werden, nicht im Renderer still korrigiert werden.

## Abschlusskriterien

Der Skill ist abgeschlossen, wenn die PDF-Datei mit dem kanonischen Vektorlogo und Theme gerendert, in mindestens einem PDF-Renderer visuell geprüft, frei von Clipping/Überlappungen/Glyphenfehlern und inhaltlich identisch zum freigegebenen Report-Spec ist. Bei Reports mit `chart`-Block müssen zusätzlich beide y-Achsen, alle Datenpunkte und die LT1-/LT2-Arbeitsbereiche korrekt und eindeutig sichtbar sein.
