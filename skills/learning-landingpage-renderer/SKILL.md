---
name: learning-landingpage-renderer
description: Rendert ein kanonisches Learning-Content-Modell mit Visuals und DESIGN.md als portable responsive Landingpage-Style-HTML mit Key Takeaways, Mental Model, Kapitelstruktur, optionaler SOP und timestamp-verlinkter Source Map. Verwenden für sharebare Lernseiten; nicht zum erneuten fachlichen Autorieren des Inhalts.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - learning-content-design-system
outputs:
  - learning-landingpage
  - learning-landingpage-qa.json
lastEvaluated: 2026-08-28
---

# Learning Landingpage Renderer

## Input

- kanonisches `learning-content-model.json`;
- `learning-design-context.json` / Projekt-`DESIGN.md`;
- SVG-/Bildmanifest(e);
- Video-URL und Timestamp-Map.

Der Renderer verändert keine Claims oder SOP-Klassifikationen.

## Default-Informationsarchitektur

1. Hero: Titel, Quelle, Dauer, Lernziel;
2. `What you will learn`;
3. Key Takeaways;
4. Mental Model / Hauptvisual;
5. Kapitel-/Inhaltsnavigation;
6. `How it works`;
7. optional Procedure/SOP;
8. Critical details / Common mistakes;
9. Beispiele / FAQ / Self-check;
10. Source Map mit Timestamp-Deep-Links;
11. Quellen/Provenance.

Nur vorhandene Module rendern.

## HTML-Vertrag

- semantisches HTML;
- responsive Wide + Narrow;
- keyboard-nutzbare Navigation;
- sichtbare Fokuszustände;
- kein horizontales Clipping;
- Print-Styles für brauchbaren Ausdruck;
- lokale/portable Assets bevorzugt;
- keine zwingende JS-Abhängigkeit für Kerninhalt;
- Progressive Enhancement ist zulässig;
- externe Links eindeutig;
- Deep-Link zu YouTube-Zeitpunkten aus validierten Timestamps;
- Alt-Texte für relevante Bilder;
- SVGs skalieren ohne abgeschnittene Labels.

## Landingpage-Stil

Die Seite darf visuell hochwertig sein, bleibt aber ein Lernartefakt. Keine generische SaaS-Startseite mit dekorativen KPI-Cards. Priorität: Orientierung, Verständnis, Scanbarkeit, Quellenrücksprung.

## QA

Prüfe mindestens:

- Desktop/Wide und Mobile/Narrow;
- alle internen Anker;
- Timestamp-Links;
- Bilder/SVGs;
- Overflow;
- Heading-Hierarchie;
- Kontrast;
- Druckansicht;
- DESIGN.md-Konformität;
- bei Corporate-Kontext zusätzliche Corporate Gates soweit anwendbar.

## Abschluss

Abgeschlossen, wenn `learning-landingpage` portabel funktioniert und `learning-landingpage-qa.json` keine blockierenden Findings enthält.
