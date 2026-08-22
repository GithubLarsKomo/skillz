---
name: sport-microcycle-planning
description: Verteilt die Ziele eines Mesozylus auf einen konkreten kurzen Trainingszyklus mit Schlüsselreizen, High/Low-Logik, Recovery-Abständen und vollständigen Session-Prescriptions. Verwenden für Wochenplanung oder 5–10-Tage-Zyklen; nicht für Saisonstrategie oder medizinische Rehabilitation.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - sport-mesocycle-planning
outputs:
  - sport-microcycle.json
lastEvaluated: 2026-08-22
---

# Sport Microcycle Planning

Erzeuge den konkreten kurzen Trainingszyklus, in dem Schlüsselreize geschützt und konkurrierende Belastungen sinnvoll angeordnet werden.

## Trigger

Nutze diesen Skill für eine konkrete Trainingswoche oder einen vergleichbaren 5–10-Tage-Zyklus.

## Voraussetzungen

Benötigt aktiven Mesozylus, aktuelle Verfügbarkeit, geplante Schlüsselreize, letzte harte Einheiten, aktuelle Restriktionen und – falls vorhanden – jüngste Adaptationsentscheidung.

## Ablauf

1. **Schlüsselreize zuerst platzieren.** Sportartspezifische Hauptreize und qualitätskritische Power-/Intensitätseinheiten erhalten Priorität.
2. **High/Low-Organisation wählen.** Harte Reize sinnvoll clustern oder trennen, sodass unnötige mittelharte Dauerbelastung vermieden wird.
3. **Interferenz prüfen.** Kraft, Power, Ausdauer und Sporttechnik nach aktuellem Primärziel sequenzieren.
4. **Recovery-Abstände planen.** Individuelle Reaktion, Trainingsalter, Vorverletzung und vorangegangene Belastung berücksichtigen.
5. **Sessions vollständig beschreiben.** Ziel, Typ, geplante Dauer, Intensitätssteuerung, Stop-/Anpassungsregel und erwartete RPE angeben.
6. **Flexpunkte definieren.** Verschiebbare Sessions und nicht verhandelbare Schlüsselreize kennzeichnen.
7. **Nächsten Checkpoint setzen.** Daily Monitoring und Adaptation Engine als Eintrittspunkt vor kritischen Einheiten referenzieren.

## Alters- und Geschlechtsregeln

Altersband steuert nicht automatisch die Anzahl harter Einheiten; reale Verträglichkeit und Historie sind maßgeblich. Sex-spezifische Anpassungen erfolgen symptom- und datenbasiert.

## Prüfungen

- Sind Schlüsselreize mit ausreichender Frische geschützt?
- Sind harte Reize und Recovery plausibel verteilt?
- Enthält jede Session Ziel, Dauer/Umfang, Intensitätsregel und Stop-/Anpassungsregel?
- Ist klar, welche Einheit bei Zeitmangel zuerst entfällt?
- Widerspricht keine Session aktiven Restriktionen?

## Fehlerbehandlung

- **Zu wenig Zeit:** Zubehör/sekundäre Reize reduzieren, nicht automatisch den Hauptreiz.
- **Kollision harter Reize:** Reihung nach Mesoziel korrigieren.
- **Unklare Belastungswerte:** RPE/RIR/Technik oder konservative Zonen statt erfundener Prozentwerte nutzen.

## Übergabe

Output ist `sport-microcycle.json` gemäß `$defs.microcycle`. `sport-daily-athlete-monitoring` protokolliert die Reaktion; `sport-training-adaptation-engine` kann versionierte Änderungen erzeugen.

## Abschlusskriterien

Der Skill endet mit einem vollständig terminierbaren kurzen Zyklus, klaren Schlüsselreizen, Recovery-Abständen, Flexpunkten und ausführbaren Session-Prescriptions.
