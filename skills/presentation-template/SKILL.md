---
name: presentation-template
description: Bereitet den visuellen Handoff für Vorträge vor. Nutzt bevorzugt ein vorhandenes PPTX-Template, kann alternativ ein Referenzdeck in ein Designprofil abstrahieren oder ohne Vorlage ein kontextgerechtes Presentation-Designprofil erzeugen.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - slide-architect
outputs:
  - presentation-design-profile.json
  - presentation-template-mapping.json
lastEvaluated: 2026-08-23
---

# Presentation Template

## Modi

### `template`
Vorhandenes `.pptx` als maßgebliche Gestaltungsvorgabe behandeln. Verfügbare Master/Layouts, Typografie, Farben, Platzhalter, Diagramm-/Bildlogik und Branding erfassen und den Slide-Plan darauf abbilden.

### `reference-deck`
Bei einer vorhandenen Referenzpräsentation wiederkehrende Designprinzipien abstrahieren, ohne inhaltliche Altfolien zu kopieren.

### `design-profile`
Wenn keine Vorlage existiert, ein Designbriefing erzeugen, das Kontext, Publikum und Vortragstyp berücksichtigt.

## Designprofil

Mindestens:

- Präsentationskontext und gewünschte Wirkung
- Typografie-/Hierarchieprinzipien
- Informationsdichte
- bevorzugte Visualtypen
- Datenvisualisierungsprinzipien
- Foto-/Illustrationsstil
- Layout-/Whitespace-Regeln
- Branding-/Accessibility-Anforderungen

## Regeln

- Vorhandenes Corporate Template hat Vorrang, sofern technisch verwendbar.
- Kein erfundenes Corporate Design.
- Keine Dekoration ohne kommunikative Funktion.
- Slide-Plan bleibt semantische Quelle; Template darf Botschaft und Evidenz nicht verzerren.

## Handoff

Output ist für eine nachgelagerte Präsentations-/PPT-Erzeugung bestimmt. Die tatsächliche Dateierzeugung ist nicht Aufgabe dieses Skills.
