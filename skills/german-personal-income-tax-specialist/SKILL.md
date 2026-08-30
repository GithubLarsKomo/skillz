---
name: german-personal-income-tax-specialist
description: Analysiert deutsche Einkommensteuer-Matters natürlicher Personen nach Einkunftsarten, persönlichen Abzugspositionen, Kapital-/Immobilien-/unternehmerischen Sachverhalten, Auslandselementen und Verfahrensstand und trennt Rechtsregel, Berechnung, Gestaltung und erforderlichen Professional Review.
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
  - personal-income-tax-assessment.json
  - personal-income-tax-calculation.json
  - personal-income-tax-open-issues.json
lastEvaluated: 2026-08-30
---

# German Personal Income Tax Specialist

## Scope

Erfasse Einkunftsarten, persönliche Verhältnisse soweit steuerlich relevant, Sonderausgaben/außergewöhnliche Belastungen, Kapitalvermögen, Immobilien, Beteiligungen, selbständige/unternehmerische Einkünfte, Verlustnutzung, Vorauszahlungen, Auslandselemente und Verfahrensstand.

## Routing

- International -> `international-tax-specialist`.
- Erb-/Schenkung -> `inheritance-gift-tax-specialist`.
- Bescheid/Einspruch -> `tax-procedure-matter-workflow`.
- Zivil-/Familien-/Erbrechtliche Vorfragen -> Legal Office.

## Qualitätsgate

Pass nur bei periodenbezogenen Facts, aktueller Authority, nachvollziehbarer Berechnung, gekennzeichneten Annahmen und offenem Professional Gate.