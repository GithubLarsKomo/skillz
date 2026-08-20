---
name: frontend-design-review
description: Prüft eine konkrete Frontend-Oberfläche evidenzbasiert gegen autoritatives PRODUCT.md, DESIGN.md und bestätigte Feature-Briefs. Liefert priorisierte UX/UI-, Accessibility-, Responsive-, Copy-, Performance- und Anti-Slop-Findings mit konkreten Empfehlungen, ohne Designsystemregeln oder Produktionscode still zu verändern.
userFacing: false
implicitInvocation: true
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - frontend-product-context
  - frontend-design-system-context
outputs:
  - frontend-design-review.md
  - frontend-design-findings.json
lastEvaluated: 2026-08-20
---

# Frontend Design Review

## Zweck und Grenze

Review bewertet bestehende oder implementierte Frontend-Arbeit. Es trennt normative Verstöße, nachweisbare UX-/Technikprobleme und reine Präferenzverbesserungen. Es ändert weder Code noch `PRODUCT.md`/`DESIGN.md` automatisch.

## Voraussetzungen

Lies `PRODUCT.md`, `DESIGN.md`, vorhandenen bestätigten Feature-Brief und den konkreten Zielzustand: Code, Screenshots oder laufende Oberfläche soweit verfügbar. Fehlt autoritativer Projektkontext, route zuerst zu den Kontext-Skills.

## Review-Achsen

Prüfe zielbezogen:

1. Produktzweck, Nutzeraufgabe und Informationshierarchie.
2. Navigation, Interaktion, Feedback, Fokus und Fehler-/Empty-/Loading-Zustände.
3. Typografie, Lesbarkeit, Textbreite und Hierarchiekontrast.
4. Farbe, Kontrast, Theme und semantische Farbrollen.
5. Informationsdichte, Spacing, Raster, Rhythmus und Responsive-Verhalten.
6. Bilder/Illustrationen als echte Inhaltsrollen statt Dekoration ohne Zweck.
7. Motion auf funktionalen Nutzen, Reduced Motion und unnötige Ablenkung.
8. UX Writing, Verständlichkeit und Terminologiekonsistenz.
9. Accessibility und offensichtliche technische/Performance-Auswirkungen.
10. Einhaltung von `PRODUCT.md`, `DESIGN.md` und bestätigten Surface-Overrides.

## Anti-Slop-Gate

Markiere generische AI-Reflexe ausdrücklich, insbesondere identische Card-Grids, Gradient-Text, dekoratives Glassmorphism, Hero-plus-Metrics-plus-Cards als austauschbare Vorlage, dekorative Seitenstreifen, beliebige Stock-Illustrationen, Modal-first und unnötige Effekte. **AI-Slop-Antipatterns werden nicht schöngeredet.** Ein bestehendes Design wird dennoch evolutionär verbessert und nicht nur zur Demonstration von Originalität neu erfunden.

## Findings

Jedes Finding enthält:

- ID, Kategorie und Priorität `blocking|high|medium|low`,
- konkrete Evidenz/Ort,
- verletzte Autorität oder Heuristik,
- Nutzer-/Produktwirkung,
- kleinste sinnvolle Änderung,
- Verifikationskriterium,
- Kennzeichen `requires-product-regrilling`, `requires-design-regrilling` oder `surface-only`.

Ein Stylingwunsch ohne belegbare Autorität oder Nutzerwirkung wird als Präferenz gekennzeichnet und nicht wie ein Fehler behandelt.

## Änderungskontrolle

Würde eine Empfehlung eine dauerhafte Regel in `PRODUCT.md` oder `DESIGN.md` verändern, route zu einem neuen fokussierten Grilling. **Keine stille Designsystemänderung** aus Review oder Polish.

## Abschluss

Abgeschlossen ist der Review, wenn die Findings priorisiert, evidenzbasiert, gegen die Autoritätsquellen rückverfolgbar und mit verifizierbaren Änderungskriterien versehen sind; Empfehlungen mit globaler Wirkung sind korrekt zum Re-Grilling geroutet.
