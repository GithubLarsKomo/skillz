---
name: series-architecture
description: Plant mehrbändige Fiction über mehrere Zeitskalen hinweg als Series-, Volume-, Character-, Relationship-, Mystery- und World-Change-Arcs und führt ein explizites Setup/Payoff-Ledger. Verwenden für Reihen, Zyklen und lange Einzelromane mit vielen Handlungsfäden; nicht als Szenenprosa-Generator oder Canon-Verifier.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - speculative-worldbuilding
  - ensemble-character-architecture
consumes:
  - world-model.json
  - character-ensemble.json
outputs:
  - series-architecture.json
  - setup-payoff-ledger.json
  - series-outline.md
lastEvaluated: 2026-09-06
---

# Series Architecture

## Zweck

Halte lokale und langfristige Erzählbewegungen gleichzeitig sichtbar, ohne eine Reihe so eng zu planen, dass Entdeckungen im Schreiben unmöglich werden.

## Hierarchie

```text
Series
 -> Volume
    -> Part / Act
       -> Chapter
          -> Scene
             -> Beat
```

## Arc-Typen

Mindestens:

- Series Arc;
- Volume Arc;
- Character Arc;
- Relationship Arc;
- Mystery/Reveal Arc;
- Faction/Political Arc;
- World-Change Arc;
- Theme/Question Arc.

## Setup/Payoff Ledger

Jeder relevante narrative Vertrag erhält:

- stabile ID;
- setup description;
- first appearance;
- prominence `low|medium|high`;
- expected horizon;
- intended payoff or open purpose;
- status `open|advanced|paid|abandoned|retconned`;
- dependent arcs/entities.

## Planungstiefe

Planung kann je nach Grilling sein:

- `discovery`: nur Series Promise, Volume Direction und harte Constraints;
- `hybrid`: wichtige Arcs und Payoffs, Szenen offen;
- `architected`: detaillierte Volume-/Chapter-/Scene-Struktur.

**Planungstiefe ist eine Autorenentscheidung, kein Qualitätsranking.**

## Ablauf

1. Series Promise und gewünschte Offenheit fixieren.
2. Globalen Endzustand nur soweit nötig definieren.
3. Pro Band eigenständige Leserbelohnung und Serienfortschritt bestimmen.
4. Arc-Interdependenzen modellieren.
5. Setup/Payoff Ledger anlegen.
6. Für jeden Band offene versus absichtlich ungelöste Fragen unterscheiden.
7. Überlastung prüfen: zu viele gleichzeitig aktive Arcs sichtbar machen.
8. Architektur versionieren; Draft-Entdeckungen dürfen sie kontrolliert verändern.

## Qualitätsgate

- **Jeder Band braucht lokale Erfüllung und Serienbewegung.**
- Offene Setups werden nicht mit vergessenen Setups verwechselt.
- Eine Änderung an einem zentralen Arc löst Continuity-/Impact-Prüfung aus.
- Discovery Writing bleibt möglich, wenn es im Grilling gewünscht ist.
- Outline ist Planung, nicht Canon.

## Abschluss

Abgeschlossen, wenn Series-/Volume-Arcs, Abhängigkeiten und Setup/Payoff-Ledger für den gewünschten Planungshorizont konsistent und versionierbar vorliegen.
