---
name: legal-compliance-office
description: Orchestriert unternehmerische und private Legal-/Compliance-Matters von Intake und Mandantenstrategie über aktuelle Rechtsgrundlage, Wayfinding, Specialist Routing und Risiko bis zum Final Gate, ohne Fachlogik der Specialists zu duplizieren. Verwenden als zentralen General-Counsel-/Compliance-Einstieg für komplexe oder mehrdomänige Sachverhalte.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - legal-matter-intake
  - legal-client-strategy
  - current-law-context
  - privilege-and-counsel-routing
  - legal-matter-wayfinder
  - legal-specialist-router
  - legal-compliance-risk-assessment
  - legal-matter-final-gate
outputs:
  - legal-matter-status.json
  - legal-matter-plan.md
  - legal-matter-handoff.json
lastEvaluated: 2026-08-28
---

# Legal Compliance Office

## Zweck

Dünner General-Counsel-/Compliance-Orchestrator. Er hält Matter-Ziel, Evidenz, Specialist-Arbeit, Risiko, Autorität und nächste Aktion zusammen, trifft aber keine zweite fachliche Entscheidung neben den Specialists.

## Ablauf

1. Matter mit `legal-matter-intake` strukturieren.
2. Mandantenstrategie mit `legal-client-strategy` fixieren.
3. Früh `privilege-and-counsel-routing` anwenden.
4. Rechts-/Regelwerkskontext über `current-law-context` verifizieren.
5. Bei komplexer Unsicherheit `legal-matter-wayfinder` einsetzen.
6. Fachfragen über `legal-specialist-router` routen und Ergebnisse integrieren.
7. `legal-compliance-risk-assessment` auf aktualisierte Specialist Outputs anwenden.
8. Entscheidungen/Risk Acceptance an die zuständige Autorität übergeben.
9. Vor Abschluss `legal-matter-final-gate` ausführen.
10. Status, offene Punkte und genau nächste sichere Aktion dokumentieren.

## Orchestrator-Regeln

- Fach-Specialists besitzen ihre Domänenlogik; der Orchestrator dupliziert keine Subsumtion.
- Existing Assets first: Regulatory-, QMS-, Patent-, Biopatent-, FTO-, Research- und Grilling-Skills werden bevorzugt wiederverwendet.
- Sport-/Vereinsmatters können `german-association-law-specialist`, `german-sports-law-specialist` und für Rudern `german-rowing-sport-law-specialist` erhalten.
- Ein L3-Gate beendet nicht automatisch alle vorbereitenden Arbeiten.
- Die nächste Aktion muss aus dem aktuellen Matter State ausführbar und autorisiert sein.

## Grenzen

- Keine Simulation einer Rechtsanwaltszulassung, Behördenentscheidung, gerichtlichen Entscheidung, notariellen Beurkundung oder sonstigen externen Autorität.
- Keine Vermischung von staatlichem Recht und privaten Vereins-/Verbandsregeln.

## Qualitätsgate

Pass nur, wenn Matter-Ziel, Current Law, Specialist Ownership, Risiko, Autorität, offene Punkte und Final-Gate-State konsistent zusammenpassen.