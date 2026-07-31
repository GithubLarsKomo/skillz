---
name: round-based-requirements-grilling
description: Führt Requirements Engineering als datengetriebenen, rundenbasierten Grilling-Prozess durch. Bei Softwareprojekten ist eine verpflichtende KI-/ML-Readiness-Prüfung einschließlich Einsatzpotenzial, Architekturvorbereitung, Datensammlung, Labeling und Governance Bestandteil des Grillings. Die generische, token-geschützte WebApp verwaltet parallele aktive und historische Grillings. Eine SPEC.md wird im Chat geprüft und erst nach Approval in ein separates Produkt-Repository übergeben.
version: 1.0.0
status: stable
owners:
  - GithubLarsKomo
requires: []
outputs:
  - GRILL-REPORT.md
  - approved SPEC.md
lastEvaluated: 2026-07-31
---

# Datengetriebenes Requirements Grilling

## Zweck und Trennung

Das Repository `GithubLarsKomo/grilling` enthält ausschließlich die generische Grilling-Plattform, versionierte JSON-Rundendefinitionen, lokale Reportfunktionen sowie Review- und Übergabemetadaten. Produktimplementierungen und finale `SPEC.md`-Dateien gehören nicht in dieses Repository.

## Laufzeitstruktur

- App: `site/index.html`, `site/styles.css`, `site/app.js`
- Katalog: `site/catalog.json`
- Runden: `site/rounds/*.json`
- Schema: `site/round-schema.json`
- vorgeschalteter Worker: `src/index.js`
- Deployment-Konfiguration: `wrangler.jsonc`
- URL: `https://grilling.larskomo.workers.dev/`

Der Worker muss wegen `assets.run_worker_first: true` vor sämtlichen statischen Assets ausgeführt werden.

## Zwei unabhängige Statusebenen

### Globaler WebApp-Status

`wrangler.jsonc` enthält unter `vars.APP_STATUS` genau einen der Werte:

- `active`: Die WebApp ist erreichbar und verlangt den aktuellen Token.
- `inactive`: Die gesamte WebApp ist gesperrt. Der Worker liefert nur eine neutrale Inaktiv-Seite mit HTTP 503 aus. Token, Cookies, direkte Asset-URLs und Bearer-Zugriffe dürfen diesen Zustand nicht umgehen.

Der globale Status ist unabhängig von den Statuswerten einzelner Grillings. Er wird verwendet, wenn die Plattform über längere Zeit nicht benötigt wird.

Deaktivierung:

1. `APP_STATUS` auf `inactive` setzen.
2. Einen neuen Token programmgesteuert erzeugen und gleichzeitig eintragen.
3. Änderungen pushen.
4. Keinen funktionierenden Zugriffslink ausgeben, sondern bestätigen, dass die WebApp inaktiv ist.

Reaktivierung:

1. `APP_STATUS` auf `active` setzen.
2. Mit Python `secrets`, Node.js `crypto` oder einem gleichwertigen kryptografischen Zufallsgenerator einen neuen Token erzeugen.
3. Den Token in `vars.ACCESS_TOKEN_CURRENT` eintragen.
4. Änderungen pushen.
5. Den vollständigen neuen Link im Chat ausgeben.

Tokens dürfen niemals frei erfunden werden.

### Status einzelner Grillings

Zulässige Werte sind mindestens:

- `draft`
- `active`
- `review`
- `approved`
- `stopped`
- `archived`

Diese Statuswerte steuern fachliche Lebenszyklen, nicht die globale Erreichbarkeit. Aktive, parallele und historische Grillings bleiben auswählbar, solange `APP_STATUS` global `active` ist.

## Katalog und Navigation

`site/catalog.json` enthält alle Grillings und Runden. `activeGrillingId` und `activeRoundId` bestimmen die Vorauswahl. Andere Einträge bleiben über Auswahl und URL-Parameter erreichbar:

```text
?grilling=<grilling-id>&round=<round-id>
```

Antworten werden pro Browser, Grilling, Runde und Definitions-Hash getrennt gespeichert. Veröffentlichte Rundendefinitionen sind unveränderlich; Änderungen erfolgen als neue Revision oder Runde.

## Anforderungen an jede Runde

Jede Runde verwendet stabile IDs und enthält Kontext, fokussierte Fragen, Reportkonfiguration und unmittelbar vor der Abschlussentscheidung dieses allgemeine Feld:

```json
{
  "id": "notes",
  "label": "Anmerkungen, Ergänzungen oder abweichende Festlegungen",
  "type": "textarea",
  "rows": 5
}
```

Unterstützte Feldtypen sind mindestens `text`, `textarea`, `number`, `select`, `radio` und `checkbox`.

## Workflow pro veröffentlichendem Push

1. Vorherige Reports und Festlegungen analysieren.
2. Nur Fragen ergänzen, die relevante Unsicherheit reduzieren.
3. Neue unveränderliche Rundendefinition anlegen und Katalog aktualisieren.
4. Bei jeder Änderung der veröffentlichten Plattform, einer Runde oder eines Katalogstatus einen neuen Token programmgesteuert erzeugen.
5. `vars.ACCESS_TOKEN_CURRENT` ersetzen.
6. `APP_STATUS` bewusst auf `active` oder `inactive` setzen; niemals implizit ändern.
7. Änderungen pushen.
8. Bei `active` den vollständigen Zugriffslink ausgeben. Bei `inactive` ausdrücklich mitteilen, dass kein Zugriffslink funktioniert.

Der vorherige Token und alle daraus abgeleiteten Cookies werden nach dem Deployment ungültig. Es gibt keinen `ACCESS_TOKEN_PREVIOUS`.

## Token-Schutz

Beispielkonfiguration:

```jsonc
{
  "main": "./src/index.js",
  "vars": {
    "APP_STATUS": "active",
    "ACCESS_TOKEN_CURRENT": "<programmgesteuert erzeugter Token>"
  },
  "assets": {
    "directory": "./site",
    "binding": "ASSETS",
    "run_worker_first": true
  }
}
```

Zulässige Anmeldung:

- Token-Eingabe auf der Login-Seite
- `?access=<token>` mit sofortiger Weiterleitung auf eine tokenfreie URL
- `Authorization: Bearer <token>`

Das Cookie enthält nur einen SHA-256-Ableitungswert und muss `HttpOnly`, `Secure` und `SameSite=Lax` sein. Geschützte und inaktive Antworten erhalten `Cache-Control: private, no-store`.

Der committed Token ist nur eine einfache Zugriffshürde und kein echtes Secret. In Rundendefinitionen und Reports dürfen deshalb keine vertraulichen oder personenbezogenen Inhalte veröffentlicht werden.

## Verpflichtende KI-/ML-Readiness bei Softwareprojekten

### Erkennung

Sobald das Grilling eine Software, WebApp, mobile App, Datenplattform, Automatisierung, API, digitale Entscheidungsunterstützung oder ein softwaregestütztes Gerät betrifft, ist die KI-/ML-Readiness ein verpflichtender Bestandteil des Requirements Engineerings.

Der Abschnitt darf nur dann als nicht anwendbar abgeschlossen werden, wenn nachvollziehbar dokumentiert ist, warum weder heutige noch absehbare datengetriebene Funktionen einen sinnvollen Nutzen besitzen. Eine bloße Feststellung wie „aktuell keine KI geplant“ reicht nicht aus.

### Pflichtfragen

Vor Erstellung einer freigabefähigen `SPEC.md` müssen mindestens folgende Themen geklärt sein:

1. **KI-/ML-Relevanz**
   - Welche Entscheidungen, Klassifikationen, Prognosen, Priorisierungen, Empfehlungen oder Inhaltsverarbeitungen könnten datengetrieben verbessert werden?
   - Wo bietet klassische Regel- oder Statistiklogik den besseren Ansatz?
   - Welche Entscheidungen dürfen aus Sicherheits-, Compliance- oder Haftungsgründen niemals ausschließlich durch ein Modell getroffen werden?

2. **Einsatzform und Nutzen**
   - Assistenz, Automatisierung, Vorhersage, Anomalieerkennung, Suche/RAG, Generierung, Optimierung oder Personalisierung.
   - Erwarteter fachlicher Nutzen und messbare Zielgrößen.
   - Geeignete Einführungsstufe: Experiment, Offline-Evaluation, Shadow Mode, Human-in-the-Loop oder produktive Teilautomatisierung.

3. **Architekturvorbereitung**
   - Trennung von Datenaufnahme, Normalisierung, Feature Engineering, Regelengine, Modellinferenz und Ergebnisdarstellung.
   - Stabile, versionierte Schnittstellen für spätere Modelle.
   - Austauschbarkeit von Modell, Anbieter und Laufzeitumgebung.
   - Fallback auf deterministische oder manuelle Verfahren.

4. **Datensammlung**
   - Welche Rohdaten entstehen ohnehin?
   - Welche zusätzlichen Daten müssen bereits im MVP erhoben werden, damit spätere Modelle trainierbar und evaluierbar sind?
   - Welche Kontextinformationen, Zeitbezüge, Datenqualitätsmerkmale und Entscheidungsresultate müssen gemeinsam gespeichert werden?
   - Welche Daten dürfen nicht erhoben werden?

5. **Labels und Ground Truth**
   - Welche Zielvariablen werden benötigt?
   - Wer kann sie zuverlässig vergeben: Nutzer, Experten, nachgelagerte Prozesse oder objektive Messungen?
   - Wie werden `nicht beurteilbar`, `nicht beobachtet`, fehlende Werte und widersprüchliche Bewertungen behandelt?
   - Ist ein einfaches Rating ausreichend oder sind strukturierte Teilbewertungen notwendig?

6. **Lernstrategie**
   - Eignung von Supervised Learning, Active Learning, Human-in-the-Loop, Expert Review, Self-Supervised Learning oder anderen Verfahren.
   - Maßnahmen gegen Selection Bias, Survivorship Bias, Label Leakage, Feedback Loops und unausgewogene Klassen.
   - Strategie für seltene, sicherheitskritische oder nicht direkt beobachtbare Fälle.

7. **Evaluation und Governance**
   - Baseline und Vergleich gegen bestehende Regeln oder menschliche Bearbeitung.
   - Qualitäts-, Sicherheits-, Fairness- und Kalibrierungsmetriken.
   - Modell-, Prompt-, Feature- und Datensatzversionierung.
   - Freigabe, Monitoring, Drift-Erkennung, Retraining, Rollback und Auditierbarkeit.
   - Datenschutz, Einwilligung, Aufbewahrung, Export und Löschung.

### Grundprinzipien

- **KI-ready, aber nicht KI-abhängig:** Das MVP muss ohne noch unvalidierte KI sicher und fachlich nutzbar bleiben.
- **Datensammlung vor Modellwahl:** Zuerst Ground Truth, Datenqualität und Nutzen klären; erst danach Modellfamilie oder Anbieter festlegen.
- **Strukturierte Labels vor Sternebewertung:** Ein Sterne-Rating darf ergänzen, aber nicht automatisch als ausreichende Ground Truth gelten.
- **Aktive Datenauswahl:** Bei begrenzter Bewertungsbereitschaft bevorzugt Active Learning informative Grenzfälle, Quellenkonflikte, seltene Situationen und Modell-Regel-Abweichungen.
- **Shadow Mode vor Einflussnahme:** Ein neues Modell wird zunächst parallel evaluiert und darf produktive Entscheidungen erst nach dokumentierter Validierung beeinflussen.
- **Harte Grenzen bleiben deterministisch:** Amtliche Warnungen, zwingende Compliance-Regeln und nicht übersteuerbare Sicherheitsgrenzen bleiben außerhalb der freien Modellentscheidung.

### Ergebnis im Grilling-Report

Jeder Software-Grilling-Report enthält einen eigenen Abschnitt `KI-/ML-Readiness` mit mindestens:

- KI-/ML-Potenzial und begründeter Relevanzeinstufung,
- geeigneten und ungeeigneten Anwendungsfällen,
- erforderlichen Daten und Features,
- Label- und Ground-Truth-Strategie,
- Datensammlungs- und Aufbewahrungskonzept,
- empfohlener Lern- und Validierungsstrategie,
- Sicherheits-, Datenschutz- und Governance-Grenzen,
- MVP-Vorbereitungen und späterer KI-Roadmap,
- offenen Entscheidungen und Risiken.

Die Abschlussentscheidung `SPEC.md erstellen` darf bei einem Softwareprojekt erst angeboten oder akzeptiert werden, wenn dieser Abschnitt ausreichend beantwortet ist oder eine begründete Nichtanwendbarkeit dokumentiert wurde.

### Ergebnis in der SPEC.md

Die finale `SPEC.md` eines Softwareprojekts enthält ein eigenständiges Kapitel `KI-/ML-Architektur und Datenstrategie`. Das Kapitel beschreibt mindestens:

- Ziel und Abgrenzung der KI-/ML-Nutzung,
- Datenquellen, Datenmodell und Feature Engineering,
- Datensammlung, Labels und Ground Truth,
- Regel-, Modell- und Fallback-Architektur,
- Evaluation, Shadow Mode und Freigabekriterien,
- Datenschutz, Governance, Monitoring und Versionierung,
- Roadmap vom MVP bis zu einem möglichen produktiven Modellbetrieb.

## Report, SPEC und Entscheidung

Wenn `SPEC.md erstellen` gewählt wird:

1. Reports des betreffenden Grillings konsolidieren.
2. Bei Softwareprojekten prüfen, dass die verpflichtende KI-/ML-Readiness vollständig behandelt oder begründet als nicht anwendbar dokumentiert ist.
3. `SPEC.md` vollständig im Chat als freigabefähigen Entwurf liefern; nicht im Grilling-Repository speichern.
4. Nur dieses Grilling auf `review` und `handoffStatus: awaiting-spec-decision` setzen.
5. Den globalen `APP_STATUS` nicht automatisch ändern, da parallele und historische Grillings weiterhin benötigt werden können.
6. Der Nutzer entscheidet zwischen Genehmigung, Ablehnung mit neuer Runde oder Ablehnung mit Abbruch.
7. Bei neuer Runde: Grilling wieder `active`, Beanstandungen fokussiert abfragen.
8. Bei Abbruch: Grilling `stopped`; historische Runden bleiben erhalten.
9. Bei Approval: Grilling `approved`, geeigneten Namen für ein separates Produkt-Repository vorschlagen.
10. Erst nachdem der Nutzer das neue Repository angelegt und freigegeben hat, dort `SPEC.md`, README, Architektur und initiale Projektdateien erstellen und pushen.

## Abschluss

Ein einzelnes Grilling endet fachlich mit Approval, Abbruch oder Archivierung. Die Plattform kann unabhängig davon global aktiv bleiben oder über `APP_STATUS: inactive` vollständig stillgelegt werden.