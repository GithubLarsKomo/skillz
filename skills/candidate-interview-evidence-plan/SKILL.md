---
name: candidate-interview-evidence-plan
description: Übersetzt rollenbezogene Evidence Gaps und Widersprüche in priorisierte, faire Interview- und Referenzfragen für Führungs- oder Expertenkandidaten. Verwenden, wenn nach öffentlicher Personenrecherche gezielt Scope, Attribution, Entscheidungserfahrung, Verantwortung oder Konflikte verifiziert werden sollen, ohne Pseudo-Psychometrie, versteckte Fit-Scores oder Einstellungsentscheidungen zu erzeugen.
userFacing: true
implicitInvocation: true
category: research-knowledge
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - role-capability-evidence-map
outputs:
  - candidate-interview-plan.md
  - candidate-evidence-questions.json
  - reference-check-topics.json
lastEvaluated: 2026-08-20
---

# Candidate Interview Evidence Plan

## Zweck und Grenze

Erzeuge aus einer `role-capability-map` und ihren `evidence-gaps` einen priorisierten Plan für menschliche Interviews und spätere Referenzprüfungen.

Der Skill beantwortet ausschließlich:

> **What must a human clarify next?**

Er ist **kein Interviewer, kein Personality Test, kein psychometrisches Verfahren, kein Candidate Ranking und keine Einstellungsentscheidung**.

## Trigger

Verwenden, wenn:

- öffentliche Evidenz für relevante Rollen-Kriterien unvollständig ist,
- Scope oder Verantwortungsumfang verifiziert werden muss,
- persönliche Attribution an Unternehmensereignisse unklar ist,
- widersprüchliche öffentliche Angaben geklärt werden müssen,
- verhaltensbezogene Anforderungen fair im Interview geprüft werden sollen,
- Referenzthemen aus offenen Evidence Gaps vorbereitet werden sollen.

Nicht verwenden, wenn noch keine rollenbezogene Evidence Map existiert.

## Eingaben

Mindestens:

1. `role-capability-map.json`,
2. `evidence-gaps.json`,
3. Rollen-Kriterien und Prioritäten,
4. bekannte Claim-/Source-Provenance für konfliktbehaftete oder teilweise belegte Punkte.

Optional:

- Interviewformat und verfügbare Dauer,
- Interviewerrollen,
- bereits bestätigte Informationen,
- rechtliche oder organisatorische Grenzen für Referenzchecks.

## Fragetypen

### Scope Verification

Prüft den tatsächlichen Verantwortungsumfang.

Beispiele:

- „Welche direkte Umsatz- und Ergebnisverantwortung hatten Sie in dieser Rolle?“
- „Wie groß waren Team, Budget und geografischer Verantwortungsbereich?“
- „Welche Funktionen berichteten direkt an Sie?“

### Attribution

Trennt Unternehmensereignis von persönlichem Beitrag.

Beispiele:

- „Welche Teile dieser Transformation lagen unmittelbar in Ihrer Verantwortung?“
- „Welche Entscheidungen haben Sie selbst getroffen und welche lagen beim Board oder Konzern?“
- „Woran lässt sich Ihr eigener Beitrag zum Ergebnis konkret festmachen?“

### Decision Evidence

Prüft beobachtbares Entscheidungsverhalten statt abstrakter Persönlichkeitsbegriffe.

Beispiel:

- „Beschreiben Sie eine konkrete Situation, in der technische Qualität und Time-to-Market miteinander kollidierten. Welche Entscheidung haben Sie getroffen und warum?“

### Scale and Transferability

Prüft, ob Erfahrung auf den Zielkontext übertragbar ist.

Beispiele:

- „Welche Entscheidungen konnten Sie im Konzern selbst treffen und welche waren zentral vorgegeben?“
- „Was würde sich an Ihrem Vorgehen in einem Unternehmen mit 100 statt 5.000 Mitarbeitenden ändern?“

### Failure / Learning

Prüft konkrete Erfahrung mit Rückschlägen.

Beispiele:

- „Welche größere Initiative hat nicht wie geplant funktioniert?“
- „Welche Annahme war falsch?“
- „Was haben Sie anschließend konkret verändert?“

### Evidence Reconciliation

Klärt widersprüchliche öffentliche Evidenz neutral.

Beispiel:

- „Öffentlich verfügbare Quellen nennen unterschiedliche Zeiträume beziehungsweise Verantwortungsumfänge für diese Rolle. Wie war die tatsächliche Abfolge?“

Keine Quelle als Vorwurf formulieren.

## Behavioral Evidence statt Eigenschaftswörter

Diffuse Kriterien aus dem Rollenbrief werden nur über konkrete Situationen geprüft.

Nicht fragen:

> „Sind Sie konfliktfähig?“

Besser:

> „Beschreiben Sie einen Konflikt mit einem gleichrangigen Funktionsleiter, bei dem beide Seiten legitime, aber unvereinbare Ziele hatten. Welche Entscheidung wurde getroffen und welchen Anteil hatten Sie daran?“

Nicht fragen:

> „Sind Sie unternehmerisch?“

Besser:

> „Nennen Sie eine Situation, in der Sie mit unvollständigen Informationen eine wirtschaftlich relevante Entscheidung treffen mussten. Welche Risiken haben Sie bewusst akzeptiert?“

## Keine Pseudo-Psychometrie

Der Skill darf weder aus öffentlichen Informationen noch aus Interviewantworten ohne validiertes Verfahren Eigenschaften diagnostizieren wie:

- Introversion/Extraversion,
- Narzissmus,
- Loyalität,
- Aggressivität,
- emotionale Stabilität,
- Risikofreude,
- politische Geschicklichkeit,
- „Cultural Fit“ als diffuse Persönlichkeitseigenschaft.

Stattdessen dokumentiert er beobachtbare Beispiele, Verantwortungsumfang, Entscheidungen, Ergebnisse und Evidenzlücken.

## Priorisierung

Fragen werden nach Rollenrelevanz und Evidenzlücke priorisiert.

Empfohlene Prioritäten:

- `critical` — Essential Criterion ist ungeklärt oder widersprüchlich,
- `high` — Strongly Preferred oder großer Scope-/Attribution-Gap,
- `medium` — Kontext- oder Transferability-Frage,
- `low` — ergänzende Vertiefung ohne wesentlichen Einfluss auf Rollenverständnis.

Keine Priorisierung nach persönlicher Sympathie, öffentlicher Bekanntheit oder vermutetem Candidate Ranking.

## Question Record

```json
{
  "id": "Q1",
  "criterionId": "R4",
  "gapType": "interview-gap",
  "priority": "critical",
  "questionType": "scope-verification",
  "question": "What direct revenue, margin and P&L accountability did you hold in this role?",
  "whyItMatters": "Direct P&L responsibility is essential for the target role.",
  "evidenceContext": {
    "supportingClaimRefs": ["C17", "C18"],
    "contradictingClaimRefs": []
  },
  "strongEvidenceWouldInclude": [
    "clear scope",
    "specific financial accountability",
    "decision authority",
    "concrete period or business unit"
  ],
  "followUps": []
}
```

## Antwortbewertung

Der Skill darf eine Antwort strukturell dokumentieren, aber keine verborgene psychologische oder globale Eignungsnote erzeugen.

Zulässige Evidenzzustände nach Interview:

- `confirmed`
- `partially-confirmed`
- `not-confirmed`
- `contradictory`
- `still-unclear`

Jede Bewertung benötigt eine kurze sachliche Begründung.

Beispiel:

```text
confirmed:
Candidate states direct P&L ownership for €45m business unit and describes pricing, margin and investment authority with concrete examples.
```

Nicht zulässig:

```text
9/10 entrepreneurial personality
```

## Referenzprüfung

`reference-check-topics.json` enthält nur Themen, die nach Interview noch relevant und zulässig sind.

Typische Themen:

- tatsächlicher Verantwortungsumfang,
- Rolle in konkreten Programmen oder Transformationen,
- Entscheidungsbefugnis,
- Führungsumfang,
- Zusammenarbeit in klar definierten beruflichen Situationen,
- bestätigbare Ergebnisse.

Referenzfragen sollen keine privaten oder sensiblen Informationen erheben.

## Interview-Struktur

Ein Plan kann in Blöcke gegliedert werden:

1. `mission-and-context`
2. `critical-evidence-gaps`
3. `scope-and-attribution`
4. `behavioral-decision-evidence`
5. `transferability`
6. `candidate-questions`
7. `reference-follow-up`

Für kurze Interviews zuerst Critical Gaps abdecken.

## Ausgabe

`candidate-evidence-questions.json`:

```json
{
  "schemaVersion": 1,
  "roleRef": "...",
  "personRef": "...",
  "questions": [],
  "coverage": {
    "criteriaCovered": [],
    "criticalGapsCovered": [],
    "remainingGaps": []
  },
  "decisionBoundary": {
    "candidateRankingProduced": false,
    "hireRecommendationProduced": false,
    "personalityDiagnosisProduced": false
  }
}
```

`candidate-interview-plan.md` enthält Agenda, priorisierte Fragen, Evidence Context und Follow-ups.

`reference-check-topics.json` enthält nur nach Interview verbleibende, professionell relevante Verifikationsthemen.

## Fairness- und Datenschutzgrenzen

Keine Fragen oder Bewertungen zu:

- Religion,
- ethnischer Zugehörigkeit,
- sexueller Orientierung,
- Gesundheitsinformationen,
- politischer Überzeugung,
- Gewerkschaftszugehörigkeit,
- privaten Familienverhältnissen,
- sonstigen geschützten oder rollenirrelevanten privaten Merkmalen.

Keine Umgehung durch Proxies.

Karrierepausen, Ortswechsel oder andere biografische Muster werden nicht spekulativ erklärt. Falls sie für eine bestätigte Rollenanforderung tatsächlich relevant sind, nur sachlich und rechtlich angemessen nach beruflichem Kontext fragen.

## Prüfungen

Vor Übergabe prüfen:

- jede Frage ist auf ein konkretes Rollen-Kriterium oder Evidence Gap rückgebunden,
- Critical Gaps werden zuerst adressiert,
- Scope, Attribution und Verhalten werden durch konkrete Beispiele statt Eigenschaftswörter geprüft,
- Widersprüche werden neutral formuliert,
- keine Personality-Diagnose oder globale Eignungsnote entsteht,
- keine geschützten oder privaten Merkmale werden erhoben,
- Referenzthemen sind professionell relevant und aus verbleibenden Gaps abgeleitet.

## Fehlerbehandlung

### Zu viele Fragen

Wenn die Interviewzeit nicht reicht, priorisiere Essential Criteria und offene Widersprüche. Niedrig priorisierte Vertiefungen werden nicht künstlich in einen überladenen Plan gepresst.

### Diffuses Rollen-Kriterium

Wenn ein Gap auf einem nicht operationalisierten Begriff beruht, route zurück an `executive-role-search-brief` statt eine suggestive Interviewfrage zu erfinden.

### Spekulative Persönlichkeit

Wenn ein vorgeschlagener Plan Persönlichkeit aus öffentlichem Auftreten oder Antwortstil ableiten will, entferne die Diagnose und formuliere stattdessen eine beobachtbare Verhaltensfrage.

### Unzulässige Referenzfrage

Private oder sensible Themen nicht aufnehmen; professionellen Scope neu begrenzen.

## Übergaben

Nachgelagerte Verbraucher können sein:

- `meeting-preparation` für konkrete Interviewtermine,
- `decision-record` für tatsächlich getroffene Prozessentscheidungen,
- `role-capability-evidence-map` für aktualisierte Evidence States nach bestätigten Antworten,
- spätere Referenzprüfungs-Skills.

Interviewantworten werden nicht automatisch als öffentliche Evidenz umklassifiziert; ihre Provenance bleibt `interview` beziehungsweise `reference`.

## Qualitätsfälle

### Happy Path

Eine Evidence Map enthält zwei Critical Gaps zu P&L und Turnaround, einen partiellen International-Scope und ein Interview-only Konfliktkriterium. Ergebnis: priorisierte Fragen zu Scope, Attribution und konkreten Entscheidungssituationen sowie passende Follow-ups.

### Grenzfall

Öffentliche Quellen widersprechen sich zum Verantwortungsumfang. Ergebnis: neutrale Reconciliation-Frage ohne Vorwurf; vorhandene Claims bleiben als Context referenziert.

### Fehlerfall

Ein vorgeschlagener Interviewplan fragt nach Familienplanung, bewertet Podcast-Auftritte als Charisma-Score und vergibt nach Antworten eine globale 9/10-Fit-Note. Stoppe und korrigiere Datenschutz, Pseudo-Psychometrie und Decision Boundary.

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn alle entscheidungsrelevanten Interview- und Referenzlücken in priorisierte, rollenbezogene und evidenzorientierte Fragen übersetzt wurden, jede Frage ihren Ursprung in einem Kriterium oder Gap erkennen lässt, sensible/private Themen ausgeschlossen sind und der Plan menschliche Verifikation unterstützt, ohne Candidate Ranking, Personality Diagnosis oder Hiring-Urteil vorwegzunehmen.
