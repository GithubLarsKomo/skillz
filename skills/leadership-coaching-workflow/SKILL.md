---
name: leadership-coaching-workflow
description: Orchestriert longitudinales Führungskräfte-Coaching von Contracting und Entwicklungsmodell über reale Führungssituationen, Reflexion und Verhaltensexperimente bis zu Review und Re-Kalibrierung. Verwenden als kanonischen Leadership-Coaching-Entry-Point; Safety-, HR-, Legal- und Compliance-Grenzen bleiben explizite Routing-Gates.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
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
consumes: []
outputs:
  - leadership-coaching-state.json
lastEvaluated: 2026-09-03
---

# Leadership Coaching Workflow

## Zweck

Dies ist der kanonische User Entry Point für longitudinales Führungskräfte-Coaching. Der Workflow routet zwischen vorhandenen und neuen Spezialskills; er dupliziert deren Fachlogik nicht.

## Kernzyklus

`contract -> development goal -> real situation -> reflection -> behavior experiment -> real situation -> review -> retain/modify/stop`.

## Routing

1. Kein belastbarer Coaching-Auftrag → `leadership-coaching-intake`.
2. Kein beobachtbares Entwicklungsziel → `leadership-development-model`.
3. Reale relevante Situation liegt vor → `leadership-reflection`.
4. Testbare Lernhypothese liegt vor → `leadership-behavior-experiment`.
5. Experiment wurde real angewendet → `leadership-coaching-review`.
6. Safety-/HR-/Legal-/Compliance-Signal → zuerst `coaching-safety-routing`.
7. Meeting-Vorbereitung, Entscheidungen und offene Schleifen nutzen bestehende Skills wie `meeting-preparation` und `decision-and-follow-up-tracker`, statt eigene Parallelobjekte zu erzeugen.

## State Contract

`leadership-coaching-state.json` ist nur ein Zustandsindex und enthält mindestens `schemaVersion`, `coachingCaseId`, `version`, `status`, `mode`, `contractRef`, `roleContextRefs`, `activeDevelopmentGoalIds`, `activeExperimentIds`, `latestReflectionRef`, `latestReviewRef`, `safetyState`, `routing`, `persistencePolicy` und `updatedAt`.

Zulässige Statuswerte: `draft | active | paused | routed | completed | superseded`.

## Persistenz

Rohgespräche, unnötige Mitarbeiterdaten und sensible Drittinformationen werden nicht automatisch in den State kopiert. Der Contract steuert, welche strukturierten Coaching-Artefakte dauerhaft gehalten werden dürfen.

## Grenzen

Der Workflow ist kein Psychotherapie-, Krisen-, HR-Entscheidungs-, Investigation- oder Rechtsberatungssystem. Er erzeugt keine spekulativen Persönlichkeitsprofile und unterstützt keine manipulative Einflussnahme auf Mitarbeiter.

## Abschlusskriterien

Der Workflow hält zu jedem Zeitpunkt den nächsten fachlich passenden Coaching-Schritt und die relevanten Safety-/Persistenzgrenzen nachvollziehbar, ohne Spezialskill-Logik zu duplizieren.
