---
name: presentation-layout-qa
description: Prüft PowerPoint-Folien strukturell auf Text- und Box-Overflow, Objektüberlagerungen, Slide-Grenzen, Font-Ausreißer, inkonsistente Ausrichtung, Platzhaltermissbrauch, Bildverzerrung, Chart-/Tabellen-Clipping und Footer-Kollisionen. Verwenden als technische QA vor finalem Rendering; nicht als visuelle Geschmacksprüfung.
---

# Presentation Layout QA

Dieser Skill prüft ein Deck auf objekt- und geometriebasierte Layoutfehler. Template-spezifische Baselines haben Vorrang vor universellen Grenzwerten.

## Inputs

- PPTX/POTX oder editierbares Deck.
- `presentation-template-profile.json`, sofern verfügbar.
- optional bekannte Render- oder Exportwarnungen.

## Prüfklassen

### Text und Boxen

- Text overflow / autofit anomalies.
- Box overflow und abgeschnittene Inhalte.
- Zu enge Innenränder.
- Unerwartete Zeilenumbrüche oder einzelne Restwörter.
- Font-Größen-Ausreißer relativ zu Template-Baselines.
- Font-Substitutionen oder inkonsistente Font Families/Weights.

### Geometrie

- Objektüberlagerungen.
- Objekte außerhalb der Slide-Grenzen.
- Inkonsistente Titel-, Inhalts- und Footer-Positionen.
- Alignment- und Spacing-Ausreißer.
- Platzhalter, die ohne Not durch freie Textboxen ersetzt wurden.

### Visuals

- verzerrte Bilder oder Logos.
- abgeschnittene Chart-Labels, Legends oder Axis Titles.
- Tabellenüberlauf, zu enge Zeilen/Höhen oder unlesbare Zelltexte.
- Footer-, Quellen- oder Branding-Kollisionen.

## Baseline-Logik

Keine starre globale Mindestschriftgröße behaupten, wenn das Template andere gültige Werte vorgibt. Stattdessen beobachtete Werte aus `presentation-template-profile.json` verwenden, z. B. Median und typische Range für Titel, Body, Quelle, Tabellen und Chart-Labels.

Beispiel:

```json
{
  "slide": 14,
  "object": "body-2",
  "finding": "font-size-outlier",
  "observedPt": 11,
  "templateMedianPt": 18,
  "severity": "review"
}
```

## Schweregrade

- `critical`: Inhalt abgeschnitten, nicht sichtbar oder objektiv fehlerhaft.
- `major`: deutliche Template-Abweichung oder Lesbarkeitsrisiko.
- `review`: auffälliger Ausreißer, der visuell geprüft werden muss.
- `info`: dokumentierte Abweichung ohne unmittelbaren Fehler.

## Korrekturprinzip

Bei Textproblemen in dieser Reihenfolge korrigieren:

1. sprachlich kürzen oder Redundanz entfernen,
2. Informationsarchitektur vereinfachen oder Slide teilen,
3. Box innerhalb des Template-Rasters anpassen,
4. alternatives vorhandenes Layout nutzen,
5. Schriftgröße nur als letzte Option und innerhalb der Template-Range reduzieren.

## Grenzen

- Dieser Skill bewertet nicht allein, ob eine Slide ästhetisch gut wirkt.
- Ein struktureller Pass ersetzt keinen Render-Test.
- Keine eigenmächtigen Brand-Abweichungen zur Fehlerbehebung.

## Abschluss

Abgeschlossen, wenn alle kritischen und major Findings behoben oder explizit begründet sind und ein maschinen-/menschenlesbarer QA-Bericht pro Slide und Objekt vorliegt.
