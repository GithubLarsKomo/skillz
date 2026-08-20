---
name: llm-prose-pattern-audit
description: Prüft deutsche und englische Sachtexte auf redaktionell relevante Muster generischer LLM-Prosa wie Signifikanzinflation, Pseudoanalyse, rhetorische Templates, Synonymvariation, Hedging, Nominalstil und syntaktische Gleichförmigkeit, ohne daraus KI-Autorschaft zu behaupten. Verwenden vor sprachgenauer Überarbeitung oder zur Stil-Diagnose.
---

# LLM Prose Pattern Audit

## Zweck und Grenze

Erkenne **Editing-Signale, keine Autorschaft**. Ein einzelnes Wort, Satzzeichen oder Muster beweist weder LLM- noch menschliche Autorschaft. Die Analyse fragt ausschließlich, ob ein Merkmal Präzision, Natürlichkeit, Genrepassung oder Informationsdichte beeinträchtigt.

Die ausführliche Taxonomie und Forschungsbasis steht in `references/pattern-taxonomy.md`.

## Workflow

1. Sprache, Genre und Zielgruppe bestimmen.
2. Optional `scripts/style_metrics.py` ausführen und Messwerte als diagnostische Evidenz übernehmen.
3. Muster nur im Kontext markieren. Keine pauschale Wortverbotsliste anwenden.
4. Jeden Befund mit Textstelle, Kategorie, Auswirkung und empfohlener Editieraktion dokumentieren.
5. Priorisieren: semantische Unklarheit und Pseudoanalyse vor kosmetischer Stilvarianz.
6. Deutsch und Englisch getrennt behandeln.

## Kernkategorien

Sprachübergreifend: `generic-significance`, `pseudo-analysis`, `unnecessary-hedging`, `rule-of-three`, `negative-parallelism`, `elegant-variation`, `connector-overuse`, `syntactic-uniformity`, `format-template`, `unsupported-evaluation`, `redundancy`.

Deutsch zusätzlich: `nominalization-density`, `subject-initial-uniformity`, `english-interference-de`, `bureaucratic-register`.

Englisch zusätzlich: `inflated-academic-register`, `participial-pseudo-analysis`, `template-transition-density`.

## Output-Vertrag

```json
{
  "schemaVersion": 1,
  "language": "en",
  "genre": "report",
  "authorshipAssessment": null,
  "findings": [
    {
      "id": "F1",
      "category": "pseudo-analysis",
      "severity": "medium",
      "span": "...",
      "reason": "adds evaluative wording without additional evidence",
      "action": "remove-or-substantiate"
    }
  ],
  "metrics": {},
  "priorities": []
}
```

## Qualitätsregeln

- **Editing-Signale, keine Autorschaft.**
- Keine Eigenschaft allein als Fehler behandeln.
- Terminologiewiederholung nicht als Stilproblem markieren, wenn sie Referenzklarheit erhält.
- Metriken sind **Abweichungsindikatoren, keine Zielwerte**.
- Bei unklarer Wirkung lieber `observe` als zwanghaft umformulieren.

## Abschluss

Abgeschlossen, wenn alle relevanten Befunde kontextbezogen klassifiziert, nach Wirkung priorisiert und ohne Autorschaftsbehauptung an einen Rewriter oder menschlichen Editor übergeben werden können.
