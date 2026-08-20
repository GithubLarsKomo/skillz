---
name: spec-to-vertical-issues
description: Zerlegt eine freigegebene, konsistente Spezifikation in kleine, unabhängig abnehmbare vertikale Implementierungs-Issues mit vollständiger Rückverfolgbarkeit, Abnahmeevidenz, Abhängigkeiten und expliziten Nicht-Zielen. Verwenden, wenn aus SPEC.md und Entscheidungsregister eine geordnete Engineering-Backlog-Übergabe entstehen soll, ohne irreversible Architekturentscheidungen stillschweigend zu treffen.
---

# Spezifikation in vertikale Issues zerlegen

Erzeuge aus einer freigegebenen `SPEC.md`, dem Entscheidungsregister und dem Konsistenzbericht einen kleinen, geordneten Satz vertikaler Issues. Jedes Issue muss einen beobachtbaren Nutzer- oder Betriebswert liefern und innerhalb eines begrenzten Implementierungs- und Review-Zyklus abnehmbar sein.

## Routing und Abgrenzung

`spec-to-vertical-issues` beantwortet ausschließlich die Frage: **Wie wird eine bereits freigegebene normative SPEC in unabhängig abnehmbare vertikale Umsetzungsschnitte zerlegt?**

Der Skill startet erst nach erfolgreichem `conversation-to-spec` und ausdrücklicher SPEC-Freigabe. Er klärt keine neuen Produktanforderungen und führt keine breite technische Exploration durch.

Bei während der Zerlegung sichtbar werdenden Lücken gilt:

- Fehlende fachliche Präferenz-, Scope- oder Produktentscheidung → betroffene Requirements blockieren und an `round-based-requirements-grilling` routen. Nach der Entscheidung muss `conversation-to-spec` die SPEC aktualisieren und erneut freigeben, bevor die Zerlegung fortgesetzt wird.
- Fehlende technische Evidenz oder ein technisch nicht sicher schneidbarer Slice → den betroffenen Scope an `large-work-wayfinder` routen.
- Wayfinder-Evidenz ändert eine normative Architektur-, Sicherheits-, Daten- oder Migrationsannahme → zuerst zurück zu `conversation-to-spec`; keine Issue-Zerlegung gegen eine veraltete SPEC fortsetzen.
- Eine reversible Implementierungs- oder Anbieterwahl hinter stabiler Schnittstelle darf als explizite Annahme im Slice bleiben.

Der Skill implementiert keinen Produktionscode. Nach erfolgreicher Zerlegung geht genau das nächste freigegebene Issue an den vorgesehenen Engineering-/Implementierungsworkflow.

## Eingaben und Vorbedingungen

Erforderlich sind:

- ausdrücklich freigegebene `SPEC.md`,
- stabile Requirement-IDs,
- Entscheidungsregister mit entschieden, angenommen und offen,
- Konsistenzbericht ohne ungelöste Widersprüche,
- bekannte Sicherheits-, Compliance-, Datenmigrations- und Betriebsgrenzen.

Fehlt die Freigabe oder besteht ein normativer Widerspruch, keine Issues erzeugen. Den Blocker mit betroffenen Requirement-IDs und Routingziel ausgeben.

## Vertikale Slice-Regel

Ein Issue ist vertikal, wenn es einen vollständigen beobachtbaren Pfad von Eingabe oder Nutzeraktion bis Ergebnis und Nachweis umfasst. Es darf Schema, API, Logik, UI, Migration, Telemetrie und Dokumentation gemeinsam enthalten, soweit diese für den einen Wertpfad nötig sind.

Keine getrennten horizontalen Issues für Datenbank, API und UI erzeugen, wenn keines davon eigenständig Wert oder Abnahmeevidenz liefert. Technische Infrastruktur darf ein eigenes Issue sein, wenn sie selbständig einen Betriebs-, Sicherheits- oder Risikoreduktionsnachweis besitzt und klar als Enabler gekennzeichnet ist.

## Rückverfolgbarkeit bewahren

Für jedes Issue vollständig übernehmen:

- `sourceRequirementIds`,
- fachliches Verhalten und Domäneninvarianten,
- Akzeptanzkriterien,
- Sicherheits- und Berechtigungsgrenzen,
- Migrations- und Kompatibilitätsanforderungen,
- explizite Nicht-Ziele,
- bekannte Komponenten oder Dateien,
- Tests und beobachtbare Abnahmeevidenz.

Keine Anforderung darf verschwinden, dupliziert oder in einem Sammel-Issue verborgen werden. Bereits erledigte Arbeit nicht erneut einplanen.

## Entscheidungen und Annahmen

Irreversible oder weitreichende offene Entscheidungen, die Datenmodell, Migration, Sicherheit, Deployment oder Akzeptanz wesentlich verändern, blockieren die betroffenen Issues. Genau die früheste blockierende Entscheidung, die betroffenen Requirement-IDs und das Routingziel ausgeben; nicht stillschweigend entscheiden.

Eine offene, reversible Anbieter- oder Implementierungswahl darf als explizite Annahme geführt werden, wenn eine stabile Schnittstelle den Slice unabhängig hält. Die Annahme, Austauschgrenze und spätere Entscheidungsstelle im Issue dokumentieren.

## Issue-Schema

`vertical-issues.json` enthält mindestens:

```json
{
  "schemaVersion": 1,
  "specId": "string",
  "issues": [
    {
      "id": "VI-001",
      "title": "string",
      "outcome": "string",
      "sourceRequirementIds": ["REQ-001"],
      "behavior": ["string"],
      "domainInvariants": ["string"],
      "components": ["string"],
      "dependencies": ["VI-000"],
      "assumptions": ["string"],
      "securityAndMigration": ["string"],
      "tests": ["string"],
      "acceptanceEvidence": ["string"],
      "nonGoals": ["string"],
      "handoff": "iterate-software-projects"
    }
  ],
  "blocked": [
    {
      "sourceRequirementIds": ["REQ-000"],
      "reason": "string",
      "routingTarget": "round-based-requirements-grilling|large-work-wayfinder|conversation-to-spec"
    }
  ]
}
```

`dependency-order.json` enthält eine topologisch gültige Reihenfolge, Blocker und Begründungen. `vertical-issues.md` ist die lesbare Fassung mit denselben Informationen.

## Reihenfolge und Größe

Issues ordnen nach:

1. Blocker- und Risikoreduktion,
2. notwendigen Abhängigkeiten,
3. frühestem unabhängig demonstrierbarem Wert,
4. Lerngewinn und Reversibilität.

Ein Issue neu schneiden, wenn es mehrere unabhängige Outcomes, mehrere getrennte Abnahmeentscheidungen oder einen unverhältnismäßig großen Diff benötigt. Zusammenführen, wenn getrennte Teile allein keinen Wert nachweisen können.

## Validierung

Vor Übergabe prüfen:

- jede Requirement-ID ist genau nachvollziehbar abgedeckt oder als Blocker mit Routingziel ausgewiesen,
- jedes Issue besitzt beobachtbare Abnahmeevidenz,
- Abhängigkeiten sind zyklenfrei,
- Sicherheits- und Migrationsthemen sind nicht versteckt,
- kein Issue entscheidet eine irreversible offene Frage,
- technisch unklare Slices wurden an Wayfinder geroutet statt spekulativ geschnitten,
- die Reihenfolge ermöglicht schrittweise Demonstration,
- JSON- und Markdown-Fassung stimmen überein.

## Übergabe

Das nächste freigegebene Issue an `iterate-software-projects` übergeben. Der spätere Skill `implement-from-issue` darf nur ein freigegebenes Issue umsetzen und muss dessen Requirement-IDs, Scope, Nicht-Ziele und Abnahmeevidenz unverändert als Prüfbasis verwenden.

Issues nicht automatisch in einem Produkt-Repository anlegen, solange der Nutzer dies nicht ausdrücklich autorisiert hat.

## Abschluss

Abgeschlossen ist die Zerlegung, wenn alle Anforderungen eindeutig in unabhängigen vertikalen Issues oder transparenten Blockern mit korrektem Routingziel abgebildet sind, die Reihenfolge zyklenfrei ist und jedes freigegebene Issue durch beobachtbare Evidenz separat abgenommen werden kann.
