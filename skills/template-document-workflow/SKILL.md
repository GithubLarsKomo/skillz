---
name: template-document-workflow
description: Orchestriert die Erstellung oder Überarbeitung editierbarer DOCX-Dokumente auf Basis eines vorhandenen Word-Templates oder einer bestätigten Referenz, bewahrt fachlich finalisierten Inhalt, wendet Template-/Designregeln an und erzwingt strukturelle DOCX- sowie seitenweise DOCX/PDF-Render-QA. Verwenden für template-basierte Reports, Memos, Handouts und professionelle Dokumente; Corporate-Spezialregeln bleiben in dünnen Wrappern.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - document-template-profiler
  - document-layout-qa
  - document-render-verifier
consumes:
  - document-template-profile.json
  - document-layout-qa.json
  - document-layout-qa.md
  - document-render-qa.json
  - document-render-qa.md
  - document-preview.pdf
outputs:
  - document.docx
  - document.pdf
  - document-qa.md
  - document-delivery-manifest.json
lastEvaluated: 2026-08-28
---

# Template Document Workflow

## Zweck und Grenze

`template-document-workflow` ist der generische Orchestrator für editierbare, template-basierte Word-Dokumente und die daraus abgeleitete PDF-Ausgabe. Fachliche Inhalte müssen upstream bestimmt sein. Der Workflow besitzt Dokumentstruktur, Template-Anwendung und Delivery-QA, aber keine Regulatory-, Medical-, Legal-, Scientific- oder andere Fachentscheidung.

Corporate- oder domänenspezifische Skills sollen langfristig dünne Adapter bleiben: Sie liefern Brand-/DESIGN.md-Kontext, kontrollierte Template-Identität, erlaubte Blocktypen und spezielle Visual-/Chart-Producer, während der generische Ablauf hier zentral bleibt.

## Trigger

Verwenden für:

- professionelle Reports und Management-/Technical-Memos;
- strukturierte Handouts und Study Guides;
- Dokumente auf Basis eines vorhandenen DOCX/DOTX-Templates;
- Überarbeitung eines bestehenden Dokuments unter Erhalt von Template und editierbarer Struktur;
- DOCX-first-Workflows mit daraus abgeleitetem PDF.

Nicht verwenden, um einen Inhalt fachlich zu recherchieren oder ein Corporate Design neu zu erfinden.

## Voraussetzungen

Mindestens erforderlich:

1. fachlich finalisierter oder freigegebener strukturierter Inhalt;
2. Ziel, Dokumenttyp, Zielgruppe und Sprache;
3. vorhandenes Template/Referenzdokument oder explizite Erlaubnis für einen neutralen Fallback;
4. gewünschte Ausgaben `docx` und optional `pdf`;
5. bei Corporate-Kontext die verbindliche Design-/Template-Authority.

## Ablauf

### 1. Inhalt und Authority fixieren

Fachliche Source of Truth, Content-Fingerprint und Template-/Brand-Priorität dokumentieren. Ein konkretes kontrolliertes Template hat Vorrang vor rekonstruierten Designregeln.

### 2. Template profilieren

`document-template-profiler` ausführen. Binärtemplate nicht durch ein frei erfundenes Layout ersetzen. Sichere Einfügepunkte, kontrollierte Regionen, Sections, Styles, Header/Footer und Nummerierung übernehmen.

### 3. Dokumentarchitektur bestimmen

Den vorhandenen Inhalt in eine für den Dokumenttyp angemessene Struktur projizieren, ohne Claims zu erfinden. Bei langen Inhalten Hierarchie, Sections, Tabellen, Captions, Callouts, Anhänge und Quellen so strukturieren, dass Editierbarkeit und Seitenlogik erhalten bleiben.

### 4. DOCX erzeugen

`document.docx` aus dem fachlich fixierten Inhalt und der Template-Authority erzeugen.

Regeln:

- Named Styles und vorhandene Template-Strukturen bevorzugen;
- Header/Footer, Seitenzahlen, Logos, Felder und kontrollierte Regionen nicht unnötig rekonstruieren;
- Tabellen innerhalb des Satzspiegels halten und mehrseitige Tabellen robust gestalten;
- Bilder/Charts mit stabiler Caption-/Provenance-Zuordnung einfügen;
- keine Layoutprobleme durch Änderung fachlicher Zahlen oder Aussagen lösen.

### 5. Strukturelle DOCX-QA

`document-layout-qa` ausführen. Critical/Major Findings korrigieren. Nach strukturellen Änderungen erneut prüfen.

### 6. Render- und PDF-QA

`document-render-verifier` ausführen. DOCX vollständig rendern, bei gewünschtem PDF `document.pdf` aus exakt derselben DOCX-Version erzeugen und beide Seitenrender vergleichen. Nach Korrekturen erneut rendern.

### 7. Finalisieren

`document-qa.md` fasst Template-Identity, Content-Fingerprint, strukturelle QA, Render-/Parity-QA, verbleibende Warnings und den finalen Status zusammen.

`document-delivery-manifest.json` referenziert:

```json
{
  "schemaVersion": 1,
  "contentRef": "...",
  "contentFingerprint": "...",
  "templateProfileRef": "document-template-profile.json",
  "outputs": [
    {"format": "docx", "ref": "document.docx"},
    {"format": "pdf", "ref": "document.pdf"}
  ],
  "layoutQaRef": "document-layout-qa.json",
  "renderQaRef": "document-render-qa.json",
  "status": "pass|review|fail"
}
```

## Corporate Wrapper

Corporate-/Domain-Wrapper dürfen:

- verbindliche `DESIGN.md`-Regeln setzen;
- eine kontrollierte Template-Referenz und SHA-Identität bestimmen;
- Terminologie, Pflichtfooter, Dokumentklassifikation und zulässige Block-/Charttypen ergänzen;
- generische Outputs in brand-spezifische Endnamen routen.

Sie sollen nicht erneut eigene allgemeine Regeln für Template-Profilierung, Overflow-/Tabellen-QA, Seitenrender oder DOCX/PDF-Parität implementieren, sobald sie auf diesen Kern migriert wurden.

## Prüfungen

Vor PASS:

- fachliche Inhalte sind gegenüber der Source of Truth unverändert oder jede redaktionelle Änderung ist autorisiert;
- Template-/Referenzstatus ist nachvollziehbar;
- `document-layout-qa` enthält keine offenen Critical/Major Findings;
- tatsächlicher DOCX-Seitenrender wurde geprüft;
- bei PDF-Ausgabe wurde PDF aus der kanonischen DOCX-Version erzeugt und auf Parität geprüft;
- nach Korrekturen wurde erneut gerendert;
- `template-derived` wird nur bei tatsächlich verifizierter Template-Fidelity behauptet;
- finale DOCX bleibt editierbar.

## Fehlerbehandlung

- **Kein Template und kein erlaubter Fallback:** abbrechen statt Design zu erfinden.
- **Kein sicherer Einfügepunkt in kontrolliertem Template:** `fail|not-run`; Template nicht destruktiv umbauen.
- **DOCX strukturell beschädigt:** korrigieren oder blockieren; kein PDF als Ersatz für fehlende Editierbarkeit.
- **Renderer/PDF-Export fehlt:** DOCX kann separat geliefert werden, aber visuelle/PDF-Paritätsclaims bleiben `not-run`.
- **Fachlicher Konflikt im Input:** upstream zurückgeben; nicht beim Layouten lösen.

## Übergabe

Eigene Outputs sind `document.docx`, optional `document.pdf`, `document-qa.md` und `document-delivery-manifest.json`. Profiler- und QA-Artefakte bleiben bei ihren spezialisierten Producer-Skills und werden referenziert.

## Abschlusskriterien

Abgeschlossen, wenn der fachlich fixierte Inhalt template-treu in einem editierbaren DOCX vorliegt, strukturelle QA bestanden ist, der tatsächliche Seitenrender geprüft wurde, ein gewünschtes PDF aus derselben DOCX-Version erzeugt und auf Parität verifiziert wurde und Manifest sowie QA-Bericht den finalen Status ohne simulierte Template- oder Rendererfolge dokumentieren.
