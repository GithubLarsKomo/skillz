---
name: precision-writing-revision
description: Orchestriert die sprachgenaue Überarbeitung deutscher oder englischer Reports, Memos und Sachtexte durch Muster-Audit, optionales Author-Voice-Profil, Precision Rewrite und anschließende Fidelity-Prüfung. Verwenden, wenn ein vollständiger wiederholbarer Editierworkflow statt einer isolierten Umformulierung gewünscht ist.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
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
lastEvaluated: 2026-08-20
---

# Precision Writing Revision

## Rolle

Dieser Skill ist ein **dünner Orchestrator**. Er koordiniert vier Fach-Skills und dupliziert deren Stil-, Profil- oder Fidelity-Logik nicht.

## Ablauf

1. **Kontext fixieren:** Sprache, Genre, Zielgruppe, Modus und bei Englisch Zielvariante bestimmen.
2. **Audit:** `llm-prose-pattern-audit` ausführen.
3. **Author Voice:** Nur bei `mode=author` ein vorhandenes belastbares `author-voice-profile.json` verwenden oder bei explizitem Auftrag `author-voice-profiler` ausführen. Fehlt ein Profil, dokumentiert auf Genre-/Sprachregeln zurückfallen.
4. **Fidelity Lock:** Claims, Zahlen, Quellen, Negationen, Bedingungen, Zeitbezug, Modalität und geschützte Terminologie aus Quelle beziehungsweise vorhandener Evidence Note fixieren.
5. **Rewrite:** `precision-language-rewriter` mit Audit, Profil und Fidelity Lock ausführen.
6. **Verification:** `rewrite-fidelity-verifier` ausführen.
7. **Korrekturschleife:** Bei `review` nur markierte Stellen nacharbeiten und erneut prüfen. Bei Hard Fail die betroffene Änderung zurücknehmen oder fachlich autorisieren lassen.
8. **Ausgabe:** finalen Text plus kompakten Revisionsbericht liefern.

## Integrationen

Wenn eine Recherche bereits durch `research-to-evidence-note` strukturiert wurde, deren Claims und Confidence als bevorzugte Fidelity-Basis verwenden. Bei Dokumentproduktion wird nur der sprachlich verifizierte Endtext an DOCX/PDF-Renderer weitergereicht.

## Modusgrenzen

- `light`: lokale Entglättung und Präzisierung
- `author`: zusätzlich bestätigte persönliche Voice
- `editorial`: stärkere Absatzredaktion, aber unveränderte Fakten- und Claim-Grenze

## Output

```json
{
  "schemaVersion": 1,
  "mode": "author",
  "language": "en",
  "genre": "report",
  "audit": "prose-audit.json",
  "authorProfile": "author-voice-profile.json",
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
- Orchestrator bleibt dünn und verändert nicht selbst Fachlogik.

## Abschluss

Abgeschlossen, wenn der finale Text das gewünschte Sprach-/Genre-/Modusprofil erfüllt, der Fidelity-Verifier `pass` meldet oder verbleibende Review-Punkte ausdrücklich autorisiert sind und der Revisionsbericht den Ablauf nachvollziehbar macht.
