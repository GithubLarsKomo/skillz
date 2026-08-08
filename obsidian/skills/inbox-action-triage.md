---
type: skill
generated: true
name: "inbox-action-triage"
category: "productivity"
userFacing: true
evaluationPassed: true
evaluationMode: "compatibility"
caseCount: 3
recordedResultCount: 3
sourcePath: "skills/inbox-action-triage/SKILL.md"
tags:
  - skill
  - skill-category/productivity
---

# inbox-action-triage

Klassifiziert eine abgegrenzte Menge bereits geladener Nachrichten nach Dringlichkeit und Handlungsbedarf und leitet überprüfbare nächste Aktionen ab. Verwenden, wenn Inbox-Nachrichten in urgent, reply-soon, waiting, delegated, FYI/archive oder needs-context geordnet werden sollen, ohne Gmail-/Outlook-Connectorlogik oder Mailbox-Mutationen zu duplizieren.

> Generated from canonical repository metadata. Do not edit this note manually.

## Category

[[categories/productivity|productivity]]

## Requires

- —

## Required by

- [[skills/daily-and-weekly-review|daily-and-weekly-review]]

## Outputs

- `inbox-triage.json`
- `inbox-triage.md`

## Output consumers

### `inbox-triage.json`

- [[skills/daily-and-weekly-review|daily-and-weekly-review]]

### `inbox-triage.md`

- [[skills/daily-and-weekly-review|daily-and-weekly-review]]

## Evaluation

- Mode: `compatibility`
- Passed: `True`
- Cases: `3`
- Recorded results: `3`

## Canonical source

`skills/inbox-action-triage/SKILL.md`
