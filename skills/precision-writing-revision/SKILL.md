---
name: precision-writing-revision
description: Orchestriert die sprachgenaue Überarbeitung deutscher oder englischer Reports, Memos, Sachtexte, Reden, Sprechertexte und Folientexte durch Muster-Audit, optionales Author-/Speaker-Voice-Profil, Precision Rewrite und anschließende Fidelity-Prüfung.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.2.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - author-voice-profiler
  - llm-prose-pattern-audit
  - precision-language-rewriter
  - rewrite-fidelity-verifier
outputs:
  - final-revised-text
  - precision-writing-report.json
lastEvaluated: 2026-08-23
---

# Precision Writing Revision

## Rolle

Dieser Skill ist ein **dünner Orchestrator**. Er koordiniert vier Fach-Skills und dupliziert deren Stil-, Profil- oder Fidelity-Logik nicht. Er ist die gemeinsame Sprachoptimierungsstufe für dokumentbasierte und gesprochene Kommunikation.

## Genres

Unterstützt werden `report|memo|general|speech|speaker-notes|slide-copy` in `de|en`.

## Ablauf

1. **Kontext fixieren:** Sprache, Genre, Zielgruppe, Modus und bei Englisch Zielvariante bestimmen.
2. **Audit:** `llm-prose-pattern-audit` ausführen; bei gesprochener Sprache Muster als Editing-Signale, nicht als starre Report-Regeln interpretieren.
3. **Voice:** Bei `mode=author` ein belastbares `author-voice-profile.json` beziehungsweise bei Speaking-Workflows ein kompatibles `speaker-profile.json` verwenden. Fehlt ein Profil, dokumentiert auf Genre-/Sprachregeln zurückfallen.
4. **Fidelity Lock:** Claims, Zahlen, Quellen, Negationen, Bedingungen, Zeitbezug, Modalität und geschützte Terminologie fixieren.
5. **Rewrite:** `precision-language-rewriter` mit Sprache, Genre, Audit, Profil und Fidelity Lock ausführen.
6. **Verification:** `rewrite-fidelity-verifier` ausführen.
7. **Korrekturschleife:** Nur markierte Stellen nacharbeiten und erneut prüfen. Bei Hard Fail Änderung zurücknehmen oder fachlich autorisieren lassen.
8. **Ausgabe:** finalen Text plus kompakten Revisionsbericht liefern.

## Speaking-Integration

### Rede

`speech-writer → precision-writing-revision(genre=speech) → speech-review`

Die Optimierung darf die Dramaturgie und bewusst gesetzte rhetorische Wiederholungen nicht versehentlich als Redundanz entfernen.

### Vortrag

Zwei getrennte Sprachpfade verwenden:

- On-Slide-Text: `slide-architect → precision-writing-revision(genre=slide-copy)`
- gesprochener Vortrag/Speaker Notes: `presentation-writer → precision-writing-revision(genre=speaker-notes)`

Danach führt `presentation-review` beide Ebenen wieder zusammen. Eine Kürzung auf der Folie darf keine fachliche Information verlieren; ausführliche Inhalte werden bei Bedarf in Speaker Notes verschoben.

## Modusgrenzen

- `light`: lokale Entglättung und Präzisierung
- `author`: zusätzlich bestätigte persönliche Voice beziehungsweise Speaker Voice
- `editorial`: stärkere Absatz-/Passagenredaktion, aber unveränderte Fakten- und Claim-Grenze

## Output

```json
{
  "schemaVersion": 1,
  "mode": "author",
  "language": "en",
  "genre": "speaker-notes",
  "audit": "prose-audit.json",
  "voiceProfile": "speaker-profile.json",
  "fidelityStatus": "pass",
  "correctionPasses": 0,
  "warnings": []
}
```

## Qualitätsgate

- **Fidelity vor Stil.**
- Kein finaler Text bei ungeklärtem Hard Fail.
- Kein persönlicher Stil ohne belastbare Profilbasis behaupten.
- Kein Detector-Evasion-Ziel einführen.
- Gesprochene Sprache wird nicht auf Report-Prosa normalisiert.
- Orchestrator bleibt dünn und verändert nicht selbst Fachlogik.

## Abschluss

Abgeschlossen, wenn der finale Text das gewünschte Sprach-/Genre-/Modusprofil erfüllt, der Fidelity-Verifier `pass` meldet oder verbleibende Review-Punkte ausdrücklich autorisiert sind und der Revisionsbericht den Ablauf nachvollziehbar macht.
