---
name: fda-dual-510k-clia-waiver
description: Orchestriert 510(k)-SE- und CLIA-Waiver-Evidence zu einer konsistenten Dual-Submission-Strategie ohne Reviews zu duplizieren.
---

# FDA Dual 510(k) + CLIA Waiver

## Zweck und Grenze

Dieser Skill entscheidet und strukturiert den gemeinsamen Dual-510(k)/CLIA-Waiver-Pfad für IVDs, wenn 510(k)-Clearance und CLIA Waiver in einer koordinierten Submission verfolgt werden sollen. Er **bewertet SE und CLIA-Waiver-Eignung nicht neu**, sondern synchronisiert deren Evidence-/Study-/Gap-Verträge.

## Kernprinzipien

- **Dual is one coordinated pathway:** 510(k)- und Waiver-Teil bleiben fachlich getrennt nachvollziehbar, werden aber als ein gemeinsamer FDA-Pfad geplant.
- **No double-study by default:** gemeinsame Study Evidence wird nur einmal geplant, wenn Design/Population/Acceptance Logic beide Regulatory Questions belastbar trägt.
- **Distinct conclusions remain distinct:** ein positives SE-Hypothesis schließt Waiver-Gaps nicht; Waiver-Evidence ersetzt keine SE-/Safety-/Performance-Evidence.
- **Q-Sub before avoidable ambiguity:** wesentliche offene Study-Design-/Predicate-/Waiver-Fragen werden über `fda-qsub-strategy` geroutet statt im Dual-Paket geraten.
- **Current eSTAR dual mode:** aktuelle FDA-eSTAR-Anforderungen für Dual 510(k)/CLIA werden über `fda-estar-submission-builder` im Modus `dual-510k-clia` assembliert.
- **One external state:** Draft/ready/submitted/received/decision werden nicht separat erfunden; externe Zustände benötigen verifizierte Evidence.

## Workflow

### 1. Dual Eligibility/Value fixieren

Erfasse Product/Pathway Context, Predicate/SE State, CLIA-Waiver Strategy, Zielsetting/User, gemeinsame Study-Möglichkeiten, wesentliche Gaps und aktuelle FDA Dual/Q-Sub/eSTAR-Quellen mit `asOf`.

### 2. Evidence Contracts synchronisieren

Mappe SE- und CLIA-Anforderungen auf gemeinsame bzw. getrennte Evidence Items. Klassifiziere `shared|510k-only|clia-only|conflicting-design-needs|unknown` und dokumentiere die Regulatory Question hinter jedem Item.

### 3. Study Design integrieren

Prüfe, ob gemeinsame Studien beide Ziele mit geeigneten Populations-/User-/Comparator-/Challenge-/Acceptance-Designs tragen. Vermeide künstliche Zusammenlegung, wenn ein gemeinsames Design eine Regulatory Question schwächt.

### 4. Q-Sub Gate

Bei wesentlichen Unsicherheiten zu Dual-Strategie, Study Design oder Evidenzverwendung → `fda-qsub-strategy`. Tatsächliches FDA-Feedback bleibt projektbezogene Decision Evidence und wird nicht global verallgemeinert.

### 5. Dual Evidence Package erzeugen

`dual-evidence-package.json` enthält die pathway-spezifischen Inputs für den bestehenden `fda-estar-submission-builder` im Modus `dual-510k-clia`. Der Builder bleibt Eigentümer der aktuellen eSTAR-Struktur und Submission Assembly.

### 6. Downstream Routing

- eSTAR Assembly → `fda-estar-submission-builder` (`dual-510k-clia`)
- Acceptance Preflight → `fda-acceptance-readiness`
- FDA Review Questions → `fda-additional-information-response`
- fehlende SE-Evidence → `fda-510k-substantial-equivalence`
- fehlende Waiver/Flex Evidence → `fda-ivd-clia-waiver`
- External Submission → verifizierter Human-/External-Action-Path.

## Output-Verträge

`dual-510k-clia-strategy.json` enthält Pathway Rationale, Current Sources/`asOf`, SE/Waiver States, Shared-vs-Distinct Evidence Strategy, Q-Sub Need, Critical Gaps und Authority Boundary.

`dual-study-evidence-map.json` enthält Regulatory Question, Evidence/Study Item, `shared|510k-only|clia-only`, Design/Acceptance References, Risk/Claim Links, Owner und Gap State.

`dual-evidence-package.json` enthält einen kanonischen `pathway: dual-510k-clia`, SE Inputs, CLIA Inputs, shared evidence references, unresolved gaps und eSTAR handoff metadata.

## Memory Path

Persistenzwürdig sind validierte Dual-Evidence-Reuse-Heuristiken, Study-Sharing-Entscheidungsmuster und abstrahierte Q-Sub-Trigger. Konkrete Predicates, Product Study Designs, FDA Feedback, Submission IDs, current eSTAR versions und Dual Decision States bleiben run-only bzw. in kontrollierten Regulatory Records. Regulatory Candidates benötigen `sourceRefs`, `asOf` und `reviewAfter`. Übergib nur abstrahierte geeignete `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- **Dual is one coordinated pathway** ohne fachliche Vermischung der SE-/Waiver-Schlüsse umgesetzt wird,
- gemeinsame Evidenz nur bei belastbarer Eignung wiederverwendet wird,
- separate Gaps/Conclusions sichtbar bleiben,
- wesentliche FDA-Study-/Strategy-Unsicherheit an Q-Sub geroutet wird,
- das Dual-Paket in den bestehenden eSTAR-/Acceptance-/Response-Pfad mündet,
- externe Submission/FDA Decision nicht simuliert wird,
- konkrete Dual-/FDA-/Study-Zustände nicht in globales dauerhaftes Memory gelangen.
