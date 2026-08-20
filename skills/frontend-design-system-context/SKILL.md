---
name: frontend-design-system-context
description: Erzeugt oder aktualisiert den autoritativen visuellen und interaktiven Projektkontext in DESIGN.md. Nutzt ein bestätigtes PRODUCT.md und analysiert vorhandene Tokens, Komponenten, Screens und Assets als Evidenz; alle offenen visuellen Systementscheidungen werden in einem eigenen fokussierten Grilling bestätigt.
userFacing: false
implicitInvocation: true
category: engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - frontend-product-context
  - round-based-requirements-grilling
outputs:
  - DESIGN.md
  - frontend-design-system-context-handoff.json
lastEvaluated: 2026-08-20
---

# Frontend Design System Context

## Zweck

Dieser Skill verwandelt ein autoritatives `PRODUCT.md`, vorhandene visuelle Repo-Evidenz und bestätigte Gestaltungsentscheidungen in ein autoritatives `DESIGN.md`.

## Voraussetzungen

Ein bestätigtes `PRODUCT.md` muss vorliegen. Unbestätigte persönliche Defaults dürfen nur als Vorschläge/Hypothesen verwendet werden.

## Ablauf

### 1. Visuellen Ist-Zustand analysieren

Prüfe CSS-Variablen/Tokens, Tailwind- oder Theme-Konfiguration, Typografie, Komponenten, Layouts, Screens, Icons, Fotos/Illustrationen, Responsive-Regeln, Fokus-/Fehler-/Loading-Zustände und vorhandene Motion. Trenne konsistente Regeln von Zufällen und Legacy-Abweichungen. **Bestehende Tokens sind Evidenz, nicht automatisch Entscheidung.**

### 2. DESIGN-Grilling eröffnen oder fortsetzen

Route offene Designsystem-Entscheidungen an `round-based-requirements-grilling`. Das Grilling für `DESIGN.md` klärt mindestens:

- Theme und Umgebungs-/Nutzungsszene,
- Farbstrategie, Rollen, Kontrast und Brand-Farbanteil,
- Typografie, Hierarchie und Textbreiten,
- Informationsdichte, Abstände, Raster und Layout-Rhythmus,
- Komponentencharakter und Interaktionsmuster,
- Bildsprache, Fotografie, Illustration und generierte Assets,
- Motion-Energie und erlaubte funktionale Microtransitions,
- Responsive- und Touch-Verhalten,
- relevante Design-Tokens und Designsystem-Grenzen,
- visuelle Accessibility-Regeln zusätzlich zu `PRODUCT.md`.

Repo-Befunde und persönliche Defaults werden als begründete Defaults vorgeschlagen, aber erst durch bestätigte Antworten normativ.

### 3. DESIGN.md schreiben

Schreibe oder ersetze `DESIGN.md` nur nach bestätigtem Grilling-Handoff. Eine bestehende autoritative Fassung bleibt bis dahin gültig.

## DESIGN.md-Vertrag

```markdown
# Design System

## Theme and Scene
...

## Color System
...

## Typography
...

## Density, Spacing and Layout
...

## Components and Interaction
...

## Imagery
...

## Motion
...

## Responsive Behavior
...

## Tokens and System Boundaries
...

## Accessibility
...

## Provenance
...
```

## Änderungskontrolle

Ein Feature-Brief kann einen expliziten lokalen Surface-Override enthalten. Wird daraus eine dauerhafte Systemregel, **neues fokussiertes DESIGN-Grilling** durchführen und erst danach `DESIGN.md` ändern. Feature-Arbeit darf das Dokument nicht stillschweigend mutieren.

## Fehlerbehandlung

Stoppe vor dem Schreiben bei unbestätigten materiellen Konflikten zwischen `PRODUCT.md`, vorhandener Brand-Evidenz und gewünschter visueller Richtung. Technische Tragfähigkeitsfragen werden nicht gestalterisch wegentschieden.

## Abschluss

Abgeschlossen ist der Skill, wenn ein bestätigtes **autoritativen `DESIGN.md`** vorliegt, seine Provenance nachvollziehbar ist und lokale Abweichungen nicht als globale Regeln eingeschmuggelt wurden.
