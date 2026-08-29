---
name: frontend-product-context
description: Erzeugt oder aktualisiert den autoritativen strategischen Frontend-Projektkontext in PRODUCT.md. Analysiert zuerst Repository-Evidenz und lässt alle nicht bereits bestätigten Produkt-, Zielgruppen-, Register-, Marken-, Accessibility- und für öffentliche Deployments relevanten Legal-Baseline-Entscheidungen anschließend in einem eigenen fokussierten Grilling bestätigen.
---

# Frontend Product Context

## Zweck

Dieser Skill verwandelt Repository-Evidenz plus bestätigte Produktentscheidungen in ein autoritatives `PRODUCT.md`. Er entscheidet Produktfragen nicht selbst.

## Voraussetzungen

Benötigt werden Projektroot, unveränderlicher Repositoryzustand soweit verfügbar und Zugriff auf vorhandene Dokumentation, Oberflächen und Brand-Assets. Persönliche Defaults dürfen nur als Hypothesen aus einem Director-Handoff einfließen.

## Ablauf

### 1. Repository-Evidenz erheben

Prüfe README und Fachdocs, Routen/Seiten, bestehende Copy, Personas, Brand-Unterlagen, Logos, Screens und vorhandenes `PRODUCT.md`. Trenne Fakten, bereits bestätigte Entscheidungen, Hypothesen und offene Fragen. **Repo-Evidenz ersetzt kein Grilling.**

Für öffentlich deploybare Apps/PWAs/Websites prüfe zusätzlich, ob bereits eine belastbare Legal-Baseline existiert: Betreiberidentität, Impressum, Datenschutzhinweise, Hosting-/Datenflussbeschreibung, öffentliche Erreichbarkeit der Legal-Seiten und vorhandene Deployment-/Acceptance-Checks.

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

### 3. Public-Deployment-Legal-Baseline für öffentliche Produkte

Wenn das Produkt öffentlich im Web bereitgestellt wird oder werden soll, muss vor Production Release zusätzlich eine projektbezogene Legal-Baseline existieren. Als Referenzmuster gilt `docs/templates/public-web-app-legal-baseline.md`.

Mindestens zu erfassen und zu verifizieren sind:

- Betreibername, ladungsfähige Anschrift, überwachte Kontaktadresse,
- Rechtsform/Registerangaben nur wenn tatsächlich anwendbar,
- öffentlich erreichbares `Impressum` und `Datenschutz`/`Datenschutzhinweise`,
- Hostinganbieter und relevante technische Dienstleister,
- tatsächliche Server-/Proxy-/Container-Logging-Konfiguration und belegbare Retention-Kriterien,
- lokale Speicherung, Accounts, Cloud-Sync, Analytics, Telemetrie, Drittanbieter-Embeds, Cookies und sonstige Datenflüsse,
- Backup-, Monitoring-, CDN-, DNS-, Error-Reporting- oder sonstige Empfänger, sofern relevant,
- direkte URL-Erreichbarkeit und ein Link aus dem öffentlichen App-Chrome in höchstens einer Interaktion,
- Aktualisierungspflicht vor Einführung neuer nicht-technisch-erforderlicher Datenflüsse.

**Keine Infrastruktur- oder Retention-Angabe darf aus einem Template ungeprüft übernommen werden.** Ein anderer Projektstand ist nur Referenz, keine Evidenz. Betreiber-Platzhalter dürfen nie in einem öffentlichen Release verbleiben.

Die Legal-Baseline ist ein Engineering-/Release-Completeness-Gate und ersetzt keine anwaltliche Rechtsberatung.

### 4. Nur bestätigte Entscheidungen schreiben

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

## Public Deployment and Legal Baseline
- public deployment: yes|no|planned
- legal baseline artifact: ...
- unresolved release blockers: ...

## Provenance
...
```

`Provenance` verweist auf Grilling-Handoff und relevante Repo-Evidenz, ohne Chat-Rohdaten zu kopieren. Bei nicht öffentlichen Produkten kann der Legal-Abschnitt kurz als `not applicable` dokumentiert werden.

## Änderungskontrolle

Wenn spätere Feature-Arbeit eine dauerhafte Produktannahme infrage stellt, **neues fokussiertes PRODUCT-Grilling** eröffnen. Ein Surface-Override darf niemals `PRODUCT.md` still umdefinieren.

Wenn Hosting, Accounts, Cloud-Sync, Analytics, Telemetrie, Tracking, Drittanbieter-Embeds oder sonstige Datenflüsse geändert werden, muss die Public-Deployment-Legal-Baseline vor Release erneut geprüft werden.

## Fehlerbehandlung

Stoppe vor dem Schreiben, wenn Register, Nutzer, Zweck oder Accessibility materiell widersprüchlich oder unbestätigt sind. Technische Evidenzfragen, die eine fachliche Entscheidung blockieren, werden über die Grilling-Routingregeln an Wayfinder gegeben.

Ein öffentlicher Release darf nicht als vollständig gelten, wenn Betreiberidentität ungeklärt ist, Legal-Seiten fehlen, Platzhalter enthalten oder Datenfluss-/Hosting-Angaben nicht gegen den tatsächlichen Deploymentzustand geprüft wurden.

## Abschluss

Abgeschlossen ist der Skill, wenn ein bestätigtes, nachvollziehbares und **autoritäres `PRODUCT.md`** vorliegt, offene technische oder fachliche Punkte explizit geroutet sind und bei öffentlichen Produkten eine projektbezogene Legal-Baseline als eigener Release-Check referenziert ist.
