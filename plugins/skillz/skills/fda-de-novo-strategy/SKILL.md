---
name: fda-de-novo-strategy
description: Entwickelt eine evidenzgebundene FDA-De-Novo-Strategie für neuartige Low-/Moderate-Risk-Devices ohne tragfähigen Predicate und verbindet Risiko, Controls, Evidenz und offene FDA-Fragen.
---

# FDA De Novo Strategy

## Zweck und Grenze

Dieser Skill entwickelt eine De-Novo-Strategie für ein neuartiges Device, wenn kein tragfähiger legally marketed Predicate für eine 510(k)-SE-Argumentation vorhanden ist und eine risikobasierte Class-I-/Class-II-Einordnung mit General Controls bzw. General + Special Controls plausibel erscheint.

Er stellt **keinen De-Novo-Request bei FDA**, gewährt keine Marketing Authorization und entscheidet nicht endgültig, dass De Novo der richtige Pathway ist. PMA-/HDE-/andere Pathways bleiben sichtbar, wenn Risk/Controls oder Device-Kontext eine Low-/Moderate-Risk-De-Novo-Hypothese nicht tragen.

## Kernprinzipien

- **Kein Predicate ist Ausgangspunkt, nicht alleinige Begründung:** De Novo braucht zusätzlich eine belastbare Risk-/Control-Story für Class I oder II.
- **Risk-first:** bekannte und plausible Risiken werden mit General Controls, vorgeschlagenen Special Controls und Evidence Needs verknüpft.
- **Controls müssen prüfbar sein:** ein vorgeschlagener Special Control braucht Risk Link, Ziel, Verifikations-/Evidenzlogik und residuale Unsicherheit.
- **Authority Boundary:** nur FDA kann einen De-Novo-Request grant/decline und eine neue Classification Regulation samt Controls etablieren.
- **Aktueller Submission-Kontext:** aktuelle De-Novo-, eSTAR-, Acceptance- und Q-Sub-Anforderungen werden aus offiziellen FDA-Quellen geladen statt als statische Workflow-Details konserviert.
- **Pathway nicht erzwingen:** wenn General/Special Controls keine reasonable assurance of safety and effectiveness plausibel tragen, bleibt De Novo blocked und andere Pathways müssen bewertet werden.

## Workflow

### 1. Eligibility-Hypothese fixieren

Übernimm Product Context und FDA Classification/Product-Code-Assessment. Dokumentiere, warum kein tragfähiger legally marketed Predicate vorhanden ist oder warum eine 510(k)-SE-Route nicht belastbar erscheint.

### 2. Risk-/Class-Hypothese entwickeln

Nutze `medical-device-risk-management-iso14971`, um zentrale Hazards, hazardous situations, harms, Risk Controls und Residual Risks zu strukturieren. Leite daraus eine begründete Hypothese ab, ob General Controls allein oder General + Special Controls eine Class-I-/II-Einordnung plausibel machen könnten.

### 3. Control Architecture aufbauen

Erfasse bestehende Controls und Control Gaps. Für potenzielle Special Controls dokumentiere mindestens Risk Link, Control Objective, proposed Control Mechanism, Verification/Evidence Need, Applicability und offene Unsicherheit. Detailausarbeitung geht an `fda-de-novo-special-controls`.

### 4. Evidence Package kartieren

Verknüpfe Claims, Risks, Controls und erforderliche Bench-/Analytical-/Software-/Human-Factors-/Clinical-/andere Evidenz über `regulatory-evidence-traceability`. Eine universelle Testliste ist unzulässig; Evidenz folgt den konkreten Risks/Claims/Controls.

### 5. FDA-Fragen isolieren

Formuliere die Fragen, deren Beantwortung durch FDA die Strategy wesentlich de-risken würde, z. B. Device Type/Classification, Proposed Special Controls, Evidence Scope oder Study Design. Übergib geeignete Fragen an `fda-qsub-strategy`.

### 6. Aktuelle Submission-/Acceptance-Anforderungen prüfen

Verifiziere aktuelle eSTAR-/Electronic-Submission-, Acceptance-Review- und sonstige formale Anforderungen aus offiziellen FDA-Quellen. Diese Informationen werden mit `asOf` geführt und nicht als zeitlose Skill-Konstanten behandelt.

### 7. Strategy State ableiten

Status mindestens `de-novo-plausible|de-novo-plausible-with-gaps|qsub-recommended|blocked-by-risk-controls|blocked-by-evidence|alternative-pathway-review-required|unknown`. Ein positives Resultat bleibt Strategy Hypothesis, keine FDA-Entscheidung.

## Output-Verträge

`de-novo-strategy.json` enthält Product Context, no-viable-predicate Rationale, proposed Class, General-/Special-Control-Hypothese, Risk/Control Links, Evidence Coverage, FDA Questions, Current Submission Context, Strategy State, Authority Boundary, `asOf` und Source References.

`de-novo-evidence-gaps.json` enthält Gap-ID, Risk/Claim/Control-Bezug, benötigte Evidenz oder FDA-Feedback, Impact, Next Skill/Owner, Stop Condition und Re-evaluation Trigger.

## Downstream

Primäre Consumer sind `fda-de-novo-special-controls`, `fda-qsub-strategy` und später `fda-estar-submission-builder`. Risk-/Evidence-Gaps gehen an ihre bestehenden Fach-Skills zurück. Ein ungeeigneter De-Novo-Case wird an `fda-medical-device-ivd-regulatory-specialist` für alternative Pathway-Bewertung zurückgegeben.

## Memory Path

Persistenzwürdig sind validierte produktspezifische Risk-/Control-Muster, robuste De-Novo-Eligibility-Heuristiken und wiederverwendbare Evidence-Mapping-Patterns. Aktuelle Pathway-Hypothesen, proposed Class, momentane FDA-Submission-Regeln, offene FDA-Fragen und unbestätigte Special-Control-Vorschläge bleiben run-only. Regulatory Candidates benötigen `sourceRefs`, `asOf` und für veränderliche FDA-Prozessinformationen `reviewAfter`. Übergib nur geeignete `memory-candidate-handoff-v1`-Kandidaten an `communication-memory-governance`; der Skill persistiert nichts selbst.

## Qualitätsgate

Bestanden nur wenn:

- fehlender Predicate nicht als alleinige De-Novo-Begründung verwendet wird,
- Risk und Controls die Class-I-/II-Hypothese nachvollziehbar tragen,
- vorgeschlagene Special Controls nicht als von FDA etablierte Controls dargestellt werden,
- Evidence Needs konkret an Risks/Claims/Controls gebunden sind,
- aktuelle Submission-/Acceptance-Anforderungen aus FDA-Quellen stammen,
- FDA-Fragen gezielt an Q-Sub statt in Annahmen aufgelöst werden,
- ungeeignete Low-/Moderate-Risk-Hypothesen alternative Pathway-Prüfung triggern,
- aktuelle Strategy-Hypothesen nicht als dauerhaftes Memory-Faktum gespeichert werden.
