---
name: legal-negotiation-strategy
description: Übersetzt Mandantenstrategie, Legal-/Commercial-Risiken und Vertrags-Findings in priorisierte Verhandlungspositionen mit Opening, Target, Fallback, Red Line, Concession Value, Gegenparteiinteresse und Freigabegrenzen. Verwenden vor oder während wesentlichen Vertrags- und Legal-Verhandlungen.
userFacing: true
implicitInvocation: false
discoverability: advanced
category: analysis
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - legal-client-strategy
  - legal-compliance-risk-assessment
consumes:
  - client-strategy.json
  - legal-decision-boundaries.json
  - legal-risk-register.json
  - commercial-exposure-analysis.json
  - legal-risk-decision-handoff.json
outputs:
  - negotiation-positions.json
  - negotiation-playbook.md
lastEvaluated: 2026-08-28
---

# Legal Negotiation Strategy

## Zweck

Mache aus Findings eine verhandelbare Mandantenstrategie. Der Skill optimiert nicht jede Klausel isoliert, sondern schützt das Gesamtziel, die Red Lines und den Wert der verfügbaren Konzessionen.

## Position Model

Für jedes materielle Issue erfasse:

```json
{
  "issueId": "...",
  "ideal": "...",
  "opening": "...",
  "target": "...",
  "fallback": "...",
  "redLine": "...",
  "concessionValue": "low|medium|high|unknown",
  "counterpartyInterest": "...",
  "rationale": "...",
  "tradeableAgainst": [],
  "authorityNeeded": "..."
}
```

## Kernregeln

- `ideal`, `target`, `fallback` und `redLine` sind verschiedene Zustände; nicht alles ist eine Red Line.
- Eine Konzession wird nicht kostenlos abgegeben, wenn sie für die Gegenseite Wert besitzt und für den Mandanten handelbar ist.
- Legal Risk und Commercial Value werden gemeinsam betrachtet, aber nicht vermischt.
- Positionen dürfen bestätigte `client-strategy.json`-Red-Lines nicht stillschweigend unterschreiten.
- Ein Fallback oberhalb der Freigabegrenze bleibt `authority-needed`, nicht automatisch akzeptabel.
- Gegenparteiinteressen werden als Hypothesen markiert, wenn sie nicht belegt sind.

## Workflow

1. Material Issues und Risk Register priorisieren.
2. Für jedes Issue Ziel- und Grenzposition definieren.
3. Concession Value und mögliche Trades bestimmen.
4. Gegenparteiinteressen/Hebel als Facts oder Hypothesen trennen.
5. Reihenfolge und Paketierung der Verhandlung festlegen.
6. Freigabegrenzen und Eskalationspunkte kennzeichnen.
7. Positionsmatrix und Playbook ausgeben.

## Playbook

Das Playbook enthält Top Objectives, No-Go Areas, Ask/Trade Packages, Begründungslinien, Informationslücken, Authority Gates und eine Reihenfolge, die unnötige frühe Konzessionen vermeidet.

## Qualitätsgate

Pass nur, wenn jede materielle Position auf Mandantenziel und Risk Register zurückführbar ist, Fallback und Red Line getrennt sind und keine nicht autorisierte Konzession als akzeptiert behandelt wird.
