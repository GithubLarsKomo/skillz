---
name: skill-lifecycle-migration
description: Plant und verifiziert sichere Skill-Lifecycle-Änderungen von candidate/stable zu deprecated und späterer Entfernung, einschließlich replacedBy, Discoverability, Consumer-Migration, Output-Ownership und Compatibility-Evaluation. Verwenden bei Skill-Ablösung oder struktureller Konsolidierung; keine aktiven Consumer stillschweigend brechen.
---

# Skill Lifecycle Migration

## Trigger

Nutze den Skill, wenn ein Skill ersetzt, deprecated, als Compatibility-Fassade weitergeführt oder später entfernt werden soll.

Nicht für bloße Textüberarbeitung oder harmlose Patch-Versionen verwenden.

## Voraussetzungen

Erforderlich sind:

- alter Skill und vorgesehener Nachfolger;
- aktuelle Dependents und Output Contracts aus dem Capability-/Dependency-Modell;
- bestehende Evaluationen und relevante produktive Contract-Tests;
- bekannte externe/gespeicherte Aufrufer soweit verfügbar;
- Zielzustand und gewünschte Migrationsfrist.

## Ablauf

1. **Ist-Vertrag erfassen.** Trigger, Inputs, Outputs, Consumers, userFacing/Discoverability, Status und Evaluation des alten Skills dokumentieren.
2. **Nachfolger prüfen.** Sicherstellen, dass der vorgeschlagene `replacedBy`-Skill die tatsächlich benötigte Semantik abdeckt. Ähnlicher Name genügt nicht.
3. **Consumer migrieren.** Aktive interne `requires` und normative Workflow-Texte zuerst auf den Nachfolger umstellen.
4. **Ownership migrieren.** Kanonische Outputs genau einem Producer zuweisen. Die Compatibility-Fassade darf Nachfolger-Artefakte referenzieren, aber nicht erneut als eigene Outputs deklarieren.
5. **Deprecation setzen.** `status: deprecated`, `discoverability: compatibility`, `deprecatedSince`, `replacedBy`, explizite statt implizite Invocation und klare Migration dokumentieren.
6. **Compatibility-Evaluation erstellen.** Explizite Auswahl, Input-Mapping, Nachfolger-Routing, Fehlerverhalten und fehlende Doppel-Ownership testen.
7. **Removal Readiness prüfen.** Entfernung erst empfehlen, wenn keine aktiven internen Dependents, keine erforderlichen Legacy-Consumer und kein einzigartiger Compatibility-Vertrag mehr bestehen.
8. **Migrationsplan ausgeben.** Reihenfolge, Dateien, Gates, Rollback und Acceptance Criteria dokumentieren.

## Prüfungen

- Ist `replacedBy` semantisch passend statt nur ähnlich benannt?
- Sind aktive Consumer vor der Deprecation migriert?
- Bleibt jedes kanonische Output-Artefakt bei genau einem Producer?
- Ist `compatibility` nicht user-facing/default-discoverable?
- Existiert eine Compatibility-Evaluation?
- Ist Removal separat von Deprecation entschieden?

## Fehlerbehandlung

- **Nachfolger deckt Semantik nicht ab:** Migration stoppen oder einen passenden kanonischen Orchestrator einführen.
- **Aktiver Consumer verbleibt:** Removal blockieren; Consumer zuerst migrieren.
- **Output würde doppelt produziert:** alte Output-Deklaration entfernen und nur Referenz/Compatibility-Manifest behalten.
- **Externer Consumer unbekannt:** Compatibility-Fassade erhalten und Unsicherheit dokumentieren.
- **Safety-/Compliance-Grenze verändert sich:** als inkompatible Migration behandeln und explizit reviewen.

## Übergabe

`skill-lifecycle-migration-plan.json` enthält Source, Replacement, Consumer-Matrix, Output-Ownership-Deltas, Frontmatter-Änderungen, Evaluation-Gates, Removal-Readiness und Rollback. Die Markdown-Fassung liefert eine reviewbare Migrationssequenz.

## Abschlusskriterien

Die Lifecycle-Migration ist geplant, wenn Nachfolger und Consumer-Pfade eindeutig sind, kein kanonisches Artefakt doppelt produziert wird, Compatibility-Verhalten evaluiert ist und Deprecation/Removal als getrennte Entscheidungen behandelt werden.
