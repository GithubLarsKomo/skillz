---
name: source-to-context
description: Normalisiert bereits geladene Quelleninhalte in einen provider-neutralen, provenance-erhaltenden Kontextvertrag mit stabilen Segmentgrenzen, Digests, Extraktionshinweisen und expliziten Datenlücken. Verwenden, wenn Web-, Datei-, OCR-, PDF-, Datenbank- oder Connector-Inhalte vor Research, Evidence-Synthese oder Knowledge-Artifacts vereinheitlicht werden sollen, ohne Retrieval oder fachliche Schlussfolgerungen zu duplizieren.
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
outputs:
  - source-context.json
  - source-context.md
lastEvaluated: 2026-08-03
implicitInvocation: true
---

# Source to Context

## Zweck und Grenze

Erzeuge aus **bereits verfügbaren** Quelleninhalten einen stabilen Kontextvertrag. Der Skill normalisiert Form, Grenzen und Provenance; er recherchiert, lädt, OCRt oder interpretiert die Quelle nicht selbst.

Upstream können Browser, Web-Suche, Drive, GitHub, Datenbanken, PDF-/Dokumentenparser, OCR oder andere Connectoren stehen. Downstream kann insbesondere `research-to-evidence-note` die normalisierten Segmente als Evidenzbasis verwenden.

## Trigger

Verwenden, wenn:
- Inhalte aus unterschiedlichen Retrieval-/Extraktionswegen in ein gemeinsames Format gebracht werden sollen,
- Seiten-, Abschnitts-, Block- oder Chunk-Grenzen für spätere Zitate erhalten bleiben müssen,
- Extraktionslücken, Truncation oder stale Metadaten explizit sichtbar sein sollen,
- downstream Research nicht von provider-spezifischen Payloads abhängen soll.

## Voraussetzungen

Mindestens erforderlich:
- eine stabile Quellenreferenz oder lokale Source-ID,
- bereits geladener/extrahierter Inhalt oder explizite Information, dass Inhalt fehlt,
- soweit verfügbar Retrieval-/Observed-Zeitpunkt und Originalgrenzen.

Fehlende Informationen bleiben `unknown` oder als `gaps` markiert. Sie werden nicht ergänzt.

## Output-Vertrag

### `source-context.json`

```json
{
  "schemaVersion": 1,
  "source": {
    "id": "stable-source-id",
    "reference": "uri-or-connector-ref",
    "title": "optional",
    "language": "de",
    "retrievedAt": "ISO-8601",
    "observedAt": "ISO-8601",
    "extractionMethod": "connector|parser|ocr|manual|unknown",
    "contentSha256": "sha256"
  },
  "segments": [
    {
      "id": "stable-segment-id",
      "ordinal": 1,
      "locator": {"page": 1, "section": "...", "block": "..."},
      "text": "exact normalized source text",
      "textSha256": "sha256",
      "normalizationNotes": [],
      "quality": {"state": "complete|partial|unreadable|unknown", "confidence": "high|medium|low|unknown"}
    }
  ],
  "gaps": [],
  "truncated": false,
  "stale": false,
  "normalization": {"lossy": false, "notes": []}
}
```

### `source-context.md`

Optionale menschlich lesbare Projektion. Sie muss Source-ID, Referenz, Segment-IDs, Locators, Qualitätszustände und Datenlücken erhalten. JSON bleibt der präzisere Maschinenvertrag.

## Identität und Digests

Source-ID wird von einer vorhandenen stabilen Identität übernommen, wenn verfügbar. Eine Formatkonvertierung erzeugt keine neue logische Quelle.

Segment-IDs sind deterministisch innerhalb der Quelle und müssen bei identischem Input und identischen Originalgrenzen stabil bleiben. Geeignete Inputs sind Source-ID plus Original-Locator bzw. – falls kein Locator existiert – eine dokumentierte stabile Segmentierungsregel.

`contentSha256` und `textSha256` beziehen sich auf die tatsächlich verwendeten normalisierten Inhalte. Digests ersetzen keine Source-Provenance.

## Grenzen erhalten

Originale Seiten-, Abschnitts-, Absatz-, Tabellen-, Block- oder Datensatzgrenzen werden soweit technisch vorhanden als `locator` erhalten. Mehrere Originalblöcke dürfen zusammengeführt werden, wenn die Zuordnung nachvollziehbar bleibt; ein Segment darf nicht so umgebaut werden, dass eine spätere Quellenlokalisierung unmöglich wird.

## Normalisierung

Zulässig sind mechanische, dokumentierbare Transformationen wie:
- Zeichencodierung vereinheitlichen,
- technische Zeilenumbrüche normalisieren,
- eindeutig technische Wrapper entfernen,
- vorhandene Strukturmarker in neutrale Locators übertragen.

Nicht zulässig sind stilles Paraphrasieren, Zusammenfassen, Übersetzen, Ergänzen fehlender Sätze oder fachliche Korrektur der Quelle. Solche Schritte gehören downstream oder in einen expliziten separaten Transformationsvertrag.

## Unsicherheit und Extraktionsqualität

OCR-/Parser-/Connector-Unsicherheit wird nicht als sicherer Originaltext ausgegeben. Bei unvollständiger Extraktion:
- betroffene Segmente als `partial`, `unreadable` oder `unknown` markieren,
- konkrete bekannte Lücken unter `gaps` aufführen,
- `normalization.lossy=true` setzen, wenn Inhalte/Struktur verloren gingen,
- keine fehlenden Zeichen, Wörter, Tabellenzellen oder Abschnitte erfinden.

`truncated=true` kennzeichnet bewusst oder technisch abgeschnittenen Input. `stale=true` kennzeichnet Quellenmetadaten oder Inhalt, deren Aktualität für den Downstream-Kontext fraglich ist.

## Provenance

Der Kontextvertrag erhält die ursprüngliche Quelle und den Retrieval-/Extraktionspfad, soweit bekannt. Provider-spezifische Rohpayloads müssen nicht persistiert werden; stabile Referenzen und für Audit relevante Extraktionsmetadaten reichen aus.

Eine URL, Datei, Message-ID, Dokument-ID oder Connector-Referenz ist Herkunft, keine Aussage über inhaltliche Autorität. Der Skill bewertet nicht, ob die Quelle glaubwürdig oder fachlich richtig ist.

## Workflow

1. Source-Scope und vorhandene Referenzen fixieren.
2. Bereits gelieferten Inhalt und Originalgrenzen inventarisieren.
3. Source-Metadaten ohne neue Fakten normalisieren.
4. Segmente deterministisch ordnen und identifizieren.
5. Mechanische Textnormalisierung durchführen und dokumentieren.
6. Digests über den tatsächlich verwendeten Kontext bilden.
7. Truncation, stale state, Extraktionsfehler und Datenlücken explizit erfassen.
8. JSON erzeugen und optional Markdown spiegeln.
9. Prüfen, dass jedes Segment auf die Quelle bzw. einen nachvollziehbaren Locator zurückgeführt werden kann.

## Downstream-Grenze

`source-to-context` erzeugt **keine Claims**. `research-to-evidence-note` oder andere Research-Skills können aus den Segmenten Claims, Quellenqualität, Konflikte und Synthesen erarbeiten. Diese Schlussfolgerungen dürfen nicht rückwirkend als Originaltext in `source-context` geschrieben werden.

`structured-knowledge-artifact` kann einen Source-Context oder daraus erzeugte Evidence-Notes adressierbar verpacken, ändert aber ebenfalls nicht den Quelleninhalt.

## Datenschutz und Persistenz

Nur für den Downstream erforderliche Inhalte und Provenance persistieren. Secrets, Credentials, unnötige personenbezogene Rohdaten oder komplette Connector-Payloads nicht allein aus Bequemlichkeit in den Kontextvertrag kopieren.

## Qualitätsgate

Bestanden nur wenn:
- Source- und Segmentidentitäten stabil und nachvollziehbar sind,
- Originalgrenzen/Locators soweit verfügbar erhalten bleiben,
- mechanische Normalisierung und mögliche Verluste sichtbar sind,
- Truncation, stale state und Extraktionslücken explizit bleiben,
- kein fehlender oder unlesbarer Inhalt erfunden wird,
- keine Claims, Übersetzungen oder Zusammenfassungen als Originalquelle ausgegeben werden,
- gleiche Inputs unter gleicher Segmentierungsregel dieselbe Reihenfolge und Identität erzeugen.

## Memory Path

At completion, extract only confirmed, reusable, non-sensitive learnings that remain useful beyond the current run. Current task state, open follow-ups, tool snapshots, speculative hypotheses, secrets, sensitive personal data and raw connector payloads remain run-only. Encode eligible candidates using `memory-candidate-handoff-v1` from `docs/MEMORY-PATH-CONTRACT.md`, preserve provenance and freshness, and pass the ephemeral handoff to `communication-memory-governance`. The producing skill does not persist memory and never claims persistence succeeded without confirmation from the memory layer.

