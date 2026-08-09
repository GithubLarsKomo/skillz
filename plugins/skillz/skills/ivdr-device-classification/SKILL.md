---
name: ivdr-device-classification
description: Erstellt für ein IVD eine evidenzgebundene IVDR-Qualifikations- und Klassifikationshypothese nach Artikel 47/Anhang VIII mit expliziter Regelbegründung, konkurrierenden Regeln, Unsicherheiten und aktueller MDCG-Guidance. Verwenden für Class A/B/C/D Assessments; keine endgültige Behörden-/NB-Entscheidung simulieren.
---

# IVDR Device Classification

## Zweck

Dieser Skill führt einen eng begrenzten IVDR-Klassifikationsschritt durch. Er prüft zuerst, ob der betrachtete Gegenstand unter dem vorliegenden Intended Purpose als IVD/IVD-Komponente qualifiziert werden kann, und wendet anschließend die Durchführungs- und Klassifizierungsregeln von Anhang VIII auf einen fixierten Produktkontext an.

Er ersetzt weder den breiten `eu-mdr-ivdr-regulatory-specialist` noch Conformity Assessment, Performance Evaluation, Risk Management oder eine Entscheidung von Benannter Stelle/zuständiger Behörde.

## Trigger

Verwenden für:

- IVDR-Klasse A/B/C/D,
- Annex-VIII-Regelzuordnung,
- konkurrierende Klassifizierungsregeln,
- Klassifikation von IVD-Software, Zubehör, Kalibratoren oder Kontrollmaterialien,
- Neubewertung nach Änderung des Intended Purpose oder anderer klassifikationsrelevanter Produktmerkmale.

Bei unklarer IVD-Qualification zuerst aktuelle Qualification Guidance über `mdcg-guidance-navigator` einbeziehen.

## Autoritative Basis

- Regulation (EU) 2017/746, insbesondere Artikel 47 und Anhang VIII.
- Aktuelle offizielle MDCG-Guidance zur IVD-Qualification und -Klassifikation.
- Aktuelle EC-Informationen zu Borderline/Classification, wenn der Scope dies erfordert.

Als geprüfte Baseline am 6. August 2026 führt die Europäische Kommission `MDCG 2024-11` zur Qualification von IVDs und `MDCG 2020-16 rev.4` zur Anwendung der IVDR-Klassifizierungsregeln. Diese Revisionen werden bei jeder neuen Ausführung über `mdcg-guidance-navigator` erneut auf Aktualität geprüft.

## Klassifikationsinvarianten

- Die Klassifikation richtet sich nach der **Zweckbestimmung**.
- Zubehör wird eigenständig klassifiziert.
- Software wird entsprechend den Durchführungsregeln separat oder zusammen mit dem beeinflussten/gesteuerten Produkt bewertet.
- Kalibratoren und Kontrollmaterialien mit zugeordneten Werten werden gemäß den einschlägigen Durchführungsregeln behandelt.
- Alle anwendbaren Durchführungs- und Klassifizierungsregeln werden geprüft, nicht nur die zuerst passende.
- Bei mehreren Intended Purposes bzw. mehreren anwendbaren Regeln mit unterschiedlichen Klassen wird die höhere resultierende Klasse angewendet, soweit die aktuelle Fassung des Anhangs VIII dies vorsieht.
- First-line, confirmatory und supplemental assays werden nicht allein aufgrund ihrer Rolle von den Klassifizierungsregeln ausgenommen.
- Rule-1-bis-Rule-7-Entscheidungen werden aus dem konkreten Intended Purpose und den relevanten Merkmalen abgeleitet; der Skill erfindet keine vereinfachte „Testtyp → Klasse“-Tabelle.

## Workflow

### 1. Produktkontext einfrieren

Übernimm mindestens:

- Intended Purpose und Claims,
- Analyte/Measurand bzw. Target,
- klinischen/diagnostischen Zweck,
- Specimen,
- Zielpopulation und Anwender,
- Use Environment,
- qualitative/quantitative Nutzung,
- Screening/Diagnosis/Monitoring/Prediction/Companion-Diagnostic-Kontext soweit relevant,
- Produktform: reagent/device/software/accessory/calibrator/control/instrument/specimen receptacle,
- bekannte Qualification-/Borderline-Fragen.

Fehlende klassifikationsrelevante Angaben bleiben Blocker oder explizite Annahmen.

### 2. IVD-Qualification prüfen

Nutze aktuelle Qualification Guidance, wenn der Status nicht bereits belastbar bestätigt ist. Integral products, Software-/Accessory-Grenzen und Produkte mit mehreren Funktionen werden nicht allein nach Handelsbezeichnung eingeordnet.

Wenn IVD-Qualification nicht ausreichend belegt ist, stoppt die finale Klassenzuordnung bei `classificationState: blocked-qualification`.

### 3. Durchführungsregeln anwenden

Prüfe die Durchführungsregeln von Anhang VIII vor den Rules 1–7. Dokumentiere insbesondere Intended Purpose, Kombinationen, Zubehör, Software, Kalibratoren, Kontrollmaterialien und mehrere Intended Purposes.

### 4. Rules 1–7 systematisch prüfen

Für jede Regel erfasse:

- `applicable|not-applicable|unknown`,
- Source/Locator,
- produktbezogene Begründung,
- resultierende Klasse, falls anwendbar,
- offene Evidenz oder Interpretationsfrage.

Eine Regel wird nicht nur deshalb verworfen, weil bereits eine andere Regel passt.

### 5. Konkurrenz auflösen

Wenn mehrere Regeln/Intended Purposes unterschiedliche Klassen ergeben, wende die aktuellen Annex-VIII-Durchführungsregeln zur höheren Klasse an und dokumentiere den Weg. Falls die Konkurrenz von einer ungelösten Qualification-/Interpretationsfrage abhängt, bleibt die Klassifikation `provisional|blocked`.

### 6. Guidance und Evidence verknüpfen

Verwende `mdcg-guidance-set.json` nur als Guidance-Evidence und `regulatory-evidence-traceability` für Source/Claim/Interpretation-Verknüpfung. Guidance ersetzt den Gesetzestext nicht.

### 7. Ergebnis und Authority Boundary ausgeben

Gib eine `confirmed-context|provisional|blocked|needs-authority-resolution` Klassifikationsbewertung aus. Eine interne Analyse wird nie als verbindliche NB-/Behördenentscheidung dargestellt. Bei echter Meinungsverschiedenheit im formalen Conformity-Assessment-Kontext gelten die behördlichen Mechanismen der IVDR; der Skill entscheidet sie nicht selbst.

## Output-Verträge

### `ivdr-classification-assessment.json`

```json
{
  "schemaVersion": 1,
  "asOf": "ISO-8601",
  "productContextRef": "...",
  "qualification": {},
  "implementingRules": [],
  "classificationRules": [],
  "applicableRules": [],
  "resultingClass": "A|B|C|D|unknown",
  "classificationState": "confirmed-context|provisional|blocked|blocked-qualification|needs-authority-resolution",
  "guidanceRefs": [],
  "evidenceRefs": [],
  "assumptions": [],
  "unknowns": [],
  "authorityBoundary": "..."
}
```

### `ivdr-classification-rationale.md`

Enthält Intended Purpose, Qualification, angewandte Durchführungsregeln, Rule-by-Rule-Matrix, konkurrierende Regeln, Higher-class-Resolution, relevante Guidance/Evidence, Unknowns und die klare Grenze zwischen interner Assessment-Hypothese und autoritativer Entscheidung.

## Downstream

Primäre Consumers sind `eu-mdr-ivdr-regulatory-specialist`, die geplante IVDR-Performance-Evaluation-Kette, Conformity-Route-/Class-D-Spezialisten, EUDAMED/UDI und `design-change-regulatory-impact`.

Eine Änderung von Intended Purpose oder anderen klassifikationsrelevanten Fakten invalidiert den alten Assessment-Stand und triggert eine Neubewertung statt stiller Fortschreibung.

## Memory Path

Persistenzwürdig sind bestätigte projektspezifische klassifikationsrelevante Produktmerkmale, validierte Rule-Application-Muster für eine klar abgegrenzte Produktfamilie und dauerhaft nützliche Hinweise darauf, welche Merkmale vor einer Klassifikation zwingend fixiert werden müssen. Die resultierende Klasse selbst bleibt ohne formale Autorität eine `interpretation` bzw. projektbezogene Assessment-Hypothese und darf nicht als allgemein bestätigter regulatorischer Fakt gespeichert werden. Aktuelle MDCG-Revisionen, Borderline-Listen und andere volatile externe Stände benötigen offizielle `sourceRefs`, `observedAt/asOf` und `reviewAfter`; ungeklärte Qualification-/Rule-Fragen bleiben run-only. Übergib zulässige Kandidaten als `memory-candidate-handoff-v1` an `communication-memory-governance`; dieser Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- Intended Purpose und klassifikationsrelevanter Produktkontext sichtbar sind,
- IVD-Qualification bei Bedarf geprüft wurde,
- Durchführungsregeln vor der Rule-Zuordnung berücksichtigt wurden,
- Rules 1–7 systematisch bewertet und konkurrierende Regeln nicht versteckt wurden,
- aktuelle offizielle MDCG-Guidance mit `asOf` geprüft wurde,
- Gesetz, Guidance und Interpretation getrennt bleiben,
- die resultierende Klasse mit Source-/Evidence-Traceability begründet ist,
- Unsicherheiten und Authority Boundary explizit sind,
- Memory Candidates eine Klassifikationshypothese nicht zu einem autoritativen Fakt hochstufen.
