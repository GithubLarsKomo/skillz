---
name: candidate-role-fit-assessment
description: Bewertet eine konkrete Person evidenzbasiert gegen eine freigegebene Role Architecture und Scorecard, trennt belegte Fakten, plausible Inferenz und Unbekanntes und erzeugt gezielte Verifikations- und Interviewfragen. Verwenden für Führungs-, Experten- und Schlüsselrollen, ohne aus öffentlicher Sichtbarkeit oder Lebenslauf-Proxys unbelegte Eignung abzuleiten.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.2.0
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

## Eintritt und Freigabe-Gate

Erforderlich sind:

- `role-architecture.json` mit `status=approved`,
- `role-scorecard.json` mit `status=approved`,
- exakt übereinstimmende `roleArchitectureId` und `roleArchitectureVersion`,
- eine vor Sichtung dieses Kandidaten freigegebene `scoringModelVersion`.

Fehlt eines dieser Gates, wird die Bewertung blockiert. Eine öffentliche Ausschreibung, ein Search Brief oder eine frühere Kandidatenbewertung kann diese normative Basis nicht ersetzen.

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

Ein numerischer Fit-Score ist nur zulässig, wenn Gewichte und Scoringregeln vor Sichtung des Kandidaten festgelegt und freigegeben wurden. `unknown` ist nicht automatisch negativ und darf nicht als Null-Eignung codiert werden. Knockout-Kriterien dürfen nur aus der freigegebenen Role Architecture stammen.

Gewichte, Dimensionen, Mindestniveaus oder Knockouts dürfen während oder nach Sichtung eines Kandidaten nicht verändert werden, um dessen Fit zu verbessern oder zu verschlechtern. Falls eine echte Rollenänderung erforderlich ist, wird sie unabhängig vom Kandidaten in `role-architecture` begründet und versioniert; anschließend werden alle Kandidaten gegen dieselbe neue freigegebene Version neu bewertet.

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

- `roleArchitectureId`,
- `roleArchitectureVersion`,
- `scoringModelVersion`,
- `assessmentStatus: current | stale`,
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

## Verbotene Übergänge

- Kein Assessment ohne freigegebene Role Architecture und passende freigegebene Scorecard.
- Keine Bewertung ausschließlich gegen `public-job-posting.md`, `job-description.md` oder `executive-search-brief.md`.
- Keine direkte Übernahme von Kandidatenevidenz in neue Rollenanforderungen oder Scorecard-Gewichte.
- Kein Vergleich verschiedener Kandidaten auf unterschiedlichen Role-Architecture- oder Scoring-Versionen, sofern das Ergebnis als gemeinsame Rangfolge interpretiert werden soll.

## Rücksprung und Invalidierung

Wenn die Kandidatenbewertung zeigt, dass das Rollenmodell selbst unklar, widersprüchlich oder auf ungeeigneten Proxys basiert, nicht den Kandidaten passend rechnen. Zurück zu `role-architecture`; falls dahinter eine echte Stakeholder-Entscheidung fehlt, weiter zu `role-requirements-grilling`.

Wird danach eine neue Role-Architecture- oder Scorecard-Version freigegeben, wird die bisherige Bewertung `stale`. Sie bleibt nachvollziehbar, darf aber nicht als aktuelle Fit-Bewertung oder Vergleichsbasis dienen. Der Kandidat muss gegen die neue normative Version erneut bewertet werden.

## Abschluss

Abgeschlossen ist der Skill, wenn jede relevante Fit-Aussage evidenzklassifiziert, Lücken explizit, normative Versionen festgehalten und die nächsten Verifikationsfragen auf die entscheidungsrelevanten Unsicherheiten fokussiert sind.
