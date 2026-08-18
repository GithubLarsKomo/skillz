---
name: dr-komorowski-sport-report-renderer
description: Rendert strukturierte Sportdiagnostik- und Trainingsinhalte als professionellen A4-PDF-Report im etablierten Dr.-Komorowski-Diagnose-&-Training-Design mit Vektorlogo, Navy/Teal-Farbsystem, Tabellen, Callouts, Kopf-/Fußzeilen und visueller Qualitätskontrolle. Verwenden, wenn ein fertiger fachlicher Inhalt im wiederverwendbaren Dr.-Komorowski-Template ausgegeben werden soll; der Skill erfindet keine Diagnostik oder Trainingslogik.
---

# Dr. Komorowski Sport Report Renderer

Setze bereits fachlich geklärten Inhalt in das etablierte Erscheinungsbild des **Dr. Komorowski Diagnose- und Trainingszentrums**. Der Renderer kapselt Logo, Farben, Typografie, Tabellen, Callouts, Kopf-/Fußzeilen und Seitenlogik, damit spätere Reports nicht jedes Mal neu gestaltet werden.

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
3. **Report-Spec validieren.** Pflichtfelder, unterstützte Blocktypen und Tabellenstruktur prüfen.
4. **PDF rendern.** `scripts/render_report.py INPUT.json OUTPUT.pdf` verwenden. Unterstützte Blöcke: `heading`, `subheading`, `paragraph`, `bullets`, `table`, `callout`, `spacer`, `pagebreak`.
5. **Kopf-/Fußzeilen prüfen.** Oben rechts Dokumentkontext, unten Dokumenttyp/Datum sowie Seitennummer; Linien dezent in Border-Grau.
6. **Visuell verifizieren.** PDF mit mindestens einem Renderer in PNGs rendern und auf abgeschnittene Texte, überlaufende Tabellen, Glyphenfehler, ungewollte Seitenumbrüche und inkonsistente Abstände prüfen.
7. **Bei Layoutfehlern korrigieren.** Nicht durch manuelle Leerzeichen oder hart codierte Zeilenumbrüche kaschieren; Spaltenbreiten, Absatzstile oder Blockstruktur korrigieren und erneut rendern.
8. **Finale Datei benennen.** Aussagekräftiger ASCII-kompatibler Dateiname, PDF-Metadaten setzen und nur die finale Version ausgeben.

Beispiel:

```bash
python scripts/render_report.py assets/report-spec.example.json /tmp/dr-komorowski-report.pdf
```

## Designstandard

Das aktuelle Referenzdesign verwendet:

- Navy `#173652` für Marke, Kopfzeile und Hauptüberschriften,
- Dark `#1C2B3A` / Body `#24313E` für Titel und Lesetext,
- Teal `#2B8884` für Linien und Akzente,
- Teal Text `#246F6C` für Subheads,
- Border `#D6E0E6`, Table Fill `#EDF3F6`, Callout Fill `#F6F8F9`,
- Warning Fill `#FFF4D6` und Warning Border `#9A6500`,
- A4, großzügige Weißräume, serifenlose DejaVu-Sans/Helvetica-Fallbacks.

Weitere Details: `references/brand-guide.md`.

## Prüfungen

Vor Übergabe prüfen:

- Logo bleibt scharf und ist nicht gerastert.
- Alle Seiten tragen konsistente Kopf-/Fußzeilen.
- Überschriftenhierarchie ist klar, ohne dekorative Überladung.
- Tabellen sind auf A4 lesbar; kein Text läuft aus Zellen.
- Callouts verwenden nur definierte Info-/Warning-Rollen.
- Umlaute, Prozentzeichen, ×/x und Sonderzeichen rendern korrekt; bei Rendererproblemen ASCII-kompatible Zeichen bevorzugen.
- PDF-Metadaten enthalten Titel, Subject und Author ohne unbeabsichtigte personenbezogene Zusatzdaten.
- Visuelle PNG-Prüfung ist erfolgt.

## Fehlerbehandlung

- **ReportLab fehlt:** Abhängigkeit explizit melden; keine leere oder ersatzweise HTML-Datei als PDF ausgeben.
- **Font nicht vorhanden:** DejaVu Sans über Fontconfig/übliche Systempfade suchen, andernfalls Helvetica-Fallback verwenden; keine Fontdatei in den Skill kopieren.
- **Zu breite Tabelle:** Spaltenbreiten anpassen, Text umbrechen oder Tabelle in logisch getrennte Tabellen teilen; niemals horizontal aus A4 herauslaufen lassen.
- **Seitenüberlauf:** ReportLab-Flowables und PageBreaks verwenden, keine absolute Positionierung langer Fließtexte.
- **Ungültiges Blockformat:** mit verständlicher Fehlermeldung und Blockindex abbrechen.

## Übergabe

Primärer Output ist `dr-komorowski-report.pdf`. Zusätzlich kann die geprüfte Report-Spec zusammen mit einem Render-Preview als Audit-/Reproduktionsartefakt erhalten bleiben. Inhaltliche Änderungen müssen an den vorgelagerten Fach-Skill zurückgegeben werden, nicht im Renderer still korrigiert werden.

## Abschlusskriterien

Der Skill ist abgeschlossen, wenn die PDF-Datei mit dem kanonischen Vektorlogo und Theme gerendert, in mindestens einem PDF-Renderer visuell geprüft, frei von Clipping/Überlappungen/Glyphenfehlern und inhaltlich identisch zum freigegebenen Report-Spec ist.
