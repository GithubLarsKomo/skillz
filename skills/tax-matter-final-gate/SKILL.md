---
name: tax-matter-final-gate
description: Prüft vor Abschluss, Filing, Änderung, Einspruch, Umsetzung oder Übergabe eines Tax Matters, ob Facts, aktuelle Rechtsgrundlage, Berechnung, Positionen, Professional Review, Legal-/Accounting-/Valuation-Dependencies, Fristen und Autorität konsistent geschlossen oder ausdrücklich offen dokumentiert sind.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - tax-position-register
  - tax-professional-routing
outputs:
  - tax-final-gate-status.json
  - tax-open-items.json
  - tax-next-safe-action.json
lastEvaluated: 2026-08-30
---

# Tax Matter Final Gate

## Zweck

Verhindere, dass ein fachlich oder organisatorisch unvollständiger Tax Matter als abgeschlossen, filing-ready oder umsetzungsreif erscheint.

## Gate Checks

Prüfe mindestens:

- bestätigter Taxpayer/Entity- und Periodenbezug,
- relevante Steuerarten und Jurisdiktionen,
- vollständige oder ausdrücklich offene Facts/Belege,
- aktueller Rechts-/Guidance-/Case-Law-Stand,
- nachvollziehbare Berechnung und Szenarioannahmen,
- Status aller materiellen `tax-position` Records,
- erforderlicher T2 Professional Review,
- offene Legal-/Accounting-/Valuation-Dependencies,
- Filing-/Einspruchs-/Änderungs-/Zahlungsfristen,
- zuständige Entscheidungs-/Vertretungsautorität,
- genau nächste sichere Aktion.

## Outcome

`pass`, `pass-with-open-follow-up` oder `blocked`. Ein Gate darf nicht durch bloße Narrative überstimmt werden; offene Punkte bleiben strukturierte Outputs.

## Qualitätsgate

Pass nur, wenn der Matter State und die geplante externe/interne Aktion konsistent sind und kein erforderlicher Professional-/Authority-Schritt als bereits erfolgt dargestellt wird.