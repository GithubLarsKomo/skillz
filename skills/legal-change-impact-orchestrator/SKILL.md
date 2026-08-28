---
name: legal-change-impact-orchestrator
description: Übersetzt verifizierte Legal-Change-Events in strukturierte Impact-Work-Orders für betroffene Rechtsträger, Prozesse, Verträge, Policies, Controls und Specialist Domains, ohne die fachliche Rechtsbewertung selbst zu übernehmen. Verbindet Legal Change Monitoring mit Obligation Register, Specialist Router und Executive Governance.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - legal-change-monitoring
  - legal-specialist-router
  - compliance-obligation-register
  - legal-compliance-risk-assessment
outputs:
  - legal-change-impact-map.json
  - legal-change-work-orders.json
  - legal-change-decision-queue.json
lastEvaluated: 2026-08-28
---

# Legal Change Impact Orchestrator

## Zweck

Dieser Skill ist ein **Router, kein Fachgutachter**. Er beantwortet: Wer muss welche Auswirkung eines bestätigten Legal Change Events bis wann prüfen? Die materielle Antwort gehört dem zuständigen Specialist und der zuständigen Decision Authority.

## Inputs

- `legal-change-events.json`
- aktuelles `compliance-obligation-register.json`
- Matter-/Entity-/Process-/Contract-/Policy-/Control-Kontext soweit vorhanden
- Legal/Compliance Risk Context

## Applicability Funnel

Für jedes Change Event schrittweise prüfen:

1. **Jurisdiction:** welche Länder/Regionen können betroffen sein?
2. **Entity:** welche Rechtsträger fallen potentiell in den Scope?
3. **Activity/Product/Role:** welche Tätigkeit, Rolle, Produkt-/Daten-/Arbeits-/Transaktionskonstellation löst die Norm aus?
4. **Obligation:** welche bestehenden Pflichten werden neu, geändert, aufgehoben oder unklar?
5. **Implementation Surface:** welche Policy, SOP, Contract, Template, Control, System, Training, Record, Reporting-/Approval-Gate oder externe Beziehung kann betroffen sein?
6. **Specialist Owner:** wer beurteilt die materielle Auswirkung?
7. **Decision Authority:** wer darf Risiko, Änderung oder Nicht-Handeln freigeben?

Unklarheit in einer Stufe bleibt als `unknown` sichtbar und wird nicht durch die nächste Stufe übersprungen.

## Work Order Contract

```json
{
  "changeId": "LC-...",
  "specialist": "...",
  "question": "...",
  "entity": "...",
  "jurisdiction": "...",
  "effectiveFrom": "...",
  "affectedObjects": [],
  "knownFacts": [],
  "unknowns": [],
  "sourceRefs": [],
  "riskHint": "critical|high|normal|low",
  "deadline": "...",
  "expectedOutput": "..."
}
```

## Obligation Delta Gate

Ein Change Event wird nicht automatisch als neue Unternehmenspflicht eingetragen. Der zuständige Specialist bestätigt `applicable`, `not-applicable`, `changed`, `repealed`, `transitional` oder `unresolved`. Erst danach wird das `compliance-obligation-register` aktualisiert.

## Priority Model

Priorität aus Effective Date, möglicher Sanktion/Haftung, operativer Vorlaufzeit, irreversibler Wirkung, betroffenen Personen/Produkten, Control Gap und Decision Lead Time ableiten. Keine künstliche Präzisionszahl vortäuschen; begründete Kategorien und konkrete Deadlines bevorzugen.

## Cross-Domain Routing

Ein Event darf mehrere unabhängige Work Orders erzeugen. Beispiel: neue Beschäftigtendatenregel → Privacy + Employment + Works-Council/Control Work Orders. Neue Produkthaftungsregel → Product Liability + Contract + Insurance + Regulatory Interface. Keine Harmonisierung fachlicher Antworten durch den Router.

## Closure Gate

Ein Change Event ist erst `implemented/closed`, wenn:

- Applicability fachlich entschieden,
- Obligation Register aktualisiert,
- erforderliche Controls/Policies/Contracts/Systems geändert,
- erforderliche Evidence/Training/Communication vorhanden,
- offene Residual Risks autorisiert oder weiter eskaliert,
- Wirksamkeits-/Follow-up-Prüfung terminiert oder abgeschlossen ist.

`reviewed` allein ist kein Closure Status.

## Qualitätsgate

Pass nur, wenn Jurisdiction→Entity→Trigger→Obligation→Implementation Surface→Specialist→Authority rückverfolgbar ist, Unknowns erhalten bleiben und kein Change Event ohne fachliche Applicability-Entscheidung als umgesetzt geschlossen wird.