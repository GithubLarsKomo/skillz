---
name: legal-client-strategy
description: Übersetzt einen bestätigten Legal-Matter-Kontext in eine explizite Mandantenstrategie mit Zielbild, Must-haves, Red Lines, Risikotoleranz, Verhandlungsspielraum, Fallbacks und Entscheidungsautorität. Verwenden, bevor Specialists, Vertragsreview oder Verhandlungen Empfehlungen priorisieren.
---

# Legal Client Strategy

## Zweck

Fixiere die anwaltliche Perspektive: Nicht die abstrakt eleganteste Rechtsposition ist das Ziel, sondern die rechtlich tragfähige Lösung, die das bestätigte Mandantenziel schützt.

## Kernregeln

- `preferredOutcome`, `mustHaves`, `niceToHaves`, `redLines` und `walkAwayPoint` getrennt erfassen.
- Rechtliches Risiko, wirtschaftliches Risiko, Zeitdruck und Verhandlungsmacht nicht vermischen.
- Ein Risiko darf nur akzeptiert werden, wenn die zuständige Autorität bekannt und die Akzeptanz explizit ist.
- Unbekannte Mandantenpräferenzen werden nicht durch Standardpräferenzen des Skills ersetzt.
- Bei privaten Matters dieselbe Logik verwenden, aber persönliche Zielsetzungen und Kosten-/Stress-/Zeitdimensionen sichtbar halten.

## Workflow

1. `legal-matter.json` lesen und Mandantenziel bestätigen.
2. Zielbild und Erfolgsdefinition formulieren.
3. Must-haves, Red Lines und Fallbacks bestimmen.
4. Risikotoleranz getrennt nach Legal, Financial, Regulatory, Reputation und Personal Exposure erfassen.
5. Verhandlungsmacht, Zeitconstraints und Reversibilität bewerten.
6. Entscheidungs- und Freigabegrenzen dokumentieren.
7. `client-strategy.json` und `legal-decision-boundaries.json` ausgeben.

## Mindestfelder

```json
{
  "preferredOutcome": "...",
  "mustHaves": [],
  "niceToHaves": [],
  "redLines": [],
  "riskTolerance": {},
  "timeConstraints": [],
  "economicConstraints": [],
  "negotiationPower": "low|balanced|high|unknown",
  "fallbackOutcome": "...",
  "walkAwayPoint": "...",
  "authorityRequired": []
}
```

## Qualitätsgate

Pass nur, wenn Empfehlungen eines nachfolgenden Specialists gegen explizite Mandantenziele, Red Lines und Autoritätsgrenzen priorisiert werden können.
