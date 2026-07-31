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

## Deprecation

Ein veralteter Skill erhält `status: deprecated`, benennt `replacedBy` und dokumentiert Migration sowie verbleibende Nutzer. Er wird erst entfernt, wenn keine aktiven Abhängigkeiten mehr bestehen.

## Repository-Gates

Pull Requests müssen den Repository-Validator und die Prüfung generierter Dateien bestehen. Ausnahmen werden im Pull Request begründet und zeitlich begrenzt.
