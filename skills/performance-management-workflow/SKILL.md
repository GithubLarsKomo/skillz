---
name: performance-management-workflow
description: Strukturiert Performance Management von Erwartung und beobachtbarer Evidenz über Leistungslücke, Ursachenhypothesen, Mitarbeiterperspektive und Unterstützung bis zu Review und formellem Routing.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - leadership-feedback
  - coaching-safety-routing
  - decision-and-follow-up-tracker
consumes:
  - role-architecture.json
  - leadership-feedback-plan.json
outputs:
  - performance-management-plan.json
lastEvaluated: 2026-09-03
---

# Performance Management Workflow

## Zweck

Strukturiert informelles und entwicklungsorientiertes Performance Management von bestätigter Erwartung und beobachtbarer Evidenz bis zu Unterstützung, Commitments und Review. Der Workflow unterscheidet Coaching von formeller Disziplin und ersetzt keine HR- oder arbeitsrechtliche Prüfung.

## Kernlogik

`expected outcome -> observed evidence -> gap -> evidence quality -> cause hypotheses -> employee perspective -> support -> expectation -> commitments -> review`.

## Ablauf

1. Erwartete Outcomes, Verantwortungen und Erfolgskriterien aus bestätigter Rollen- oder Aufgabenbasis fixieren.
2. Beobachtbare Performance-Evidenz mit Zeitraum und Provenance erfassen.
3. Leistungslücken beschreiben, ohne aus ihnen automatisch Motivation, Capability oder Persönlichkeit abzuleiten.
4. Ursachen als konkurrierende Hypothesen führen, jeweils mit Evidenz dafür, dagegen und offenen Fragen.
5. Status der Mitarbeiterperspektive explizit halten: `not-yet-obtained`, `partial` oder `captured`.
6. Unterstützungsmaßnahmen, Ressourcen, Erwartung und mögliche Commitments voneinander trennen.
7. Review-Kriterien und Zeitraum definieren.
8. Formelles HR-/Employment-Law-/Compliance-Gate prüfen.
9. Nur bestätigte Commitments und Follow-ups an `decision-and-follow-up-tracker` übergeben.

## Output

`performance-management-plan.json` enthält mindestens `schemaVersion`, `performancePlanId`, `roleContextRefs`, `expectedOutcomes`, `observedEvidence`, `performanceGaps`, `causeHypotheses`, `employeePerspective`, `supportActions`, `expectations`, `commitmentCandidates`, `reviewCriteria`, `professionalGate`, `status`, `unknowns` und `updatedAt`.

## Professional Gate

Das Gate wird ausgelöst, sobald der Kontext formelle Disziplin, Abmahnung, Kündigung, Vergütungsmaßnahme, Diskriminierung, Harassment, Mitbestimmung, Investigation oder andere arbeitsrechtlich relevante Maßnahmen berührt. Dann ist Coaching nur ergänzend; die formelle Bewertung wird an HR beziehungsweise zuständige Legal-/Compliance-Spezialisten geroutet.

## Regeln

- `performance gap != motivation problem != capability problem != personality problem`.
- Einzelereignisse nicht ohne belastbare Basis zu dauerhaften Leistungsurteilen hochstufen.
- Mitarbeiterperspektive nicht erfinden oder aus Schweigen ableiten.
- Unterstützungsbedarf und klare Erwartung können gleichzeitig bestehen; keines ersetzt das andere.
- Keine formelle Sanktion, Kündigung oder arbeitsrechtliche Aussage als geprüft darstellen, solange der professionelle Prozess dies nicht bestätigt.
- Geschützte oder sachfremde Merkmale dürfen nicht als Performance-Kriterium verwendet werden.

## Übergaben

- Feedback-Vorbereitung → `leadership-feedback`;
- schwieriges Gespräch → `difficult-conversation-workflow`;
- bestätigte Follow-ups → `decision-and-follow-up-tracker`;
- formelles Gate → HR, `german-employment-labor-law-specialist`, Compliance oder Investigation-Workflow nach tatsächlichem Trigger.

## Abschlusskriterien

Erwartung, Evidenz, Lücke, Ursachenhypothesen, Mitarbeiterperspektive, Unterstützung, Commitments und Review sind getrennt; formelle Personalmaßnahmen werden nicht durch Coaching simuliert.