---
name: mdcg-guidance-navigator
description: Ermittelt für Medical-Device-/IVD-Fragen die aktuell anwendbaren MDCG-Dokumente aus offiziellen EU-Quellen, inklusive Revision, Status, Scope, Freshness und Änderungen gegenüber einem früheren Stand. Verwenden, wenn aktuelle MDCG-Guidance identifiziert oder ein Guidance-Set aktualisiert werden muss; der Skill entscheidet selbst keine Compliance oder Klassifikation.
userFacing: true
implicitInvocation: true
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - regulated-product-context
  - research-to-evidence-note
  - regulatory-evidence-traceability
outputs:
  - mdcg-guidance-set.json
  - mdcg-guidance-changes.json
lastEvaluated: 2026-08-06
---

# MDCG Guidance Navigator

## Zweck

Dieser Skill ersetzt statische, schnell veraltende MDCG-Listen durch eine aktuelle, scope-begründete Guidance-Auswahl. Er findet relevante aktuelle und – wenn für Historie/Transition notwendig – obsolete oder superseded Dokumente, dokumentiert Revision und Status und übergibt sie als Evidence Input an EU-/IVDR-Spezialisten.

MDCG-Guidance ist nicht rechtsverbindlich. Der Navigator behandelt sie als `guidance` und nicht als Verordnung oder behördliche Entscheidung.

## Trigger

Verwenden bei Fragen wie:

- Welche MDCG-Guidance ist für diesen IVD-/MDR-Sachverhalt aktuell relevant?
- Hat sich ein bereits verwendetes Guidance-Set geändert?
- Welche Revision ist aktuell und welche frühere Version wurde ersetzt?
- Welche IVD-spezifische Guidance ist zusätzlich zu allgemeinen MDR/IVDR-Dokumenten relevant?

Nicht verwenden, um aus Guidance allein Compliance, Klassifikation, CE-Konformität oder eine NB-/Behördenposition abzuleiten.

## Autoritative Quellenhierarchie

1. Aktuelle European-Commission-Seite `Guidance - MDCG endorsed documents and other guidance`.
2. Offizielle EC-Publikations-/Update-Seite des konkreten MDCG-Dokuments.
3. Das verlinkte offizielle Dokument selbst, wenn Scope/Revision/Details geprüft werden müssen.
4. Obsolete/archivierte EC-Guidance nur für Historie, Transition oder ausdrücklich rückwirkende Analyse.

Drittseiten, Skill-Shops und Suchmaschinen dürfen Discovery unterstützen, sind aber keine Autorität für aktuellen Status oder Revision.

## Current-baseline-Regel

Der Skill speichert keine zeitlose Liste. Bei jeder fachlich relevanten Ausführung wird die offizielle Guidance-Übersicht mit aktuellem `asOf` geprüft. Als Baseline vom 6. August 2026 führt die EC-Seite im IVD-Bereich unter anderem `MDCG 2024-11` zur IVD-Qualification und `MDCG 2020-16 rev.4` zur IVDR-Klassifikation; diese Beispiele sind keine Garantie für zukünftige Aktualität.

## Workflow

### 1. Kontext und Frage fixieren

Übernimm Produktart, Intended Purpose, Markt, Lifecycle und konkrete Fragestellung aus `regulated-product-context`. Trenne IVD-spezifische von allgemeinen Medical-Device-Themen.

### 2. Offizielle Guidance-Übersicht prüfen

Ermittle Kandidaten nach Themenbereich, Referenz, Titel, Revision, Publikationsdatum und aktuellem/obsoletem Status. Dokumente mit ähnlichem Titel werden nicht allein über Textähnlichkeit gleichgesetzt.

### 3. Scope verifizieren

Öffne die offizielle Dokumentseite bzw. das Dokument, wenn Titel/Index nicht ausreichen. Erfasse:

- Reference/Revision,
- Titel,
- Publication/Update Date,
- Scope und Regime (`MDR|IVDR|both`),
- relevante Produkt-/Lifecycle-Aspekte,
- Source Reference,
- `asOf` und Freshness.

### 4. Applicability begründen

Jedes ausgewählte Dokument erhält `applicability: applicable|potentially-applicable|not-applicable|unknown` plus kurze evidenzgebundene Begründung. Der Navigator entscheidet nicht über die finale Compliance-Wirkung.

### 5. Änderungen erkennen

Wenn ein früheres Guidance-Set vorliegt, vergleiche Referenzen, Revisionen, Status und Scope. Unterscheide mindestens `added`, `revised`, `superseded`, `archived`, `scope-changed`, `unchanged`. Ohne früheren Snapshot ist `mdcg-guidance-changes.json` ein Baseline-Resultat, keine erfundene Änderungshistorie.

### 6. Evidence Traceability übergeben

Verknüpfe die Guidance-Auswahl über `regulatory-evidence-traceability` mit den Claims/Requirements des nachgelagerten Fach-Skills.

## Output-Verträge

### `mdcg-guidance-set.json`

```json
{
  "schemaVersion": 1,
  "asOf": "ISO-8601",
  "question": "...",
  "productContextRef": "...",
  "documents": [],
  "unknowns": [],
  "sourceIndexRefs": []
}
```

Jedes Dokument enthält mindestens `reference`, `title`, `revision`, `publicationDate`, `status`, `regime`, `applicability`, `applicabilityRationale`, `sourceRefs` und `checkedAt`.

### `mdcg-guidance-changes.json`

Enthält Baseline/Previous-Snapshot-Referenz, Change Classification, betroffene Dokumente, Evidenz und erforderliche Downstream-Neubewertungen.

## Downstream

Primäre Consumers sind `eu-mdr-ivdr-regulatory-specialist`, `ivdr-device-classification`, Performance-Study-/Performance-Evaluation-Skills, PMS/PMPF und andere EU-Facharbeiter. Sie müssen selbst die fachliche Interpretation und Entscheidung vornehmen.

## Memory Path

Persistenzwürdig sind validierte Such-/Applicability-Muster, stabile projektspezifische Guidance-Relevanz oder bestätigte Hinweise darauf, welche Dokumentfamilien bei einem wiederkehrenden Produkttyp geprüft werden müssen. Die Aussage „Revision X ist aktuell“ ist grundsätzlich volatil und darf nur mit offizieller `sourceRef`, `observedAt/asOf` und einem zeitnahen `reviewAfter` als Memory Candidate weitergegeben werden; sie darf nie zur zeitlosen Wahrheit werden. Suchresultate, momentane EC-Seitenstände und ungeprüfte Drittquellen bleiben run-only. Übergib Kandidaten als `memory-candidate-handoff-v1` an `communication-memory-governance`; Persistenz bleibt dessen Entscheidung.

## Qualitätsgate

Bestanden nur wenn:

- der aktuelle offizielle EC-Index tatsächlich geprüft wurde,
- Revision/Status nicht aus Erinnerung oder Drittquellen geraten werden,
- Guidance klar von Regulation/Law getrennt bleibt,
- Applicability mit Scope-Evidenz begründet ist,
- obsolete Dokumente nicht als aktuelle Guidance erscheinen,
- Änderungen nur gegen einen echten vorherigen Snapshot behauptet werden,
- Downstream eine aktuelle, nachvollziehbare Guidance-Basis erhält,
- volatile Guidance-Memory einen Review-/Expiry-Pfad besitzt.
