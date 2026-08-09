---
name: fda-estar-submission-builder
description: Assembliert 510(k)-, De-Novo- oder Dual-CLIA-Evidenz pathway-aware in eine aktuelle FDA-eSTAR-Content-Map ohne extern einzureichen.
---

# FDA eSTAR Submission Builder

## Zweck und Grenze

Dieser Skill assembliert vorhandene, fachlich bewertete Evidence-/Regulatory-Artefakte für **genau einen** FDA-Premarket-Pfad in eine aktuelle eSTAR-orientierte Content Map. Unterstützte Modi sind `510k`, `de-novo` und `dual-510k-clia`. Er prüft, welche Inhalte in die aktuelle FDA-eSTAR-Struktur gehören, wo Evidenz fehlt, welche Cross-References verwendet werden und welche Artefakte noch nicht submission-ready sind.

Er führt **keine FDA-Einreichung** durch, erzeugt keine FDA-Receipt-Bestätigung und bewertet fachliche 510(k)-SE-, De-Novo- oder CLIA-Waiver-Strategie nicht neu. Die aktuelle eSTAR-Version, FDA-Template-Struktur, Portal-/Electronic-Submission-Anforderungen und etwaige Ausnahmen werden vor jeder Ausführung aus aktuellen offiziellen FDA-Quellen ermittelt statt im Skill festgeschrieben.

## Pathway Contract

Genau ein Modus ist aktiv:

### `510k`
Erwartete fachliche Inputs umfassen mindestens:
- `fda-device-classification.json`,
- `substantial-equivalence-assessment.json`,
- `substantial-equivalence-matrix.md`,
- zugehörige Safety-/Performance-/Risk-Evidenz.

### `de-novo`
Erwartete fachliche Inputs umfassen mindestens:
- `fda-device-classification.json`,
- `de-novo-strategy.json`,
- `special-controls-matrix.json`, soweit für die Strategy relevant,
- zugehörige Safety-/Performance-/Risk-Evidenz.

### `dual-510k-clia`
Erwartete fachliche Inputs umfassen mindestens:
- `dual-evidence-package.json`,
- die referenzierten 510(k)-SE-Artefakte,
- `clia-waiver-strategy.json`,
- zugehörige shared/510k-only/clia-only Study-/Performance-/Risk-Evidenz.

Der Skill besitzt bewusst **keine harten Dependencies auf alle Pathway-Skills**, damit die Pfade sich nicht gegenseitig künstlich erforderlich machen. Der aktive Modus muss jedoch seine pathway-spezifischen Input-Verträge erfüllen.

## Kernprinzipien

- **Current eSTAR first:** Template-/Version-/Formatregeln werden aus der aktuellen FDA-eSTAR-Quelle geladen.
- **Assembly statt Re-Assessment:** fachliche Schlussfolgerungen bleiben Eigentum ihrer Upstream-Skills.
- **One pathway per package:** 510(k), De Novo und Dual 510(k)/CLIA werden als getrennte Modi behandelt; Dual ist ein eigener koordinierter FDA-Pfad und kein zufälliges Hybridpaket.
- **Evidence reuse statt Duplikation:** gleiche Evidenz wird über stabile Cross-References wiederverwendet, nicht inkonsistent mehrfach erzählt.
- **Omission ist eine Entscheidung:** fehlende oder nicht anwendbare Inhalte werden mit Requirement/Reason dokumentiert; leere Abschnitte gelten nicht automatisch als zulässig.
- **External action boundary:** CDRH-Portal-/eSTAR-Upload und tatsächliche Submission bleiben autorisierte Human-/External-Actions.

## Workflow

### 1. Pathway und Current FDA Context fixieren

Setze `pathway: 510k|de-novo|dual-510k-clia`. Ermittle aktuelle eSTAR-Version/Downloadquelle, relevante elektronische Submission-Anforderungen, aktuelle FDA-Hinweise und `asOf`. Ein historisches lokales Template wird nicht ungeprüft weiterverwendet.

### 2. Fachliche Inputs validieren

Prüfe, ob die pathway-spezifischen Upstream-Artefakte vorhanden, aktuell, widerspruchsfrei und ausreichend referenziert sind. Ein internes SE-/De-Novo-/CLIA-Resultat bleibt als Hypothese/Strategy gekennzeichnet; der Builder macht daraus keine FDA-Entscheidung.

### 3. Content Map erzeugen

Mappe aktuelle eSTAR-Sektionen/Felder auf:
- Source Artifact,
- Claim/Requirement,
- Evidence Reference,
- geplanten Submission Content,
- Owner,
- Status `ready|partial|missing|not-applicable-with-rationale|blocked`,
- Cross-References,
- Current-Template Reference.

### 4. Konsistenz prüfen

Suche insbesondere nach:
- widersprüchlichem Intended Use/Indications,
- inkonsistenten Device-/Product-Code-/Classification-Angaben,
- nicht synchronen Risk-/Performance-Schlussfolgerungen,
- Predicate-/SE-, De-Novo-Control- oder Dual-CLIA-Aussagen ohne Source Evidence,
- bei Dual nach widersprüchlicher shared-vs-pathway-specific Evidence-Zuordnung,
- doppelten Inhalten mit abweichender Aussage,
- veralteten Template-/Guidance-Annahmen.

### 5. Submission Readiness ableiten

`submission-readiness.json` bewertet technische/contentbezogene Assembly-Readiness, **nicht** FDA Acceptance oder substantive scientific adequacy. Blocker und Partial Items bleiben getrennt von bloßen redaktionellen Restarbeiten.

### 6. Handoff

Übergib die Content Map an `fda-acceptance-readiness`. Fachliche Gaps gehen zurück an den jeweiligen Evidence-/Risk-/SE-/De-Novo-/CLIA-Skill. Externe Submission geht an `human-procedure-wizard` oder den autorisierten Regulatory-Prozess und benötigt anschließend verifizierte Receipt-/Submission-Evidenz.

## Output-Verträge

`estar-content-map.json` enthält `pathway`, `asOf`, Current eSTAR Source/Version Reference, Section/Field Mapping, Source Artifacts, Evidence/Requirement Links, Cross-References, Content Status, Owners und Gaps.

`submission-readiness.json` enthält Assembly Scope, Pathway, Required Inputs, Ready/Partial/Missing/Blocked Counts, Critical Gaps, Current-Template Verification, External Submission State und Next Actions. Vor externer Einreichung ist `externalSubmissionState` niemals `submitted`.

## Memory Path

Persistenzwürdig sind validierte pathway-spezifische Content-Mapping-Muster, stabile Cross-Reference-Strategien und wiederverwendbare Assembly-Failure-Patterns. Aktuelle eSTAR-Versionen, lokale Template-Dateien, aktuelle Submission-Pakete, Submission IDs, Portalzustände, Draft Content und momentane Readiness bleiben run-only. Regulatory Candidates benötigen `sourceRefs`, `asOf` und für eSTAR-/Prozessinformationen `reviewAfter`. Übergib nur geeignete `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- genau ein Pathway aktiv ist,
- aktuelle eSTAR-/Electronic-Submission-Anforderungen verifiziert wurden,
- fachliche Upstream-Schlüsse nicht neu bewertet oder umgedeutet werden,
- alle Content-Elemente auf Source/Evidence/Requirement zurückführbar sind,
- Not-Applicable-/Omission-Entscheidungen begründet sind,
- Submission Readiness nicht mit FDA Acceptance verwechselt wird,
- externe Submission/Receipt nicht simuliert wird,
- aktuelle eSTAR-/Submission-Zustände nicht als dauerhaftes Memory-Faktum gespeichert werden.
