---
name: regulatory-evidence-traceability
description: Verwandelt regulatorische Quellen, Verpflichtungen und ausdrücklich markierte Interpretationen in stabile Requirement-to-Evidence-Verknüpfungen mit Provenance, Freshness und Gap-Status. Verwenden als gemeinsamen Evidence-Kern für EU-/FDA-/QMS-Spezialisten; der Skill entscheidet selbst weder Compliance noch Klassifikation oder Zulassung.
---

# Regulatory Evidence Traceability

## Zweck

Dieser Skill ist der gemeinsame Provenance- und Traceability-Kern für regulatorische Fach-Skills. Er übersetzt belegte regulatorische Aussagen in nachvollziehbare Links von Quelle und Verpflichtung über Produktanforderung und Interpretation bis zu Evidenz und Status, ohne selbst eine positive Compliance-, Klassifikations- oder Zulassungsentscheidung zu treffen.

## Trigger

Verwenden, wenn ein nachgelagerter Regulatory-/QMS-Skill belastbare, wiederverwendbare Evidence Contracts benötigt oder wenn Quellen, Interpretationen, Anforderungen und Nachweise über mehrere Artefakte konsistent verbunden werden müssen.

Nicht verwenden als Ersatz für `research-to-evidence-note`, `two-axis-compliance-review`, `medical-device-risk-management-iso14971` oder einen markt-/pathway-spezifischen Spezialisten.

## Grundregeln

- Trenne `regulation-law`, `standard`, `guidance`, `organizational-policy`, `interpretation` und `project-decision`.
- Eine Interpretation übernimmt niemals stillschweigend die Autorität ihrer Quelle. Quelle und abgeleitete Aussage bleiben getrennte Knoten.
- Zeitabhängige Fakten tragen `asOf`; volatile Guidance-/Datenbank-/Programmstände zusätzlich `reviewAfter` oder `expiresAt`.
- Sekundärquellen dürfen bei der Recherche helfen, aber zentrale regulatorische Claims benötigen eine nachvollziehbare autoritative Primärquelle oder bleiben als Gap markiert.
- Fehlende Evidenz ist `missing|partial|unknown`, niemals implizit `satisfied`.
- Ein vollständiger Evidence-Link beweist noch keine Compliance oder Wirksamkeit; diese Entscheidung gehört zu `two-axis-compliance-review` oder einem Fach-Skill.
- Volltexte lizenzierter Standards werden nicht reproduziert. Referenziere normativ relevante Stellen nur im zulässigen Umfang und bewahre organisationsinterne Volltexte außerhalb portabler Skill-Artefakte auf.

## Stabile Identität

Jeder Claim bzw. jede Requirement-Verknüpfung erhält eine stabile ID, die nicht nur von frei formulierter Prosa abhängt. Nutze soweit vorhanden:

- Jurisdiktion/Regime,
- Authority Class,
- Source Identifier und Revision,
- Artikel/Anhang/Section/Locator,
- normalisierten Gegenstand der Aussage.

Wenn sich nur die Formulierung ändert, soll dieselbe fachliche Verpflichtung nicht unnötig eine neue Identität erhalten. Ändert sich die normative Quelle oder fachliche Bedeutung, wird eine neue Version/Lineage erzeugt.

## Workflow

### 1. Scope fixieren

Übernimm Produkt-/Markt-/Lifecycle-Kontext aus `regulated-product-context`. Formuliere die konkrete regulatorische Frage und die erwarteten Consumers.

### 2. Quellen inventarisieren

Übernimm evidenzgebundene Research Notes. Erfasse pro Quelle mindestens Authority Class, Identifier, Revision/Datum, Locator, Source Reference, `asOf` und Freshness.

### 3. Claims und Verpflichtungen separieren

Trenne:

- wörtlich bzw. eng paraphrasierte normative Aussage,
- fachliche Interpretation,
- Anwendbarkeitsannahme,
- daraus abgeleitete Produkt-/Prozessanforderung.

Unklare Anwendbarkeit wird nicht durch eine Interpretation geschlossen.

### 4. Evidence Links bilden

Verknüpfe nach Möglichkeit:

`source -> obligation/claim -> interpretation -> product/process requirement -> implementation/control -> verification -> evidence -> status`

Nicht vorhandene Glieder bleiben explizite Gaps.

### 5. Widersprüche und Freshness prüfen

Markiere konkurrierende Guidance, veraltete Revisionen, widersprüchliche Quellen oder stale Daten. Neuere Veröffentlichung ersetzt ältere nicht automatisch, wenn Scope oder Status abweichen.

### 6. Outputs erzeugen

`regulatory-evidence-map.json` enthält die stabilen Beziehungen. `regulatory-evidence-gaps.json` enthält ausschließlich offene Provenance-, Applicability-, Verification- oder Freshness-Lücken mit einem klaren nächsten Evidenzschritt.

## Output-Verträge

### `regulatory-evidence-map.json`

Enthält mindestens:

```json
{
  "schemaVersion": 1,
  "asOf": "ISO-8601",
  "scope": {},
  "sources": [],
  "claims": [],
  "requirements": [],
  "evidence": [],
  "links": [],
  "conflicts": []
}
```

Jeder regulatorisch relevante Claim verweist auf Source/Locator und unterscheidet normative Aussage von Interpretation.

### `regulatory-evidence-gaps.json`

Enthält mindestens Gap-ID, betroffenen Claim/Requirement-Link, Gap-Typ, benötigte Evidenz, Owner/Consumer soweit bekannt, Freshness-Bedingung und Stop Condition.

## Downstream

Typische Consumers sind `mdcg-guidance-navigator`, `ivdr-device-classification`, EU-/FDA-Frontdoors, `two-axis-compliance-review`, Submission-/Report-Builder und `controlled-quality-documentation`.

Der Skill aggregiert deren Entscheidungen nicht zurück und erzeugt keine eigene regulatorische Freigabe.

## Memory Path

Persistenzwürdig sind nur bestätigte, wiederverwendbare Traceability-Muster, stabile projektspezifische Regulatory Constraints oder validierte Source-to-Requirement-Heuristiken. Einzelne Suchtreffer, aktuelle Guidance-Snapshots, offene Gaps, laufende Klassifikationshypothesen und momentane Toolzustände bleiben run-only. Regulatory Memory Candidates müssen `sourceRefs`, Authority Class und bei zeitabhängigen Inhalten `observedAt/asOf` plus `reviewAfter` oder `expiresAt` tragen. Übergib Kandidaten als `memory-candidate-handoff-v1` an `communication-memory-governance`; dieser Skill persistiert nichts selbst und behauptet keine erfolgreiche Speicherung.

## Qualitätsgate

Bestanden nur wenn:

- zentrale Claims eine nachvollziehbare Quelle und Locator besitzen,
- normative Aussage und Interpretation getrennt bleiben,
- Freshness für volatile Inhalte sichtbar ist,
- fehlende Evidenz als Gap erhalten bleibt,
- keine Compliance-/Klassifikations-/Zulassungsentscheidung simuliert wird,
- Downstream-Consumers die Artefakte ohne zusätzliche mündliche Erklärung übernehmen können,
- Memory Candidates die Governance- und Freshness-Regeln einhalten.
