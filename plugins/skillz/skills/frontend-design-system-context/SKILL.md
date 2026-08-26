---
name: frontend-design-system-context
description: Erzeugt oder aktualisiert den autoritativen visuellen und interaktiven Projektkontext in DESIGN.md. Nutzt ein bestätigtes PRODUCT.md und analysiert vorhandene Tokens, Komponenten, Screens und Assets als Evidenz; alle offenen visuellen Systementscheidungen werden in einem eigenen fokussierten Grilling bestätigt.
---

# Frontend Design System Context

## Zweck

Dieser Skill verwandelt `PRODUCT.md`, visuelle Repo-Evidenz und bestätigte Gestaltungsentscheidungen in ein autoritatives `DESIGN.md`.

## Corporate- und Brand-Profile

Freigegebene Corporate-Paletten sind Source of Truth für Brandfarben. Built-in-Profile werden vor Farb-Grilling automatisch aufgelöst. EUROIMMUN verwendet das EUROIMMUN-Profil; Sportprojekte verwenden das verbindliche `sport-performance`-Profil. Bei EUROIMMUN+Sport gewinnt EUROIMMUN.

Für Sportanwendungen ist das Sport-Farbspektrum verbindlich; eine lokale Ersatzpalette ist nicht zulässig. Änderungen am Farbsystem erfordern eine explizite Profilversionsänderung.

## Sport-Produktfamilie

Verwandte Sportprodukte teilen Sport-Performance-Farbwelt, geometrische Disziplin, Strich-/Liniencharakter, Typografie und Icon-Konstruktionslogik, erhalten aber eigenständige Produktzeichen. Logo, Favicon und App-Icon werden aus demselben produktspezifischen Zeichen abgeleitet und bleiben bei 32 px unterscheidbar.

## Verbindliche Sport-Design-Templates

Für Sportanwendungen gilt `references/design-templates/sport-performance-apps.md` als verbindlicher Referenzvertrag.

### Layer A — Impeccable UI Template

Impeccable besitzt Layout und UI-Grammatik: Application Shell, Header/Navigation, Grid, Cards, Typografie, Spacing, Radii, Breakpoints, Informationshierarchie, KPI-/Chart-/Listen-/Form-Strukturen, Responsive-Verhalten und Interaktionsmuster.

Für bestehende Sportanwendungen mit akzeptiertem Impeccable-Stand ist dieser Layer **standardmäßig eingefroren**.

### Layer B — Sport Performance Branding

Sport Performance besitzt ausschließlich:

- kanonische Farben und semantische Farbrollen;
- produktspezifisches Logo/Wordmark;
- Favicon;
- App-/PWA-Icons;
- unterstützte Chart-/Statusfarben;
- Brand-/PWA-Theme-Metadaten.

Branding-, Logo-, Favicon-, App-Icon- oder Palette-Aufträge autorisieren **keine** Änderung an Layout, Komponentengeometrie, Typografie-Skala, Spacing, Navigation, Breakpoints oder Informationshierarchie.

Die bestätigten Referenztypen sind:

- **Sport Athlete Management** für Athlete Management, Training, Adaptation, Readiness und Coaching;
- **Masters Diagnostics** für Sportdiagnostik, Test Review, Messwertinterpretation und longitudinale Analyse.

Neue Sportanwendungen starten von der nächstliegenden Designgrammatik und passen nur fachlich erforderliche Informationsarchitektur/Module an.

Wenn ein Auftrag ausdrücklich **„nur Logos und Farben“** oder sinngleich lautet, bleibt nicht-farbbezogenes CSS/Layout unverändert bzw. verhaltensgleich. Unvermeidbare technische Integrationsänderungen müssen minimal und dokumentiert sein.

## Verbindliche Sportfarben

Navy `#173652`, Dark `#1C2B3A`, Body `#24313E`, Teal `#246F6C`, Bright Teal `#2B8884`, Muted `#6B7785`, Energy `#B54708`, Success `#2E7D32`, Warning `#9A6500`, Critical `#B42318`, Recovery `#6D5BD0`, Border `#D6E0E6`, Surface `#EDF3F6`, Surface Subtle `#F6F8F9`, Warning Surface `#FFF4D6` und White `#FFFFFF` sind kanonische Tokenwerte.

## DESIGN.md Pflichtangaben für Sportapps

`DESIGN.md` dokumentiert:

- Template family: `sport-performance`;
- Template type: `sport-athlete-management`, `masters-diagnostics` oder dokumentierte Ableitung;
- Template reference: `references/design-templates/sport-performance-apps.md`;
- Impeccable UI layer frozen for branding-only changes: `yes`;
- Branding layer scope: colors + product-specific brand assets;
- explizite Redesign-Freigabe, falls Layer A geändert werden soll.

## Acceptance Gate

Ein Sport-Designkontext ist nur akzeptabel, wenn:

- Built-in-Profil korrekt aufgelöst wurde;
- kanonische Sportfarben unverändert sind;
- Logo/Favicon/App-Icon zusammengehören und produktspezifisch unterscheidbar sind;
- Impeccable UI-Layer und Sport-Branding-Layer ausdrücklich getrennt sind;
- Branding-only-Diffs keine nicht-farbbezogenen Layout-/Komponentenregeln verändern;
- ein visueller Spot Check unveränderte Header-Proportionen, Grid/Card-Struktur, Typografie, Spacing und Responsive-Verhalten bestätigt;
- WCAG AA und die Regel „Bedeutung nie nur durch Farbe“ eingehalten werden.

Ein Layout-Redesign benötigt einen separaten expliziten Scope oder eine bestätigte DESIGN-Grilling-Entscheidung. Branding-Arbeit allein reicht nicht als Autorisierung.

## Abschluss

Abgeschlossen ist der Skill, wenn ein autoritatives `DESIGN.md` vorliegt, die Brand-/Template-Provenance dokumentiert ist und bei Sportanwendungen der akzeptierte Impeccable UI-Layer vor unbeabsichtigten Branding-Regressionen geschützt ist.
