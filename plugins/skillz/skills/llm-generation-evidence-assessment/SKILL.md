---
name: llm-generation-evidence-assessment
description: Bewertet voneinander getrennte Sprach-, Provenienz-, Autorenprofil-, Struktur- und Inhaltsindikatoren darauf, wie stark sie eine LLM-Unterstützung eines Dokuments stützen oder relativieren, ohne unkalibrierte Detector-Scores in Autorschaftswahrscheinlichkeiten umzudeuten. Als Fach-Skill nach Artefaktforensik und Textmuster-Audit verwenden.
---

# LLM Generation Evidence Assessment

## Zweck

Dieser Skill synthetisiert bereits erhobene Evidenz zu einer nachvollziehbaren Aussage über **Hinweise auf LLM-Beteiligung**. Er ist kein universeller AI-Textdetektor und darf keine sichere menschliche oder maschinelle Autorschaft behaupten, wenn keine direkte, überprüfbare Provenienz vorliegt.

Das vollständige Evidenzmodell und die Forschungsbasis stehen in `references/evidence-model.md`.

## Eingänge

Mindestens eines der folgenden Artefakte muss vorliegen:

- `prose-audit.json` aus `llm-prose-pattern-audit`,
- `document-forensics.json` aus `document-generation-forensics`,
- ein belastbares `author-voice-profile.json` plus dokumentierter Vergleich zum Zieltext,
- verifizierte Workflow-Provenienz wie Entwurfsstände, Kommentare, Prompt-/Tool-Protokolle oder signierte Content Credentials,
- externe Detector-Ergebnisse mit Modell-/Versions-, Sprach-, Domänen- und Kalibrierungsinformationen,
- inhaltliche Verifikationsbefunde zu Quellen, Zitaten, Formeln, Claims oder Platzhaltern.

Fehlt eine Evidenzfamilie, wird sie als `not-observed` oder `not-available` dokumentiert, niemals als Gegenbeweis.

## Unabhängige Evidenzfamilien

1. `direct-provenance`: explizite und überprüfbare LLM-/GenAI-Provenienz.
2. `workflow-trace`: Entwurfs-, Kommentar-, Prompt-, Versions- oder Tool-Spuren.
3. `author-voice`: Abweichung oder Übereinstimmung mit authentischen, sprach- und genrepassenden Referenztexten.
4. `prose-patterns`: kombinierte Muster aus `llm-prose-pattern-audit`.
5. `artifact-structure`: formatbezogene Struktur- und Generatorhinweise.
6. `content-integrity`: Quellen-/Zitat-/Claim-/Formel-/Platzhalterauffälligkeiten.
7. `external-detector`: Scores externer Detektoren als ergänzende, kalibrierungsabhängige Evidenz.
8. `counterevidence`: belastbare Spuren eines menschlichen oder nicht-LLM-geprägten Arbeitsprozesses.

Korrelierte Indikatoren nicht doppelt zählen. Beispielsweise sind `rule-of-three`, `format-template` und eine immer gleiche Drei-Bullet-Slide-Struktur oft dieselbe zugrunde liegende Templatisierung und damit keine drei unabhängigen Beweise.

## Bewertungsleiter

`llmEvidenceLevel` verwendet **keine Prozentwerte**:

- `documented`: direkte, überprüfbare Provenienz dokumentiert LLM-Beteiligung am untersuchten Inhalt.
- `strong`: mehrere unabhängige Evidenzfamilien stützen LLM-Beteiligung deutlich; mindestens eine davon muss stärker als bloßes Stil-/Layoutmuster sein.
- `moderate`: mehrere kompatible Indizien sind vorhanden, aber Provenienz fehlt oder wichtige Alternativerklärungen bleiben offen.
- `limited`: einzelne oder schwache Indizien ohne ausreichende Unabhängigkeit.
- `insufficient`: keine belastbare positive Evidenz oder die Datenlage ist zu dünn/widersprüchlich.

Zusätzlich `humanWorkflowEvidenceLevel` als `strong|moderate|limited|none|not-available` ausweisen. Das ist Gegen- bzw. Kontext-Evidenz und beweist nicht, dass überhaupt kein LLM verwendet wurde.

## Entscheidungsregeln

### `documented`

Nur vergeben, wenn die Provenienz den konkreten untersuchten Inhalt nachvollziehbar mit einem LLM-/GenAI-Werkzeug verbindet. Ein frei editierbares `Creator=ChatGPT`-Feld allein reicht nicht; es benötigt zusätzliche Verifikation oder unabhängige Workflow-Evidenz.

### `strong`

Nur vergeben, wenn mindestens zwei **unabhängige** positive Evidenzfamilien vorliegen und mindestens eine davon `direct-provenance`, `workflow-trace`, belastbare `author-voice`-Abweichung oder eine andere inhaltsspezifische, nicht bloß kosmetische Spur ist. Ein externer Detector darf diese Mindestanforderung nicht allein erfüllen.

### `moderate`

Geeignet für konsistente Muster über mehrere Abschnitte oder Artefakte hinweg, wenn zusätzlich mindestens eine weitere Evidenzfamilie stützt, aber Provenienz oder Kalibrierung fehlen.

### `limited`

Für isolierte Stil-, Struktur-, Tooling- oder Detector-Hinweise. Ein einzelnes Wort, Gedankenstrich, Konnektor, Template, Metadatenfeld oder ungewöhnlich sauberes Layout bleibt maximal `limited`, sofern keine unabhängige Stützung existiert.

### `insufficient`

Bei kurzen Texten, stark redigierter Prosa, Übersetzungen, unpassenden Referenzkorpora, unzugänglichen Quelldateien, widersprüchlichen Signalen oder ausschließlich neutralen Tool-Metadaten bevorzugen.

## Author-Voice-Regeln

`author-voice-profiler` nur als Vergleichsbasis nutzen, wenn:

- die Referenztexte authentisch bestätigt sind,
- Sprache und Genre hinreichend passen,
- ausreichend Text für stabile Beobachtungen vorhanden ist,
- bekannte starke Redaktion/Übersetzung/Koautorenschaft dokumentiert ist.

Voice-Mismatch ist keine Identitätsforensik. Bei unpassendem Genre oder zu kleinem Korpus die Evidenz abwerten.

## External-Detector-Regeln

- Score, Tool, Version, Sprache, Domäne, Textlänge und bekannte Kalibrierung separat protokollieren.
- Einen Detector-Score niemals direkt als `P(LLM)` interpretieren.
- Unbekannte False-Positive-Rate, nicht passende Sprache/Domäne oder adversarielle/paraphrasierte Texte führen zur Abwertung.
- Detector-Ergebnis allein ergibt maximal `limited`.
- In Hochrisikokontexten darf ein Detector-Ergebnis nie allein Grundlage für Sanktion, Personalentscheidung oder Täuschungsvorwurf sein.

## Output-Vertrag

```json
{
  "schemaVersion": 1,
  "llmEvidenceLevel": "moderate",
  "humanWorkflowEvidenceLevel": "limited",
  "conclusion": "Mehrere unabhängige Indizien sind mit LLM-Unterstützung vereinbar; direkte Provenienz fehlt.",
  "confidenceInAssessment": "medium",
  "evidence": [
    {
      "family": "prose-patterns",
      "direction": "supports-llm",
      "strength": "limited",
      "source": "prose-audit.json#F3-F8",
      "reason": "multiple contextual patterns across independent sections",
      "alternativeExplanations": ["corporate template", "heavy copy-editing"]
    }
  ],
  "counterevidence": [],
  "externalDetectorScores": [],
  "limitations": [],
  "recommendedFollowUp": []
}
```

## Berichtssprache

- `documented`: „Dokumentierte LLM-Beteiligung“ nur bei erfüllter Provenienzregel.
- `strong`: „Starke Hinweise auf LLM-Beteiligung“, nicht „von KI geschrieben“.
- `moderate`: „Mehrere Hinweise, aber keine belastbare Provenienz“.
- `limited`: „Einzelne schwache Hinweise“.
- `insufficient`: „Keine belastbare Aussage möglich“.

## Qualitätsgate

- Keine numerische Autorschaftswahrscheinlichkeit aus heuristischen Merkmalen.
- Kein `documented` aus frei editierbaren Metadaten allein.
- Kein `strong` aus nur einer Evidenzfamilie.
- Externe Detector-Scores nie allein entscheidend.
- Pro- und Gegenindikatoren sowie Alternativerklärungen sichtbar machen.
- Abwesenheit eines Signals nie automatisch als Beweis menschlicher Autorschaft behandeln.

## Abschluss

Abgeschlossen, wenn jede verwendete Evidenz auf eine Quelle zurückgeführt, Korrelationen und Alternativerklärungen berücksichtigt, Gegenindikatoren dokumentiert und `llmEvidenceLevel` sowie Unsicherheit ohne überzogene Autorschaftsbehauptung begründet sind.
