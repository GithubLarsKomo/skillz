---
name: document-generation-forensics
description: Extrahiert reproduzierbare Provenienz-, Metadaten- und Strukturhinweise aus Text-, DOCX-, PDF-, XLSX- und PPTX-Artefakten, ohne aus Dateieigenschaften allein LLM-Autorschaft abzuleiten. Als Fach-Skill für LLM-Generierungsprüfungen verwenden, wenn Dateiherkunft, Generator-Tooling, Revisionen oder formatbezogene Spuren getrennt von Sprachmustern erhoben werden müssen.
userFacing: false
implicitInvocation: false
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires: []
outputs:
  - document-forensics.json
  - document-forensics.md
lastEvaluated: 2026-08-27
---

# Document Generation Forensics

## Zweck

Dieser Skill sammelt **Artefakt-Evidenz**, nicht Autorschaftsurteile. Er untersucht Textdateien sowie OOXML- und PDF-Dateien auf nachvollziehbare Provenienz-, Metadaten-, Revisions- und Strukturhinweise. Die fachliche Bewertung, ob diese Hinweise mit LLM-Unterstützung vereinbar sind, gehört in `llm-generation-evidence-assessment`.

## Grundregeln

- Originaldatei nicht verändern; vor der Analyse SHA-256 und Dateigröße erfassen.
- Metadaten sind Hinweise und können fehlen, durch Konvertierung überschrieben oder absichtlich manipuliert worden sein.
- Ein Office-Programm, `python-docx`, `openpyxl`, `python-pptx`, Pandoc, LibreOffice, ReportLab oder ähnliche Generatoren belegen **programmatische Dokumenterzeugung**, aber nicht LLM-Nutzung.
- Produktnamen wie ChatGPT, Copilot, Claude oder Gemini sind nur dann stärker als Kontext zu werten, wenn sie in Provenienz-/Generatorfeldern oder überprüfbaren Workflow-Spuren stehen. Erwähnungen im eigentlichen Inhalt sind kein Herkunftsnachweis.
- Abwesenheit von Metadaten ist kein Gegenbeweis gegen LLM-Nutzung.
- PDF ist häufig ein Endformat. Wenn die bearbeitbare DOCX/XLSX/PPTX-Quelldatei verfügbar ist, diese zusätzlich und bevorzugt untersuchen.

## Deterministischer Erstpass

Für unterstützte Dateien zuerst ausführen:

```bash
python skills/document-generation-forensics/scripts/inspect_document_artifact.py <datei> --pretty
```

Der Erstpass verwendet nur Python-Standardbibliothek und gibt Fakten zu Hash, Format, Metadaten, Paketstruktur und ausgewählten Formatmerkmalen aus. Er darf keinen LLM-Score erzeugen.

## Formatpfade

### Text (`.txt`, `.md`, `.csv`, `.tsv`)

- Hash, Größe, Encoding-/Lesbarkeitsstatus und Zeilenstruktur dokumentieren.
- Keine Herkunft aus bloßen Schlüsselwörtern im Text ableiten.
- Für sprachliche Muster an `llm-prose-pattern-audit` übergeben.

### DOCX

- `docProps/core.xml`, `docProps/app.xml` und vorhandene Custom Properties erfassen.
- Creator, LastModifiedBy, Created/Modified, Revision, Application/AppVersion, Company und Template dokumentieren.
- Revisionen (`w:ins`, `w:del`), Kommentare, Tabellen, Felder, eingebettete Objekte und Beziehungen inventarisieren, soweit aus dem Paket reproduzierbar lesbar.
- Track-Changes-Spuren sind Workflow-Evidenz, aber weder automatisch menschliche noch LLM-Evidenz.

### XLSX

- Workbook-/App-Metadaten, Sheets und deren Sichtbarkeit, Defined Names, Formeln, Kommentare, External Links, Calc Chain und Makrohinweise erfassen.
- Gleichförmige Formeln, viele Formeln oder saubere Tabellenstruktur sind **keine** LLM-Indikatoren.
- Narrative Zellen, Anweisungen, Kommentare oder Quellenhinweise getrennt für spätere Sprach-/Inhaltsprüfung markieren.

### PPTX

- Core-/App-Metadaten, Slides, Notes, Kommentare, Master, Layouts, Media, Charts und Tabellen inventarisieren.
- Wiederverwendung eines Masters oder wiederholte Layouts sind normale PowerPoint-Eigenschaften und neutral.
- Slide-Text und Speaker Notes werden später slideweise sprachlich geprüft; der forensische Skill bewertet deren Stil nicht.

### PDF

- Info-Dictionary und XMP-Hinweise zu Author, Creator, Producer, CreationDate und ModDate best effort erfassen.
- Seitenindikatoren, Verschlüsselung und eingebettete Dateien dokumentieren.
- Bei gescannten, verschlüsselten oder stark objektkomprimierten PDFs Parsing-Limitierungen explizit melden.
- Creator/Producer nennen den Erzeugungsweg, nicht zwingend den Autor und nicht zwingend ein LLM.

## Signalmodell

Jeder relevante Befund wird einer dieser Klassen zugeordnet:

- `explicit-provenance`: explizite Generator-/Workflow-Angabe in Provenienzfeldern oder verifizierbaren Spuren.
- `generator-tooling`: Office-/PDF-/Programmbibliothek oder Konverter.
- `revision-workflow`: Track Changes, Kommentare, Notes, Revisions- oder Bearbeitungsspuren.
- `artifact-structure`: Paket-, Sheet-, Slide-, Formula-, Layout- oder Objektstruktur.
- `limitation`: fehlende oder nicht zuverlässig lesbare Evidenz.

`explicit-provenance` darf nur dann `llmSpecific=true` tragen, wenn die konkrete Quelle tatsächlich ein LLM-/GenAI-Werkzeug benennt. Alle übrigen Klassen bleiben standardmäßig `llmSpecific=false`.

## Output-Vertrag

```json
{
  "schemaVersion": 1,
  "artifact": {
    "path": "example.pptx",
    "format": "pptx",
    "sha256": "...",
    "sizeBytes": 12345
  },
  "metadata": {},
  "inventory": {},
  "signals": [
    {
      "id": "S1",
      "class": "generator-tooling",
      "strength": "context",
      "llmSpecific": false,
      "source": "docProps/app.xml:Application",
      "observed": "Microsoft Office PowerPoint",
      "interpretation": "Identifies document tooling, not LLM authorship",
      "forgeability": "medium"
    }
  ],
  "limitations": []
}
```

Ergänzend `document-forensics.md` als lesbare Zusammenfassung mit denselben Fakten erzeugen.

## Qualitätsgate

- Kein LLM-Wahrscheinlichkeitswert.
- Keine Autorschaftsaussage aus Office-/PDF-Metadaten allein.
- Inhaltsnennungen von AI-Produkten nicht mit Provenienzfeldern verwechseln.
- Programmatische Dokumenterzeugung und LLM-Erzeugung strikt trennen.
- Nicht lesbare oder fehlende Spuren als Limitation statt als negative Evidenz behandeln.

## Abschluss

Abgeschlossen, wenn das Artefakt unverändert gehasht, formatbezogene Fakten reproduzierbar erhoben, alle interpretativen Grenzen dokumentiert und die Ergebnisse als `document-forensics.json`/`.md` an `llm-generation-evidence-assessment` übergeben werden können.
