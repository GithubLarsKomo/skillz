---
name: frontend-product-context
description: Erzeugt oder aktualisiert den autoritativen strategischen Frontend-Projektkontext in PRODUCT.md. Analysiert zuerst Repository-Evidenz und lässt alle nicht bereits bestätigten Produkt-, Zielgruppen-, Register-, Marken- und Accessibility-Entscheidungen anschließend in einem eigenen fokussierten Grilling bestätigen.
---

# Frontend Product Context

## Zweck

Dieser Skill verwandelt Repository-Evidenz plus bestätigte Produktentscheidungen in ein autoritatives `PRODUCT.md`. Er entscheidet Produktfragen nicht selbst.

## Voraussetzungen

Benötigt werden Projektroot, unveränderlicher Repositoryzustand soweit verfügbar und Zugriff auf vorhandene Dokumentation, Oberflächen und Brand-Assets. Persönliche Defaults dürfen nur als Hypothesen aus einem Director-Handoff einfließen.

## Ablauf

### 1. Repository-Evidenz erheben

Prüfe README und Fachdocs, Routen/Seiten, bestehende Copy, Personas, Brand-Unterlagen, Logos, Screens und vorhandenes `PRODUCT.md`. Trenne Fakten, bereits bestätigte Entscheidungen, Hypothesen und offene Fragen. **Repo-Evidenz ersetzt kein Grilling.**

### 2. PRODUCT-Grilling eröffnen oder fortsetzen

Route die offenen fachlichen Entscheidungen an `round-based-requirements-grilling`. Das Grilling für `PRODUCT.md` ist eigenständig und fokussiert auf:

- Register: `brand`, `product` oder begründete Projektstruktur mit primärem Register,
- konkrete Nutzergruppen, Nutzungskontext und Job-to-be-done,
- Produktzweck, gewünschtes Ergebnis und Erfolgskriterien,
- Markenpersönlichkeit, Stimme und gewünschte emotionale Wirkung,
- Anti-Referenzen und ausdrücklich unerwünschte Muster,
- 3–5 strategische Designprinzipien,
- Accessibility- und Inklusionsgrundsätze.

Farben, Fonts, Radien, konkrete Dichte oder Komponentenstil gehören nicht in dieses Grilling; sie werden erst in `frontend-design-system-context` geklärt.

### 3. Nur bestätigte Entscheidungen schreiben

Erzeuge oder ersetze `PRODUCT.md` erst aus einem bestätigten Grilling-Handoff. Ein bestehendes autoritatives `PRODUCT.md` bleibt bis zur Freigabe einer neuen Fassung gültig. Keine stille Aktualisierung aus Repo-Inferenz oder Feature-Arbeit.

## PRODUCT.md-Vertrag

```markdown
# Product

## Register
...

## Users and Context
...

## Product Purpose and Success
...

## Brand Personality and Emotional Goal
...

## Anti-References
...

## Strategic Design Principles
...

## Accessibility and Inclusion
...

## Provenance
...
```

`Provenance` verweist auf Grilling-Handoff und relevante Repo-Evidenz, ohne Chat-Rohdaten zu kopieren.

## Änderungskontrolle

Wenn spätere Feature-Arbeit eine dauerhafte Produktannahme infrage stellt, **neues fokussiertes PRODUCT-Grilling** eröffnen. Ein Surface-Override darf niemals `PRODUCT.md` still umdefinieren.

## Fehlerbehandlung

Stoppe vor dem Schreiben, wenn Register, Nutzer, Zweck oder Accessibility materiell widersprüchlich oder unbestätigt sind. Technische Evidenzfragen, die eine fachliche Entscheidung blockieren, werden über die Grilling-Routingregeln an Wayfinder gegeben.

## Abschluss

Abgeschlossen ist der Skill, wenn ein bestätigtes, nachvollziehbares und **autoritäres `PRODUCT.md`** vorliegt und offene technische oder fachliche Punkte explizit geroutet sind.
