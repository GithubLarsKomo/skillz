---
name: learning-svg-generator
description: Erzeugt aus einem evidenzgebundenen Visual-Plan und dem aktiven DESIGN.md skalierbare Diagramme, Prozessgrafiken, Timelines, Matrizen und technische Schematics als saubere SVG-Assets. Verwenden für strukturierte Lernvisuals; nicht zum Erfinden von Daten, Markenassets oder fachlichen Beziehungen.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - learning-visual-planner
  - learning-content-design-system
outputs:
  - learning-svg-manifest.json
  - learning-svg-assets
lastEvaluated: 2026-08-28
---

# Learning SVG Generator

## Zweck

Rendere präzise, formatübergreifend nutzbare Vektorgrafiken aus `learning-visual-plan.json` und `learning-design-context.json`.

## Geeignete Visuals

- Prozess- und Stage-Diagramme;
- Timelines;
- Decision Trees;
- Concept Maps;
- Architektur-/Systemdiagramme;
- Vergleichsmatrizen;
- annotierte technische Schematics;
- einfache Datenvisualisierungen aus explizit vorhandenen Daten.

## SVG-Vertrag

Jedes SVG:

- besitzt `viewBox`;
- bleibt ohne eingebettete proprietäre Fontdatei funktionsfähig;
- hält Text als Text, sofern keine technisch zwingende Ausnahme besteht;
- verwendet DESIGN.md-Farben und semantische Rollen;
- nutzt konsistente Linien, Pfeile, Radien und Abstände;
- enthält sinnvolle `<title>`/`<desc>`-Information, soweit kompatibel;
- vermeidet Clipping bei PPTX-, Browser- und PDF-Rendering;
- nutzt keine externen Remote-Assets ohne explizite Freigabe;
- besitzt ein Manifest mit Quellclaims, Timestampbezug und Zieloberflächen.

## Fachliche Grenze

- Keine Zahl, Beziehung, Reihenfolge oder Komponentenbezeichnung ergänzen, die nicht im Visual-Plan verankert ist.
- Keine Corporate-Logos nachzeichnen.
- Keine experimentellen/scientific figures stilistisch „verbessern“, wenn dadurch Datengeometrie verändert würde.
- Keine Infografik als Beweisquelle darstellen.

## Multi-Format-Prüfung

Vor Freigabe mindestens prüfen:

- Browser-Render;
- Raster-Fallback in praxisnaher Größe;
- Lesbarkeit bei geplanter PPTX-/A4-Nutzung;
- Kontrast und Farbunabhängigkeit kritischer Unterscheidungen;
- keine abgeschnittenen Labels oder Pfeilspitzen.

## Abschluss

Abgeschlossen, wenn Asset(s) und `learning-svg-manifest.json` fachlich fidel, DESIGN.md-konform und auf den vorgesehenen Medien lesbar sind.
