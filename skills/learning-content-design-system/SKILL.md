---
name: learning-content-design-system
description: Bindet Lernartefakte formatübergreifend an einen autoritativen DESIGN.md-Vertrag für HTML, Präsentation, DOCX/PDF, Diagramme, SVGs und generierte Bilder und löst Corporate-/Template-Autorität vor generischen Learning-Defaults auf. Verwenden vor Visual- oder Renderarbeit; nicht zum stillen Erfinden einer Unternehmensmarke.
userFacing: false
implicitInvocation: true
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires: []
outputs:
  - learning-design-context.json
lastEvaluated: 2026-08-28
---

# Learning Content Design System

## Zweck

Dieser Skill stellt sicher, dass **alle Formate und Visualgeneratoren dieselbe Designautorität verwenden**. Die gemeinsame Default-Policy liegt in `docs/learning-content/DESIGN.md`.

Der Skill kann für ein konkretes Projekt einen lokalen `DESIGN.md` materialisieren oder einen vorhandenen `DESIGN.md` validieren. Um die globale Artifact-Ownership im Skill-Graph nicht zu duplizieren, deklariert das Skill-Frontmatter nur `learning-design-context.json` als maschinelle Übergabe.

## Autoritätshierarchie

1. explizit bereitgestelltes, freigegebenes Template/Brand-System für das Zielartefakt;
2. anwendbarer normativer Corporate-Vertrag, insbesondere `docs/corporate/euroimmun/DESIGN.md` für EUROIMMUN-Firmeninhalte;
3. bestätigter projektlokaler `DESIGN.md`;
4. `docs/learning-content/DESIGN.md`;
5. Renderer-Defaults nur für nicht definierte technische Details.

Ein niedrigerer Layer darf einen höheren nicht überschreiben.

## Projekt-DESIGN.md

Wenn ein Projekt noch keinen `DESIGN.md` besitzt, materialisiere einen schlanken Vertrag mit:

- Design-/Brand-Quelle und Provenance;
- Zielgruppen- und Lernkontext;
- Farben und semantische Rollen;
- Typografie;
- Informationsdichte;
- Diagramm-/SVG-Grammatik;
- Bild-/Illustrationssprache;
- Screenshot-/Quellframe-Regeln;
- HTML-Regeln;
- Präsentationsregeln;
- DOCX/PDF-Regeln;
- Accessibility;
- QA-/Render-Gates;
- lokale Overrides mit Begründung.

Keine Unternehmensfarben oder Logos raten.

## `learning-design-context.json`

Dokumentiert mindestens:

- `designContractPath`;
- `authorityChain`;
- `corporateContext`;
- `templateContext`;
- `formatProfiles`;
- `visualRules`;
- `accessibilityRules`;
- `requiredQaGates`;
- `warnings`;
- `status`.

## Corporate-Integration

Bei EUROIMMUN-Inhalten bleibt der bestehende Corporate Design Gate vollständig verbindlich. Learning-Regeln dürfen Storytelling, Diagrammwahl oder didaktische Struktur ergänzen, aber **keine** Brand-, Template-, Footer-, Font-, Classification- oder Render-Regel des Corporate-Vertrags abschwächen.

## Qualitätsgate

- Autorität eindeutig;
- keine konkurrierenden Farb-/Fontquellen;
- Visualgeneratoren verwenden dieselben Tokens;
- alle angeforderten Formate sind abgedeckt;
- Corporate-Gate zusätzlich aktiviert, wenn anwendbar;
- lokale Overrides sind explizit und provenance-gebunden.

## Abschluss

Abgeschlossen, wenn Render- und Visual-Skills `learning-design-context.json` ohne eigene Stilentscheidungen konsumieren können und der verbindliche Projekt-`DESIGN.md`-Status nachvollziehbar ist.
