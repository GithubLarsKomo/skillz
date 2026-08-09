---
name: fda-registration-listing-udi
description: Bereitet FDA Establishment Registration, Device Listing und UDI/GUDID-Masterdaten für Medical Devices strukturiert vor, trennt 21 CFR 807 von UDI-Pflichten und simuliert weder Registrierung noch Identifier-Vergabe.
---

# FDA Registration Listing UDI

## Zweck und Grenze

Dieser Skill bereitet die kontrollierten Masterdaten und Readiness-Entscheidungen für FDA Establishment Registration und Device Listing nach 21 CFR Part 807 sowie UDI/GUDID-Pflichten vor. Er trennt Establishment-, Device- und Labeler-/UDI-Kontext und verwechselt Registration/Listing ausdrücklich nicht mit Marketing Authorization.

Der Skill registriert keine Establishments, listet keine Devices, beantragt oder vergibt keine UDI und schreibt nicht in FURLS/GUDID. Solche Schritte bleiben verifizierte Human-/External-Actions.

## Kernprinzipien

- **Establishment and device are different entities:** Registration Activity/Role und Device Listing werden getrennt geführt.
- **Registration/listing is not approval:** Registration Number, Listing oder Datenbankeintrag bedeutet keine FDA Clearance/Approval.
- **UDI applicability before identifier data:** Labeler, Device Class/Type, Exceptions/Alternatives und aktuelle Compliance Policy werden vor DI/GUDID-Daten bestimmt.
- **DI and PI stay distinct:** GUDID führt Device Identifier-bezogene Masterdaten; Production Identifier gehört nicht als GUDID-Stammdatensatz hinein.
- **External identifiers are evidence, never inventions:** Registration Number, Owner/Operator Number, Listing Number, DI und GUDID State werden nur aus belegten Quellen übernommen.

## Workflow

### 1. US Product/Establishment Context fixieren

Erfasse Legal Manufacturer/Specification Developer/Contract Manufacturer/Importer/Relabeler/Repackager bzw. andere relevante Activities, Domestic/Foreign Status, US Agent soweit relevant, Device/Product Code/Class, Marketing Authorization Context und `asOf`.

### 2. Registration- und Listing-Pflichten mappen

Prüfe pro Establishment Activity aktuelle 21 CFR Part 807/FDA-Anforderungen für `register|required/not-required/uncertain`, `list|required/not-required/uncertain` und Fee/Annual Renewal Context. Jahresgebühren oder temporäre Waiver-Regeln werden als volatile Current Context behandelt.

### 3. Device Listing Readiness

Mappe Device Name, Proprietary/Common Name, Product Code, Establishment Activities, Marketing Submission Number soweit erforderlich, Listing State und offene Masterdata Gaps. Bestehende Listing-/Registration-Daten werden nicht als Produktzulassung interpretiert.

### 4. UDI Applicability bestimmen

Bestimme Device Labeler und prüfe aktuelle UDI Rule/Exceptions/Alternatives/Compliance Policy. Klassifiziere `udi-required|exception/alternative-evidence|policy-dependent|not-applicable|uncertain`.

### 5. UDI/GUDID Masterdata vorbereiten

Für anwendbare Devices mappe issuing-agency/DI Evidence, Label/Package Levels, DI Masterdata, GMDN/aktuelle Terminologie, Premarket Submission References und GUDID-required fields. PI-Daten wie Lot/Serial/Expiration werden nur als Label-/production context referenziert, nicht als GUDID-DI-Stammdaten gespeichert.

### 6. Cross-links und externe Aktion

- Labeling/UDI placement → `medical-device-labeling-ifu`.
- Product/Classification/Authorization gaps → passende FDA Classification-/Submission-Skills.
- Recall/Correction Masterdata → `fda-corrections-removals`.
- tatsächliche FURLS/GUDID Registration/Listing/Submission → autorisierter Human-/External-Action-Pfad mit nachgelagerter Verifikation.

## Output-Verträge

`fda-registration-readiness.json` enthält Establishment, Activities, Registration/fee/renewal requirements, Current Sources/`asOf`, existing verified IDs, gaps und External Action State.

`fda-device-listing-readiness.json` enthält Device/Establishment Mapping, Product Code/Class, Marketing Authorization Reference, Listing Requirements, verified existing state und gaps.

`gudid-udi-readiness.json` enthält Labeler, UDI Applicability, Exceptions/Alternatives Evidence, DI/Package-level Masterdata, GUDID fields/gaps, external-submission state und verification evidence.

## Memory Path

Persistenzwürdig sind nur abstrahierte validierte Registration-/Listing-/UDI-Dependency- und Masterdata-Muster. Konkrete Registration/Owner-Operator/Listing/DI IDs, Account-/Portalzustände, Gebühren, Waiver-Status, aktuelle GUDID Records und nicht veröffentlichte Produktdaten bleiben run-only bzw. kontrollierte Regulatory/Masterdata Records. Geeignete Memory Candidates gehen ausschließlich an `communication-memory-governance`.

## Qualitätsgate

Bestanden nur wenn:

- Establishment Activity und Device Scope getrennt modelliert sind,
- Registration/Listing nicht als Clearance/Approval dargestellt wird,
- UDI Applicability vor DI/GUDID-Datenerfassung bewertet wird,
- DI und PI nicht vermischt werden,
- IDs und externe Portalzustände nur aus verifizierter Evidence stammen,
- volatile Fees/Waiver/Compliance Policies mit `asOf` statt als dauerhaftes Wissen geführt werden,
- tatsächliche FURLS-/GUDID-Aktionen nicht simuliert werden,
- konkrete IDs/Portal-/Fee-/Produktzustände nicht in globales dauerhaftes Memory gelangen.
