---
name: leadership-1on1-workflow
description: Orchestriert die Vorbereitung eines entwicklungsorientierten 1:1 aus bestätigtem Meeting-Kontext, früheren Commitments, Feedback- und Entwicklungsthemen sowie konkreten Follow-up-Kandidaten.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - meeting-preparation
  - leadership-feedback
  - decision-and-follow-up-tracker
consumes:
  - meeting-prep.json
  - leadership-development-model.json
  - decision-follow-up-register.json
outputs:
  - leadership-1on1-plan.json
lastEvaluated: 2026-09-03
---

# Leadership 1:1 Workflow

## Zweck

Bereitet ein wiederkehrendes 1:1 als Führungs- und Entwicklungsformat vor. Der Workflow kombiniert bestätigten Meeting-Kontext, offene Commitments, Entwicklungsziele und gegebenenfalls Feedback, ohne ein Protokoll vorzutäuschen oder private Mitarbeiterdaten unnötig zu persistieren.

## Ablauf

1. Meeting-Fakten, Zweck und verfügbare Zeit aus `meeting-preparation` übernehmen.
2. Offene Commitments, Waiting- und Delegationszustände aus dem Follow-up-Register filtern.
3. Themen der Mitarbeiterseite und Themen der Führungskraft getrennt strukturieren.
4. Fortschritt, Hindernisse und notwendige Entscheidungen priorisieren.
5. Entwicklungsfragen und gegebenenfalls vorbereitetes Feedback integrieren.
6. Gesprächsfragen so formulieren, dass Perspektive und Ownership der Mitarbeiterseite sichtbar werden.
7. Entscheidungen, Commitments und Follow-up-Kandidaten als noch zu bestätigende Outcomes markieren.
8. Nach dem Gespräch nur tatsächlich bestätigte Schleifen an `decision-and-follow-up-tracker` übergeben.

## Output

`leadership-1on1-plan.json` enthält mindestens `schemaVersion`, `oneOnOnePlanId`, `meetingRef`, `participantRef`, `objectives`, `previousCommitments`, `employeeTopics`, `managerTopics`, `developmentTopics`, `feedbackRefs`, `questions`, `decisionsToConfirm`, `followUpCandidates`, `risks`, `privacy`, `status`, `unknowns` und `updatedAt`.

## Regeln

- Der Workflow ist kein verdecktes Performance-Rating und kein Ersatz für formelles Performance Management.
- Mitarbeiteragenda und Manageragenda nicht automatisch vermischen oder hierarchisch gewichten.
- Private oder sensible Informationen nur aufnehmen, wenn sie für das konkrete Gespräch erforderlich sind.
- Keine Persönlichkeit, Motivation oder Karriereabsicht aus Tonfall oder Einzelereignissen ableiten.
- Eine geplante Entscheidung oder Zusage ist noch keine bestätigte Entscheidung oder Verpflichtung.

## Übergaben

- bestätigte Entscheidungen/Commitments → `decision-and-follow-up-tracker`;
- neue Leadership-Lernhypothese der Führungskraft → `leadership-reflection`;
- konkrete Feedback-Situation → `leadership-feedback`;
- formeller Performance-Kontext → `performance-management-workflow`.

## Abschlusskriterien

Das 1:1 besitzt eine fokussierte Agenda mit offenen Schleifen, Perspektivfragen, Entwicklungsthemen und klar markierten Entscheidung-/Follow-up-Kandidaten, ohne Gesprächsergebnis oder Mitarbeitermerkmale zu erfinden.