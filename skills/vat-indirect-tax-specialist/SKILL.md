---
name: vat-indirect-tax-specialist
description: Analysiert Umsatzsteuer-/VAT-Matters entlang Steuerbarkeit, Leistungsart, Leistungsort, Steuerbefreiung, Steuersatz, Bemessungsgrundlage, Reverse Charge, Rechnung, Vorsteuer und grenzüberschreitender Behandlung und hält Contract-, Customs- und International-Tax-Abhängigkeiten getrennt.
userFacing: true
implicitInvocation: true
category: tax-specialist
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - current-tax-context
  - tax-position-register
outputs:
  - vat-assessment.json
  - vat-transaction-map.json
  - vat-open-issues.json
lastEvaluated: 2026-08-30
---

# VAT / Indirect Tax Specialist

## Prüflogik

1. steuerbarer Umsatz?
2. Unternehmer/Leistungsaustausch?
3. Lieferung oder sonstige Leistung?
4. Leistungsort?
5. Steuerbefreiung/Option?
6. Bemessungsgrundlage und Steuersatz?
7. Steuerschuldnerschaft/Reverse Charge?
8. Rechnung und Zeitpunkt?
9. Vorsteuerabzug?
10. Melde-/Compliance-Folgen?

## Qualitätsgate

Pass nur, wenn Transaktion, Parteienrollen, Ort, Zeitpunkt, Belege/Rechnung, Authority und grenzüberschreitende Abhängigkeiten nachvollziehbar sind.