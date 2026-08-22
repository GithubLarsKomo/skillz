---
name: sport-performance-psychology
description: Erstellt ein individualisiertes sportpsychologisches Performance-Training für Ziel-/Prozessfokus, Imagery, Self-Talk, Aufmerksamkeit, Aktivierungsregulation und Wettkampfroutinen. Verwenden für Leistungspsychologie; nicht für Diagnose, Psychotherapie oder Krisenbehandlung.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - sport-athlete-profile
  - sport-goal-performance-model
  - sport-microcycle-planning
outputs:
  - performance-psychology-plan.json
lastEvaluated: 2026-08-22
---

# Sport Performance Psychology

Übersetze konkrete Leistungsanforderungen in wenige trainierbare psychologische Fertigkeiten. Behandle sportpsychologische Techniken wie andere Trainingsreize: Ziel, Dosis, Übung, Transfer und individuelle Response werden sichtbar gemacht.

## Trigger

Nutze diesen Skill bei Wettkampfnervosität ohne Mental-Health-Red-Flag, inkonsistentem Fokus, schwacher Pre-Performance-Routine, Motivations-/Selbstwirksamkeitsproblemen, technischem Imagery-Bedarf oder wenn psychologische Fertigkeiten systematisch in einen Meso-/Mikrozyklus integriert werden sollen.

## Voraussetzungen

Benötigt mindestens Performance-Ziel, sportartspezifische Situation und Athletenpräferenzen. Wenn Symptome oder Belastungen auf ein mögliches Mental-Health-Problem statt eine reine Performance-Frage hindeuten, zuerst `sport-mental-health-routing` verwenden.

## Ablauf

1. **Performance-Frage operationalisieren.** Beobachtbares Problem und gewünschtes Verhalten definieren, z. B. Startfokus, Umgang mit Fehlern oder Aktivierung vor einer Schlüsselsequenz.
2. **Eine primäre Fertigkeit wählen.** Imagery, Self-Talk, attentional control, goal/process cues, arousal regulation, mindfulness/acceptance oder pre-performance routine nur nach Bedarf kombinieren.
3. **Praxis in den Trainingskontext einbauen.** Kurze wiederholbare Übungen an bestehende Warm-ups, Technikblöcke, Erholung oder Wettkampfsimulationen koppeln statt zusätzliche unspezifische Mentalarbeit anzuhäufen.
4. **Transfer definieren.** Cue, Auslöser, gewünschtes Verhalten und reale Trainings-/Wettkampfsituation festlegen.
5. **Response messen.** Adhärenz, subjektive Nützlichkeit, Zielverhalten und relevante Performance-Marker getrennt beobachten.
6. **Evidenzunsicherheit erhalten.** Psychologische Interventionen können Leistungsnutzen zeigen, Effekte sind jedoch heterogen; keine garantierte Leistungssteigerung behaupten.
7. **Minimal revidieren.** Technik nur beibehalten oder erweitern, wenn sie akzeptiert wird und im individuellen Kontext nützt.

## Motivation

Motivation nicht als moralische Eigenschaft oder einzelnen Score behandeln. Prozessziele, Autonomie, wahrgenommene Kompetenz, Umgebungsbarrieren, Belastung und Sinn des Ziels gemeinsam betrachten. Ein kurzfristiges Motivationstief allein ist keine Diagnose und kein Grund für umfassende Planänderung.

## Imagery und Routinen

Imagery soll sportartspezifisch, kontrollierbar und mit realen Cues verknüpft sein. Die konkrete Dosis wird als testbare Prescription formuliert, nicht aus einer einzelnen Meta-Analyse als universaler Standard übernommen. Wettkampfroutinen werden unter realitätsnahen Bedingungen geprobt.

## Safety Boundary

Dieser Skill behandelt **Performance-Psychologie**. Er diagnostiziert keine psychische Erkrankung, ersetzt keine Psychotherapie und führt keine Krisenintervention durch. Hinweise auf Selbstgefährdung, schwere Funktionsbeeinträchtigung, Essstörung, Substanzproblematik, anhaltende depressive/Angstsymptomatik oder andere klinisch relevante Sorgen werden an `sport-mental-health-routing` übergeben.

## Alters-/Geschlechtsmodifier

Alter und Geschlecht erzeugen keine festen psychologischen Profile. Sprache, Lebenskontext, Erfahrung, Präferenzen, Sportkultur und individuelle Response sind maßgeblich.

## Prüfungen

- Ist das Ziel beobachtbar statt nur „mentaler stärker werden“?
- Hat jede Technik eine konkrete Übung, Dosis und Transfersituation?
- Sind Adhärenz/Nützlichkeit von Performance-Outcome getrennt?
- Wird Evidenz nicht überverkauft?
- Ist Mental-Health-Routing klar getrennt?

## Fehlerbehandlung

- **Unspezifisches Problem:** erst Performance-Frage operationalisieren.
- **Technik wird nicht akzeptiert:** nicht erzwingen; Alternative mit gleichem Ziel wählen.
- **Kein Transfer:** Übung stärker an reale Cues/Belastung koppeln oder verwerfen.
- **Mental-Health-Signal:** Performance-Coaching nicht als Ersatzbehandlung verwenden; routen.

## Übergabe

`performance-psychology-plan.json` enthält Version, Performance-Frage, Zielverhalten, ausgewählte Fertigkeiten, konkrete Praxisblöcke, Cues, Transfer-Situationen, Monitoring, Re-Evaluation, Unsicherheiten und Safety Flags.

## Abschlusskriterien

Der Plan ist abgeschlossen, wenn höchstens wenige priorisierte psychologische Fertigkeiten konkret trainierbar sind, deren Transfer überprüfbar ist und klinische Themen außerhalb der Performance-Schicht bleiben.
