# Governance

## Änderungen

- Neue Skills und wesentliche Verhaltensänderungen erfolgen über Pull Requests.
- Ein Skill bleibt `draft`, bis Happy Path, Grenzfall und Fehlerfall dokumentiert und geprüft sind.
- Der Status `stable` setzt mehrere erfolgreiche reale Wiederverwendungen und stabile Übergaben voraus.
- Sicherheits-, Compliance- oder Architekturentscheidungen werden nicht stillschweigend in Fach-Skills eingebaut.

## Eigentümerschaft

Das Frontmatter-Feld `owners` benennt die fachlich verantwortlichen Personen oder Teams. Eigentümer prüfen Trigger, Grenzen, Übergaben und Evaluationsergebnisse.

## Versionierung

Skills verwenden semantische Versionierung:

- Patch: Klarstellungen ohne Verhaltensänderung
- Minor: rückwärtskompatible neue Fähigkeiten oder Übergaben
- Major: inkompatible Trigger-, Eingabe-, Ausgabe- oder Governance-Änderungen

## Lifecycle

`status` ist die kanonische Lifecycle-Achse und bleibt unabhängig von Sichtbarkeit:

- `draft`: Vertrag oder Verhalten noch nicht ausreichend validiert;
- `candidate`: evaluierter Skill vor ausreichender realer Wiederverwendung;
- `stable`: mehrfach real bewährt und mit stabilen Übergaben;
- `deprecated`: nur noch für Migration oder explizite Kompatibilität vorhanden.

Ein veralteter Skill erhält zwingend `status: deprecated`, `discoverability: compatibility`, `replacedBy` und `deprecatedSince`. Er wird erst entfernt, wenn keine aktiven Abhängigkeiten mehr bestehen und die dokumentierte Migration abgeschlossen ist.

## Discoverability

`discoverability` ist orthogonal zum Lifecycle und steuert, wie ein Skill in Auswahl-/Discovery-Oberflächen behandelt werden soll:

- `public`: normaler user-facing Entrypoint;
- `advanced`: user-facing, aber für gezielte/fortgeschrittene Nutzung statt Standardauswahl;
- `internal`: nur Komposition durch andere Skills, nicht als normaler Nutzer-Entrypoint;
- `compatibility`: deprecated, nur explizit für Legacy-/Migrationsfälle.

Für bestehende Skills ohne explizites Feld löst der Capability Index rückwärtskompatibel auf: user-facing -> `public`, nicht user-facing -> `internal`, deprecated -> `compatibility`. Neue Deprecations müssen `compatibility` explizit deklarieren. `public`/`advanced` erfordern `userFacing: true`; `internal`/`compatibility` dürfen nicht user-facing sein.

## Deprecation

Eine Deprecation ist eine Migration, kein Alias auf Dauer. Der alte Skill darf die Artefakte seines Nachfolgers referenzieren, soll deren Producer-Ownership aber nicht erneut deklarieren. Compatibility-Evaluationen prüfen mindestens:

- explizite statt implizite Auswahl;
- nachvollziehbares Routing zum `replacedBy`-Skill;
- Erhalt relevanter Eingaben/Constraints;
- keine zweite fachliche Wahrheit oder zweite Ownership für das kanonische Output-Artefakt.

## Repository-Gates

Pull Requests müssen den Repository-Validator und die Prüfung generierter Dateien bestehen. Ausnahmen werden im Pull Request begründet und zeitlich begrenzt. Der Capability-Health-Report trennt Evaluationserfolg, Evaluation-Coverage, Discoverability und Output-Ownership voneinander.
