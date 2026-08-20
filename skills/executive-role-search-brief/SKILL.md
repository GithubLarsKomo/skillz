---
name: executive-role-search-brief
description: Übersetzt Unternehmenskontext und Ergebnisse eines Requirements-Grillings in einen operationalisierbaren Search Brief für Führungs- oder Expertenrollen. Verwenden, wenn aus einer Besetzungsabsicht eine evidenzprüfbare Rollenmission, Muss-/Soll-Kriterien, Suchhypothesen und Interview-only Fragen entstehen sollen, ohne Kandidaten zu recherchieren oder zu bewerten.
userFacing: true
implicitInvocation: true
category: research-knowledge
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - round-based-requirements-grilling
outputs:
  - role-search-brief.json
  - role-search-brief.md
lastEvaluated: 2026-08-20
---

# Executive Role Search Brief

## Zweck und Grenze

Erzeuge aus bestätigtem Unternehmens-, Besetzungs- und Grilling-Kontext einen belastbaren Search Brief für eine Führungs- oder Expertenposition.

Der Skill beantwortet ausschließlich:

> **What is required?**

Er ist **keine Grilling-Engine, keine Kandidatensuche, keine Personenrecherche, kein Ranking und keine Einstellungsentscheidung**.

Wenn Anforderungen noch nicht ausreichend geklärt sind, delegiere an `round-based-requirements-grilling`. Dessen autoritative Prozesslogik bleibt im Repository `GithubLarsKomo/grilling`.

## Trigger

Verwenden bei:

- Executive Search,
- Expert Search,
- Nachfolgeplanung,
- Ersatzbesetzung strategisch wichtiger Rollen,
- Aufbau neuer Funktionen,
- Suche nach technischen, wissenschaftlichen oder kommerziellen Schlüsselpersonen.

Nicht verwenden, wenn bereits ein operationalisierter und freigegebener Search Brief vorliegt oder der primäre Auftrag die Recherche einer konkreten Person ist.

## Voraussetzungen

Vor Erstellung mindestens fixieren:

1. Organisation bzw. Unternehmen,
2. Anlass der Besetzung,
3. Mission oder zu lösendes Problem,
4. organisatorischen Kontext,
5. verfügbare Grilling-Ergebnisse beziehungsweise explizit bestätigte Anforderungen.

Unklare oder widersprüchliche Kernanforderungen nicht durch plausible Annahmen ersetzen. Stattdessen als `unknowns` oder `grillingQuestions` markieren.

## Grilling-Schnittstelle

`round-based-requirements-grilling` bleibt die einzige autoritative Requirements-Schnittstelle.

Ein Search Brief darf vorhandene Grilling-Ergebnisse konsumieren, aber keine eigene Rundensemantik, Statuslogik, Authentifizierung, Runtime oder parallele Requirements-Engine implementieren.

Wenn eine Frage für die Rolle entscheidungsrelevant ist und nicht belastbar beantwortet werden kann, wird sie an Grilling zurückgegeben.

## Rollenmodell

### Mission

Formuliere in beobachtbarer Wirkung:

- Warum existiert die Rolle?
- Welches Problem soll die Person lösen?
- Was muss nach 12–24 Monaten anders sein?

### Verantwortungsumfang

Nur bestätigte oder ausdrücklich noch offene Dimensionen erfassen, z. B.:

- Umsatz / P&L,
- Mitarbeiter,
- Regionen,
- Produkte,
- Technologien,
- regulatorische Verantwortung,
- operative Verantwortung,
- Board-/Investor-Exposure.

### Unternehmenssituation

Beispiele:

- Wachstum,
- Turnaround,
- Internationalisierung,
- Integration,
- Transformation,
- Professionalisierung,
- Skalierung,
- Restrukturierung,
- Nachfolge,
- Innovation.

### Kriterienklassen

Jedes Kriterium genau einer Klasse zuordnen:

- `essential`
- `strongly-preferred`
- `contextual-advantage`
- `trainable`
- `irrelevant`

Unklare Kriterien bleiben offen, statt stillschweigend hochgestuft zu werden.

## Operationalisierung

Jedes entscheidungsrelevante Kriterium benötigt mindestens:

- `criterion`: präzise Anforderung,
- `priority`: Kriterienklasse,
- `rationale`: warum sie für die Mission relevant ist,
- `evidenceQuestions`: welche öffentlich oder im Interview prüfbaren Beobachtungen dafür sprechen würden,
- `acceptableEvidence`: geeignete Evidenztypen,
- `antiEvidence`: relevante Gegenindikatoren, falls sinnvoll,
- `interviewOnly`: ob die Frage aus öffentlichen Daten typischerweise nicht belastbar beantwortbar ist.

Beispiel:

```json
{
  "criterion": "international commercialization experience",
  "priority": "essential",
  "rationale": "Die Rolle verantwortet internationale Expansion.",
  "evidenceQuestions": [
    "Did the person hold commercial responsibility across multiple countries?",
    "Were international launches or market expansions documented?",
    "Was regional revenue responsibility publicly described?"
  ],
  "acceptableEvidence": [
    "official biography",
    "company announcement",
    "annual report",
    "conference biography",
    "professional profile"
  ],
  "interviewOnly": false
}
```

## Nicht operationalisierte Begriffe

Begriffe wie

- `strategisch`,
- `unternehmerisch`,
- `dynamisch`,
- `charismatisch`,
- `politisch geschickt`,
- `kulturell passend`

dürfen nicht unverändert als Candidate-Kriterien verwendet werden.

Entweder:

1. auf beobachtbare berufliche Erfahrungen oder Verhaltensbeispiele zurückführen,
2. als Interview-only Frage formulieren,
3. oder verwerfen, wenn sie nicht rollenrelevant beziehungsweise nicht fair operationalisierbar sind.

Geschützte oder sensible Merkmale dürfen nicht als Suchkriterien verwendet oder über Proxy-Kriterien rekonstruiert werden.

## Search Hypotheses

Der Brief darf erste, explizit als Hypothese markierte Suchannahmen enthalten, z. B. relevante Unternehmensarten, Funktionsfamilien oder Karrierepfade.

Diese Hypothesen sind keine bestätigten Suchergebnisse und werden später durch `talent-search-strategy` geprüft.

## Ausgabe

`role-search-brief.json`:

```json
{
  "schemaVersion": 1,
  "role": {
    "title": "...",
    "organization": "...",
    "reasonForHire": "..."
  },
  "companyContext": {},
  "mission": {
    "statement": "...",
    "expectedOutcomes12to24Months": []
  },
  "responsibilities": [],
  "criteria": [
    {
      "id": "R1",
      "criterion": "...",
      "priority": "essential",
      "rationale": "...",
      "evidenceQuestions": [],
      "acceptableEvidence": [],
      "antiEvidence": [],
      "interviewOnly": false
    }
  ],
  "constraints": [],
  "searchHypotheses": [],
  "unknowns": [],
  "grillingQuestions": [],
  "interviewOnlyQuestions": []
}
```

`role-search-brief.md` enthält dieselben Inhalte lesbar gegliedert in Mission, Outcomes, Verantwortungsumfang, Kriterien, Constraints, Suchhypothesen, Unknowns und Interview-only Fragen.

## Datenschutz und Fairness

Der Search Brief fokussiert ausschließlich rollenbezogene Anforderungen.

Nicht als Kriterien aufnehmen oder ableiten:

- Religion,
- ethnische Zugehörigkeit,
- sexuelle Orientierung,
- Gesundheitsinformationen,
- politische Überzeugungen,
- Gewerkschaftszugehörigkeit,
- private Familienverhältnisse,
- sonstige geschützte oder für die berufliche Qualifikation irrelevante Merkmale.

Auch indirekte Proxy-Kriterien sind unzulässig, wenn sie faktisch solche Merkmale rekonstruieren sollen.

## Prüfungen

Vor Übergabe prüfen:

- Mission und erwartete Outcomes sind konkreter als ein Jobtitel,
- jedes `essential`- und `strongly-preferred`-Kriterium besitzt Evidence Questions,
- diffuse Eigenschaftswörter wurden operationalisiert oder entfernt,
- öffentliche Evidenz und Interview-only Kriterien sind getrennt,
- Unknowns und Widersprüche sind sichtbar,
- keine Candidate-Namen oder Candidate-Bewertungen wurden eingeführt,
- keine Grilling-Logik wurde dupliziert,
- keine geschützten/sensiblen Merkmale sind Bestandteil der Auswahlkriterien.

## Fehlerbehandlung

Wenn Mission, Anlass oder zentrale Muss-Kriterien widersprüchlich beziehungsweise zu unklar sind, liefere keinen scheinbar vollständigen Search Brief. Erzeuge einen partiellen Stand und route die entscheidungsrelevanten Lücken an `round-based-requirements-grilling`.

Wenn ein gewünschtes Kriterium nicht beobachtbar oder nicht fair operationalisierbar ist, markiere es als nicht geeignet und ersetze es nicht durch spekulative Proxies.

## Übergaben

Geeignete nachgelagerte Verbraucher:

- `talent-search-strategy` für Suchräume und Search Hypotheses,
- `role-capability-evidence-map` für die spätere Gegenüberstellung mit beruflicher Evidenz,
- `candidate-interview-evidence-plan` indirekt über evidenzbezogene Lücken,
- `document-production` für freigegebene Search Briefs.

## Qualitätsfälle

### Happy Path

Ein freigegebenes Grilling definiert Mission, Transformationssituation, internationale Verantwortung und mehrere Muss-/Soll-Kriterien. Ergebnis: operationalisierte Kriterien mit Evidence Questions, Constraints und wenigen offenen Interview-only Fragen.

### Grenzfall

Die Anforderung enthält `unternehmerisch` und `politisch geschickt`, aber keine Definition. Ergebnis: Begriffe werden nicht als harte Kriterien übernommen; stattdessen werden konkrete Entscheidungssituationen beziehungsweise Interviewfragen gefordert.

### Fehlerfall

Ein vorgeschlagener Brief übernimmt Alter, Familienstand oder vermutete Persönlichkeit als Auswahlkriterium und beginnt bereits Kandidaten zu ranken. Stoppe und korrigiere Scope, Fairnessgrenze und Skill-Handoff.

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn Rolle, Mission, Outcomes, Verantwortungen, Constraints und entscheidungsrelevante Kriterien operationalisiert vorliegen, jedes wesentliche Kriterium eine überprüfbare Evidenzfrage besitzt, offene Requirements sichtbar an Grilling zurückgegeben werden können und nachgelagerte Search-/Research-Skills ohne Interpretation diffuser Jobbeschreibung starten können.
