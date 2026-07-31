# Skill-Evaluation

Jeder neue oder wesentlich geänderte Skill wird mindestens in drei Fällen geprüft:

1. **Happy Path:** vollständige und konsistente Eingaben führen zum erwarteten Ergebnis.
2. **Grenzfall:** unvollständige, aber sicher behandelbare Eingaben führen zu einer transparenten Annahme oder begrenzten Teilausgabe.
3. **Fehlerfall:** widersprüchliche, unsichere oder nicht ausführbare Eingaben werden erkannt und kontrolliert beendet.

## Fixture-Struktur

```text
skills/<skill>/tests/
  happy-path/
    input.md
    expectations.md
  edge-case/
    input.md
    expectations.md
  failure-case/
    input.md
    expectations.md
```

`expectations.md` beschreibt beobachtbare Eigenschaften statt eines einzigen wortgleichen Outputs. Dazu gehören erforderliche Abschnitte, verbotene Behauptungen, Abschlussnachweise und erwartete Übergaben.

## Reifegrad

- `draft`: keine vollständige Evaluation
- `candidate`: alle drei Qualitätsfälle einmal bestanden
- `stable`: mehrfach in realen Abläufen wiederverwendet und erneut evaluiert
- `deprecated`: Nachfolger und Migration dokumentiert

Das Datum der letzten Evaluation wird im Frontmatter als `lastEvaluated` geführt.
