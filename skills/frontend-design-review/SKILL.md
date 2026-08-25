---
name: frontend-design-review
description: Prüft eine konkrete Frontend-Oberfläche evidenzbasiert gegen autoritatives PRODUCT.md, DESIGN.md und bestätigte Feature-Briefs. Liefert priorisierte UX/UI-, Accessibility-, Responsive-, Branding-, Copy-, Performance- und Anti-Slop-Findings mit konkreten Empfehlungen, ohne Designsystemregeln oder Produktionscode still zu verändern.
userFacing: false
implicitInvocation: true
version: 0.3.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - frontend-product-context
  - frontend-design-system-context
outputs:
  - frontend-design-review.md
  - frontend-design-findings.json
lastEvaluated: 2026-08-25
---

# Frontend Design Review

## Zweck und Grenze

Review bewertet bestehende oder implementierte Frontend-Arbeit. Es trennt normative Verstöße, nachweisbare UX-/Technikprobleme und reine Präferenzverbesserungen. Es ändert weder Code noch `PRODUCT.md`/`DESIGN.md` automatisch.

## Voraussetzungen

Lies `PRODUCT.md`, `DESIGN.md`, vorhandenen bestätigten Feature-Brief und den konkreten Zielzustand: Code, Screenshots oder laufende Oberfläche soweit verfügbar. Prüfe außerdem vorhandene Corporate-Brand-Quellen (`.ase`, bestätigte Palette-JSONs, Brand-Guides) sowie generierte `brand.css`-/Kontrast-Artefakte, soweit vorhanden. Fehlt autoritativer Projektkontext, route zuerst zu den Kontext-Skills.

## Review-Achsen

Prüfe zielbezogen:

1. Produktzweck, Nutzeraufgabe und Informationshierarchie.
2. **Branding-Kohärenz:** Logo ist projektspezifisch; Favicon ist sichtbar aus demselben Markensystem abgeleitet; bei Apps/PWAs/mobile/desktop ist ein übereinstimmendes App-Icon vorhanden. Prüfe Motiv, Formensprache, Farbwelt und Erkennbarkeit in kleinen Größen.
3. Navigation, Interaktion, Feedback, Fokus und Fehler-/Empty-/Loading-Zustände.
4. Typografie, Lesbarkeit, Textbreite und Hierarchiekontrast.
5. **Corporate-Farbintegrität:** Liegt eine freigegebene Corporate-Palette vor, stimmen die Corporate Tokens exakt mit der autoritativen Quelle überein. Template-/Framework-Farben dürfen keine Brandwerte ersetzt haben. Corporate-, Semantic- und Component-Layer sind getrennt.
6. **Farbkontext und Traceability:** Semantische Rollen passen zu Projektkontext, Marke, Nutzungsszene und gewünschter Wirkung. Abgeleitete Hover-/Surface-/State-Farben sind als Ableitungen dokumentiert und auf Corporate- oder semantische Basistokens rückverfolgbar.
7. **Farb-Accessibility:** Prüfe tatsächlich verwendete Foreground/Background-Paare gegen dokumentierte Kontrast-Evidenz. Ein vorhandener `brand-contrast-report.json` ist Evidenz für Black/White-Paare, ersetzt aber nicht die Prüfung zusätzlicher Kombinationen in der realen UI.
8. Informationsdichte, Spacing, Raster, Rhythmus und Responsive-Verhalten.
9. **Semantische Bildwirkung:** Bilder/Illustrationen erfüllen echte Inhaltsrollen. Das Key Visual muss mindestens zwei der in `DESIGN.md` priorisierten 2–3 Projekteigenschaften/Value-Propositionen grafisch nachvollziehbar transportieren; rein dekorative oder austauschbare Motive werden beanstandet.
10. Motion auf funktionalen Nutzen, Reduced Motion und unnötige Ablenkung.
11. **Kontexttreue Copy:** UX Writing, Claims, Überschriften, Labels, CTAs, Beispiele sowie Empty-/Error-States verwenden Domäne, Zielgruppe und Terminologie des konkreten Projekts. Generische SaaS-/AI-Texte, Lorem ipsum und austauschbare Platzhalter gelten ohne ausdrückliche Freigabe als Finding.
12. Accessibility und offensichtliche technische/Performance-Auswirkungen.
13. Einhaltung von `PRODUCT.md`, `DESIGN.md` und bestätigten Surface-Overrides.

## Verbindliches Brand-and-Context-Gate

Der Review darf nicht mit `pass` enden, wenn einer der anwendbaren Punkte verletzt ist:

- `brand-logo`: kein projektspezifisches oder dokumentiertes bestehendes Logo/Markensystem,
- `brand-favicon`: Favicon fehlt oder wirkt unabhängig vom Logo,
- `brand-app-icon`: bei einer App/PWA/mobile/desktop fehlt ein konsistentes App-Icon,
- `brand-asset-coherence`: Logo, Favicon und App-Icon wirken nicht wie dieselbe Marke,
- `corporate-palette-source`: eine vorhandene freigegebene Corporate-Palette ist in `DESIGN.md` nicht als Quelle/Provenance dokumentiert,
- `corporate-token-integrity`: Corporate-Werte wurden gegenüber der autoritativen Quelle verändert oder durch erfundene Brandfarben ersetzt,
- `derived-color-traceability`: nicht-corporate UI-Farben mit Markenfunktion sind weder als Ableitung noch als explizite semantische Ausnahme nachvollziehbar,
- `color-accessibility`: relevante Foreground/Background-Paare erfüllen das im Designsystem geforderte WCAG-Ziel nicht oder wurden nicht belegt,
- `color-context-fit`: Farbrollen sind beliebig/templatehaft oder widersprechen Projektcharakter bzw. Nutzungsszene,
- `copy-context-fit`: zentrale sichtbare Texte sind generisch, fachlich unpassend oder verwenden nicht die projektspezifische Terminologie,
- `visual-semantic-fit`: die 2–3 visuellen Projektprioritäten sind nicht dokumentiert oder das Key Visual bildet weniger als zwei davon nachvollziehbar ab,
- `system-coherence`: Branding, Farbe, Typografie, Bildsprache und Oberfläche ergeben kein kohärentes Gesamtsystem.

Fehlt die dafür notwendige normative Festlegung in `DESIGN.md`, markiere das Finding als `requires-design-regrilling` statt die Lücke mit einer eigenen Designentscheidung zu füllen. **Corporate-Quellwerte werden im Review nie „optimiert“; eine gewünschte Änderung benötigt eine aktualisierte autoritative Markenquelle.**

## Farb-Evidenz

Bei RGB-Corporate-Paletten kann `frontend-design-system-context/scripts/ase_to_tokens.py` die Source-Werte und Black/White-Kontraste reproduzierbar normalisieren. Review prüft mindestens:

- Anzahl und Namen der übernommenen Corporate-Swatches,
- exakte HEX-Werte der RGB-Corporate-Tokens,
- fehlende oder zusätzliche `--brand-*` Tokens,
- semantische Tokens, die direkt auf beliebige Hex-Werte statt auf dokumentierte Quellen zeigen,
- Derived Colors ohne `derived-from`/Formel/Provenance,
- Text-/Icon-Foregrounds, deren Kontrast die freigegebene Schwelle unterschreitet.

CMYK/LAB/Spot ohne freigegebene sRGB-Repräsentation darf nicht durch eine naive mathematische Näherung als Corporate-Webwert freigegeben werden.

## Anti-Slop-Gate

Markiere generische AI-Reflexe ausdrücklich, insbesondere identische Card-Grids, Gradient-Text, dekoratives Glassmorphism, Hero-plus-Metrics-plus-Cards als austauschbare Vorlage, dekorative Seitenstreifen, beliebige Stock-Illustrationen, Modal-first, generische Produktclaims und unnötige Effekte. **AI-Slop-Antipatterns werden nicht schöngeredet.** Ein bestehendes Design wird dennoch evolutionär verbessert und nicht nur zur Demonstration von Originalität neu erfunden.

## Findings

Jedes Finding enthält:

- ID, Kategorie und Priorität `blocking|high|medium|low`,
- konkrete Evidenz/Ort,
- verletzte Autorität oder Heuristik,
- Nutzer-/Produktwirkung,
- kleinste sinnvolle Änderung,
- Verifikationskriterium,
- Kennzeichen `requires-product-regrilling`, `requires-design-regrilling` oder `surface-only`.

Verstöße gegen das verbindliche Brand-and-Context-Gate sind mindestens `high`; fehlende Pflicht-Assets, manipulierte Corporate-Quellwerte oder eine offensichtlich fremde/generische Markenidentität dürfen `blocking` sein, wenn sie den freigegebenen Zielzustand verhindern.

Ein Stylingwunsch ohne belegbare Autorität oder Nutzerwirkung wird als Präferenz gekennzeichnet und nicht wie ein Fehler behandelt.

## Änderungskontrolle

Würde eine Empfehlung eine dauerhafte Regel in `PRODUCT.md` oder `DESIGN.md` verändern, route zu einem neuen fokussierten Grilling. **Keine stille Designsystemänderung** aus Review oder Polish. Änderungen an Corporate-Quellwerten verlangen zusätzlich eine aktualisierte autoritative Brand-Quelle.

## Abschluss

Abgeschlossen ist der Review, wenn die Findings priorisiert, evidenzbasiert, gegen die Autoritätsquellen rückverfolgbar und mit verifizierbaren Änderungskriterien versehen sind, das Brand-and-Context-Gate einschließlich Corporate-Palette-Integrität soweit anwendbar explizit bewertet wurde und Empfehlungen mit globaler Wirkung korrekt zum Re-Grilling geroutet sind.
