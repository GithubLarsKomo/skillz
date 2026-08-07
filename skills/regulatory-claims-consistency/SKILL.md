---
name: regulatory-claims-consistency
description: Prüft Medical-Device- und IVD-Claims über Labeling, Design und Regulatory Evidence auf Widersprüche und unbelegte Aussagen.
userFacing: true
implicitInvocation: true
category: regulated-engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - medical-device-labeling-ifu
  - regulated-product-context
  - regulatory-evidence-traceability
  - design-control-traceability
outputs:
  - claims-consistency-map.json
  - claim-conflicts.json
  - claims-remediation-plan.md
lastEvaluated: 2026-08-07
---

# Regulatory Claims Consistency

## Zweck und Grenze

Dieser Skill prüft, ob produktbezogene Claims über Intended Purpose/Use, Labeling/IFU, Design Inputs, Performance Evidence, Risk Information und vorhandene Submission-/Regulatory-Artefakte konsistent und evidenzgedeckt sind. Er erzeugt **keine neue Claim-Wahrheit** und ändert keine kontrollierten Dokumente selbst.

## Kernprinzipien

- **One claim identity:** semantisch gleiche Claims werden über stabile Claim-IDs verbunden, auch wenn Wortlaut oder Sprache abweichen.
- **Claim scope matters:** Market, Product Variant, Population, Specimen, User, Setting, Method und Version gehören zum Claim-Kontext.
- **Evidence before harmonization:** Widersprüche werden nicht durch sprachliche Vereinheitlichung kaschiert; zuerst wird geklärt, welche Aussage evidenz- und regulatorisch tragfähig ist.
- **No weakest-link promotion:** eine weitergehende Aussage in Marketing/Website darf nicht still zur neuen Produktbasis werden.
- **Risk and limitations count:** Safety-, Limitation- und Contraindication-Aussagen werden genauso konsistent geprüft wie Benefit-/Performance-Claims.
- **Regulatory state is scoped:** authorized/cleared/certified wording eines Marktes wird nicht automatisch auf andere Märkte übertragen.

## Workflow

### 1. Claim Sources registrieren

Indexiere relevante Claims/Statements aus Product Context, Labeling/IFU, Design Inputs, Risk Information, Performance/Clinical/Analytical Evidence, eSTAR/510(k)/De-Novo-Artefakten, IVDR-PER/PMS sowie freigegebenen externen Kommunikationsartefakten soweit im Scope.

### 2. Claim Normalization

Erzeuge pro Claim eine stabile ID und erfasse Wortlaut/Meaning, Market, Variant, Population/Specimen/User/Setting, Evidence/Requirement References, Version, Source Artifact und Approval/Authorization Context.

### 3. Konsistenz prüfen

Klassifiziere mindestens:
- `consistent`,
- `wording-difference-same-meaning`,
- `scope-mismatch`,
- `evidence-mismatch`,
- `regulatory-state-mismatch`,
- `risk/limitation-conflict`,
- `unsupported-claim`,
- `unknown`.

### 4. Conflict Authority bestimmen

Bei Konflikten gilt nicht automatisch die jüngste oder marketingstärkste Formulierung. Bestimme die tragfähige Basis aus confirmed Product Context, aktueller Regulatory-/Authorization-Evidence, Design-/Performance-Evidence und Risk/Limitations. Offene Konflikte bleiben offen.

### 5. Remediation Routing

- Label/IFU-Korrektur → `medical-device-labeling-ifu` + `controlled-quality-documentation`
- Design-/Evidence-Gap → zuständiger Design-/Analytical-/Clinical-Skill
- Risk-/Limitation-Gap → `medical-device-risk-management-iso14971`
- marktbezogene Submission-/Change-Frage → FDA/EU Front Door bzw. `design-change-regulatory-impact`
- Postmarket-Signal aus Claim/Use-Konflikt → `fda-complaint-mdr-reportability` oder `ivdr-pms-vigilance`
- systemischer Qualitätsfehler → bestehender CAPA/RCA-Lifecycle.

## Output-Verträge

`claims-consistency-map.json` enthält Claim ID, Meaning, Scope, Source Artifacts, Evidence/Requirement/Risk Links, Regulatory State und Consistency Status.

`claim-conflicts.json` enthält Conflict ID, beteiligte Claims/Sources, Conflict Type, Impact, Evidence Gap, Market Scope, Decision Owner und Next Skill.

`claims-remediation-plan.md` priorisiert evidenzbasierte Korrekturen; er ändert keine freigegebenen Claims automatisch.

## Memory Path

Persistenzwürdig sind validierte Claim-Normalisierungs-, Scope- und Konflikt-Heuristiken sowie stabile Regeln zur Evidence-/Risk-Verknüpfung. Konkrete Claims, aktuelle Webseiten-/IFU-Texte, Submission-Wording, unveröffentlichte Evidenz und offene Claim-Konflikte bleiben run-only bzw. in kontrollierten Records. Regulatory Candidates benötigen `sourceRefs`, `asOf` und `reviewAfter`. Übergib nur abstrahierte geeignete `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- **Evidence before harmonization** eingehalten wird,
- Claim Scope und Regulatory State explizit sind,
- Marketing-/Website-Wording nicht still zur Produktbasis wird,
- Safety/Limitations genauso geprüft werden wie Performance-/Benefit-Claims,
- Konflikte nicht ohne Evidence/Authority-Rationale aufgelöst werden,
- Remediation an bestehende Owner statt Parallelprozesse geroutet wird,
- konkrete Claims und offene Konflikte nicht in globales dauerhaftes Memory gelangen.
