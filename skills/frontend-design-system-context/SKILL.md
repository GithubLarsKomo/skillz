---
name: frontend-design-system-context
description: Erzeugt oder aktualisiert den autoritativen visuellen und interaktiven Projektkontext in DESIGN.md. Nutzt ein bestätigtes PRODUCT.md und analysiert vorhandene Tokens, Komponenten, Screens und Assets als Evidenz; alle offenen visuellen Systementscheidungen werden in einem eigenen fokussierten Grilling bestätigt.
userFacing: false
implicitInvocation: true
version: 0.6.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - frontend-product-context
  - round-based-requirements-grilling
outputs:
  - DESIGN.md
  - frontend-design-system-context-handoff.json
lastEvaluated: 2026-08-26
---

# Frontend Design System Context

## Zweck

Dieser Skill verwandelt ein autoritatives `PRODUCT.md`, vorhandene visuelle Repo-Evidenz und bestätigte Gestaltungsentscheidungen in ein autoritatives `DESIGN.md`.

## Voraussetzungen

Ein bestätigtes `PRODUCT.md` muss vorliegen. Unbestätigte persönliche Defaults dürfen nur als Vorschläge/Hypothesen verwendet werden.

## Ablauf

### 1. Visuellen Ist-Zustand analysieren

Prüfe CSS-Variablen/Tokens, Tailwind- oder Theme-Konfiguration, Typografie, Komponenten, Layouts, Screens, Icons, Fotos/Illustrationen, Logo, Favicon, bei Apps vorhandene App-Icons, **Corporate-Color-Dateien (`.ase`) oder daraus extrahierte Palette-JSONs**, Responsive-Regeln, Fokus-/Fehler-/Loading-Zustände, sichtbare Copy und vorhandene Motion. Trenne konsistente Regeln von Zufällen und Legacy-Abweichungen. **Bestehende Tokens und Assets sind Evidenz, nicht automatisch Entscheidung.**

Ermittle aus `PRODUCT.md` und Repo-Evidenz außerdem die **2–3 wichtigsten Projekteigenschaften bzw. Value-Propositionen**, die das visuelle System wiedererkennbar transportieren soll. Diese Eigenschaften sind die semantische Grundlage für Branding, Key Visual und Bildsprache.

### 1a. Corporate Palette als autoritative Farbquelle behandeln

Ist eine freigegebene Corporate-Palette vorhanden, ist sie die **Source of Truth für Brandfarben**. `.ase` und ein daraus extrahiertes JSON werden nicht als lose Inspiration behandelt. Erfinde keine alternative Brandfarbe, nur weil ein Framework oder Template eine andere Default-Farbe anbietet.

Für RGB-Paletten kann die maschinenlesbare Ebene mit dem mitgelieferten Tool erzeugt werden:

```bash
python skills/frontend-design-system-context/scripts/ase_to_tokens.py path/to/palette.ase --out-dir design/tokens
# alternativ: bereits extrahiertes ASE-JSON als Input
```

Das Tool erzeugt `brand-palette.json`, `brand.css` und `brand-contrast-report.json`. CMYK-, LAB- oder Spot-Werte werden **nicht naiv in sRGB umgerechnet**.

Die Token-Architektur hat drei strikt getrennte Ebenen:

1. **Corporate / immutable:** exakte freigegebene Markenwerte.
2. **Semantic / project-specific:** bestätigte Rollen wie `--color-primary`, `--color-accent`, `--color-success`.
3. **Component:** konkrete Rollen wie `--button-primary-bg`, `--nav-active` oder `--input-focus`.

Abgeleitete UI-Farben sind erlaubt, wenn sie rückverfolgbar dokumentiert werden; sie sind keine neuen Corporate Colors.

### 1b. Eingebaute Brand-Profile automatisch auflösen

Vor einem Farb-Grilling muss geprüft werden, ob der Projektkontext bereits einem kanonischen Brand-Profil entspricht. Die maschinenlesbaren Profile liegen unter `references/brand-profiles/`.

Es gilt folgende Priorität:

1. Explizite Alias-Auflösung auf ein eingebautes Profil wird respektiert.
2. **EUROIMMUN-Kontext** lädt automatisch `brand-profiles/euroimmun.json`; die Corporate-Werte sind autoritativ und unveränderlich.
3. **Sport-Kontext** lädt automatisch `brand-profiles/sport-performance.json`; für Sportanwendungen ist dieses Profil verbindlicher Standard.
4. Ein beliebiger lokaler Brand-Name darf die verbindliche Sport-Palette nicht unterdrücken. Nur ein höher priorisiertes autoritatives Corporate-Profil darf sie ersetzen.
5. Nur wenn kein eingebautes Profil und keine freigegebene Projektpalette greift, wird die Farbquelle im DESIGN-Grilling geklärt.

Bei Überschneidung **EUROIMMUN + Sport** gewinnt das EUROIMMUN-Corporate-Profil.

Ist ein Profil automatisch aufgelöst, werden Palette und semantische Defaults nicht erneut als offene Farbentscheidung gegrillt. Eine Änderung des Sport-Farbspektrums erfordert eine explizite Versionsänderung des kanonischen `sport-performance`-Profils.

### 1c. Sport-Produktfamilie als gemeinsame Markenlogik behandeln

Sportanwendungen teilen Palette, geometrische Disziplin, Strich-/Liniencharakter, Typografie und Icon-Konstruktionslogik. Sie dürfen jedoch **nicht dasselbe Produktzeichen** verwenden.

Für verwandte Sportprodukte gilt:

- gemeinsame Sport-Performance-Farbwelt und visuelle Grammatik;
- je Produkt ein eigenständiges Markenzeichen, das mindestens zwei der 2–3 priorisierten Projekteigenschaften grafisch widerspiegelt;
- Logo, Favicon und App-Icon werden aus demselben Produktzeichen abgeleitet;
- Produktzeichen bleiben auch bei 32 px unterscheidbar;
- Differenzierung erfolgt durch Motiv, Geometrie und Hierarchie, nicht durch neue Farbsysteme.

### 1d. Sport-Design-Templates und Branding-Layer strikt trennen

Für Sportanwendungen gilt zusätzlich der verbindliche Referenzvertrag `references/design-templates/sport-performance-apps.md`.

**Layer A — Impeccable UI Template** besitzt Layout und UI-Grammatik: Application Shell, Header/Navigation, Grid, Cards, Typografie, Spacing, Radii, Breakpoints, Informationshierarchie, KPI-/Chart-/Listen-/Form-Strukturen, Responsive-Verhalten und Interaktionsmuster.

**Layer B — Sport Performance Branding** besitzt ausschließlich die kanonischen Farben/semantischen Farbrollen sowie produktspezifische Logo-, Wordmark-, Favicon-, App-Icon- und PWA-Theme-Assets.

Für eine bestehende Sportanwendung mit bestätigtem Impeccable-Stand ist Layer A **standardmäßig eingefroren**. Ein Auftrag zu Palette, Branding, Logo, Favicon oder App-Icon autorisiert **keine** Änderung an Layout, Komponentengeometrie, Typografie-Skala, Spacing, Navigation, Breakpoints oder Informationshierarchie.

Die bestätigten Referenztypen sind:

- **Sport Athlete Management:** Template für Athlete Management, Training, Adaptation, Readiness und Coaching.
- **Masters Diagnostics:** Template für Sportdiagnostik, Test Review, Messwertinterpretation und longitudinale Analyse.

Neue Sportanwendungen starten von der nächstliegenden Designgrammatik, passen aber Informationsarchitektur und Fachmodule an ihren tatsächlichen Zweck an. Sie übernehmen nicht blind fachfremde Screens.

Wenn ein Auftrag ausdrücklich **„nur Logos und Farben“** oder sinngleich lautet, ist dies wörtlich zu behandeln: Nicht-farbbezogenes CSS/Layout bleibt unverändert bzw. verhaltensgleich; minimale technische Integrationsänderungen müssen dokumentiert werden.

### 2. DESIGN-Grilling eröffnen oder fortsetzen

Route offene Designsystem-Entscheidungen an `round-based-requirements-grilling`. Das Grilling klärt mindestens Theme/Nutzungsszene, visuelle Prioritäten, Branding-System, Farbquelle, semantische Rollen, Typografie, Dichte, Layout, Komponenten, Bildsprache, UX Writing, Motion, Responsive-Verhalten und Accessibility.

Bei Sportanwendungen gilt: Ein bereits bestätigtes Impeccable-Template wird nicht erneut als offene Branding-Entscheidung behandelt. Nur ein expliziter Redesign-Auftrag oder ein bestätigtes DESIGN-Grilling darf Layer A verändern.

Repo-Befunde und persönliche Defaults werden als begründete Defaults vorgeschlagen, aber erst durch bestätigte Antworten normativ. **Die Werte einer ausdrücklich freigegebenen Corporate-Palette oder eines automatisch aufgelösten kanonischen Brand-Profils werden nicht neu gegrillt. Für Sportanwendungen ist das `sport-performance`-Farbspektrum verbindlich.**

### 3. DESIGN.md schreiben

Schreibe oder ersetze `DESIGN.md` nur nach bestätigtem Grilling-Handoff. Eine bestehende autoritative Fassung bleibt bis dahin gültig.

`DESIGN.md` darf nicht als vollständig gelten, solange Branding, Farbherleitung, Brand-Profil-Provenance, kontextgebundene Copy-Regeln oder die 2–3 bildlich zu transportierenden Projekteigenschaften fehlen. Bei Sportanwendungen dokumentiert `DESIGN.md` zusätzlich den verwendeten Sport-Template-Typ und die Layer-Grenze zwischen Impeccable UI und Sport Performance Branding.

## Harte Branding- und Kontextregeln

1. **Logo ist Pflicht.** Jedes Projekt erhält ein kontextpassendes Logo bzw. eine dokumentierte bestehende Wort-/Bildmarke.
2. **Favicon muss zur Marke gehören.** Kein unabhängiges Standard-Favicon.
3. **App-Icon ist bei Apps Pflicht.** Es wird aus derselben Markenfamilie abgeleitet.
4. **Corporate-Farben sind unveränderlich.** Framework-/Template-Farben dürfen keine Brandfarben ersetzen.
5. **Built-in-Profile sind normative Standards.** EUROIMMUN-Projekte verwenden EUROIMMUN; Sport-Projekte Sport Performance; bei EUROIMMUN+Sport gilt EUROIMMUN.
6. **Sport-Farbspektrum ist verbindlich.** Navy `#173652`, Dark `#1C2B3A`, Body `#24313E`, Teal `#246F6C`, Bright Teal `#2B8884`, Muted `#6B7785`, Energy `#B54708`, Success `#2E7D32`, Warning `#9A6500`, Critical `#B42318`, Recovery `#6D5BD0`, Border `#D6E0E6`, Surface `#EDF3F6`, Surface Subtle `#F6F8F9`, Warning Surface `#FFF4D6` und White `#FFFFFF` sind kanonisch.
7. **Farbe folgt dem Projekt innerhalb des verbindlichen Systems.** Kontrast und semantische Rollen bleiben verpflichtend.
8. **Sport-Produkte sind verwandt, aber individuell.** Gemeinsame Palette und Designgrammatik, eigenständige Produktzeichen.
9. **Sport-Branding überschreibt kein Impeccable-Layout.** Branding-only-Arbeit darf nur Farb-Tokens/semantische Farbrollen und Markenassets verändern. Änderungen an Layout, Spacing, Typografie, Komponentengeometrie, Navigation, Breakpoints oder Informationshierarchie benötigen einen expliziten Redesign-Scope.
10. **Sport-Templates sind verbindlich.** Bestehende akzeptierte Sport Athlete Management- und Masters Diagnostics-Oberflächen sind Referenzzustände. Neue Sportapps starten von der nächstliegenden Designgrammatik aus `references/design-templates/sport-performance-apps.md`.
11. **Text folgt dem Projektkontext.** Keine generische Template-Copy.
12. **Key Visual transportiert Bedeutung.** Mindestens zwei priorisierte Projekteigenschaften müssen visuell erkennbar sein.
13. **Asset-Familie statt Einzeldateien.** Logo, Favicon, App-Icon, Farbwelt und Bildsprache funktionieren als System.

## DESIGN.md-Vertrag

```markdown
# Design System

## Theme and Scene
...

## Project Character and Visual Priorities
...

## Brand Identity and Assets
...

## Sport Template Contract # if Sport application
- Template family: sport-performance
- Template type: sport-athlete-management | masters-diagnostics | derived-new-sport-app
- Template reference: Skillz `references/design-templates/sport-performance-apps.md`
- Impeccable UI layer frozen for branding-only changes: yes
- Branding layer scope: colors + product-specific brand assets
- Explicit layout-redesign approval: no|yes + provenance

## Color System
- Built-in profile ID/version: ...
- Canonical tokens: ...
- Semantic mapping: ...
- Derived-color traceability: ...

## Typography
...

## Density, Spacing and Layout
...

## Components and Interaction
...

## Imagery and Key Visual
...

## Content and UX Writing
...

## Motion
...

## Responsive Behavior
...

## Accessibility
...

## Provenance
...
```

## DESIGN.md Acceptance Gate

Ein `DESIGN.md` ist nur akzeptabel, wenn alle anwendbaren Prüfungen bestanden sind:

- `brand-logo`, `brand-favicon`, `brand-app-icon`, `brand-asset-coherence`;
- `brand-product-distinction` für verwandte Sportprodukte;
- `brand-profile-resolution` und `sport-palette-binding`;
- `corporate-token-integrity`, `derived-color-traceability`, `color-accessibility`;
- `copy-context-fit`, `visual-semantic-fit`, `system-coherence`;
- **`sport-template-selection`:** Sportprojekt ist einem Referenztemplate oder einer dokumentierten Ableitung zugeordnet;
- **`sport-template-layer-separation`:** Impeccable UI-Layer und Sport-Branding-Layer sind explizit getrennt;
- **`sport-branding-no-layout-regression`:** Branding-only-Diffs verändern keine nicht-farbbezogenen Layout-/Komponentenregeln;
- **`sport-template-visual-regression`:** Spot Check bestätigt unveränderte Header-Proportionen, Grid/Card-Struktur, Typografie, Spacing und Responsive-Verhalten, außer ein Redesign wurde ausdrücklich freigegeben.

Fehlt einer der anwendbaren Punkte, ist der Kontext-Schritt **nicht abgeschlossen**.

## Änderungskontrolle

Ein Feature-Brief kann einen expliziten lokalen Surface-Override enthalten. Wird daraus eine dauerhafte Systemregel, neues fokussiertes DESIGN-Grilling durchführen und erst danach `DESIGN.md` ändern.

Eine Änderung des Sport-Standardprofils benötigt eine explizite Profilversionsänderung und Regressionstests. **Eine Branding-/Logo-/Palette-Änderung darf den akzeptierten Impeccable UI-Layer nicht mitändern.** Ein Layout-Redesign ist ein eigener Scope und muss ausdrücklich beauftragt oder bestätigt werden.

## Fehlerbehandlung

Stoppe bei unbestätigten materiellen Konflikten zwischen `PRODUCT.md`, Brand-Evidenz, Template-Vertrag und gewünschter visueller Richtung. Existieren mehrere widersprüchliche Corporate-Paletten, kläre die führende Quelle. Existieren Logo/Favicon/App-Icon mit widersprüchlicher Markenlogik, kläre die führende Markenquelle statt eine dritte Richtung zu erzeugen.

## Abschluss

Abgeschlossen ist der Skill, wenn ein bestätigtes autoritäres `DESIGN.md` vorliegt, seine Provenance nachvollziehbar ist, das Acceptance Gate vollständig bestanden ist und bei Sportanwendungen Template-Layer und Branding-Layer sauber getrennt sind.
