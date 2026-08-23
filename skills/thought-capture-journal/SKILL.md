---
name: thought-capture-journal
description: Normalisiert fortlaufend aufgezeichnete, unstrukturierte Gedanken aus einer einzelnen datierten Markdown- oder Textdatei zu einem nachvollziehbaren Thought Journal. Verwenden, wenn Ideen per Smartphone, Diktat oder Quick-Note gesammelt und anschließend für Graphanalyse vorbereitet werden sollen; der Skill interpretiert noch keine Beziehungen zwischen Gedanken.
userFacing: true
implicitInvocation: true
category: productivity
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires: []
outputs:
  - thought-journal.md
  - thought-journal.json
lastEvaluated: 2026-08-23
---

# Thought Capture Journal

## Zweck

Überführe eine pragmatische, fortlaufende Gedankensammlung in ein stabiles Importformat. Die Erfassung soll auf dem Smartphone möglichst reibungsarm sein und darf zunächst bewusst unstrukturiert bleiben.

## Empfohlener Capture-Workflow

Für Android ist **Markor QuickNote** der Standardvorschlag: QuickNote ist eine frei wählbare einzelne Markdown-Datei, Markor ist freie Open-Source-Software, arbeitet offline und bietet eine Date/Time-Aktion. Diktat erfolgt pragmatisch über die Spracheingabe der installierten Android-Tastatur, z. B. Gboard. Wenn Markor nicht verfügbar oder nicht gewünscht ist, ist jede App zulässig, die eine einzelne exportierbare UTF-8-Text-/Markdown-Datei ohne proprietären Lock-in erzeugt.

Empfohlenes Minimalformat:

```markdown
## 2026-08-23 22:17
Gedanke frei diktiert oder geschrieben.

## 2026-08-24 07:42
Nächster Gedanke. Darf fragmentarisch sein.
```

Akzeptiere auch Zeilenpräfixe wie `2026-08-23T22:17`, lokale Datumsformate oder undatierte Blöcke. Undatierte Einträge werden markiert, nicht erfunden.

## Eingaben

- eine einzelne `.md`- oder `.txt`-Datei oder deren vollständiger Inhalt,
- optional Zeitzone und Sprache,
- optional bekannte Projekt-/Themenbezeichnung.

## Workflow

1. Datei unverändert als Quelle inventarisieren.
2. Einträge anhand vorhandener Zeitstempel, Überschriften, Leerzeilen oder eindeutiger Trenner segmentieren.
3. Jedem Eintrag eine stabile ID geben, z. B. `thought-20260823-2217-001`.
4. Originaltext unverändert erhalten und zusätzlich eine vorsichtig bereinigte Fassung erzeugen.
5. Offensichtliche ASR-/Diktatfehler nur korrigieren, wenn die beabsichtigte Form eindeutig ist; sonst als Unsicherheit markieren.
6. Sprache, Timestamp, Quelle und optionale Tags als Metadaten speichern.
7. Keine Themencluster, Kausalitäten oder Prioritäten erfinden; diese gehören in `thought-graph-extractor`.

## JSON-Vertrag

```json
{
  "schemaVersion": 1,
  "source": {"type": "single-file-journal", "path": "QuickNote.md"},
  "entries": [
    {
      "id": "thought-20260823-2217-001",
      "timestamp": "2026-08-23T22:17:00+02:00",
      "timestampStatus": "explicit",
      "raw": "...",
      "normalized": "...",
      "language": "de",
      "uncertainties": []
    }
  ]
}
```

## Qualitätsregeln

- Rohtext nie überschreiben.
- Zeitstempel nie aus Dateireihenfolge erfinden.
- Diktatfehler nicht kreativ umdeuten.
- Ein Gedanke darf mehrere Sätze enthalten; nicht mechanisch pro Satz splitten.
- Persönliche oder vertrauliche Inhalte nicht an externe Dienste senden, sofern der Nutzer dies nicht ausdrücklich erlaubt.

## Abschluss

Der Skill endet, wenn alle erfassbaren Einträge stabil segmentiert, datiert oder als undatiert markiert und sowohl menschenlesbar als auch maschinenlesbar an `thought-graph-extractor` übergeben werden können.
