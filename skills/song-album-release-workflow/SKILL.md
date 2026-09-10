---
name: song-album-release-workflow
description: Orchestriert Singles, EPs und Alben von einem verpflichtenden Requirements-Grilling über Konzept, Songwriting, Creative-Writing-Revision, generative oder konventionelle Musikproduktion, Audio-QC, Artwork, Rechte-/Metadaten-Freeze und Distributor-Handoff bis zur verifizierten Veröffentlichung auf Spotify. Verwenden, wenn ein Musikprojekt nicht nur textlich entwickelt, sondern reproduzierbar bis zum realen Release geführt werden soll.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - round-based-requirements-grilling
  - project-second-brain
  - creative-writing-workshop
  - creative-prose-revision
  - creative-revision-regression
outputs:
  - album-project-contract.json
  - album-architecture.md
  - track-production-packages/
  - album-audio-qc.json
  - release-metadata.json
  - release-readiness.json
  - spotify-publication-record.json
lastEvaluated: 2026-09-10
---

# Song / Album Release Workflow

## Zweck

Dieser Skill führt ein Musikprojekt **vom ungeklärten Vorhaben bis zur real verifizierten Spotify-Veröffentlichung**. Er ist ein Orchestrator, kein Ersatz für Grilling, Creative-Writing-Revision, Musikgeneratoren, DAWs, Mastering-Werkzeuge, Bildgeneratoren, Distributoren oder Spotify.

Die Kernfrage lautet:

> Ist aus einer bestätigten künstlerischen Absicht ein kohärentes, rechtlich/provenienzseitig belastbares, technisch geprüftes Release geworden, das auf Spotify tatsächlich korrekt live ist?

## Harte Startbedingung: Grilling zuerst

Jeder neue Lauf beginnt mit `round-based-requirements-grilling`.

Das Grilling muss mindestens ausreichend klären:

- Format: Single, EP oder Album;
- künstlerische Kernidee und emotionale/inhaltliche Zielwirkung;
- Sprache und Perspektive;
- Zielhörer bzw. gewünschter Hörkontext;
- Anzahl/ungefähre Länge der Tracks;
- Album-/Track-Arc oder Nicht-Ziel einer narrativen Klammer;
- musikalische Referenzeigenschaften auf beschreibbarer Craft-Ebene;
- Stimme/Persona und gewünschte Kontinuität;
- Grenzen zu Künstlerimitation, Samples, fremden Stimmen und Rechten;
- Produktionsweg: generativ, konventionell oder hybrid;
- Zielplattformen, mindestens Spotify wenn dieser Workflow bis zum Ende laufen soll;
- Budget-/Tool-/Zeitgrenzen;
- gewünschte kommerzielle oder private Nutzung;
- offene Nutzerentscheidungen.

Fehlt ein ausreichend aufgelöstes Grilling-Handoff, wird **nicht** mit Songwriting oder Generierung begonnen. Ungeklärte Präferenzen werden nicht erraten.

## Project-Second-Brain-Pflicht

Nach dem ersten abgeschlossenen projektbezogenen Grilling wird `project-second-brain` initialisiert oder fortgeführt.

Jeder wesentliche Übergang wird dort verankert:

`Grilling -> Album Architecture -> Track Loop -> Audio Freeze -> Artwork/Metadata -> Rights/Distributor -> Spotify Delivery -> Spotify Live Verification`.

Kanonische Artefakte bleiben an ihrem Producer-Ablageort; Project Memory verlinkt Status, Evidenz, Entscheidungen, offene Schleifen und nächste Aktion.

## Phase 1 — Album Project Contract

Erzeuge aus dem Grilling ein `album-project-contract.json` mit mindestens:

- projectTitle / workingTitle;
- releaseType;
- artistIdentity;
- voiceProfile;
- language;
- thematicPremise;
- emotionalTrajectory;
- targetTrackCount;
- productionMethod;
- targetPlatforms;
- rightsIntent;
- hardConstraints;
- nonGoals;
- unresolvedDecisions;
- projectMemoryRef.

### Gate A — Contract Ready

Nur weiter, wenn alle produktionsrelevanten Nutzerentscheidungen entweder bestätigt oder bewusst als reversible Working Assumption markiert sind.

## Phase 2 — Album Architecture

Für EP/Album vor dem Track-Loop eine Albumarchitektur schreiben. Für Singles entsprechend einen Song-Arc.

Albumarchitektur enthält:

- Track-Reihenfolge und Funktion jedes Tracks;
- emotionale Entwicklung;
- Perspektiv-/Persona-Kontinuität;
- wiederkehrende Motive und deren Entwicklung;
- musikalische Variationskarte: Tempo, Takt, Groove, Dichte, Lead-Instrumente, Dynamik;
- bewusst geschützte Wiedererkennungsmerkmale;
- geplante Kontraste;
- Opener-/Closer-Funktion;
- Redundanzrisiken;
- Release-Länge als grobe Zielgröße.

Kein Album soll nur durch identische Tempo-/Arrangement-Templates kohärent wirken. Kohärenz und Variation werden getrennt geplant.

### Gate B — Architecture Coherent

Weiter nur, wenn:

- jeder Track eine eigene Funktion besitzt;
- der Album-Arc ohne Track-Synopsen rekonstruierbar ist;
- musikalische Wiederholung nicht versehentlich aus Default-Prompts entsteht;
- Opener und Closer klar begründet sind.

## Phase 3 — Track Loop

Jeder Track durchläuft denselben kontrollierten Loop.

### 3.1 Track Brief

Erzeuge pro Track:

- Funktion im Gesamtprojekt;
- Ausgangs- und Endzustand der Stimme/Persona;
- zentrale Bilder/Motive;
- Hook-/Titelkandidaten;
- lyrische Grenzen;
- musikalische Rolle gegenüber den Nachbartracks;
- Ziel-Länge.

### 3.2 Lyrics Draft

Texte dürfen stilistische Eigenschaften, Genre- und Craft-Merkmale nutzen, aber keine direkte Nachahmung eines lebenden Künstlers verlangen.

Bevorzugt werden konkrete Bilder, Handlung, Subtext und singbare Wiederholung statt therapeutischer oder erklärender Metasprache.

### 3.3 Creative Writing Workshop

`creative-writing-workshop` vor der Revision anwenden. Mindestens prüfen:

- Cold Read / wahrgenommene Geschichte;
- Stimme und Perspektive;
- emotionale Kausalität;
- Bildsprache;
- Refrain-/Hook-Funktion;
- Redundanz;
- Verhältnis von Erklärung zu Szene/Bild;
- Funktion im Album;
- Strength Preservation.

### 3.4 Creative Prose Revision

`creative-prose-revision` in Developmental -> Scene/Section -> Line-Reihenfolge verwenden.

Song-spezifisch zusätzlich prüfen:

- Singbarkeit und Atemlängen;
- Betonungsfähigkeit der Schlüsselzeilen;
- Wiederholungen, die musikalisch tragen statt nur Text zu verlängern;
- Titel-/Hook-Payoff;
- überladene Regieanweisungen im Lyrics-Feld;
- unnötige Wörter, die musikalische Zeit verbrauchen.

### 3.5 Regression

Nach materiellen Änderungen `creative-revision-regression` verwenden. Geschützte Bilder, Charakterentwicklung, Ambiguität und Album-Payoffs dürfen durch Politur nicht verloren gehen.

### Gate C — Lyric Freeze Candidate

Track darf in Produktion, wenn die Lyrics strukturell tragen und keine offenen Major-Findings aus Workshop/Revision verbleiben.

## Phase 4 — Music / Generation Package

Erzeuge pro Track ein `track-production-package` mit:

- frozen/candidate lyrics;
- concise style prompt;
- voice continuity prompt;
- BPM / meter if desired;
- groove;
- primary instrumentation;
- arrangement arc;
- negative constraints;
- neighboring-track differentiation;
- version/tool/model notes.

### Generative Produktion

Wenn Suno oder ein vergleichbares Tool verwendet wird:

- Tool-/Modellversion dokumentieren;
- kommerzielle Nutzungsberechtigung zum Zeitpunkt der Erzeugung dokumentieren;
- mehrere Takes als Varianten behandeln, nicht automatisch Take 1 wählen;
- Voice-Kontinuität und musikalische Variation getrennt bewerten;
- lange Lyrics nicht blind kürzen, wenn ein Generator das Ende abschneidet;
- bei langen narrativen Songs gezielte Extensions oder bewusst getrennte Parts erwägen;
- bei Split-Generierung verlustfreie WAV-Parts extern musikalisch sauber zusammenfügen;
- keine nicht verifizierten Plattformgrenzen oder Features als Fakt behaupten.

Wenn kein direkter Toolzugriff verfügbar ist, einen kopierfertigen Produktionsblock erzeugen, den Nutzer-Export/WAV abwarten und danach fortsetzen. Den externen Produktionsschritt niemals als ausgeführt behaupten.

### Konventionelle/hybride Produktion

DAW-, Musiker-, Aufnahme- oder Mix-Handoffs müssen dieselben Track-Contracts und Versions-/Provenienzregeln erfüllen.

## Phase 5 — Take Review und Audio QC

Pro Track prüfen:

- vollständige Lyrics oder bewusst genehmigte Abweichung;
- keine abgeschnittenen Enden;
- keine unerwünschten hallucinierten Textteile;
- Stimme/Persona passend;
- musikalische Funktion des Tracks;
- keine störenden Artefakte, Klicks, Clipping, abrupten Ambience-Wechsel;
- Anfang/Ende dramaturgisch korrekt;
- Format, Sample Rate, Channels, Headroom dokumentiert;
- Split-/Edit-Stellen unauffällig.

Danach Album-Level:

- Reihenfolge;
- wahrgenommene Lautheit;
- spektrale Ausreißer;
- Dynamik;
- Trackabstände;
- Wiederholungsmüdigkeit;
- Voice-Kontinuität;
- gewünschte musikalische Kontraste.

Ergebnis: `album-audio-qc.json`.

### Gate D — Audio Freeze

Nur freigeben, wenn jeder Track einen bezeichneten lossless Master besitzt und der Album-Sequenztest bestanden ist.

MP3/AAC sind Derivate, nicht primäre Freeze-Master, sofern der Zielworkflow lossless Upload akzeptiert.

## Phase 6 — Artist Identity und Artwork

Vor Artwork Freeze:

- finaler Künstlername;
- Artist-Name-Kollisionscheck auf relevanten DSPs;
- Albumtitel;
- Coverkonzept;
- Typografie;
- visuelle Beziehung zum Album-Arc;
- Bild-/Font-/Asset-Rechte.

Bei Bildgenerierung oder -bearbeitung die vorhandene Bildfähigkeit verwenden; keine fremden Künstler-/Fotografenstile direkt imitieren.

Artwork erst einfrieren, wenn Distributor-/DSP-Spezifikationen aktuell verifiziert sind.

## Phase 7 — Rights, Provenance und Policy Check

Unmittelbar vor Distribution aktuelle offizielle Quellen prüfen; keine veraltete Plattformannahme aus Project Memory blind übernehmen.

Pro Track/Release dokumentieren:

- Urheberschaft/Autorenbeiträge;
- Generator/Produktionsweg;
- kommerzielle Rechte/Lizenzstatus zum Erzeugungszeitpunkt;
- Samples und deren Clearance oder `none`;
- Voice/Persona-Provenienz;
- Coverrechte;
- AI-Kennzeichnung/Disclosure, soweit Distributor oder DSP sie verlangt;
- Explicit-Kennzeichnung;
- territoriale/rechtliche Blocker.

### Gate E — Rights Ready

Keine kommerzielle Einreichung bei ungeklärter Rechtekette, ungeklärten Samples, unzulässiger Voice-Imitation oder widersprüchlichen Plattformbedingungen.

## Phase 8 — Release Metadata Freeze

Erzeuge `release-metadata.json` mit mindestens:

- primaryArtist;
- albumTitle;
- releaseType;
- trackOrder;
- trackTitles;
- language;
- explicitFlags;
- songwriter/lyricist/composer/producer credits soweit anwendbar;
- copyright/phonographic copyright lines;
- master file refs + checksums wenn verfügbar;
- artwork ref + checksum wenn verfügbar;
- ISRCs, sobald vergeben;
- UPC/EAN, sobald vergeben;
- intendedReleaseDate;
- distributor;
- distributorReleaseId;
- Spotify artist mapping/URI sobald verfügbar.

Änderungen nach Freeze müssen versioniert werden.

## Phase 9 — Distributor Selection und Handoff

Distributor nicht dauerhaft im Skill hardcoden. Unmittelbar vor Auswahl aktuelle offizielle Bedingungen vergleichen, insbesondere:

- akzeptiert der Anbieter die verwendete Produktions-/AI-Herkunft;
- Gebühren/Abo/Revenue Share;
- Rechte-/Takedown-Bedingungen;
- Spotify-Zustellung;
- ISRC/UPC-Verhalten;
- Credits/AI-Metadaten;
- Release-Timing;
- Support für Korrekturen und Artist-Mapping.

Empfehlung mit Quellen und Freshness dokumentieren. Nutzer bestätigt den Distributor, sofern Grilling ihn nicht bereits verbindlich festgelegt hat.

## Phase 10 — Submission

Wenn autorisierte Werkzeuge/Connectoren/Computer Use für den Distributor verfügbar sind, darf die Einreichung nach expliziter Nutzerfreigabe durchgeführt werden. Andernfalls einen exakten Upload-/Metadata-Handoff liefern und auf den bestätigten externen Submission-State warten.

Keine Behauptung `submitted`, `accepted` oder `delivered` ohne verifizierte externe Evidenz.

`release-readiness.json` unterscheidet mindestens:

- `draft`
- `ready-for-submission`
- `submitted`
- `accepted-by-distributor`
- `delivered-to-spotify`
- `live-on-spotify`
- `failed-or-correction-required`

## Phase 11 — Spotify for Artists / Pre-Release

Sobald Artist-/Release-Identifier verfügbar sind:

- Artist-Mapping prüfen;
- Spotify-for-Artists-Zugriff vorbereiten/beantragen, soweit nötig;
- Release-Date und Metadaten prüfen;
- optional Pitch-/Profil-/Bio-/Canvas-/Promo-Schritte nur als separate, ausdrücklich gewünschte Erweiterung behandeln.

Diese Marketing-Schritte sind **nicht** Voraussetzung für das Kernziel `live-on-spotify`.

## Phase 12 — Publication Verification

Der Workflow endet **nicht** mit dem Distributor-Upload.

Am oder nach Release verifizieren:

- Album/Single tatsächlich auf Spotify live;
- richtiger Artist gemappt;
- Titel, Track-Reihenfolge und Artwork korrekt;
- alle Tracks vollständig abspielbar;
- keine falsche Version / kein abgeschnittener Master;
- Explicit/Metadata soweit sichtbar korrekt;
- Spotify Album-/Track-URI bzw. stabile URL erfasst;
- ISRC/UPC/Distributor-ID im Project Second Brain archiviert.

Erzeuge `spotify-publication-record.json` mit Evidenz, Zeitstempel, IDs, Restproblemen und finalem Status.

### Gate F — Published

Nur `live-on-spotify` mit erfolgreicher Playback-/Metadata-Verifikation ist PASS.

`submitted`, `accepted`, `delivered` oder eine geplante Release-Seite sind noch kein Abschluss.

## Release-Loop bei Fehlern

Bei falschem Artist-Mapping, fehlerhaften Metadaten, beschädigtem Audio oder Distributor-Ablehnung:

1. Fehlerklasse bestimmen.
2. Kleinsten ausreichenden Fix durchführen.
3. Betroffene Freeze-/Rights-/Metadata-Gates gezielt revalidieren.
4. Korrektur über Distributor auslösen.
5. Spotify erneut verifizieren.

Keine unnötige Vollproduktion neu starten, wenn nur Metadaten betroffen sind.

## Projekt-Retrospektive

Nach erfolgreicher Veröffentlichung eine kurze Project-Second-Brain-Retrospektive erzeugen:

- welche Prompts/Production-Patterns funktionierten;
- Generator-/DAW-spezifische Grenzen;
- Audio-QC-Findings;
- Distributor-/Spotify-Reibung;
- wiederverwendbare Verbesserungen für künftige Musikprojekte.

Projekt-spezifische Inhalte bleiben im Projekt-Repository. Nur allgemein wiederverwendbare, validierte Erkenntnisse dürfen später Skillz verbessern.

## Stop-Regeln

Blockierend:

- Grilling unvollständig;
- unresolved Major Creative finding vor Lyric Freeze;
- kein vollständiger lossless Master;
- unklare kommerzielle Rechte;
- ungeklärte Samples/Voice-Imitation;
- Distributor akzeptiert die Produktionsherkunft nicht;
- Spotify-Artist-Mapping unklar;
- Track auf Spotify beschädigt oder falsch.

Nicht automatisch blockierend:

- Marketing/Playlist-Pitch fehlt;
- Artist-Bio noch nicht optimiert;
- optionale Apple-Music-/YouTube-Music-Veröffentlichung noch nicht verifiziert;
- Minor Taste-Watchpoints, die bewusst akzeptiert und dokumentiert wurden.

## Abschluss

Der Skill ist abgeschlossen, wenn:

1. alle erforderlichen Grilling-/Creative-/Audio-/Rights-/Metadata-Gates gültig sind;
2. Release über einen aktuell geeigneten Distributor zugestellt wurde;
3. Spotify die Veröffentlichung korrekt live zeigt und Playback geprüft ist;
4. `spotify-publication-record.json` den verifizierten Live-Zustand enthält;
5. der abschließende Zustand im Project Second Brain dokumentiert ist.
