---
name: llm-generation-review-workflow
description: Orchestriert eine evidenzbasierte Prüfung von Text, DOCX, PDF, XLSX und PPTX auf Hinweise einer LLM-/GenAI-Beteiligung durch Dateiforensik, LLM-Prosa-Musteranalyse, optionalen Author-Voice-Vergleich, formatbezogene Inhaltsprüfung und konservative Evidenzsynthese. Verwenden bei Fragen wie „Ist das KI-generiert?“, „Prüfe dieses Dokument auf ChatGPT/LLM“ oder bei dokumentierter Herkunftsprüfung; keine binäre Detector-Gewissheit behaupten.
---

# LLM Generation Review Workflow

## Rolle

Dieser Skill ist ein **dünner Orchestrator** für Herkunfts- und Entstehungsprüfungen. Er koordiniert vorhandene Fach-Skills und formatbezogene Prüfungen, ohne selbst einen universellen AI-Detector zu simulieren.

Die dateitypspezifischen Prüfpunkte stehen in `references/format-checks.md`.

## Ziel und Grenze

Ziel ist eine nachvollziehbare Antwort auf die Frage, **welche Evidenz für oder gegen relevante LLM-/GenAI-Beteiligung am untersuchten Artefakt vorliegt**. Der Workflow unterscheidet:

- direkte/überprüfbare Provenienz,
- Workflow- und Revisionsspuren,
- LLM-typische Prosa-Muster aus der Textoptimierungs-Taxonomie,
- optionalen Author-Voice-Vergleich,
- formatbezogene Struktur-/Tooling-Hinweise,
- Inhaltsintegrität,
- externe Detector-Scores als ergänzende Evidenz,
- Gegenindikatoren und Alternativerklärungen.

Er behauptet nicht, dass LLM-Nutzung aus Stil allein sicher erkennbar ist, und beweist bei fehlenden Hinweisen keine rein menschliche Autorschaft.

## Eingang

Pflicht:
- Text oder eine Datei in `TXT/MD/DOCX/PDF/XLSX/PPTX`.

Optional, aber wertvoll:
- bearbeitbare Quelldatei zu einem PDF,
- bestätigte frühere Texte des mutmaßlichen Autors,
- Entwurfsstände/Versionshistorie/Kommentare,
- Prompt-/Copilot-/Tool-Protokolle,
- Quellen, Datengrundlagen oder Originalberechnungen,
- externe Detector-Berichte mit Tool/Version/Kalibrierung.

## Ablauf

### 1. Prüfkontext fixieren

Dokumentiere:
- Prüfgegenstand und Dateiformat,
- gewünschte Aussage (`screening`, `forensic-review`, `high-stakes-review`),
- verfügbare Herkunftsinformation,
- Sprache/Genre/Zielgruppe,
- ob das Dokument übersetzt, redigiert, koautoriert oder aus einem anderen Format exportiert wurde.

Bei `high-stakes-review` — etwa Sanktion, Personalmaßnahme, Compliance-/Täuschungsvorwurf oder Rechtsstreit — ausdrücklich festhalten, dass Stilheuristiken oder ein einzelner Detector keine alleinige Entscheidungsgrundlage bilden dürfen.

### 2. Original sichern und Artefaktforensik ausführen

`document-generation-forensics` auf der unveränderten Datei ausführen. Hash und Formatbefunde in den Endbericht übernehmen.

Wenn PDF plus DOCX/XLSX/PPTX-Quelle vorhanden sind, beide analysieren und die Quelle für Revisions-/Strukturevidenz priorisieren; PDF bleibt zusätzliche Render-/Producer-Evidenz.

### 3. Inhalt formatgerecht extrahieren und segmentieren

Den geeigneten Datei-/Dokumentenleser verwenden und die in `references/format-checks.md` definierten Segmente bilden.

- Text/DOCX/PDF: Prosa abschnitts- oder seitenbezogen.
- XLSX: narrative Zellen/Kommentare getrennt von Formeln, Daten und Struktur.
- PPTX: pro Slide Titel, Body und Speaker Notes getrennt; globale Muster zusätzlich erfassen.

Nicht lesbare Bereiche als Limitation dokumentieren. OCR nur einsetzen, wenn tatsächlich kein zuverlässiger Textlayer verfügbar ist.

### 4. Sprachmuster prüfen

`llm-prose-pattern-audit` auf ausreichend umfangreiche Prosa anwenden.

Die dortige Grenze bleibt unverändert: Muster wie Signifikanzinflation, Pseudoanalyse, mechanische Übergänge, Synonymdrift, Nominalstil oder syntaktische Gleichförmigkeit sind **Editing-/Stilindikatoren**, keine Autorschaftsbeweise.

Bei gemischten Dokumenten abschnittsweise prüfen statt einen globalen Durchschnitt zu bilden. Kurze Titel, Tabellenköpfe, reine Formeln und Stichwörter nicht künstlich als Fließtext bewerten.

### 5. Optional Author Voice vergleichen

Nur wenn authentische Referenztexte verfügbar und Sprache/Genre hinreichend vergleichbar sind:

1. vorhandenes `author-voice-profile.json` verwenden oder `author-voice-profiler` ausführen,
2. beobachtbare Merkmale des Zielartefakts gegen das Profil vergleichen,
3. Übereinstimmung und Abweichung mit möglichen Alternativerklärungen dokumentieren.

Kein Voice-Mismatch bei Genrewechsel, Übersetzung oder starkem Editing übergewichten.

### 6. Inhaltsintegrität prüfen

Formatabhängig kontrollieren:
- Quellen, Zitate, URLs und Literaturangaben,
- Zahlen, Claims und interne Konsistenz,
- offensichtliche Prompt-/Assistentenreste oder Platzhalter,
- XLSX-Formeln, unerklärte Hardcodes, Referenzfehler und externe Links,
- PPTX-Quellen, Bild-/Chart-Beschriftungen, Slide-Notes und generische Platzhalter,
- Inkonsistenzen zwischen Text, Tabellen, Charts und Quelldaten.

Halluzinationsähnliche Fehler sind nicht automatisch LLM-spezifisch; sie werden als `content-integrity`-Evidenz mit Alternativerklärungen übergeben.

### 7. Externe Detector-Ergebnisse einordnen

Falls vorhanden:
- Tool, Version, Sprache, Domäne, Textlänge, Score und bekannte Kalibrierung erfassen,
- niemals einen Detector-Score direkt als Autorschaftswahrscheinlichkeit interpretieren,
- Ergebnisse ohne passende Kalibrierung deutlich abwerten.

Keine zusätzliche Detector-Abfrage erzwingen, wenn keine belastbare, validierte Methode für den konkreten Kontext verfügbar ist.

### 8. Evidenz synthetisieren

`llm-generation-evidence-assessment` mit allen Pro-, Gegen- und Limitationsevidenzen ausführen.

Die Endbewertung verwendet `llmEvidenceLevel = documented|strong|moderate|limited|insufficient` und zusätzlich `humanWorkflowEvidenceLevel`.

### 9. Bericht erzeugen

`llm-generation-review.md` enthält:

1. **Kurzurteil** mit Evidence Level und Assessment Confidence,
2. **Prüfumfang** und Artefakt-Hash,
3. **stärkste positive Evidenz**,
4. **Gegenindikatoren/Alternativerklärungen**,
5. **formatbezogene Befunde**,
6. **externe Detector-Ergebnisse** mit Kalibrierungsgrenzen,
7. **Limitationen**,
8. **empfohlene nächste Verifikation**.

Zusätzlich maschinenlesbares `llm-generation-review.json` erzeugen.

## Output-Vertrag

```json
{
  "schemaVersion": 1,
  "artifact": {
    "format": "docx",
    "sha256": "..."
  },
  "reviewMode": "forensic-review",
  "language": "de",
  "genre": "report",
  "llmEvidenceLevel": "moderate",
  "humanWorkflowEvidenceLevel": "limited",
  "confidenceInAssessment": "medium",
  "summary": "Mehrere voneinander teilweise unabhängige Hinweise sind mit LLM-Unterstützung vereinbar; direkte Provenienz fehlt.",
  "evidenceFamiliesUsed": ["prose-patterns", "author-voice", "artifact-structure"],
  "strongestEvidence": [],
  "counterevidence": [],
  "limitations": [],
  "recommendedFollowUp": []
}
```

## Sprachregeln für das Urteil

Bevorzugen:
- „Dokumentierte LLM-Beteiligung“
- „Starke Hinweise auf LLM-Beteiligung“
- „Mehrere Hinweise, aber keine belastbare Provenienz“
- „Einzelne schwache Hinweise“
- „Keine belastbare Aussage möglich“

Vermeiden:
- „zu 87 % KI-generiert“ ohne validiertes probabilistisches Modell,
- „definitiv ChatGPT“ aus Stil oder Metadaten allein,
- „definitiv menschlich“ aus fehlenden AI-Signalen.

## Übergang zur Textoptimierung

Wenn der Nutzer nach der Prüfung eine sprachliche Überarbeitung möchte, das Ergebnis an `precision-writing-revision` übergeben. Dabei nur tatsächlich redaktionell störende Muster korrigieren und Fidelity erhalten. **Detector-Evasion ist kein Ziel**; ein Text wird nicht künstlich verändert, nur um einen AI-Detector zu täuschen.

## Qualitätsgate

- Alle fünf angeforderten Artefaktklassen routen: Text, DOCX, PDF, XLSX, PPTX.
- `llm-prose-pattern-audit` behält seine Nicht-Autorschaftsgrenze.
- Metadaten, Tooling, Stil, Voice und Content Integrity getrennt dokumentieren.
- Positive und negative Evidenz sowie Limitationen sichtbar machen.
- Keine Sanktion oder Hochrisikoentscheidung aus einem einzelnen Detector oder Stilmerkmal ableiten.
- Kein finales Urteil stärker formulieren als die stärkste **kombinierte** Evidenz erlaubt.

## Abschluss

Abgeschlossen, wenn das Original eindeutig identifiziert, alle verfügbaren Evidenzfamilien formatgerecht geprüft, unabhängige Pro- und Gegenindikatoren konservativ synthetisiert und ein nachvollziehbarer JSON-/Markdown-Bericht mit klaren methodischen Grenzen vorliegt.
