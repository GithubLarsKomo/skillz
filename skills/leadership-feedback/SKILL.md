---
name: leadership-feedback
description: Strukturiert Führungsfeedback aus beobachtbarem Verhalten, Wirkung, Perspektivklärung, Erwartung und Follow-up. Verwenden für Feedback geben oder empfangen, ohne Motive oder Persönlichkeit zu erfinden.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires: []
consumes:
  - leadership-development-model.json
  - leadership-reflection.json
outputs:
  - leadership-feedback-plan.json
lastEvaluated: 2026-09-03
---

# Leadership Feedback

## Zweck

Bereitet Führungsfeedback so vor, dass beobachtbares Verhalten, Wirkung, Perspektive der anderen Seite, Erwartung und Follow-up getrennt bleiben. Der Skill unterstützt Feedback geben und empfangen, ist aber weder Gesprächsdurchführung noch formelle Personalmaßnahme.

## Ablauf

1. Feedback-Zweck und relevanten Kontext fixieren.
2. Beobachtungen von Interpretation, Bewertung und Motivzuschreibung trennen.
3. Wirkung nur soweit formulieren, wie sie beobachtbar oder als eigene Wahrnehmung kenntlich ist.
4. Fragen vorbereiten, die die Perspektive der anderen Seite öffnen.
5. Erwartung oder Bitte konkret und verhaltensbezogen formulieren.
6. Gewünschte Vereinbarung und Follow-up-Kandidaten definieren.
7. Unsicherheit, fehlende Evidenz und mögliche Safety-/HR-/Legal-Grenzen sichtbar halten.

## Output

`leadership-feedback-plan.json` enthält mindestens `schemaVersion`, `feedbackPlanId`, `purpose`, `contextRefs`, `observations`, `interpretationsToAvoid`, `impact`, `questions`, `expectation`, `dialogueRisks`, `desiredAgreement`, `followUpCandidates`, `unknowns`, `status` und `updatedAt`.

## Regeln

- Aussagen über Motive, Charakter oder Persönlichkeit sind keine Beobachtungen.
- Feedback beschreibt keine geschützten oder sachfremden persönlichen Merkmale als Leistungs- oder Führungsdefizit.
- Eine geplante Formulierung ist keine erfolgte Kommunikation; Status wird nicht ohne Evidenz auf `delivered` oder `agreed` gesetzt.
- Bei formeller Disziplin, Harassment, Diskriminierung, Investigation, Gesundheits- oder Krisensignalen zuerst `coaching-safety-routing` verwenden.
- Feedback darf nicht als manipulative Technik zur Umgehung legitimer Interessen oder Entscheidungsrechte eingesetzt werden.

## Übergaben

- geplantes Gespräch → `meeting-preparation` oder `difficult-conversation-workflow`;
- entwicklungsorientiertes 1:1 → `leadership-1on1-workflow`;
- Performance-Kontext → `performance-management-workflow`;
- bestätigte Follow-ups → `decision-and-follow-up-tracker`.

## Abschlusskriterien

Beobachtung, Wirkung, offene Perspektivfragen, konkrete Erwartung und gewünschte Vereinbarung liegen getrennt und ohne erfundene Motive vor.