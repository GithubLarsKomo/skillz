---
name: role-requirements-grilling
description: Klärt den tatsächlichen Bedarf an einer Führungs-, Experten- oder Schlüsselrolle durch fokussiertes Grilling von Auftrag, Ergebnissen, Entscheidungsrechten, Schnittstellen, Kontext, Muss-Kriterien und bewusst ausgeschlossenen Anforderungen. Verwenden, bevor eine Role Architecture oder Stellenbeschreibung entworfen wird.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - round-based-requirements-grilling
outputs:
  - role-requirements-handoff.json
  - role-requirements-report.md
lastEvaluated: 2026-08-20
---

# Role Requirements Grilling

## Zweck und Abgrenzung

Dieser Skill ist die domänenspezifische Fassade für Rollen- und Stellenklärung auf Basis des autoritativen `round-based-requirements-grilling`. Er beantwortet: **Welche Rolle braucht die Organisation tatsächlich und welche Entscheidungen müssen dazu noch getroffen werden?**

Er entwirft noch keine normative Role Architecture, schreibt keine Stellenanzeige und bewertet keine Kandidaten. Die Grilling-Runtime, Runden- und Statuslogik bleibt ausschließlich beim autoritativen Grilling.

## Eintritt

Verwenden, wenn mindestens eines davon offen ist:

- Zweck und geschäftlicher Anlass der Rolle,
- erwartete Ergebnisse nach 6, 12 oder 24 Monaten,
- Ergebnisverantwortung und Entscheidungsrechte,
- Reporting Line, Team-, Budget- oder geografischer Scope,
- zentrale Schnittstellen und Konfliktfelder,
- organisatorischer Reifegrad, Aufbau-, Transformations- oder Krisenkontext,
- wirklich kausale Fähigkeiten gegenüber bloßen Proxy-Merkmalen wie Titel, Branche oder Abschluss,
- Must-have, trainierbare und verzichtbare Kriterien,
- ausdrücklich nicht zur Rolle gehörende Aufgaben.

## Grilling-Dimensionen

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

## Evidenz und Fairness

Trenne bestätigte Organisationsfakten, Stakeholder-Präferenzen, Annahmen und Hypothesen. Verwende keine geschützten oder sachfremden persönlichen Merkmale als Auswahlkriterien. Formuliere Anforderungen funktionsbezogen und begründe harte Kriterien durch den tatsächlichen Rollenauftrag.

## Übergabe

Erzeuge `role-requirements-handoff.json` mit mindestens:

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
- `sources`.

Zusätzlich `role-requirements-report.md` als lesbare Fassung.

Wenn blockierende Rollenentscheidungen geklärt sind, Übergabe an `role-architecture`. Keine Job Description direkt aus dem Grilling erzeugen.

## Abschluss

Abgeschlossen ist der Skill, wenn der tatsächliche Rollenbedarf von bloßen Wunschmerkmalen getrennt, blockierende Entscheidungen sichtbar und die Inputs für eine normative Role Architecture ausreichend belastbar sind.
