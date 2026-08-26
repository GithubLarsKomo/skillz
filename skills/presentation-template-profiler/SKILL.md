---
name: presentation-template-profiler
description: Analysiert eine vorhandene PowerPoint-Referenz oder ein Corporate-Template und erzeugt ein wiederverwendbares Präsentationsprofil für Master, Layouts, Theme, Typografie, Farben, Platzhalter, Footer, Abstände und wiederkehrende visuelle Regeln. Verwenden, wenn Look & Feel eines bestehenden Templates übernommen werden soll; nicht zum Erfinden eines neuen Brand Designs.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires: []
outputs:
  - presentation-template-profile.json
  - presentation-template-profile.md
lastEvaluated: 2026-08-26
---

# Presentation Template Profiler

Dieser Skill verwandelt eine vorhandene Präsentationsvorlage in ein explizites, überprüfbares Designprofil, das nachgelagerte Presentation-Skills als Source of Truth verwenden können.

## Priorität der Quellen

1. Originale PPTX/POTX-Datei im aktuellen Arbeitskontext.
2. Vom Nutzer bestätigte Referenzpräsentation mit demselben Corporate Design.
3. Dokumentierte Template-Spezifikation.
4. Nur wenn nichts davon verfügbar ist: transparent als `template-compatible fallback` arbeiten.

Ein vorhandenes echtes Template darf nicht durch eine frei erfundene Nachbildung ersetzt werden.

## Zu erfassende Eigenschaften

- Seitenformat und Aspect Ratio.
- Theme Fonts und tatsächlich verwendete Font Families, Weights und Fallbacks.
- Theme Colors, Akzentfarben, Hintergrundfarben und zulässige Kontrastkombinationen.
- Slide Master, Layout-Namen und Platzhaltertypen.
- Titel-, Untertitel-, Body-, Caption-, Quellen- und Footer-Positionen.
- Typische Schriftgrößen und Größenbereiche je Elementtyp.
- Textbox-Margins, Absatzabstände, Bullet-Einzüge und Zeilenabstände.
- Logo-, Footer-, Confidentiality- und Seitennummernlogik.
- Tabellen-, Diagramm-, Timeline-, KPI- und Section-Header-Stile.
- Wiederkehrende grafische Elemente, Flächen, Linien, Icons und Bildmasken.
- Raster, Außenränder, Spaltenlogik, typische Objektabstände und Alignment-Regeln.
- Typische Informationsdichte und Verhältnis von Text zu Visuals.

## Template-Fidelity-Regel

Nachgelagerte Deck-Produktion muss vorhandene Master, Layouts, Platzhalter und Theme-Eigenschaften bevorzugt wiederverwenden. Manuelles Nachbauen ist nur zulässig, wenn das benötigte Layout technisch nicht verfügbar ist. Abweichungen werden explizit dokumentiert.

## Profilformat

Mindestens folgende Felder dokumentieren:

```json
{
  "schemaVersion": 1,
  "source": {"type": "pptx|potx|reference|spec", "templateDerived": true},
  "slideSize": {"aspectRatio": "16:9"},
  "fonts": {},
  "colors": {},
  "layouts": [],
  "typography": {},
  "spacing": {},
  "branding": {},
  "visualPatterns": [],
  "qaBaselines": {},
  "fallbacks": [],
  "warnings": []
}
```

`qaBaselines` soll beobachtete Median-/Bereichswerte für Titel, Body, Quellen, Tabellen und Chart-Labels enthalten, damit spätere QA nicht mit universellen, template-fremden Grenzwerten arbeitet.

## Grenzen

- Keine vertraulichen Inhalte der Referenzpräsentation in das Profil übernehmen, sofern sie nicht für Designregeln erforderlich sind.
- Keine proprietäre PPTX/POTX in ein öffentliches Skill-Repository einchecken.
- Keine Brand-Regeln erfinden, wenn sie aus dem Template nicht ableitbar sind.
- Keine Layoutänderung durchführen; dieser Skill analysiert nur.

## Abschluss

Abgeschlossen, wenn das Profil die wiederverwendbaren Design- und Layoutregeln ausreichend beschreibt, Template-Fidelity von Fallbacks trennt und nachgelagerte Skills ohne implizites Wissen Master, Typografie, Farben, Abstände und QA-Baselines anwenden können.
