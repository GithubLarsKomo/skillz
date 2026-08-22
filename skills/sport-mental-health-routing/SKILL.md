---
name: sport-mental-health-routing
description: Trennt sportpsychologische Performance-Themen von möglichem Mental-Health-/Krisenbedarf und erzeugt ein konservatives Routing mit Dringlichkeit, Support-Optionen und Trainingsgrenzen. Verwenden bei psychischer Belastung oder Warnsignalen; nicht diagnostizieren, therapieren oder medizinisch freigeben.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - sport-athlete-profile
  - sport-daily-athlete-monitoring
outputs:
  - mental-health-routing.json
lastEvaluated: 2026-08-22
---

# Sport Mental Health Routing

Schütze die Grenze zwischen Performance-Coaching und Mental Health. Ziel ist frühes Erkennen eines **Routing-Bedarfs**, nicht das Stellen einer Diagnose.

## Trigger

Nutze diesen Skill bei anhaltender oder deutlicher psychischer Belastung, Funktionsverlust, Ess-/Gewichtsproblematik, Substanzproblemen, Schlafproblemen mit relevanter Beeinträchtigung, ungewöhnlicher Angst/depressiver Symptomatik oder wenn Performance-Coaching offensichtlich nicht die passende Ebene ist.

## Voraussetzungen

Nur die tatsächlich bekannten Aussagen/Symptome verwenden. Screening-Scores können Kontext sein, sind aber nicht gleich Diagnose. Bei fehlenden Informationen Unsicherheit sichtbar lassen.

## Ablauf

1. **Safety zuerst.** Hinweise auf akute Selbst-/Fremdgefährdung, schwere Desorientierung, Psychose, akute Intoxikation oder sonstige unmittelbare Gefahr als `urgent` behandeln und normale Performance-Steuerung verlassen.
2. **Funktion und Verlauf prüfen.** Dauer, Intensität, Verschlechterung, Schlaf, Alltag/Training, soziale Funktion und vorhandene professionelle Unterstützung erfassen.
3. **Performance vs Health trennen.** Reine Wettkampfnervosität kann Performance-Psychologie sein; persistente klinisch relevante Symptome werden nicht mit Self-Talk/Imagery „behandelt“.
4. **Routing-Stufe bestimmen.** `performance_support`, `monitor`, `professional_review` oder `urgent` verwenden.
5. **Trainingsgrenze formulieren.** Nur notwendige konservative Safety-/Support-Grenzen nennen; keine psychische Diagnose in Trainingsregeln umwandeln.
6. **Support-Pfad benennen.** Geeignete qualifizierte medizinische/psychologische Unterstützung, Team-/Hausarzt oder bestehende Versorgung als Route angeben; bei akuter Gefahr lokale Notfallversorgung priorisieren.
7. **Privatsphäre minimieren.** Nur für Safety/Koordination erforderliche Informationen im Trainingssystem persistieren.

## Was der Skill nicht tut

- keine Diagnose von Depression, Angststörung, Essstörung, ADHS oder anderen Erkrankungen;
- keine Psychotherapie oder Krisentherapie;
- keine Medikamentenberatung;
- keine medizinische Freigabe;
- keine automatische Trainingssperre aus einem einzelnen Screening-Score.

## RED-S / Essverhalten

Gewichts-/Essproblematik kann mit niedriger Energieverfügbarkeit und RED-S überlappen. Bei entsprechenden Signalen zusätzlich `sport-nutrition-fueling` bzw. qualifizierte medizinische/ernährungsmedizinische Versorgung routen; dies gilt für alle Geschlechter.

## Alters-/Geschlechtsmodifier

Keine Stereotype zu Resilienz, Menopause, Männlichkeit oder psychischer Belastbarkeit verwenden. Sportkultur, Lebensphase, Stressoren und individuelle Symptomatik sind relevant.

## Prüfungen

- Wurde akute Gefahr vor Performance-Optimierung geprüft?
- Ist Routing von Diagnose klar getrennt?
- Wird ein einzelner Screening-Wert nicht überinterpretiert?
- Sind Privatsphäre und minimale Persistenz berücksichtigt?
- Kann `urgent` normale Trainingsoptimierung explizit unterbrechen?

## Fehlerbehandlung

- **Unklare Angaben:** `monitor`/`professional_review` mit Unsicherheit statt Diagnose.
- **Performance-Problem ohne klinisches Signal:** an `sport-performance-psychology` übergeben.
- **Akute Gefahr:** normale Performance-Workflows beenden und unmittelbare professionelle/Notfall-Hilfe routen.

## Übergabe

`mental-health-routing.json` enthält Routing-Version, Concern-Summary, beobachtete Signale, Funktions-/Verlaufsinformationen, Routing-Stufe, Trainingsgrenzen, Support-Pfad, Privacy-Minimization, Confidence, Unsicherheiten und Safety Flags.

## Abschlusskriterien

Der Skill endet, wenn die passende Routing-Ebene klar ist, keine Diagnose vorgetäuscht wird und akute Safety-Anforderungen Performance-Ziele überstimmen können.
