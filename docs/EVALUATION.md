# Skill-Evaluation

Jeder neue oder wesentlich geänderte Skill wird mindestens in drei Fällen geprüft:

1. **Happy Path:** vollständige und konsistente Eingaben führen zum erwarteten Ergebnis.
2. **Grenzfall:** unvollständige, aber sicher behandelbare Eingaben führen zu einer transparenten Annahme oder begrenzten Teilausgabe.
3. **Fehlerfall:** widersprüchliche, unsichere oder nicht ausführbare Eingaben werden erkannt und kontrolliert beendet.

## Ausführbare Fixtures

```text
skills/<skill>/tests/evaluation.json
```

Jede Datei enthält genau `happy-path`, `edge-case` und `failure-case`. Pro Fall werden Input, erforderliche Verhaltensmerkmale, verbotene Verhaltensmerkmale und wörtliche Anker im zugehörigen `SKILL.md` dokumentiert.

Der Runner prüft JSON-Struktur, Skill-Zuordnung, vollständige Fallabdeckung, nicht leere Erwartungen und die Verankerung aller `skillAnchors` im Skilltext.

```bash
python scripts/run_evaluations.py
```

## Aufgezeichnete Ergebnisbewertungen

Konkrete Skill-Ausführungen können als geprüfte Baselines abgelegt werden:

```text
skills/<skill>/tests/results/<case-id>.json
```

Eine Ergebnisbewertung verweist auf einen Fall aus `evaluation.json` und dokumentiert für jedes erforderliche Verhalten `passed: true` mit Evidenz. Für jedes verbotene Verhalten wird `observed: false` mit Evidenz festgehalten. In `main` eingecheckte Baselines müssen insgesamt `overall: pass` besitzen.

```bash
python scripts/score_evaluation_results.py
```

Der Scorer stellt sicher, dass keine Erwartung ausgelassen, kein verbotenes Verhalten beobachtet und jede Bewertung nachvollziehbar belegt wurde. Die Bewertung bleibt absichtlich werkzeugunabhängig: Ein Mensch, ein regelbasierter Prüfer oder ein späterer LLM-Evaluator kann die Evidenz erzeugen, während CI den Vertrag deterministisch kontrolliert.

## Reifegrad

- `draft`: keine vollständige Evaluation
- `candidate`: alle drei Qualitätsfälle einmal bestanden
- `stable`: mehrfach in realen Abläufen wiederverwendet und erneut evaluiert
- `deprecated`: Nachfolger und Migration dokumentiert

Das Datum der letzten Evaluation wird im Frontmatter als `lastEvaluated` geführt.
