---
name: candidate-role-fit-assessment
description: Bewertet eine konkrete Person evidenzbasiert gegen eine freigegebene Role Architecture und Scorecard, trennt belegte Fakten, plausible Inferenz und Unbekanntes und erzeugt gezielte Verifikations- und Interviewfragen. Verwenden für Führungs-, Experten- und Schlüsselrollen, ohne aus öffentlicher Sichtbarkeit oder Lebenslauf-Proxys unbelegte Eignung abzuleiten.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - role-architecture
outputs:
  - candidate-role-fit.json
  - candidate-role-fit.md
  - candidate-interview-question-set.md
lastEvaluated: 2026-08-20
---

# Candidate Role Fit Assessment

## Zweck und Abgrenzung

Dieser Skill beantwortet: **Wie gut belegt die verfügbare Evidenz, dass diese konkrete Person zu der normativ definierten Rolle passt, und was muss noch verifiziert werden?**

Normative Bewertungsbasis sind `role-architecture.json` und `role-scorecard.json`, nicht die verkürzte öffentliche Job Description. Der Skill trifft keine finale Einstellungsentscheidung und erfindet keine fehlenden Kandidateninformationen.

## Evidenzklassen

Jede Aussage zum Kandidaten erhält genau eine Klasse:

- `verified`: unmittelbar durch belastbare Quelle belegt,
- `supported-inference`: nachvollziehbare, aber nicht direkt belegte Schlussfolgerung,
- `unknown`: relevante Information fehlt,
- `contradicted`: verfügbare Evidenz spricht gegen die Behauptung.

Öffentlich zugängliche Recherche kann über `research-to-evidence-note` zugeliefert werden. Primärquellen und direkte Arbeitsnachweise sind höher zu gewichten als Biografietexte, PR, Rankings oder bloße Titelähnlichkeit.

## Bewertungslogik

Für jede Scorecard-Dimension dokumentiere:

- Dimension und Gewicht,
- relevante Evidenz mit Quelle,
- Evidenzklasse,
- beobachtete Stärke oder Lücke,
- Confidence,
- offene Verifikationsfrage.

Ein numerischer Fit-Score ist nur zulässig, wenn Gewichte und Scoringregeln vor Sichtung des Kandidaten festgelegt wurden. `unknown` ist nicht automatisch negativ und darf nicht als Null-Eignung codiert werden. Knockout-Kriterien dürfen nur aus der freigegebenen Role Architecture stammen.

## Fairness und Datenschutz

Nicht verwenden oder inferieren: geschützte persönliche Merkmale, Gesundheit, Religion, politische Einstellung, sexuelle Orientierung, Familienplanung oder andere sachfremde private Informationen. Alter, Foto, Name oder Herkunft dürfen nicht als Leistungsproxy dienen. Verwende nur rollenbezogene Evidenz mit nachvollziehbarer Relevanz.

## Interview- und Verifikationsplan

`candidate-interview-question-set.md` konzentriert sich auf die größten entscheidungsrelevanten Evidenzlücken. Fragen sollen konkrete Situationen, Entscheidungen, Handlungen, Ergebnisse und Lernschleifen erschließen, statt allgemeine Selbsteinschätzungen abzufragen.

Bevorzugte Struktur:

- behauptete Capability,
- vorhandene Evidenz,
- verbleibende Unsicherheit,
- Verifikationsfrage,
- erwartete starke Evidenz,
- Red Flag oder Gegenbeleg.

## Ergebnis

`candidate-role-fit.json` enthält mindestens:

- `roleArchitectureVersion`,
- `candidateEvidenceScope`,
- `dimensionAssessments`,
- `verifiedStrengths`,
- `evidenceGaps`,
- `contradictions`,
- `knockoutStatus`,
- `overallConfidence`,
- `recommendedVerification`,
- `limitations`.

`candidate-role-fit.md` ist die lesbare, quellenbezogene Fassung. Formuliere keine Gewissheit, die über die Evidenz hinausgeht.

## Rücksprung

Wenn die Kandidatenbewertung zeigt, dass das Rollenmodell selbst unklar, widersprüchlich oder auf ungeeigneten Proxys basiert, nicht den Kandidaten passend rechnen. Zurück zu `role-architecture`; falls dahinter eine echte Stakeholder-Entscheidung fehlt, weiter zu `role-requirements-grilling`.

## Abschluss

Abgeschlossen ist der Skill, wenn jede relevante Fit-Aussage evidenzklassifiziert, Lücken explizit und die nächsten Verifikationsfragen auf die entscheidungsrelevanten Unsicherheiten fokussiert sind.
