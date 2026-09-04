---
name: audio-tutorial-workflow
description: Überführt einen durch Grilling geklärten Tutorial-Auftrag in eine hörgerechte, kapitelstrukturierte Lernfassung und eine EPUB-Datei für TTS-Reader wie ElevenReader. Verwendet vor dem Rendering den vorhandenen Precision-Writing-Pfad, minimiert in deutschen Fassungen unnötige Anglizismen, verwendet für englische Fassungen amerikanisches Englisch und liefert eine passende Stimmenempfehlung oder einen Voice-Design-Prompt. Nicht verwenden, bevor Ziel, Zielgruppe, Tiefe, Stil und Ausgabeweg durch Grilling ausreichend geklärt sind.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - round-based-requirements-grilling
  - precision-writing-revision
outputs:
  - spoken-tutorial.md
  - spoken-tutorial.epub
  - audio-tutorial-run.json
  - voice-guidance.md
lastEvaluated: 2026-09-04
---

# Audio Tutorial Workflow

## Zweck

Dieser Workflow erzeugt aus einem fachlich bestimmten Tutorial eine Version, die sich in einem TTS-Reader angenehm anhören, in Kapiteln navigieren und nach Unterbrechungen sinnvoll fortsetzen lässt.

Er besitzt weder die fachlichen Claims noch die allgemeine Sprachrevision. Fachinhalt kommt aus dem vorgelagerten Tutorial- oder Lernprozess. Sprachqualität und fachliche Treue werden über `precision-writing-revision` abgesichert. Die EPUB-Erzeugung ist eine reine Medienprojektion.

## Harte Vorbedingung: Grilling zuerst

**Jeder Audio-Tutorial-Lauf beginnt mit `round-based-requirements-grilling`.**

Vor der Produktion müssen mindestens geklärt sein:

- Lernziel und gewünschter Nutzen;
- Zielgruppe und Vorwissen;
- fachliche Tiefe;
- gewünschte Tutorial-Art, zum Beispiel Erklärung, Einführung, Schritt-für-Schritt-Anleitung oder Vertiefung;
- Sprache;
- gewünschter Sprachstil;
- gewünschte Kapitelgranularität;
- Zielplattform oder Ausgabeverwendung;
- besondere Anforderungen an Slang, Poesie oder regionale Sprache;
- falls relevant, gewünschte Stimmencharakteristik.

Bereits beantwortete Punkte werden nicht erneut gefragt. Ein vorhandener `GRILL-REPORT.md`, `requirements-handoff.json` oder ein äquivalenter bestätigter Handoff wird weiterverwendet.

Fehlt der Grilling-Handoff oder bleiben entscheidende Ziel- oder Vorgehensfragen offen, beginnt keine Audio-Produktion.

## Eingänge

Mindestens:

- bestätigter Grilling-Handoff;
- fachlich belastbarer Tutorial-Text oder kanonisches Lernmodell;
- Sprache `de|en`;
- Zielplattform, standardmäßig ein EPUB-fähiger TTS-Reader.

Optional:

- gewünschte maximale Kapitellänge;
- vorhandene Kapitelstruktur;
- gewünschte Stimme;
- gewünschte Voice-Design-Merkmale.

## Sprachprofil

Die vollständigen Regeln stehen in `references/spoken-language-profile.md`.

Verbindliche Defaults:

### Deutsch

- idiomatisches Hochdeutsch;
- technisch-wissenschaftliche Klarheit, sofern Inhalt oder Grilling keinen anderen Stil verlangen;
- unnötige Anglizismen vermeiden;
- englische Wörter auf ein sinnvolles Minimum begrenzen;
- etablierte Fachbegriffe nicht künstlich eindeutschen;
- englische Originalbegriffe eines Modells beim ersten Auftreten erklären und anschließend bevorzugt deutsch weiterführen.

### Englisch

- amerikanisches Englisch als Standard;
- Parameter an `precision-writing-revision`: `language=en`, `englishVariant=us`.

### Stilabweichungen

Slang, poetische Sprache oder regionale Färbung nur verwenden, wenn sie im Grilling ausdrücklich gewünscht wurden.

## Ablauf

### 1. Grilling-Handoff fixieren

Ziel, Zielgruppe, Tiefe, Stil, Sprache, Ausgabeform und besondere Einschränkungen aus dem bestätigten Grilling als Run-Contract übernehmen.

### 2. Fachlichen Tutorial-Kern fixieren

Den fachlich autoritativen Tutorial-Text oder das kanonische Lernmodell bestimmen. Quellen, Zahlen, Bedingungen, Einschränkungen und Fachterminologie als Fidelity Lock behandeln.

### 3. Precision Writing Revision

`precision-writing-revision` ausführen.

Für deutsche Fassungen zusätzlich das Spoken-Language-Profil anwenden. Unnötige Anglizismen werden ersetzt, ohne etablierte Terminologie oder fachliche Bedeutung zu beschädigen.

Für englische Fassungen immer `englishVariant=us` setzen, sofern der Grilling nicht ausdrücklich einen anderen Zielstandard fordert.

Fidelity hat Vorrang vor stilistischer Glättung.

### 4. Hörgerechte Adaption

Die redigierte Fassung für lineares Zuhören optimieren:

- Kapitel mit klarer Orientierung beginnen;
- lange Schachtelsätze auflösen;
- Klammerinhalte in normale Sätze überführen oder streichen, wenn semantisch entbehrlich;
- Tabellen in gesprochene Vergleichs- oder Aufzählungsstrukturen übersetzen;
- Abkürzungen beim ersten Auftreten verständlich einführen;
- Aufzählungen hörbar ankündigen;
- natürliche Wiedereinstiegspunkte schaffen;
- bei längeren Kapiteln kurze Zwischenzusammenfassungen einbauen;
- Wiederholungen nur didaktisch einsetzen;
- keine künstlichen Füllsätze oder theatrale Sprache ergänzen.

Die Kapitelstruktur soll dem Lernweg dienen, nicht nur der ursprünglichen Dokumentgliederung.

### 5. EPUB rendern

`spoken-tutorial.md` deterministisch als EPUB3 rendern.

Anforderungen:

- echte Kapitel-Navigation;
- EPUB-Navigation und NCX für breite Reader-Kompatibilität;
- UTF-8;
- keine inhaltliche Veränderung während des Renderings;
- Kapitelüberschriften müssen die Wiedereinstiegslogik erhalten.

### 6. Stimme empfehlen

`voice-guidance.md` erzeugen.

Reihenfolge:

1. Wenn eine zum Inhalt passende, aktuell verfügbare ElevenReader-Stimme belastbar bekannt ist, diese empfehlen.
2. Für neutrale deutschsprachige technisch-wissenschaftliche Tutorials kann `George` als bereits praktisch erprobtes Beispiel genannt werden, solange die Stimme auf der Zielplattform verfügbar ist.
3. Wenn keine geeignete Stimme verifizierbar ist oder eine spezifische Sprechweise benötigt wird, einen Voice-Design-Prompt liefern.

Der Prompt beschreibt mindestens:

- Sprache und Sprachvariante;
- ungefähres Alter;
- Stimmcharakter;
- Sprechtempo;
- Artikulation;
- fachliche Rolle oder Persona;
- emotionale Grundhaltung;
- unerwünschte Eigenschaften.

### 7. Qualitätsprüfung

Vor PASS prüfen:

- Grilling-Handoff vorhanden und berücksichtigt;
- fachliche Bedeutung gegenüber dem Ausgangstext erhalten;
- deutsche Fassung enthält keine vermeidbaren, nicht etablierten Anglizismen;
- englische Fassung verwendet amerikanisches Englisch;
- Kapitel sind lernlogisch und für Pause/Fortsetzung geeignet;
- EPUB besitzt echte Kapitel-Navigation;
- keine Tabellen- oder Layoutreste erzeugen unverständliche Sprachausgabe;
- Stimmenempfehlung oder Voice-Design-Prompt liegt vor;
- Slang, Poesie oder regionale Sprache nur bei explizitem Auftrag.

## Run Manifest

`audio-tutorial-run.json` enthält mindestens:

```json
{
  "schemaVersion": 1,
  "grillingHandoffRef": "...",
  "sourceRef": "...",
  "language": "de",
  "englishVariant": null,
  "style": "technical-scientific",
  "chapterCount": 0,
  "precisionWritingStatus": "pass|review|fail",
  "epubValidation": "pass|fail",
  "voiceGuidanceRef": "voice-guidance.md",
  "status": "pass|review|fail",
  "warnings": []
}
```

## Fehlerbehandlung

- **Kein Grilling-Handoff:** Produktion stoppen und zuerst Grilling durchführen.
- **Fachlicher Hard Fail in der Sprachrevision:** keinen finalen EPUB-Stand ausgeben.
- **Unklarer englischer Fachbegriff in deutscher Fassung:** Fachbedeutung erhalten; nicht zwanghaft eindeutschen. Bei Bedarf Originalbegriff einmal erklären.
- **EPUB-Validierungsfehler:** Datei nicht als fertig ausgeben; Renderer korrigieren und erneut prüfen.
- **Stimme nicht verifizierbar:** keine Verfügbarkeit behaupten; stattdessen Voice-Design-Prompt liefern.

## Abschluss

Der Workflow ist abgeschlossen, wenn der Auftrag durch Grilling geklärt wurde, die fachlich treue und hörgerechte Lernfassung sprachlich geprüft ist, ein navigierbares EPUB mit sinnvollen Kapiteln vorliegt und die Zielplattform eine belastbare Stimmenempfehlung oder einen passenden Voice-Design-Prompt erhält.
