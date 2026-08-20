---
name: frontend-design-director
description: Orchestriert Frontend-Designarbeit für Websites, Landingpages, Apps und Dashboards aus autoritativem PRODUCT.md und DESIGN.md, persönlichem Designprofil, featurebezogenem Shaping und evidenzbasiertem Review. Verwenden für Design, Redesign, UX/UI-Verbesserung, Kritik, Audit oder Polish; nicht für reine Backend-Arbeit.
---

# Frontend Design Director

## Zweck und Grenze

Dieser Skill ist die einzige primäre Eintrittsstelle der Frontend-Design-Familie. Er koordiniert Kontext, Shaping und Review, dupliziert deren Fachlogik aber nicht und schreibt nicht ungefragt Produktionscode.

## Autoritätshierarchie

Für jede Entscheidung gilt, in dieser Reihenfolge:

1. **PRODUCT.md und DESIGN.md sind autoritativ.**
2. Ein bestätigter, explizit abgegrenzter Feature-Brief darf lokale Surface-Overrides enthalten.
3. Persönliche Design-Defaults sind Hypothesen und Vorschläge, keine Gebote.
4. Allgemeine Impeccable-inspirierte Heuristiken füllen nur verbleibende Lücken.

Accessibility, technische Korrektheit und explizite Sicherheitsgrenzen dürfen durch keine Stilpräferenz abgeschwächt werden.

## Routing

### 1. Projektkontext zuerst

Vor substanzieller Designarbeit prüfe Repository, README/Dokumentation, vorhandene Oberflächen, Komponenten, CSS/Tokens, Bilder, Logos und bestehende Designregeln. Fehlt ein bestätigtes `PRODUCT.md`, route zu `frontend-product-context`. Fehlt danach ein bestätigtes `DESIGN.md`, route zu `frontend-design-system-context`.

Repo-Evidenz darf Fragen vorbefüllen und Hypothesen begründen, ersetzt aber niemals das jeweils erforderliche Grilling.

### 2. Aufgabe klassifizieren

- Neue oder wesentlich veränderte Surface/Feature → `frontend-design-shaping`.
- Kritik, Audit, Polish oder Qualitätsprüfung → `frontend-design-review`.
- Technische Tragfähigkeits- oder Architekturunsicherheit → `large-work-wayfinder` über den zuständigen Fach-Skill.
- Neue fachliche oder gestalterische Entscheidung → `round-based-requirements-grilling` über den zuständigen Kontext- oder Shaping-Skill.

### 3. Persönliche Defaults anwenden

Lade `references/personal-design-defaults.md`. Reiche nur die zur Aufgabe passenden Defaults als ausdrücklich überschreibbare Hypothesen weiter. Nie eine projektbezogene Entscheidung automatisch zum globalen Geschmack erklären.

### 4. Lernen ohne Projektleckage

Wiederholte oder ausdrücklich als dauerhaft bezeichnete Nutzerbewertungen dürfen als Kandidaten an `communication-memory-governance` übergeben werden. Eine einzelne Auswahl wie „Variante 2“ bleibt projektbezogen, solange keine langlebige Präferenz bestätigt ist.

## Harte Design-Qualitätsgrenzen

AI-Slop-Antipatterns werden nicht als bequeme Defaults akzeptiert: generische identische Card-Grids, dekoratives Glassmorphism, Gradient-Text, austauschbare Stock-Illustrationen, Hero-plus-Metrics-plus-Cards als Reflex, dekorative Seitenstreifen und Modal-first ohne begründeten UX-Bedarf. Eine bestehende Oberfläche wird evolutionär verbessert statt ohne Auftrag neu erfunden.

## Handoff

Erzeuge bei Routing einen kompakten Stand mit Ziel, Register/Surface, Pfaden zu `PRODUCT.md` und `DESIGN.md`, geltenden Overrides, einschlägigen persönlichen Default-Hypothesen, offenen Entscheidungen und genau dem nächsten Skill.

## Herkunft und Lizenz

Die Designmethodik ist in eigenen Formulierungen von Prinzipien aus `pbakaus/impeccable` und dem Hermes-Port `DevvGwardo/impeccable` inspiriert. Impeccable steht unter Apache License 2.0. Harness-spezifische Hooks, CLI-Installationslogik und Provider-Transformer werden in v1 nicht übernommen. Details stehen in `references/impeccable-provenance.md`.

## Abschluss

Abgeschlossen ist der Director-Schritt, wenn **Autoritätshierarchie**, Projektkontext und Aufgabe eindeutig geroutet sind und genau ein nächster Fach-Skill oder Engineering-Handoff feststeht.
