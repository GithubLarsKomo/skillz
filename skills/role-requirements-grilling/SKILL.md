---
name: role-requirements-grilling
description: Klärt den tatsächlichen Bedarf an einer Führungs-, Experten- oder Schlüsselrolle durch fokussiertes Grilling von Auftrag, Ergebnissen, Entscheidungsrechten, Schnittstellen, Kontext, Muss-Kriterien und bewusst ausgeschlossenen Anforderungen. Verwenden, bevor eine Role Architecture oder Stellenbeschreibung entworfen wird.
userFacing: true
implicitInvocation: false
category: workflow
version: 0.3.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - round-based-requirements-grilling
consumes: []
outputs:
  - role-requirements-handoff.json
  - role-requirements-report.md
lastEvaluated: 2026-08-20
---

# Role Requirements Grilling

## Trigger

Verwenden, wenn Zweck, Outcomes, Entscheidungsrechte, Scope, Schnittstellen, Capability-Anforderungen oder Nicht-Ziele einer Führungs-, Experten- oder Schlüsselrolle noch nicht ausreichend geklärt sind. Dieser Skill ist die domänenspezifische Fassade für Rollen- und Stellenklärung auf Basis des autoritativen `round-based-requirements-grilling` und beantwortet: **Welche Rolle braucht die Organisation tatsächlich und welche Entscheidungen müssen dazu noch getroffen werden?**

Er entwirft noch keine normative Role Architecture, schreibt keine Stellenanzeige und bewertet keine Kandidaten. Die Grilling-Runtime, Runden- und Statuslogik bleibt ausschließlich beim autoritativen Grilling. Wegen dieser zwingenden Delegation ist `implicitInvocation: false` bewusst gesetzt.

## Voraussetzungen

Erforderlich ist ein konkreter Rollen- oder Besetzungsanlass mit mindestens einem identifizierbaren Stakeholder oder einer nachvollziehbaren Organisationsentscheidung. Vorhandene Stellenprofile, Organigramme, Zielbilder oder Suchaufträge sind Evidenz, aber keine automatisch gültige Rollenarchitektur.

Verwende keine geschützten oder sachfremden persönlichen Merkmale als Auswahlkriterien. Formuliere Anforderungen funktionsbezogen und begründe harte Kriterien durch den tatsächlichen Rollenauftrag.

## Ablauf

### Grilling-Dimensionen

Frage bevorzugt nach beobachtbaren Ergebnissen statt nach Wunschprofilen:

1. Warum existiert die Rolle?
2. Welche drei bis fünf Ergebnisse müssen sichtbar werden?
3. Welche Entscheidungen muss die Person selbst treffen dürfen?
4. Welche Ressourcen, Informationen und Eskalationswege braucht sie?
5. Welche Schnittstellen und strukturellen Widerstände prägen die Rolle?
6. Welche Fähigkeiten sind kausal nötig, welche nur historische Proxys?
7. Welche Erfahrungen sind zwingend, trainierbar oder irrelevant?
8. Welche Arbeitsweise passt zum Kontext, ohne Persönlichkeit zu stereotypisieren?
9. Was gehört ausdrücklich nicht zur Rolle?
10. Welche offenen Entscheidungen blockieren die Rollenarchitektur?

Trenne bestätigte Organisationsfakten, Stakeholder-Präferenzen, Annahmen und Hypothesen. Ungeklärte Entscheidungspunkte bleiben sichtbar und werden nicht durch vermeintlich naheliegende Antworten ersetzt.

### Artefaktvertrag

`role-requirements-handoff.json` enthält mindestens:

- `schemaVersion: 1`,
- `handoffId`,
- `version`,
- `status: draft | review | approved | superseded`,
- `rolePurpose`,
- `businessContext`,
- `outcomes`,
- `decisionRights`,
- `scope`,
- `interfaces`,
- `constraints`,
- `mustHaveCapabilities`,
- `trainableCapabilities`,
- `nonRequirements`,
- `successEvidence`,
- `openDecisions`,
- `sources`,
- `approvedAt` und `approvalAuthority`, wenn `status=approved`.

Zusätzlich entsteht `role-requirements-report.md` als lesbare Fassung.

### Lebenszyklus

Wird ein bereits verwendeter Requirements-Handoff fachlich geändert, erhält er eine neue Version. Eine frühere Version bleibt nachvollziehbar, wird aber `superseded`. Abgeleitete Role Architectures müssen ihre konkrete `sourceHandoffId` und `sourceHandoffVersion` festhalten; sie werden nicht stillschweigend auf einen geänderten Handoff umgebogen.

## Prüfungen

Prüfe vor Abschluss:

- Zweck und gewünschte Outcomes sind konkreter als Titel oder Tätigkeitslisten.
- Entscheidungsrechte und Scope sind soweit geklärt, dass keine blockierende Rollenentscheidung verborgen bleibt.
- Must-haves sind von trainierbaren Fähigkeiten und bloßen Proxys getrennt.
- `openDecisions` enthält alle noch offenen fachlichen Entscheidungen.
- `status=approved` wird nur verwendet, wenn keine blockierende Rollenentscheidung mehr offen ist.
- Geschützte oder sachfremde persönliche Merkmale wurden nicht als Rollenanforderung übernommen.

## Fehlerbehandlung

Bei widersprüchlichen Stakeholder-Aussagen den Konflikt explizit halten und eine weitere Grilling-Runde auslösen, statt selbst eine Entscheidung zu erfinden. Bei fehlender externer Evidenz keine fachliche Präferenz simulieren; Evidenz gezielt nachfordern oder als unbekannt markieren.

Ein bloßer Wunsch nach einer Stellenanzeige ist kein Grund, die normative Zwischenstufe zu überspringen. **Keine Job Description direkt** aus dem Grilling erzeugen.

## Übergabe

Wenn blockierende Rollenentscheidungen geklärt sind, `role-requirements-handoff.json` und `role-requirements-report.md` an `role-architecture` übergeben. Die Übergabe darf als `approved` nur erfolgen, wenn der Handoff versionsgebunden und die offenen Entscheidungen nicht blockierend sind.

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn der tatsächliche Rollenbedarf von bloßen Wunschmerkmalen getrennt, die kausale Fähigkeiten gegenüber Proxy-Merkmalen nachvollziehbar gemacht, blockierende Rollenentscheidungen sichtbar und die Inputs für eine normative Role Architecture ausreichend belastbar sind.