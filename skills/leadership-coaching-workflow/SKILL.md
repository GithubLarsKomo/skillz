---
name: leadership-coaching-workflow
description: Orchestriert longitudinales Führungskräfte-Coaching von Contracting und Entwicklungsmodell über reale Führungssituationen, Reflexion und Verhaltensexperimente bis zu situativen Führungsworkflows, Review und Re-Kalibrierung.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.2.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - leadership-coaching-intake
  - leadership-development-model
  - leadership-reflection
  - leadership-behavior-experiment
  - leadership-coaching-review
  - coaching-safety-routing
  - leadership-feedback
  - leadership-delegation
  - leadership-1on1-workflow
  - difficult-conversation-workflow
  - performance-management-workflow
consumes: []
outputs:
  - leadership-coaching-state.json
lastEvaluated: 2026-09-03
---

# Leadership Coaching Workflow

## Zweck

Dies ist der kanonische User Entry Point für longitudinales Führungskräfte-Coaching. Der Workflow routet zwischen Core-Coaching und situativen Führungsworkflows; er dupliziert deren Fachlogik nicht.

## Kernzyklus

`contract -> development goal -> real situation -> reflection -> behavior experiment -> real situation -> review -> retain/modify/stop`.

Situative Führungsskills können an jeder passenden realen Situation eingesetzt werden, ohne einen zweiten Coaching-State aufzubauen.

## Core Routing

1. Kein belastbarer Coaching-Auftrag → `leadership-coaching-intake`.
2. Kein beobachtbares Entwicklungsziel → `leadership-development-model`.
3. Reale relevante Situation liegt vor → `leadership-reflection`.
4. Testbare Lernhypothese liegt vor → `leadership-behavior-experiment`.
5. Experiment wurde real angewendet → `leadership-coaching-review`.
6. Safety-/HR-/Legal-/Compliance-Signal → zuerst `coaching-safety-routing`.

## Situational Routing

- konkretes Feedback geben oder empfangen → `leadership-feedback`;
- Verantwortung mit Entscheidungsraum übertragen → `leadership-delegation`;
- wiederkehrendes entwicklungsorientiertes Mitarbeitergespräch → `leadership-1on1-workflow`;
- konfliktbeladenes oder emotional schwieriges Gespräch → `difficult-conversation-workflow`;
- wiederholte oder relevante Leistungslücke gegen bestätigte Erwartungen → `performance-management-workflow`.

Meeting-Vorbereitung, Entscheidungen und offene Schleifen nutzen weiterhin bestehende Skills wie `meeting-preparation` und `decision-and-follow-up-tracker` statt eigener Parallelobjekte. Formelle HR-, Legal-, Compliance- oder Investigation-Prozesse werden über `coaching-safety-routing` verlassen.

## State Contract

`leadership-coaching-state.json` ist nur ein Zustandsindex und enthält mindestens `schemaVersion`, `coachingCaseId`, `version`, `status`, `mode`, `contractRef`, `roleContextRefs`, `activeDevelopmentGoalIds`, `activeExperimentIds`, `latestReflectionRef`, `latestReviewRef`, `safetyState`, `routing`, `persistencePolicy` und `updatedAt`.

Zulässige Statuswerte: `draft | active | paused | routed | completed | superseded`.

Situative P1-Artefakte werden referenziert, wenn sie für den Coaching-Fall relevant sind; ihre Inhalte werden nicht in den State kopiert.

## Persistenz

Rohgespräche, unnötige Mitarbeiterdaten und sensible Drittinformationen werden nicht automatisch in den State kopiert. Der Contract steuert, welche strukturierten Coaching-Artefakte dauerhaft gehalten werden dürfen. P1-Artefakte übernehmen dieselbe Minimierungsregel.

## Grenzen

Der Workflow ist kein Psychotherapie-, Krisen-, HR-Entscheidungs-, Investigation- oder Rechtsberatungssystem. Er erzeugt keine spekulativen Persönlichkeitsprofile und unterstützt keine manipulative Einflussnahme auf Mitarbeiter.

## Abschlusskriterien

Der Workflow hält zu jedem Zeitpunkt den nächsten fachlich passenden Coaching- oder Führungsworkflow und die relevanten Safety-/Persistenzgrenzen nachvollziehbar, ohne Spezialskill-Logik oder formelle professionelle Prozesse zu duplizieren.
