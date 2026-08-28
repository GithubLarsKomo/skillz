---
name: presentation-layout-qa
description: Prüft PowerPoint-Folien strukturell und kompositorisch auf Text-/Box-Overflow, Objektüberlagerungen, Slide-Grenzen, Footer-/Quellenkollisionen, Font-Ausreißer, Bild-/Chart-/Tabellenfehler sowie objektivierbare visuelle Qualitätsmängel wie überdimensionierte Container, schlechte Information-to-Space-Ratio, schwache Leserichtung und untergewichtete Schlussfolgerungen. Verwenden als Layout-QA vor finalem Rendering; ergänzt, aber ersetzt nicht den vollständigen visuellen Render-Review.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.2.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - presentation-template-profiler
outputs:
  - presentation-layout-qa.json
  - presentation-layout-qa.md
lastEvaluated: 2026-08-28
---

# Presentation Layout QA

Dieser Skill prüft ein Deck auf objekt-, geometrie- und kompositionsbasierte Layoutfehler. Template-spezifische Baselines haben Vorrang vor universellen Grenzwerten. Ein technisch kollisionsfreies Deck ist **nicht automatisch** layoutseitig akzeptabel.

## Inputs

- PPTX/POTX oder editierbares Deck.
- `presentation-template-profile.json`, sofern verfügbar.
- optional bekannte Render- oder Exportwarnungen.
- bei Corporate Decks: aktiver Design-/Storytelling-Contract und bestätigte visuelle Referenz.

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
- Inkonsistente Titel-, Inhalts-, Quellen- und Footer-Positionen.
- Alignment- und Spacing-Ausreißer.
- Platzhalter, die ohne Not durch freie Textboxen ersetzt wurden.

### Visuals

- verzerrte Bilder oder Logos.
- abgeschnittene Chart-Labels, Legends oder Axis Titles.
- Tabellenüberlauf, zu enge Zeilen/Höhen oder unlesbare Zelltexte.
- Footer-, Quellen- oder Branding-Kollisionen.

### Komposition und Informationsarchitektur

Diese Klasse ist verpflichtend. Die folgenden Mängel dürfen nicht als reine Geschmackssache abgetan werden, wenn sie die Wahrnehmung oder Leserichtung objektiv schwächen:

#### Excessive container area

Flaggen, wenn große Cards/Container deutlich mehr leere Fläche als inhaltlich benötigte Fläche beanspruchen und dadurch die Container statt der Botschaft dominieren.

**Major**, wenn:
- mehrere große leere Container die visuelle Hauptwirkung bestimmen;
- Text in einem kleinen oberen Bereich zusammengedrängt wird, während derselbe Container überwiegend leer bleibt;
- eine einfachere Prozess-, Listen- oder Statement-Struktur mit weniger Fläche dieselbe Information klarer tragen würde.

#### Poor information-to-space ratio

Bewerten, ob Inhalt und belegte Fläche sinnvoll korrespondieren. Viel Weißraum ist erwünscht, aber **toter Raum innerhalb dominanter UI-/Card-Elemente** ist kein hochwertiger Weißraum.

**Major**, wenn die Folie gleichzeitig leer und gedrängt wirkt: z. B. sehr große Boxen, aber kleine eng gesetzte Bullet-Texte.

#### Weak visual progression / reading path

Prüfen, ob die beabsichtigte Reihenfolge ohne Sprechererklärung erkennbar ist.

**Major**, wenn:
- parallele Elemente eigentlich eine Ursache→Interpretation→Entscheidung/Gate-Logik ausdrücken sollen, aber nur als gleichrangige Container nebeneinander stehen;
- Pfeile/Nummern/Positionen die Leserichtung nicht unterstützen oder widersprüchlich sind;
- das Auge nicht erkennt, welcher Block zuerst und welcher zuletzt gelesen werden soll.

#### Insufficient conclusion dominance

Eine Folie mit einer expliziten Schlussfolgerung, Entscheidung oder Management-Implikation muss diese visuell ausreichend gewichten.

**Major**, wenn:
- die Conclusion kleiner/schwächer als unterstützende Container ist;
- die wichtigste Aussage in einer schmalen Restzone am unteren Rand steht;
- die Schlussfolgerung durch Source/Footer, Karten oder Dekoration visuell verdrängt wird.

Bei Management-/Board-Folien sollte die zentrale Implikation typischerweise innerhalb weniger Sekunden erfassbar sein.

#### Undersized or unsafe source text

Quellen müssen in einer eigenen Safe-Zone oberhalb des Corporate Footers liegen und bei 100%-Ansicht bzw. normalem Präsentationsrender lesbar bleiben.

**Major**, wenn:
- Source Text mit Footer/Branding konkurriert oder kollidiert;
- die Schrift technisch vorhanden, praktisch aber nicht lesbar ist;
- Quellenzeilen in einen Conclusion-Balken oder andere semantische Zonen hineinragen.

#### Redundant visual systems

Prüfen, ob gleichzeitig zu viele unabhängige Signaletiken eingesetzt werden, z. B. Category Tag + zweiter Badge + Card-Icon + zusätzliche Micro-Icons.

**Major**, wenn additive Dekoration die Hierarchie schwächt oder mehrere konkurrierende Orientierungssysteme erzeugt.

## Baseline-Logik

Keine starre globale Mindestschriftgröße behaupten, wenn das Template andere gültige Werte vorgibt. Stattdessen beobachtete Werte aus `presentation-template-profile.json` verwenden, z. B. Median und typische Range für Titel, Body, Quelle, Tabellen und Chart-Labels.

Für Kompositionsmetriken gilt ebenfalls die Referenzlogik: bei einem bestätigten Corporate-Storytelling-Deck dessen typische Card-Dichte, Weißraum, Conclusion-Gewichtung und Safe-Zones als qualitative Baseline verwenden.

Beispiel:

```json
{
  "slide": 9,
  "finding": "excessive-container-area",
  "severity": "major",
  "evidence": "three containers occupy most of content area while text uses only upper third",
  "recommendedAction": "recompose as three-step narrative chain with dominant conclusion"
}
```

## Schweregrade

- `critical`: Inhalt abgeschnitten, nicht sichtbar oder objektiv fehlerhaft.
- `major`: deutliche Template-/Kompositionsabweichung, Lesbarkeitsrisiko oder geschwächte Informationshierarchie.
- `review`: auffälliger Ausreißer, der visuell geprüft werden muss.
- `info`: dokumentierte Abweichung ohne unmittelbaren Fehler.

## Korrekturprinzip

Bei Text- oder Kompositionsproblemen in dieser Reihenfolge korrigieren:

1. sprachlich kürzen oder Redundanz entfernen,
2. Informationsarchitektur vereinfachen oder Slide teilen,
3. Leserichtung und dominante Botschaft neu komponieren,
4. überdimensionierte Container entfernen/verkleinern,
5. Conclusion/Decision sichtbar priorisieren,
6. Box innerhalb des Template-Rasters anpassen,
7. alternatives vorhandenes Layout nutzen,
8. Schriftgröße nur als letzte Option und innerhalb der Template-Range reduzieren.

**Nicht zulässig:** bestehende Folie lediglich mit zusätzlichen Icons/Badges dekorieren, wenn das zugrunde liegende Layoutproblem Informationsarchitektur oder Flächennutzung betrifft.

## Render-Kopplung

Dieser Skill endet nicht bei geometrischer Analyse. Jede als `major` oder `critical` korrigierte Folie MUSS anschließend gerendert und in voller Größe visuell geprüft werden. Bei Corporate Decks zusätzlich Kernfolien als Montage prüfen, um Dichte, Rhythmus und Style Coherence deckweit zu bewerten.

## Grenzen

- Der Skill bewertet keine freie ästhetische Vorliebe ohne nachvollziehbare Layoutwirkung.
- Er bewertet jedoch objektivierbare visuelle Qualität: Hierarchie, Flächennutzung, Leserichtung, Conclusion-Gewichtung und Safe-Zones.
- Ein struktureller Pass ersetzt keinen Render-Test.
- Keine eigenmächtigen Brand-Abweichungen zur Fehlerbehebung.

## Abschluss

Abgeschlossen, wenn alle `critical` und `major` Findings behoben oder explizit begründet sind, jede geänderte Folie gerendert wurde und ein maschinen-/menschenlesbarer QA-Bericht pro Slide und Finding vorliegt. Ein Deck mit kollisionsfreien, aber kompositorisch schwachen Folien darf nicht als Layout-QA-PASS ausgegeben werden.
