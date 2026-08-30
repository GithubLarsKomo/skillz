---
name: tax-position-register
description: Führt materielle Steuerpositionen mit Facts, Rechtsgrundlage, Evidenz, Berechnung, Alternativen, Unsicherheit, Professional Review und Lifecycle-Status als versionierbare Records und ermöglicht Change-Impact, Bescheidabgleich und konsistente Wiederverwendung ohne ungeprüfte Altpositionen fortzuschreiben.
userFacing: true
implicitInvocation: true
category: tax-specialist
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - current-tax-context
  - decision-record
outputs:
  - tax-position-register.json
  - tax-position.json
  - tax-position-change-impact.json
lastEvaluated: 2026-08-30
---

# Tax Position Register

## Zweck

Tax Advice wird nicht nur als Antwort, sondern als nachvollziehbare, versionierte Position behandelt.

## Minimaler Position Record

```json
{
  "positionId": "TP-...",
  "taxpayer": "...",
  "taxType": "...",
  "period": "...",
  "jurisdiction": "...",
  "facts": [],
  "assumptions": [],
  "authorityRefs": [],
  "interpretationRefs": [],
  "calculationRef": null,
  "alternatives": [],
  "exposureOrBenefit": null,
  "confidence": "high|medium|low",
  "professionalReview": "not-required|pending|confirmed|rejected",
  "status": "draft|researched|calculated|professional-review-required|confirmed|filed|challenged|superseded",
  "lawAsOf": "YYYY-MM-DD",
  "supersededBy": null
}
```

## Kernregeln

- Facts, Norm/Authority, Interpretation, Berechnung und Empfehlung getrennt halten.
- Keine Position allein aus Practitioner Content bestätigen.
- Frühere Positionen nicht automatisch auf andere Perioden übertragen.
- Änderungen in Law/Guidance/Case Law gegen offene und bestätigte Positionen impact-analysieren.
- Abgegebene Erklärung und späterer Bescheid werden gegen die zugrunde liegenden Positionen abgeglichen.

## Qualitätsgate

Pass nur, wenn Position, Evidenz, Zeitraum, Rechtsstand, Berechnung, Alternativen, Review-Status und Supersession nachvollziehbar sind.