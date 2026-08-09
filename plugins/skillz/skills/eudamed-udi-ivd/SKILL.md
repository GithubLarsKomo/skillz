---
name: eudamed-udi-ivd
description: Erzeugt IVD-UDI-/EUDAMED-Readiness-Datensätze aus Product Context, Classification und kontrollierter Device-Evidence.
---

# EUDAMED / UDI for IVDs

## Zweck und Grenze

Dieser Skill bereitet konsistente IVD-UDI-/Device-Daten und EUDAMED-Readiness für Hersteller-/Device-Registration vor. Er **registriert keine Actors oder Devices**, erzeugt keine SRN/UDI durch eigene Autorität und simuliert keine EUDAMED-Bestätigung.

## Kernprinzipien

- **Current module state first:** verpflichtende, freiwillige oder noch nicht verfügbare EUDAMED-Module werden aus dem aktuellen Kommissionsstand bestimmt.
- **Device identity is versioned:** Basic UDI-DI, UDI-DI/Device Identifier, Product/Variant, Packaging/Model und relevante Version/Legacy-Beziehungen müssen konsistent aufgelöst sein.
- **One product truth:** Intended Purpose, Risk Class, Manufacturer/Actor, Labeling und Device Facts stammen aus bestätigten Upstream-Artefakten.
- **UDI data ≠ issuance:** Issuing-Entity-/UDI-Vergabe und reale UDI-Werte werden nur aus kontrollierter Evidenz übernommen; der Skill erfindet keine Identifier.
- **Registration data ≠ registration:** ein valider Datensatz ist kein EUDAMED-Submission-/Registration-Nachweis.
- **Module boundaries stay current:** PMS/Vigilance- oder Performance-Study-Funktionen werden nicht als bereits nutzbare/mandatory Workflows behandelt, wenn der aktuelle EUDAMED-Stand das nicht trägt.

## Workflow

### 1. Actor-/Product Context fixieren

Erfasse Manufacturer/Authorised Representative soweit relevant, vorhandene Actor ID/SRN Evidence, Device/Family/Variant, IVDR Class, Intended Purpose, Markets, Labeling Baseline, Certificate/Conformity State und Legacy/Transition Context.

### 2. Current EUDAMED State laden

Verifiziere bei der Europäischen Kommission den aktuellen Status der EUDAMED-Module und die aktuell verpflichtenden Daten-/Registrierungswege mit `asOf`. Zum Stand 2026 wird insbesondere geprüft, welche Module bereits mandatory sind und welche noch nicht produktiv/mandatory verfügbar sind; der Skill speichert diesen Snapshot nicht zeitlos.

### 3. Device Identity / UDI Mapping

Mappe kontrollierte Evidenz für:
- Basic UDI-DI soweit anwendbar,
- UDI-DI/Device Identifier und Issuing Entity,
- Device Name/Model/Variant/Packaging Relations,
- EMDN Code,
- IVDR Risk Class,
- Intended Purpose/Relevant Characteristics,
- Manufacturer/Actor/SRN References,
- Certificate/NB References soweit relevant,
- Legacy-/Previous-Device-Identifiers soweit relevant,
- Labeling-/Language-/Market References.

### 4. Data Quality prüfen

Klassifiziere jedes Feld `verified|missing|conflicting|not-applicable-with-rationale|external-allocation-pending|unknown`. Prüfe besonders Identität, Parent/Child-/Family-Beziehungen, Identifier-Source, Class, Manufacturer/SRN, Certificate Links und Widersprüche zu Labeling/Product Context.

### 5. EUDAMED Readiness ableiten

Bewerte pro aktuell anwendbarem Modul/Datensatz:
- prerequisite state,
- required data/evidence,
- validation gaps,
- authorized external actor,
- external action needed,
- verified external registration state.

### 6. Routing

- Product/Identity Conflict → `regulated-product-context`
- Classification Conflict → `ivdr-device-classification`
- Labeling/UDI-Carrier/Claim Conflict → `medical-device-labeling-ifu` / `regulatory-claims-consistency`
- Class-D-/NB-/EURL Dependency → `ivdr-class-d-conformity` soweit relevant
- Certificate-/Controlled-Record Gap → `controlled-quality-documentation`
- actual EUDAMED Actor/Device operation → `human-procedure-wizard` oder autorisierter External-Action-Path.

## Output-Verträge

`ivd-udi-data-set.json` enthält Device/Family/Variant Context, Basic UDI-DI/UDI-DI References, Issuing Entity, EMDN, IVDR Class, Actor/SRN, Certificate/Labeling References, Source Evidence, Field Status und `asOf`.

`eudamed-readiness.json` enthält Current Module State/Source, Applicable Registration Objects, Prerequisites, Data Validation Status, Gaps, Authorized External Actor, External Action State und verified Completion Evidence.

## Memory Path

Persistenzwürdig sind validierte UDI-/Device-Identity-Mapping-Heuristiken, abstrahierte EUDAMED-Readiness-Checks und stabile Parent/Variant/Legacy-Mapping-Muster. Konkrete UDI-/SRN-/EUDAMED-IDs, aktuelle Module-Snapshots, Certificate IDs, Device Registration States, Portal-/User-Zustände und vertrauliche Device Data bleiben run-only bzw. in kontrollierten Regulatory/Master-Data-Records. Regulatory Candidates benötigen `sourceRefs`, `asOf` und `reviewAfter`. Übergib nur abstrahierte geeignete `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- **Current module state first** eingehalten wird,
- Device-/UDI-Identität auf kontrollierter Evidence statt erfundenen IDs beruht,
- Product Context, Classification und Labeling konsistent sind,
- **UDI data ≠ issuance** und **Registration data ≠ registration** respektiert werden,
- nicht verfügbare/nicht mandatory Module nicht fälschlich als aktive Pflichtworkflows behandelt werden,
- externe EUDAMED-Zustände nur aus verifizierter Evidenz gesetzt werden,
- konkrete Identifier-/Portal-/Registration-Zustände nicht in globales dauerhaftes Memory gelangen.
