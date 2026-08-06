---
name: opaque-system-analysis
description: Rekonstruiert das kleinste evidenzbasierte Verhaltens- und Schnittstellenmodell eines opaken oder unzureichend dokumentierten Systems, Artefakts, Protokolls oder Dateiformats, wenn Quellcode oder belastbare Dokumentation für die nächste Engineering-Entscheidung nicht ausreichen. Verwenden, bevor Diagnose oder Implementierung beginnt, wenn erst beobachtbares Verhalten, Zustände, Inputs, Outputs oder Verträge erschlossen werden müssen; nicht für Exploit-Entwicklung, allgemeine Fehlersuche mit ausreichender Sichtbarkeit oder breite Projektplanung.
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires: []
outputs:
  - recovered-system-model.json
  - opaque-analysis-evidence.md
  - remaining-unknowns.json
lastEvaluated: 2026-08-02
implicitInvocation: true
---

# Opaque System Analysis

## Zweck

Rekonstruiere nur so viel Verhalten eines nicht ausreichend einsehbaren Systems, dass der nächste Engineering-Schritt sicher und überprüfbar möglich wird.

Der Skill verwandelt ein opakes Artefakt oder beobachtbares System mit einer konkreten Engineering-Frage in ein evidenzbasiertes Minimalmodell aus Inputs, Outputs, Zuständen, Invarianten, Schnittstellen, Hypothesen und verbleibenden Unbekannten. Er endet, sobald die definierte Frage mit ausreichender Evidenz beantwortet oder als derzeit nicht beantwortbar begrenzt ist.

## Trigger

Verwenden bei beispielsweise:

- Binärdateien, Bibliotheken oder Anwendungen ohne verfügbaren Quellcode,
- undokumentierten oder widersprüchlich dokumentierten APIs und Protokollen,
- proprietären Dateiformaten,
- Firmware oder Gerätekommunikation,
- stark generiertem, minifiziertem oder anderweitig schwer verständlichem Code,
- Legacy-Komponenten, deren tatsächlicher Vertrag vor Ersatz oder Integration rekonstruiert werden muss.

Nicht verwenden, wenn bereits ein reproduzierbarer Softwarefehler bei ausreichender Sichtbarkeit untersucht wird; dann gehört die Arbeit zu `disciplined-diagnosis`. Nicht verwenden, um ein großes Vorhaben zu priorisieren; dafür ist `large-work-wayfinder` zuständig. Nicht für Exploit-Entwicklung, Credential-Umgehung, Persistenz, Schadsoftware oder offensive Ausnutzung einsetzen.

## Voraussetzungen

Vor Beginn festhalten:

- die eine Engineering-Frage, die beantwortet werden muss,
- Artefakt/System, Version, Hash oder anderer unveränderlicher Identifikator soweit verfügbar,
- erlaubte Analyseoberflächen und Testumgebungen,
- Sicherheits-, Datenschutz-, Lizenz- und Autorisierungsgrenzen,
- bekannte Dokumentation und bereits bestätigte Beobachtungen,
- akzeptables Evidenzniveau für den nächsten Schritt.

Wenn die Analyse fremde Systeme oder Daten betrifft, nur innerhalb nachweislich autorisierter und legaler Grenzen arbeiten.

## Kernprinzipien

1. **Minimalmodell statt Vollanalyse.** Rekonstruiere nur den Vertrag, der für die aktuelle Engineering-Frage nötig ist.
2. **Least invasive first.** Beginne mit Metadaten, statischer Inspektion, vorhandenen Logs und kontrollierten Beobachtungen, bevor invasive Instrumentierung erwogen wird.
3. **Beobachtung ist nicht Interpretation.** Trenne Rohbeobachtung, Evidenz, Hypothese und Finding.
4. **Falsifizierbare Hypothesen.** Jede wichtige Vermutung braucht eine unterscheidende Prüfung oder bleibt ausdrücklich offen.
5. **Keine Tool-Halluzination.** Prüfe verfügbare lokale Fähigkeiten mit `scripts/probe_toolchain.py` oder äquivalenter verifizierter Tool-Erkennung, bevor konkrete Werkzeuge vorausgesetzt werden.
6. **Keine Produktionsänderung.** Dieser Skill rekonstruiert Verhalten; Fix, Ersatz, Migration oder Feature-Implementierung werden an andere Skills übergeben.

## Ablauf

### 1. Analysefrage schneiden

Formuliere eine einzige entscheidbare Frage, zum Beispiel:

- Welche Inputs akzeptiert die Komponente und welche Outputs erzeugt sie?
- Welche Zustandsübergänge sind für den beobachteten Ablauf relevant?
- Welche Felder eines Dateiformats sind für Roundtrip-Kompatibilität zwingend?
- Welche Requests und Responses bilden den tatsächlich verwendeten API-Vertrag?

Definiere Stop-Bedingung und Nicht-Ziele. Eine vollständige Dekompilierung oder vollständige Protokollspezifikation ist kein Standardziel.

### 2. Artefakt und Umgebung charakterisieren

Erfasse unveränderliche Identität, Format, Plattform, Architektur, Packaging, Abhängigkeiten und verfügbare Dokumentation. Prüfe anschließend die tatsächlich verfügbaren Analysefähigkeiten statt Produktnamen anzunehmen.

Bevorzuge Fähigkeitsklassen wie `binary-inspection`, `archive-extraction`, `structured-text`, `network-capture`, `http-observation` oder `runtime-tracing`. Ein konkretes Tool ist nur eine lokale Implementierung dieser Fähigkeit.

### 3. Beobachtbare Oberfläche bestimmen

Liste steuerbare Inputs und messbare Outputs, Zustände und Nebenwirkungen. Wähle die kleinste Oberfläche, die zwischen den wichtigsten Hypothesen unterscheiden kann.

Vermeide unnötige Produktionsdaten, fremde Credentials und irreversible Aktionen. Erzeuge nach Möglichkeit isolierte Fixtures oder Testartefakte.

### 4. Evidenzkette aufbauen

Für jede relevante Aussage verwende:

`Observation -> Evidence -> Hypothesis -> Test -> Finding -> Recovered Contract`

Dabei gilt:

- `Observation`: direkt wahrgenommener Effekt ohne Deutung,
- `Evidence`: reproduzierbarer Nachweis mit Quelle oder Messpunkt,
- `Hypothesis`: falsifizierbare Erklärung,
- `Test`: kontrollierte Unterscheidung zwischen Hypothesen,
- `Finding`: durch Evidenz gestützte Schlussfolgerung,
- `Recovered Contract`: minimaler belastbarer Vertrag für nachgelagerte Arbeit.

### 5. Konkurrierende Hypothesen prüfen

Für jede material relevante Hypothese dokumentieren:

- erwartete Beobachtung,
- Test oder Vergleich,
- tatsächliches Ergebnis,
- Status `confirmed`, `rejected` oder `open`,
- Evidenzreferenzen.

Ein einzelner zufällig erfolgreicher Versuch bestätigt keinen Vertrag.

### 6. Minimalmodell formulieren

Das Modell enthält nur bestätigte oder ausdrücklich unsichere Elemente:

- Inputs und Vorbedingungen,
- Outputs und Fehlerverhalten,
- relevante Zustände und Übergänge,
- Invarianten,
- beobachtete Schnittstellen,
- bekannte Seiteneffekte,
- Konfidenz und Evidenz,
- verbleibende Unbekannte.

Unterscheide `observed`, `inferred` und `unknown`.

### 7. Handoff bestimmen

- beobachteter Fehler und Ursache nun untersuchbar -> `disciplined-diagnosis`
- große verbleibende Unsicherheitslandschaft -> `large-work-wayfinder`
- isoliertes Experiment nötig -> `throwaway-prototype`
- klarer Ersatz- oder Implementierungsslice -> `test-driven-vertical-slice` oder `implement-from-issue`
- tragende technische Entscheidung -> `decision-record`
- Übergabe an andere Sitzung oder Agent -> `agent-handoff`

## Toolchain Capability Contract

`scripts/probe_toolchain.py` erzeugt eine Laufzeitaufnahme der lokal verfügbaren Werkzeuge. Der Probe ist Infrastruktur, keine Routing- oder Installationslogik.

Ein Eintrag hat mindestens:

```json
{
  "capability": "binary-inspection",
  "provider": "objdump",
  "path": "/usr/bin/objdump",
  "version": "GNU objdump ...",
  "available": true,
  "verifiedAt": "2026-08-02T18:00:00Z"
}
```

Skills sollen auf Fähigkeiten zielen und konkrete Provider erst anhand dieser Aufnahme auswählen. Fehlende Fähigkeiten werden als Blocker dokumentiert; Tools werden nicht stillschweigend installiert.

## Prüfungen

Vor Abschluss müssen erfüllt sein:

- genau eine abgegrenzte Engineering-Frage und Stop-Bedingung,
- Artefakt/System eindeutig identifiziert soweit technisch möglich,
- Toolannahmen lokal verifiziert,
- Beobachtungen von Interpretationen getrennt,
- material relevante Hypothesen mit unterscheidender Evidenz bewertet,
- Recovered Contract enthält keine unbelegten Tatsachenbehauptungen,
- Nicht-Ziele und verbleibende Unbekannte explizit,
- nächster Skill oder nächste Aktion eindeutig.

## Fehlerbehandlung

Wenn die notwendige Beobachtung nicht legal, sicher oder technisch möglich ist:

1. nicht auf invasivere Methoden eskalieren, nur um ein Ergebnis zu erzwingen,
2. die fehlende Evidenz und betroffene Modellteile als `unknown` markieren,
3. den kleinsten zusätzlichen Zugang, Fixture oder Messpunkt benennen, der die Frage beantworten würde,
4. mit einem begrenzten Handoff abschließen.

Wenn eine Analyse in allgemeine Fehlersuche, Produktplanung oder Implementierung driftet, stoppen und an den zuständigen Skill übergeben.

## Übergabeformat

```json
{
  "question": "...",
  "subject": {"type": "binary|api|protocol|file-format|firmware|application|other", "identity": "..."},
  "scope": {"stopCondition": "...", "nonGoals": ["..."]},
  "toolCapabilities": [{"capability": "...", "provider": "...", "available": true}],
  "observations": [{"id": "O1", "statement": "...", "evidence": ["E1"]}],
  "hypotheses": [{"id": "H1", "status": "confirmed|rejected|open", "evidence": ["E1"]}],
  "recoveredContract": {
    "inputs": [],
    "outputs": [],
    "states": [],
    "invariants": [],
    "sideEffects": [],
    "confidence": "high|medium|low"
  },
  "unknowns": [],
  "nextSkill": "disciplined-diagnosis|large-work-wayfinder|throwaway-prototype|test-driven-vertical-slice|implement-from-issue|decision-record|agent-handoff"
}
```

## Abschlusskriterien

Abgeschlossen ist die Analyse, wenn die definierte Engineering-Frage entweder durch ein minimales evidenzbasiertes Modell beantwortet oder mit präzise benannter fehlender Evidenz begrenzt wurde und ein nachgelagerter Skill ohne zusätzliche implizite Annahmen übernehmen kann.
