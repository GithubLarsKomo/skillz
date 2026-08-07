---
name: medical-device-labeling-ifu
description: Strukturiert Medical-Device- und IVD-Labeling/IFU aus Product Context, Risk und Regulatory Evidence ohne Claims zu erfinden.
userFacing: true
implicitInvocation: true
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - regulated-product-context
  - medical-device-risk-management-iso14971
  - regulatory-evidence-traceability
outputs:
  - labeling-content-map.json
  - labeling-evidence-gaps.json
  - ifu-content-structure.md
lastEvaluated: 2026-08-07
---

# Medical Device Labeling / IFU

## Zweck und Grenze

Dieser Skill strukturiert Labeling-, Package-Insert- und IFU-Inhalte für Medical Devices und IVDs aus bereits bestätigtem Product Context, Risk Controls, Claims und Regulatory Evidence. Er **erfindet keine Claims**, ersetzt keine Design-/Risk-Analyse und führt keine kontrollierte Dokumentfreigabe durch.

## Kernprinzipien

- **Source before wording:** markt- und produktabhängige Labeling-Anforderungen werden aus aktuellen autoritativen Quellen und freigegebenen Produktdaten abgeleitet.
- **One intended purpose:** Intended Purpose/Intended Use, Population, Specimen, User, Setting und Limitations müssen zur freigegebenen Produktbasis passen.
- **Risk-to-label traceability:** Warnings, Precautions, Contraindications, Limitations und Information for Safety werden auf Risk Controls/Evidence zurückgeführt; Labeling ersetzt keine höherwertige Risk Control.
- **Claims need evidence:** Leistungs-, Nutzen- und Vergleichsclaims werden nur aufgenommen, wenn ihre Evidenz und regulatorische Zulässigkeit nachvollziehbar sind.
- **Market-specific structure:** gemeinsame Inhalte werden wiederverwendet, markt- oder pathway-spezifische Anforderungen bleiben getrennt.
- **Labeling draft ≠ approved labeling:** Strukturierung/Drafting ist kein kontrollierter Approval-/Effective-State.

## Workflow

### 1. Labeling Scope fixieren

Erfasse Device/IVD, Varianten, Zielmärkte, Intended Purpose/Use, User/Setting, Specimen/Population, qualitative/quantitative Verwendung, Lifecycle-/Authorization-State und relevante Baseline.

### 2. Current Requirements laden

Ermittle aktuelle markt- und produktspezifische Labeling-Anforderungen. Für FDA werden u. a. allgemeine Device-Labeling-Regeln und für IVDs die IVD-spezifischen Anforderungen berücksichtigt; für EU/IVDR/MDR erfolgt die aktuelle Quellenermittlung über EU Front Door/MDCG-/Regulatory-Evidence-Pfade.

### 3. Content Map bilden

Mappe mindestens:
- Identität/Produktname/Hersteller-/Verantwortlichkeitsangaben,
- Intended Purpose/Use und User/Setting,
- Specimen/Patient/Population soweit relevant,
- Principle/Method/Procedure und notwendige Materials/Equipment,
- Performance-/Clinical-/Analytical Claims,
- Warnings/Precautions/Contraindications/Limitations,
- Storage/Stability/Handling/Installation/Operation,
- Interpretation of Results/Expected Values soweit relevant,
- Symbols/UDI/Traceability-Elemente soweit im Scope,
- Versions-/Market-/Language-Status.

### 4. Evidence und Risk verknüpfen

Jeder materielle Claim und jede Safety-/Limitation-Aussage erhält Evidence-/Risk-/Requirement-Referenzen. Unbelegte oder widersprüchliche Aussagen werden als Gap markiert statt sprachlich geglättet.

### 5. Cross-Artifact Routing

- Claims-Abgleich → `regulatory-claims-consistency`
- Design-/Performance-Gap → zuständiger Design-/Analytical-/Clinical-Skill
- Risk-/Information-for-Safety-Gap → `medical-device-risk-management-iso14971`
- Change Impact → `design-change-regulatory-impact`
- kontrollierte Freigabe/Revision → `controlled-quality-documentation`
- FDA Submission Content → `fda-estar-submission-builder`
- IVDR Performance Evidence → `ivdr-performance-evaluation-report`.

## Output-Verträge

`labeling-content-map.json` enthält Market/Product Context, Content Element, Proposed/Existing Wording Reference, Requirement Source, Evidence/Risk Links, Status, Version/Language und Owner.

`labeling-evidence-gaps.json` enthält Claim/Safety/Instruction Element, Gap Type, Missing Evidence/Decision, Impact, Next Skill und Stop Condition.

`ifu-content-structure.md` ist eine strukturierte Draft-/Review-Gliederung; sie ist **keine freigegebene IFU**.

## Memory Path

Persistenzwürdig sind validierte Labeling-Strukturmuster, wiederverwendbare Risk-to-Label-/Evidence-to-Claim-Heuristiken und stabile marktübergreifende Mapping-Regeln. Konkrete Produktclaims, aktuelle IFU-Texte, unveröffentlichte Performance-Daten, UDI-/Herstellerdaten, aktuelle Guidance-Snapshots und Approval-States bleiben run-only bzw. in kontrollierten Records. Regulatory Memory Candidates benötigen `sourceRefs`, `asOf` und `reviewAfter`. Übergib nur abstrahierte geeignete `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- **Claims need evidence** konsequent eingehalten wird,
- Intended Purpose/Use und Labeling-Inhalte zur bestätigten Produktbasis passen,
- Risk-to-label traceability vorhanden ist,
- markt-/produktabhängige Anforderungen current-source-basiert sind,
- unbelegte Claims/Gaps nicht durch Formulierungen kaschiert werden,
- Drafting nicht als kontrollierte Freigabe dargestellt wird,
- konkrete Labeling-/Claim-Zustände nicht in globales dauerhaftes Memory gelangen.
