---
name: openasr-offline-model-import
description: Importiert ein bereits lokal vorhandenes OpenASR-Modell unter Windows robust in OpenASR Desktop, insbesondere wenn der signierte Online-Katalog wegen Proxy-, TLS- oder UnknownIssuer-Problemen nicht verwendet werden kann.
version: 0.2.0
status: candidate
owners:
  - GithubLarsKomo
requires: []
outputs:
  - installed OpenASR model
  - import verification
lastEvaluated: 2026-07-31
---

# OpenASR Offline Model Import

## Einsatz

Diesen Skill verwenden, wenn OpenASR Desktop ein Modell nicht regulär aus dem Modellkatalog laden kann, die Modelldatei aber bereits lokal als `.oasr` vorliegt. Typische Meldungen sind:

- `invalid peer certificate: UnknownIssuer`
- primärer Modellkatalog nicht erreichbar oder nicht vertrauenswürdig
- lokaler Katalog-Cache wird aus Sicherheitsgründen verworfen
- OpenASR verwendet nur den eingebetteten Offline-Katalog

Der Skill umgeht keine Integritätsprüfung einer unbekannten Datei. Die lokale `.oasr`-Datei muss aus einer vertrauenswürdigen Quelle stammen und zum angegebenen Modell sowie zur Quantisierung passen.

## Voraussetzungen

- OpenASR Desktop ist installiert.
- Die ausführbare Datei liegt standardmäßig unter:

```text
%LOCALAPPDATA%\OpenASR Desktop\openasr.exe
```

- Die vollständige `.oasr`-Modelldatei ist lokal vorhanden.
- Modell-ID und Variante sind bekannt, beispielsweise:

```text
parakeet-tdt-0.6b-v3:q8
```

## Bewährter PowerShell-Ablauf

### 1. Modelldatei eindeutig festlegen

```powershell
$modelFile = "$env:USERPROFILE\.openasr\models\parakeet-tdt-0.6b-v3\q8_0\parakeet-tdt-0.6b-v3-q8_0.oasr"
```

### 2. Datei vor dem Import prüfen

```powershell
if (-not (Test-Path -LiteralPath $modelFile -PathType Leaf)) {
    throw "OpenASR-Modelldatei nicht gefunden: $modelFile"
}

Get-Item -LiteralPath $modelFile | Select-Object FullName, Length, LastWriteTime
```

Eine leere oder offensichtlich unvollständige Datei darf nicht importiert werden.

### 3. OpenASR-Binary bestimmen und prüfen

```powershell
$openAsrExe = "$env:LOCALAPPDATA\OpenASR Desktop\openasr.exe"

if (-not (Test-Path -LiteralPath $openAsrExe -PathType Leaf)) {
    throw "OpenASR Desktop wurde am erwarteten Pfad nicht gefunden: $openAsrExe"
}
```

### 4. Lokale Datei über `pull --from` importieren

```powershell
& $openAsrExe `
    pull parakeet-tdt-0.6b-v3:q8 `
    --from $modelFile

if ($LASTEXITCODE -ne 0) {
    throw "OpenASR-Modellimport fehlgeschlagen. Exit-Code: $LASTEXITCODE"
}
```

Der Schalter `--from` veranlasst OpenASR, die angegebene lokale Modelldatei zu verwenden. Eine Warnung zum Online-Katalog kann dabei weiterhin erscheinen; entscheidend ist, ob der lokale Import erfolgreich abgeschlossen wird.

## Validierung

Nach dem Import:

1. OpenASR Desktop neu öffnen oder aktualisieren.
2. Prüfen, ob das Modell in der lokalen Modellliste erscheint.
3. Das importierte Modell auswählen.
4. Eine kurze Testaufnahme transkribieren.
5. Prüfen, ob keine erneute Modelldatei angefordert wird.

Optional kann die CLI-Hilfe beziehungsweise eine vorhandene Modelllisten-Funktion der installierten Version geprüft werden:

```powershell
& $openAsrExe --help
```

Da sich CLI-Unterbefehle zwischen Versionen ändern können, dürfen nicht verifizierte Befehle zur Modellauflistung nicht vorausgesetzt werden.

## Fehlerbehandlung

### `UnknownIssuer` oder Katalogwarnung

Die Warnung betrifft die TLS-Vertrauenskette des Online-Katalogs. Bei einem erfolgreichen lokalen `--from`-Import ist sie nicht automatisch ein Importfehler. Unternehmensproxy und Zertifikatsverwaltung dürfen nicht durch Abschalten der TLS-Prüfung umgangen werden.

### Datei nicht gefunden

- Pfad mit `Test-Path` prüfen.
- Auf Leerzeichen im Installationspfad achten.
- In PowerShell die ausführbare Datei mit dem Aufrufoperator `&` starten.
- Den Pfad nicht manuell in einzelne Argumente zerlegen.

### Modell-ID und Datei passen nicht zusammen

Die Modell-ID hinter `pull` muss zur Datei passen. Insbesondere Quantisierungen wie `q8`, `q8_0` oder andere Varianten dürfen nicht stillschweigend vertauscht werden.

### Import bleibt erfolglos

Dann mindestens erfassen:

- vollständiger CLI-Aufruf ohne sensible Daten
- vollständige Fehlermeldung
- OpenASR-Version
- Dateiname und Dateigröße
- verwendete Modell-ID
- Installationspfad der Binary

## Sicherheitsregeln

- Keine Zertifikatsprüfung deaktivieren.
- Keine Unternehmensproxy-Regeln dauerhaft umgehen.
- Keine unbekannten Modelldateien importieren.
- Hashwerte des Herausgebers prüfen, sofern verfügbar.
- API-Tokens, Zugangsdaten und interne Proxy-Credentials nicht in Logs oder Repositories speichern.

## Abschlusskriterium

Der Skill ist abgeschlossen, wenn das lokale Modell von OpenASR Desktop erkannt wird und eine Testtranskription mit diesem Modell erfolgreich ausgeführt wurde.
