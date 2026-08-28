---
name: learning-image-generator
description: Erzeugt aus einem evidenzgebundenen Visual-Plan und dem aktiven DESIGN.md konsistente erklärende Illustrationen oder realistische Lernbilder und kennzeichnet sie eindeutig als illustrative, nicht experimentelle Evidenz. Verwenden wenn räumliche, physische oder konzeptionelle Inhalte von einem Bild profitieren; nicht für textlastige Diagramme, Markenrekonstruktion oder erfundene wissenschaftliche Evidenz.
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
  - learning-image-manifest.json
  - learning-image-assets
lastEvaluated: 2026-08-28
---

# Learning Image Generator

## Zweck

Erzeuge neue Illustrationen/Bilder, wenn ein SVG oder Quellframe die Lernaufgabe nicht besser löst.

## Input

- `learning-visual-plan.json`;
- `learning-design-context.json`;
- evidenzgebundene Beschreibung der dargestellten Elemente;
- Zieloberflächen und Seiten-/Slide-Verhältnis.

## Regeln

- Bildinhalt muss mindestens einen priorisierten Lernclaim transportieren.
- Stil, Perspektive, Hintergründe, Kontrast und Farbwelt folgen DESIGN.md.
- Wiederkehrende Assets einer Serie bilden eine erkennbare visuelle Familie.
- Kritische Labels/Text nicht in das Rasterbild backen, wenn sie besser als SVG/HTML/PPTX-Text darübergelegt werden können.
- Keine vertraulichen Logos, Produktformen oder Markenmerkmale halluzinieren.
- Keine generierte Illustration als Foto des realen Versuchs, Patienten, Gerätezustands oder Messresultats darstellen.

## Evidenzrolle

Jedes generierte Bild ist `illustrative-only`, außer es ist ausdrücklich ein unverändertes/source-provenanced Originalbild. Das Manifest hält fest:

- `visualId`;
- `sourceClaims`;
- `designContract`;
- `generationBrief`;
- `intendedMeaning`;
- `prohibitedInterpretations`;
- `dimensions/aspectRatio`;
- `targetSurfaces`;
- `evidenceRole`.

## Copyright / Quellvideo

Ein Lernbild soll das **Konzept neu visualisieren**, nicht den visuellen Ausdruck des Quellvideos möglichst exakt kopieren. Originalframes bleiben gesondert provenance-geführte Source Assets.

## Qualitätsgate

- semantische Übereinstimmung mit Visual-Plan;
- keine fachlichen Zusatzdetails;
- DESIGN.md-konform;
- keine unlesbaren eingebrannten Texte;
- keine irreführende Evidenzwirkung;
- geeignetes Format/Seitenverhältnis;
- Manifest vollständig.

## Abschluss

Abgeschlossen, wenn Bilder und Manifest als erklärende Assets sicher in HTML, PPTX und DOCX/PDF wiederverwendet werden können.
