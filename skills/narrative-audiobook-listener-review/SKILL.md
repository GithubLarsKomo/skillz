---
name: narrative-audiobook-listener-review
description: Prüft finale narrative Prosa aus der Perspektive eines anspruchsvollen Hörbuchnutzers ohne Bildschirm auf Verständlichkeit, Figuren-/POV-Orientierung, Dialogzuordnung, Rhythmus, Hörermüdung, Kapitelwiedereinstieg und TTS-Robustheit, ohne literarische Eigenart in Tutorial-Sprache umzuschreiben. Verwenden als Gate vor Creative-Writing-EPUB-Ausgabe; nicht als Fakten-, Canon- oder Voice-Audio-Performance-Review.
userFacing: false
implicitInvocation: true
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires: []
outputs:
  - narrative-listener-review.json
  - narrative-listener-review.md
lastEvaluated: 2026-09-06
---

# Narrative Audiobook Listener Review

## Zweck

Prüfe, ob ein literarischer Text **gehört** funktioniert. Die Perspektive ist ein erfahrener Hörbuchnutzer, nicht ein Lektor und nicht ein Fachreviewer.

## Grundsatz

**Hörbarkeit ohne literarische Glättung.**

Absichtliche Fragmente, Rhythmuswechsel, Mehrdeutigkeit, Dialekt, ungewöhnliche Syntax oder knappe Dialoge dürfen bestehen bleiben, wenn sie als Hörerlebnis funktionieren.

## Prüfdimensionen

### Orientierung

- Ist nach Kapitel-/POV-Wechseln klar genug, wo und bei wem man ist?
- Kann man nach einer längeren Pause wieder einsteigen?

### Dialog

- Ist Sprecherzuordnung ohne visuelle Anführungszeichen ausreichend nachvollziehbar?
- Werden Dialogtags über- oder unterverwendet?
- Funktionieren schnelle Sprecherwechsel in Audio?

### POV und Figuren

- Bleiben Innen-/Außenperspektive und Stimmen unterscheidbar?
- Entsteht bei Ensemblekapiteln vermeidbare Namens- oder Rollenverwirrung?

### Rhythmus und Prosodie

- Trägt Satzrhythmus beim Hören?
- Werden sehr lange Sätze ohne visuelle Hilfe unverständlich?
- Sind bewusste Fragmente hörbar sinnvoll?

### Informationsdichte

- Müssen zu viele Namen, Orte oder Begriffe gleichzeitig im Arbeitsgedächtnis gehalten werden?
- Sind Worldbuilding-Blöcke akustisch verdaulich?

### Kapitelarchitektur

- Haben Kapitel klare Einstiegspunkte?
- Gibt es natürliche Pausen?
- Funktioniert ein Kapitelende als hörbarer Abschluss oder Zug?

### TTS-Robustheit

Textuell prüfen:

- ungewöhnliche Abkürzungen;
- Zahlen/Symbole;
- Fremdwörter und erfundene Namen mit hohem Aussprache-Risiko;
- typografische Bedeutungen, die beim Vorlesen verloren gehen könnten.

Keine tatsächliche Aussprachequalität behaupten, solange kein Audio gehört wurde.

## Findings

`severity`: `minor|major|critical`.

`gateStatus`:

- `pass`;
- `minor_revision`;
- `major_revision`;
- `fail`.

Finale Creative-Writing-EPUB-Ausgabe nur bei `gateStatus=pass`.

## Schutzregeln

- **Kein Tutorial-Stil für Fiction erzwingen.**
- Literarische Mehrdeutigkeit ist nicht automatisch Hörfehler.
- Dialog nicht mit unnötigen Sprecherattributen überladen.
- Keine tatsächliche Stimme oder ElevenReader-Aussprache simuliert behaupten.
- Findings müssen konkrete Hörerwirkung benennen.

## Abschluss

Abgeschlossen, wenn Hörbarkeit, Ermüdung, Orientierung, Dialog, Wiedereinstieg und TTS-Robustheit bewertet und ein belastbarer Gate-Status ausgegeben wurden.
