---
name: skill-evaluation-suite-authoring
description: Entwirft und prüft deterministische Skill-Evaluation-Suites aus dem normativen SKILL.md-Vertrag mit Happy Path, Edge Case, Failure Case, belastbaren Anchors und aufgezeichneten Resultaten. Verwenden intern beim Erstellen oder Aktualisieren von Skills; keine PASS-Evidenz erfinden und keine entfernten Vertragsanker testen.
userFacing: false
implicitInvocation: true
discoverability: internal
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires: []
outputs:
  - skill-evaluation-suite-authoring-report.json
lastEvaluated: 2026-08-28
---

# Skill Evaluation Suite Authoring

## Trigger

Intern verwenden, wenn ein neuer oder wesentlich geänderter Skill eine `tests/evaluation.json`-Suite und belastbare Ergebnisfixtures benötigt oder bestehende Anchors nach einer Vertragsmigration aktualisiert werden müssen.

## Voraussetzungen

- aktuelles kanonisches `SKILL.md`;
- bekannte Safety-/Governance-Grenzen;
- vorhandene Evaluation Suite/Resultate, falls es sich um eine Migration handelt;
- klare Information, welche Verhaltensänderung beabsichtigt ist.

## Ablauf

1. **Normativen Vertrag lesen.** Trigger, Grenzen, Ablauf, Prüfungen, Fehlerbehandlung, Outputs und Ownership extrahieren.
2. **Happy Path wählen.** Typischen erfolgreichen Gebrauch mit beobachtbaren Required/Forbidden Behaviors formulieren.
3. **Edge Case wählen.** Einen realistischen Unsicherheits-, Datenqualitäts-, Tool- oder Kompositionsfall wählen, der nicht bloß ein zweiter Happy Path ist.
4. **Failure Case wählen.** Eine relevante Fehlanwendung oder Governance-/Safety-Verletzung testen, die der Skill explizit verhindern soll.
5. **Anchors wählen.** Nur Textanker verwenden, die im aktuellen normativen `SKILL.md` tatsächlich vorkommen und die geprüfte Regel tragen.
6. **Resultate aufzeichnen.** Required Behaviors mit konkreter Vertrags-Evidenz und Forbidden Behaviors als `observed: false` dokumentieren. PASS nie aus Wunschzustand ableiten.
7. **Migration prüfen.** Wenn sich Verantwortungsgrenzen ändern, Evaluationen auf die neue Grenze umstellen statt entfernte Altverantwortung wieder in den Skill zu zwingen.
8. **Autoring-Report ausgeben.** Dateien, Fälle, Anchors, Coverage und offene Risiken dokumentieren.

## Prüfungen

- Sind Happy/Edge/Failure fachlich verschieden?
- Prüft jeder Behavior eine echte Vertragsregel?
- Existiert jeder Anchor im aktuellen Skilltext?
- Wird PASS durch nachvollziehbare Evidence begründet?
- Werden entfernte Responsibilities nicht durch stale Tests reaktiviert?
- Bleiben Runtime-/Render-/Toolerfolge unbehauptet, wenn nur statische Vertrags-Evidenz vorliegt?

## Fehlerbehandlung

- **Anchor fehlt:** Evaluation korrigieren oder echte Vertragslücke im Skill separat beheben; keinen fast-pass String erfinden.
- **Behavior nicht normativ:** entweder SKILL.md bewusst ändern oder Behavior aus der Suite entfernen.
- **Nur Happy Path verfügbar:** Suite ist unvollständig; relevante Edge-/Failure-Risiken aus Grenzen und Fehlerbehandlung ableiten.
- **Stale Result Evidence:** neu aufzeichnen statt Datums-/PASS-Felder blind zu kopieren.
- **Verantwortung wurde delegiert:** Test auf Delegation und neue Ownership umstellen.

## Übergabe

`skill-evaluation-suite-authoring-report.json` beschreibt Zielskill, drei Kernfälle, Anchor-Prüfung, erwartete Result-Dateien, Evidence-Typ und offene Lücken. Die eigentlichen `tests/evaluation.json`-/Result-Dateien bleiben Repository-Dateien des Zielskills und werden nicht als globale Cross-Skill-Outputs deklariert.

## Abschlusskriterien

Der Autor ist abgeschlossen, wenn drei unterschiedliche Fälle mit existierenden normativen Anchors vorliegen, Required/Forbidden Behaviors überprüfbar sind, Result Evidence den tatsächlichen Vertrag abbildet und kein PASS auf erfundener oder veralteter Evidenz beruht.
