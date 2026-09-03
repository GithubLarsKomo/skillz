---
name: leadership-coaching-intake
description: Klärt Auftrag, Rolle, gewünschte Verhaltensänderung, Erfolgsevidenz, Sponsor-/Vertraulichkeitsmodell, Persistenzgrenzen und Coaching-Scope für longitudinales Führungskräfte-Coaching. Verwenden vor einem neuen Leadership-Coaching-Fall oder bei Re-Contracting.
userFacing: true
implicitInvocation: false
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - round-based-requirements-grilling
consumes:
  - role-architecture.json
outputs:
  - leadership-coaching-contract.json
  - leadership-coaching-intake-report.md
lastEvaluated: 2026-09-03
---

# Leadership Coaching Intake

## Zweck

Erzeugt einen belastbaren Coaching-Auftrag. `role-architecture.json` ist optionaler Kontext; bei unklarer Rolle kann zunächst `role-requirements-grilling`/`role-architecture` genutzt werden.

## Contracting-Dimensionen

1. Coaching-Modus und Coachee-Kontext.
2. Führungsrolle und relevante Organisationsrealität.
3. konkrete Situation oder wiederkehrende Führungsherausforderung.
4. gewünschte beobachtbare Verhaltensänderung.
5. Erfolgsevidenz und Nicht-Ziele.
6. Sponsor/Auftraggeber und mögliche Zielkonflikte.
7. Vertraulichkeit, Sharing und Persistenz.
8. Safety-/HR-/Legal-/Compliance-Grenzen via `coaching-safety-routing`.

## Grilling-Regel

Bei echter Entscheidungsunsicherheit delegiert der Skill an `round-based-requirements-grilling`. Bereits bestätigte Angaben werden nicht erneut gefragt. Grilling endet, sobald ein belastbarer Contract erzeugt werden kann; Reflection und Verhaltensexperimente gehören nicht ins Intake-Grilling.

## Artefaktvertrag

`leadership-coaching-contract.json` enthält mindestens `schemaVersion`, `coachingContractId`, `version`, `status`, `coachingMode`, `coachee`, `roleContextRefs`, `coachingPurpose`, `initialChallenges`, `desiredOutcomes`, `successEvidence`, `scope`, `sponsor`, `confidentiality`, `persistence`, `openQuestions`, `createdAt` und bei aktivem Contract `approvedAt`.

Zulässige Statuswerte: `draft | review | active | paused | completed | superseded`.

## Datenschutz

Rohgespräche und unnötige Drittinformationen werden nicht automatisch persistiert. Coaching-Artefakte und Sharing benötigen die im Contract bestätigte Regel. Sensible Mitarbeiterdaten werden minimiert und nach Möglichkeit referenziert statt kopiert.

## Übergabe

- Contract belastbar → `leadership-development-model`.
- Safety-/HR-/Legal-/Compliance-Grenze → `coaching-safety-routing`.
- Rollenauftrag unklar → `role-requirements-grilling` bzw. `role-architecture`.

## Abschlusskriterien

Der Auftrag ist abgeschlossen, wenn mindestens ein operationalisierbares Entwicklungsfeld, Erfolgsevidenz, Scope, Confidentiality/Persistenz und relevante Grenzen geklärt sind.
