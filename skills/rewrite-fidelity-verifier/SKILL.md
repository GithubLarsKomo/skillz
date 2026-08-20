---
name: rewrite-fidelity-verifier
description: Vergleicht Ausgangs- und überarbeiteten Sachtext auf fachliche und epistemische Treue, einschließlich Zahlen, Quellen, Terminologie, Negationen, Modalität, Bedingungen, Kausalität und Claims. Verwenden nach sprachlicher Überarbeitung, um stilistische Verbesserung von inhaltlicher Veränderung zu trennen.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires: []
outputs:
  - rewrite-fidelity.json
  - fidelity-review.md
lastEvaluated: 2026-08-20
---

# Rewrite Fidelity Verifier

## Zweck

Beweise nicht, dass zwei Texte identisch sind, sondern finde Stellen, an denen ein sprachlicher Rewrite möglicherweise die fachliche Bedeutung verändert hat.

## Workflow

1. Quelle und Rewrite segmentweise ausrichten.
2. Optional `scripts/fidelity_tokens.py` ausführen, um konservativ Zahlen, Einheiten, DOI/PMID/URLs, nummerierte Referenzen und vorgegebene Fachtermini zu vergleichen.
3. Claims, Negationen, Bedingungen, Ausnahmen, Zeitbezug, Modalität und Hedging semantisch vergleichen.
4. Ursache-Wirkungs-Beziehungen besonders prüfen; stilistische Straffung darf keine neue Kausalität erzeugen.
5. Jede relevante Differenz klassifizieren.
6. Bei `added` oder `removed` eines fachlichen Claims sowie nicht autorisierten Zahlen-/Quellenänderungen Hard Fail auslösen.

## Klassifikation

- `preserved`: Bedeutung erhalten
- `clarified`: Bedeutung expliziter, ohne Informationszuwachs
- `potentially_changed`: Bedeutung könnte verschoben sein; Review nötig
- `added`: neue Information oder neue Aussage
- `removed`: relevante Information fehlt

## Output-Vertrag

```json
{
  "schemaVersion": 1,
  "status": "pass|review|fail",
  "differences": [
    {"type": "potentially_changed", "dimension": "modality", "source": "...", "target": "...", "reason": "..."}
  ],
  "tokenCheck": {},
  "hardFailures": []
}
```

## Prüfregeln

- **Ein neu hinzugefügter fachlicher Claim ist ein Hard Fail.**
- Zahlen- oder Quellenänderungen ohne expliziten Auftrag sind Hard Fail.
- `unknown`, `not assessed`, `not available` und ähnliche epistemisch unterschiedliche Aussagen dürfen nicht gleichgesetzt werden.
- `may`, `could`, `likely`, `supports`, `demonstrates` und ihre deutschen Entsprechungen als Modalitäts-/Evidenzmarker behandeln.
- Terminologiewechsel prüfen, wenn er Referenz oder Scope verändern könnte.
- Deterministische Token-Gleichheit beweist keine semantische Gleichheit.

## Abschluss

Abgeschlossen, wenn alle entscheidungsrelevanten Differenzen klassifiziert, Hard Fails sichtbar und unklare semantische Änderungen als Review-Punkte markiert sind.
