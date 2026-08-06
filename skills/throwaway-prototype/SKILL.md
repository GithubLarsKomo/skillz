---
name: throwaway-prototype
description: Prüft unsichere technische oder fachliche Annahmen mit bewusst kurzlebigen, isolierten Prototypen, trennt Lernnachweise von Produktionsabnahme und verhindert die unbeabsichtigte Übernahme experimentellen Codes.
userFacing: true
implicitInvocation: true
category: engineering
version: 0.2.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - large-work-wayfinder
  - disciplined-diagnosis
  - spec-to-vertical-issues
  - agent-handoff
outputs:
  - prototype-brief.md
  - prototype-evidence.json
  - disposal-record.json
lastEvaluated: 2026-08-06
---

# Throwaway Prototype

## Trigger

Verwenden, wenn eine einzelne unsichere Annahme vor einer Produktionsimplementierung mit minimalem Aufwand diskriminiert werden muss.

## Voraussetzungen

Erforderlich sind eine explizite Hypothese oder Entscheidungsfrage, Evidenzschwelle, Zeit- oder Scope-Box, Nicht-Ziele, Isolationsstrategie, Entsorgungsplan sowie ein unveränderlicher Ausgangsstand.

## Ablauf

### 1. Experimentvertrag festlegen

Definiere genau eine Hypothese, die erforderliche Evidenz, Abbruchkriterien, Prototypklasse und die Grenzen zulässiger Schlussfolgerungen.

### 2. Sicher isolieren

Nutze einen separaten Branch, ein temporäres Verzeichnis oder ein eigenständiges Harness. Produktions-Secrets, personenbezogene Daten, Sicherheitsbypässe und direkte Produktivpfade sind verboten.

### 3. Kleinsten diskriminierenden Prototyp bauen

Implementiere nur das Minimum, das die Hypothese unterscheiden kann. Dokumentiere Mocks, Abkürzungen, ignorierte Qualitätsmerkmale, Datenquellen und Sicherheitsgrenzen.

### 4. Evidenz erheben

Erfasse beobachtbare Ergebnisse gegen die vorab definierte Schwelle. Trenne Prototypnachweise ausdrücklich von Produktions-Akzeptanzkriterien.

Die Evidenz soll auch nach der Entsorgung des Codes nachvollziehbar bleiben. Erfasse deshalb mindestens:

- eine stabile Referenz auf den experimentellen Stand, falls er erhalten bleibt,
- unveränderliche Commit-, Branch-, Artifact- oder Archiv-Referenzen, soweit vorhanden,
- die verwendeten Inputs beziehungsweise Fixtures,
- beobachtete Resultate und ihre Grenzen,
- die daraus abgeleitete Entscheidung sowie deren Stärke.

Eine dauerhafte Evidenzreferenz ist kein Produktionsnachweis. Sie dient ausschließlich dazu, das Lernen später rekonstruieren oder erneut prüfen zu können.

### 5. Schlussfolgerung begrenzen

Bewerte die Hypothese als gestützt, widerlegt oder unentschieden und benenne verbleibende Unsicherheit sowie externe Nachweise, die noch fehlen.

### 6. Entsorgung explizit abschließen

Wähle genau einen Abschlusszustand:

- `deleted`: Der experimentelle Code wird vollständig entfernt. Die Lern- und Entscheidungsnachweise bleiben als `prototype-evidence.json` beziehungsweise in einem dauerhaften Decision-/Issue-Artefakt erhalten.
- `archived-evidence`: Der experimentelle Stand bleibt ausschließlich als auffindbare Primärevidenz erhalten, zum Beispiel auf einem ausdrücklich experimentellen Branch oder in einem Archiv. Er darf nicht als Produktionscode konsumiert werden.
- `promoted-to-new-task`: Das Experiment rechtfertigt eine produktionsfähige Umsetzung. Der Prototyp wird nicht weiterentwickelt; stattdessen wird ein neues, begrenztes Implementierungs-Issue oder gleichwertiger Auftrag erzeugt, der Produktionsanforderungen, Tests und Review neu definiert.

Die Zustände dürfen nicht vermischt werden. Insbesondere bedeutet `archived-evidence` nicht „für spätere Produktion aufbewahren“ und `promoted-to-new-task` bedeutet nicht, den Prototyp direkt in Produktion zu übernehmen.

### 7. Evidence-Link und Übergabe erzeugen

Übergebe unveränderliche Referenzen, Beobachtungen, Schlussfolgerungsstärke, Grenzen, Entsorgungsstatus und genau eine nächste Aktion.

Wenn die Evidenz dauerhaft referenzierbar bleiben soll, enthält `prototype-evidence.json` zusätzlich einen `evidenceReference`-Block. Dieser verweist auf eine stabile Quelle des experimentellen Stands oder dokumentiert ausdrücklich, dass nur die aufgezeichnete Evidenz erhalten bleibt.

## Prüfungen

Vor Abschluss müssen Hypothese, Evidenzschwelle, Isolation, Daten- und Sicherheitsgrenzen, Trennung zur Produktionsabnahme sowie genau ein Entsorgungszustand belegt sein.

Zusätzlich prüfen:

- `archived-evidence` besitzt eine stabile, auffindbare Referenz,
- `deleted` bewahrt die Lern- und Entscheidungsnachweise ohne experimentellen Code,
- `promoted-to-new-task` verweist auf einen neuen Implementierungsauftrag statt auf eine direkte Codeübernahme,
- keine Evidence-Referenz wird als Produktions-Akzeptanzbeleg missverstanden.

## Fehlerbehandlung

Stoppe bei Scope-Ausweitung, polierter Mini-Produktentwicklung, Nutzung sensibler Daten, Sicherheitsabschwächung, fehlender Hypothese oder stiller Übernahme experimentellen Codes.

Stoppe ebenfalls, wenn ein archivierter Prototyp als Produktionsbasis weiterverwendet, ein gelöschter Prototyp ohne erhaltene Lernnachweise entsorgt oder eine Produktionsumsetzung ohne neues Implementierungs-Issue direkt aus dem Experiment abgeleitet werden soll.

## Übergabe

```json
{
  "repository": {"name": "...", "headSha": "..."},
  "hypothesis": "...",
  "evidenceThreshold": "...",
  "prototypeClass": "code|interface|data|integration|migration|performance|user-flow",
  "isolation": "...",
  "shortcuts": ["..."],
  "observations": ["..."],
  "conclusion": {"state": "supported|rejected|inconclusive", "strength": "..."},
  "limitations": ["..."],
  "productionAcceptanceEvidence": "not established",
  "evidenceReference": {
    "state": "retained|record-only|none",
    "type": "commit|branch|artifact|archive|issue|decision-record|none",
    "reference": "immutable-or-stable-reference",
    "purpose": "replay-or-audit-learning-only"
  },
  "disposal": {
    "state": "deleted|archived-evidence|promoted-to-new-task",
    "evidence": "...",
    "implementationTask": "issue-or-task-reference-if-promoted"
  },
  "residualUncertainty": ["..."],
  "nextAction": "exactly one executable action"
}
```

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn die Hypothese mit begrenzter Evidenz bewertet, Lern- und Produktionsnachweis getrennt, genau ein expliziter Entsorgungszustand gewählt, der Lernnachweis dauerhaft rekonstruierbar gemacht und genau eine nächste Aktion übergeben wurde.
