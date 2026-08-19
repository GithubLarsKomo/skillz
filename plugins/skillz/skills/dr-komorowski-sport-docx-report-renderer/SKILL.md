---
name: dr-komorowski-sport-docx-report-renderer
description: Rendert fachlich finalisierte Sportdiagnostik-, Trainings- und Reha-Inhalte als editierbares A4-DOCX im Dr.-Komorowski-Sportdiagnose-und-Trainingszentrum-Design. Nutzt ein im Skill hinterlegtes kanonisches DOCX-Template, unterstützt kontrollierte Template-Overrides, Sporttabellen und Laktat-/Herzfrequenz-Charts und verändert keine fachlichen Aussagen.
---

# Dr. Komorowski Sport DOCX Report Renderer

Setze bereits fachlich geklärte Sportdiagnostik- und Trainingsinhalte in das kanonische editierbare Reportformat des **Dr. Komorowski Sportdiagnose und Trainingszentrums**. Fach-Skills bestimmen Diagnostik, Trainingssteuerung, Sicherheitsgrenzen und Empfehlungen; dieser Skill bestimmt ausschließlich Darstellung und Dokumentstruktur.

## Trigger

Nutze diesen Skill, wenn ein finalisierter Inhalt als editierbares DOCX im Dr.-Komorowski-Stil benötigt wird, insbesondere für:

- Laktat- und Leistungsdiagnostik,
- Trainingszonen und Testberichte,
- Kraft-, Schnellkraft-, Taper- und Wettkampfpläne,
- Reha-/Belastungssteuerungspläne,
- mehrwöchige kombinierte Kraft-/Ausdauerprogramme,
- sportmedizinisch informierte Arbeitsberichte, sofern der zugrunde liegende Befund bereits fachlich geklärt ist.

Nicht nutzen, um Testdaten neu auszuwerten, Diagnosen zu stellen oder Trainingslogik zu erfinden. Dafür zuerst `sport-performance-diagnostics` bzw. `sport-training-programming` verwenden.

## Kanonische Architektur

`Fachartefakte -> Report-Spec -> Dr.-Komorowski-DOCX-Template -> DOCX`

Das DOCX ist die einzige kanonische Layoutquelle für neue Sportreports. Ein späteres PDF wird ausschließlich aus diesem DOCX erzeugt.

## Template-Modell

- Bundled template snapshot: `assets/dr-komorowski-report-template.docx.b64`
- Editierbare Generatorquelle: `scripts/build_template.py`
- Theme: `assets/report-theme.json`
- Editierbares Markenlogo: `assets/dr-komorowski-logo.svg`
- Allgemeines Beispiel: `assets/report-spec.example.json`
- Laktatbeispiel: `assets/report-spec.lactate.example.json`
- Kontrolliertes Template-Override: `--template PATH.docx`

Die Base64-Datei ist die exakt reproduzierbare, repo-kompatible Textrepräsentation des geprüften DOCX-Templates. Keine Fontdateien in den Skill einbetten oder weitergeben.

## Template-Vertrag

Ein Override-Template muss folgende Platzhalter enthalten:

- `{{DOCUMENT_TYPE}}`
- `{{DOCUMENT_ID}}`
- `{{DATE}}`
- `{{CONFIDENTIALITY}}`
- `{{REPORT_BODY}}`

Fehlt ein Pflichtplatzhalter, abbrechen. Nicht still auf das gebündelte Template zurückfallen und nicht an beliebiger Position in ein fremdes Template schreiben. Header, Footer und Corporate Styles eines gültigen Overrides bleiben erhalten.

## Report-Spec

Pflichtfelder in `metadata`:

- `title`
- `date`
- `document_type`

Optionale Metadaten umfassen `subtitle`, `document_id`, `version`, `athlete`, `sport`, `test_or_phase`, `author`, `confidentiality` und `department`.

Unterstützte Blocktypen:

- `heading`
- `subheading`
- `paragraph`
- `bullets`
- `table`
- `callout`
- `chart`
- `image`
- `spacer`
- `pagebreak`

## Tabellenregeln

Sportreports enthalten häufig lange Wochenpläne und mehrspaltige Belastungstabellen. Deshalb gelten verbindlich:

1. Tabellen bleiben innerhalb der A4-Satzbreite.
2. Text wird umbrochen; Schrift wird nicht auf unlesbare Größe reduziert.
3. Tabellenzeilen werden mit `cantSplit` zusammengehalten und nicht zwischen zwei Seiten geteilt.
4. Die Kopfzeile mehrseitiger Tabellen wird mit `tblHeader` auf Folgeseiten wiederholt.
5. Wenn eine einzelne Zeile physisch nicht auf eine Seite passt, Inhalt fachlich neutral in logisch getrennte Zeilen/Tabellen aufteilen und erneut rendern.
6. Keine fachlichen Werte ändern, nur um Layoutprobleme zu lösen.

## Laktat-/Herzfrequenz-Chart

`chart_type: "lactate_hr_power"` stellt bereits fachlich bestimmte Messwerte dar:

- x-Achse: Leistung in Watt,
- linke y-Achse: Laktat in mmol/L,
- rechte y-Achse: Herzfrequenz in bpm,
- optionale LT1-/LT2-Bänder mit `from_w`, `to_w` und optional `working_w`.

Der Renderer berechnet oder verschiebt LT1/LT2 nicht. `power_w` muss streng aufsteigend sein; numerische Werte müssen endlich sein. Für neue DOCX-Reports wird der Chart als hochauflösende eingebettete Grafik erzeugt, damit Word und das daraus konvertierte PDF dasselbe sichtbare Ergebnis besitzen. Der frühere direkte ReportLab-Renderer bleibt für die Reproduktion historischer vektorbasierter PDFs verfügbar.

## Ablauf

1. **Inhalt einfrieren.** Nur freigegebene Fachartefakte in das Report-Spec übernehmen.
2. **Spec validieren.** Pflichtmetadaten, Blocktypen, Tabellenbreiten und Chartdaten prüfen.
3. **Template laden.** Gültiges `--template` verwenden, sonst den gebündelten Snapshot dekodieren.
4. **DOCX rendern.** `python scripts/render_report.py INPUT.json OUTPUT.docx`.
5. **Pagination prüfen.** Tabellenzeilen, Tabellenköpfe, Callouts und Charts auf sinnvolle Seitenumbrüche kontrollieren.
6. **DOCX visuell rendern.** Jede Seite mit LibreOffice/Word-kompatiblem Renderer oder der Dokument-QA-Toolchain als Bild darstellen.
7. **Visuell prüfen.** Auf Clipping, Überlappung, Glyphen, Tabellenüberlauf, abgeschnittene Charts und inkonsistente Header/Footer prüfen.
8. **Bei Fehlern neu rendern.** Layout im Spec, Theme oder Template korrigieren; keine manuellen Leerzeichen-Tricks verwenden.

## Designstandard

Das kanonische Theme nutzt:

- Navy `#173652` für Marke und Hauptüberschriften,
- Dark `#1C2B3A` / Body `#24313E` für Lesetext,
- Teal `#2B8884` / `#246F6C` für Akzente und Subheads,
- Border `#D6E0E6`, Table Fill `#EDF3F6`, Callout Fill `#F6F8F9`,
- Warning Fill `#FFF4D6` / Border `#9A6500`,
- A4 mit großzügigem Weißraum und robusten Systemfont-Fallbacks.

## Fehlerbehandlung

- **Template fehlt/defekt:** konkret abbrechen; keinen leeren Ersatzreport erzeugen.
- **Pflichtplatzhalter fehlt:** fehlenden Token nennen und Template unverändert lassen.
- **python-docx/Pillow fehlt:** Abhängigkeit melden.
- **Zu breite Tabelle:** Spaltenbreiten/Blockstruktur korrigieren oder logisch teilen.
- **Ungültiger Chart:** mit Blockkontext abbrechen; Werte nicht sortieren, erraten oder interpolieren.
- **Bild fehlt:** Pfad nennen und abbrechen.
- **Font fehlt:** Systemfallback verwenden; keine Fontdateien kopieren.

## Migration vom direkten PDF-Renderer

`dr-komorowski-sport-report-renderer` bleibt als expliziter Legacy-Renderer bestehen, damit ältere Report-Specs und archivierte ReportLab-PDFs reproduzierbar bleiben. Für neue Dokumente ist dieser DOCX-Renderer die kanonische Layoutquelle. Neue Workflows sollen den Legacy-Renderer nicht automatisch aufrufen.

## Abschlusskriterien

Der Skill ist abgeschlossen, wenn das DOCX inhaltlich identisch zum freigegebenen Report-Spec ist, Header/Footer und Marke konsistent sind, Tabellen innerhalb A4 bleiben, mehrseitige Tabellen wiederholte Kopfzeilen und ungeteilte Datenzeilen besitzen, Charts vollständig sichtbar sind und **jede gerenderte DOCX-Seite visuell geprüft** wurde.
