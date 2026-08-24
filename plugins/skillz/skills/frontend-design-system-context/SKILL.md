---
name: frontend-design-system-context
description: Erzeugt oder aktualisiert den autoritativen visuellen und interaktiven Projektkontext in DESIGN.md. Nutzt ein bestätigtes PRODUCT.md und analysiert vorhandene Tokens, Komponenten, Screens und Assets als Evidenz; alle offenen visuellen Systementscheidungen werden in einem eigenen fokussierten Grilling bestätigt.
---

# Frontend Design System Context

## Zweck

Dieser Skill verwandelt ein autoritatives `PRODUCT.md`, vorhandene visuelle Repo-Evidenz und bestätigte Gestaltungsentscheidungen in ein autoritatives `DESIGN.md`.

## Voraussetzungen

Ein bestätigtes `PRODUCT.md` muss vorliegen. Unbestätigte persönliche Defaults dürfen nur als Vorschläge/Hypothesen verwendet werden.

## Ablauf

### 1. Visuellen Ist-Zustand analysieren

Prüfe CSS-Variablen/Tokens, Tailwind- oder Theme-Konfiguration, Typografie, Komponenten, Layouts, Screens, Icons, Fotos/Illustrationen, Logo, Favicon, bei Apps vorhandene App-Icons, Responsive-Regeln, Fokus-/Fehler-/Loading-Zustände, sichtbare Copy und vorhandene Motion. Trenne konsistente Regeln von Zufällen und Legacy-Abweichungen. **Bestehende Tokens und Assets sind Evidenz, nicht automatisch Entscheidung.**

Ermittle aus `PRODUCT.md` und Repo-Evidenz außerdem die **2–3 wichtigsten Projekteigenschaften bzw. Value-Propositionen**, die das visuelle System wiedererkennbar transportieren soll. Diese Eigenschaften sind die semantische Grundlage für Branding, Key Visual und Bildsprache.

### 2. DESIGN-Grilling eröffnen oder fortsetzen

Route offene Designsystem-Entscheidungen an `round-based-requirements-grilling`. Das Grilling für `DESIGN.md` klärt mindestens:

- Theme und Umgebungs-/Nutzungsszene,
- die 2–3 wichtigsten Projekteigenschaften/Value-Propositionen, die visuell erkennbar werden sollen,
- Branding-System mit Logo, dazu passend abgeleitetem Favicon und bei Apps einem dazu passenden App-Icon,
- Farbstrategie, Rollen, Kontrast und Brand-Farbanteil **abgeleitet aus Projektkontext, Markencharakter und gewünschter Wirkung**,
- Typografie, Hierarchie und Textbreiten,
- Informationsdichte, Abstände, Raster und Layout-Rhythmus,
- Komponentencharakter und Interaktionsmuster,
- Bildsprache, Fotografie, Illustration, Key Visual und generierte Assets,
- UX Writing, Terminologie, Claims, CTA- und Microcopy-Ton passend zum konkreten Projektkontext,
- Motion-Energie und erlaubte funktionale Microtransitions,
- Responsive- und Touch-Verhalten,
- relevante Design-Tokens und Designsystem-Grenzen,
- visuelle Accessibility-Regeln zusätzlich zu `PRODUCT.md`.

Repo-Befunde und persönliche Defaults werden als begründete Defaults vorgeschlagen, aber erst durch bestätigte Antworten normativ.

### 3. DESIGN.md schreiben

Schreibe oder ersetze `DESIGN.md` nur nach bestätigtem Grilling-Handoff. Eine bestehende autoritative Fassung bleibt bis dahin gültig.

`DESIGN.md` darf nicht als vollständig gelten, solange Branding, Farbherleitung, kontextgebundene Copy-Regeln oder die 2–3 bildlich zu transportierenden Projekteigenschaften fehlen.

## Harte Branding- und Kontextregeln

1. **Logo ist Pflicht.** Jedes Projekt erhält ein zum Zweck, Namen, Publikum und Charakter passendes Logo bzw. eine dokumentierte bestehende Wort-/Bildmarke. Ein generischer Template-Marker genügt nicht.
2. **Favicon muss zur Marke gehören.** Es wird aus demselben visuellen System wie das Logo abgeleitet und verwendet dasselbe prägnante Motiv, dieselbe Geometrie bzw. dieselbe erkennbare Markenlogik. Kein unabhängiges Standard-Favicon.
3. **App-Icon ist bei Apps Pflicht.** Für installierbare Apps/PWAs/mobile oder Desktop-Apps wird ein App-Icon definiert, das Logo und Favicon eindeutig derselben Markenfamilie zuordnet. Es muss auch in kleiner Darstellung funktionieren.
4. **Farbe folgt dem Projekt.** Palette und Akzentfarben werden aus Projektkontext, Markencharakter, Nutzungsszene und gewünschter Wirkung begründet. Beliebige Template-Farben oder ästhetisch isolierte Lieblingsfarben sind kein ausreichender Grund. Kontrast und semantische Rollen bleiben verpflichtend.
5. **Text folgt dem Projektkontext.** Hero-Texte, Überschriften, Labels, CTAs, Beispiele, Empty-/Error-States und sonstige sichtbare Microcopy müssen die tatsächliche Domäne, Zielgruppe und Terminologie des Projekts widerspiegeln. Generische SaaS-/AI-Platzhalter, Lorem ipsum oder austauschbare Claims sind unzulässig, außer sie wurden ausdrücklich als temporäre Entwicklungsmarker angefordert.
6. **Key Visual transportiert Bedeutung.** Das zentrale Bild, Hero-Motiv oder die leitende Illustration muss mindestens **2 der 2–3 priorisierten Projekteigenschaften** grafisch erkennbar transportieren. Reine Dekoration oder beliebige Stock-Ästhetik genügt nicht. `DESIGN.md` benennt explizit, welche Eigenschaften durch welche visuellen Elemente dargestellt werden.
7. **Asset-Familie statt Einzeldateien.** Logo, Favicon, App-Icon, Farbwelt, Key Visual und unterstützende Bildsprache müssen als zusammenhängendes System funktionieren, nicht als unabhängig erzeugte Assets.

## DESIGN.md-Vertrag

```markdown
# Design System

## Theme and Scene
...

## Project Character and Visual Priorities
- Project property / value proposition 1: ...
- Project property / value proposition 2: ...
- Project property / value proposition 3: ... # optional
- Visual translation: ...

## Brand Identity and Assets
### Logo
- Concept and project-context rationale: ...
- Primary mark / wordmark usage: ...

### Favicon
- Derivation from logo: ...
- Small-size simplification: ...

### App Icon
- Required for app/PWA/mobile/desktop surfaces: yes|no
- Derivation from logo/favicon: ...
- Small-size/platform behavior: ...

## Color System
- Project/brand rationale: ...
- Roles, tokens and contrast: ...

## Typography
...

## Density, Spacing and Layout
...

## Components and Interaction
...

## Imagery and Key Visual
- 2–3 project properties to communicate: ...
- Graphic mapping of each property: ...
- Photography/illustration/generation rules: ...
- Decorative imagery limits: ...

## Content and UX Writing
- Domain terminology: ...
- Voice and tone: ...
- Context rules for headings, claims, CTA and microcopy: ...
- Forbidden generic/placeholding patterns: ...

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

## DESIGN.md Acceptance Gate

Ein `DESIGN.md` ist nur akzeptabel, wenn alle folgenden Prüfungen bestanden sind:

- `brand-logo`: Logo vorhanden oder bestehende Marke ausdrücklich dokumentiert und zum Projektkontext begründet.
- `brand-favicon`: Favicon vorhanden/definiert und visuell eindeutig vom Logo-System abgeleitet.
- `brand-app-icon`: bei Apps/PWAs/mobile/desktop ein konsistentes App-Icon vorhanden/definiert; bei reinen Websites explizit `not applicable`.
- `brand-asset-coherence`: Logo, Favicon und App-Icon bilden dieselbe erkennbare Markenfamilie.
- `color-context-fit`: Farbpalette ist fachlich/markenbezogen begründet, semantisch konsistent und ausreichend kontrastreich.
- `copy-context-fit`: sichtbare Texte und UX-Microcopy verwenden Projektterminologie und passen zu Zielgruppe und Nutzungsszene; keine generische Template-Copy.
- `visual-semantic-fit`: 2–3 priorisierte Projekteigenschaften sind dokumentiert und das Key Visual bildet mindestens zwei davon nachvollziehbar ab.
- `system-coherence`: Branding, Farben, Typografie, Bildsprache und UI wirken als ein zusammenhängendes Designsystem.

Fehlt einer der anwendbaren Punkte, ist der Kontext-Schritt **nicht abgeschlossen** und wird vor Implementierung fokussiert nachgeschärft.

## Änderungskontrolle

Ein Feature-Brief kann einen expliziten lokalen Surface-Override enthalten. Wird daraus eine dauerhafte Systemregel, **neues fokussiertes DESIGN-Grilling** durchführen und erst danach `DESIGN.md` ändern. Feature-Arbeit darf das Dokument nicht stillschweigend mutieren.

## Fehlerbehandlung

Stoppe vor dem Schreiben bei unbestätigten materiellen Konflikten zwischen `PRODUCT.md`, vorhandener Brand-Evidenz und gewünschter visueller Richtung. Technische Tragfähigkeitsfragen werden nicht gestalterisch wegentschieden.

Existieren bereits Logo/Favicon/App-Icon, die nicht zusammenpassen, dokumentiere den Konflikt ausdrücklich und kläre, welches Asset die führende Markenquelle ist. Erzeuge nicht stillschweigend eine dritte visuelle Richtung.

## Abschluss

Abgeschlossen ist der Skill, wenn ein bestätigtes **autoritäres `DESIGN.md`** vorliegt, seine Provenance nachvollziehbar ist, das `DESIGN.md Acceptance Gate` vollständig bestanden ist und lokale Abweichungen nicht als globale Regeln eingeschmuggelt wurden.
