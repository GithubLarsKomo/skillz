---
name: round-based-requirements-grilling
description: Führt Requirements Engineering als datengetriebenen, rundenbasierten Grilling-Prozess durch. Die generische, token-geschützte WebApp verwaltet parallele aktive und historische Grillings. Eine SPEC.md wird im Chat geprüft und erst nach Approval in ein separates Produkt-Repository übergeben.
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

## Report, SPEC und Entscheidung

Wenn `SPEC.md erstellen` gewählt wird:

1. Reports des betreffenden Grillings konsolidieren.
2. `SPEC.md` vollständig im Chat als freigabefähigen Entwurf liefern; nicht im Grilling-Repository speichern.
3. Nur dieses Grilling auf `review` und `handoffStatus: awaiting-spec-decision` setzen.
4. Den globalen `APP_STATUS` nicht automatisch ändern, da parallele und historische Grillings weiterhin benötigt werden können.
5. Der Nutzer entscheidet zwischen Genehmigung, Ablehnung mit neuer Runde oder Ablehnung mit Abbruch.
6. Bei neuer Runde: Grilling wieder `active`, Beanstandungen fokussiert abfragen.
7. Bei Abbruch: Grilling `stopped`; historische Runden bleiben erhalten.
8. Bei Approval: Grilling `approved`, geeigneten Namen für ein separates Produkt-Repository vorschlagen.
9. Erst nachdem der Nutzer das neue Repository angelegt und freigegeben hat, dort `SPEC.md`, README, Architektur und initiale Projektdateien erstellen und pushen.

## Abschluss

Ein einzelnes Grilling endet fachlich mit Approval, Abbruch oder Archivierung. Die Plattform kann unabhängig davon global aktiv bleiben oder über `APP_STATUS: inactive` vollständig stillgelegt werden.
