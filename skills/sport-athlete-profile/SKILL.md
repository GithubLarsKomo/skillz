---
name: sport-athlete-profile
description: Erfasst und versioniert den trainingsrelevanten Athletenkontext als belastbaren Ausgangszustand für Planung, Monitoring und Adaptation. Verwenden bei Neuaufnahme, Profiländerungen oder wenn Alter, Trainingsalter, Sportart, Verfügbarkeit, Präferenzen oder dokumentierte Einschränkungen für spätere Sport-Skills strukturiert bereitgestellt werden müssen; nicht für medizinische Diagnosen.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires: []
outputs:
  - athlete-profile.json
lastEvaluated: 2026-08-22
---

# Sport Athlete Profile

Erzeuge einen versionierten, minimal notwendigen Athletenkontext. Das Profil beschreibt den Ausgangszustand; es interpretiert weder Trainingsreaktionen noch stellt es Diagnosen.

## Trigger

Nutze diesen Skill bei Neuaufnahme, Profilaktualisierung oder wenn ein nachgelagerter Sport-Skill einen strukturierten Athletenkontext benötigt.

Nicht auslösen, wenn nur eine einzelne Einheit protokolliert oder eine bestehende Diagnose interpretiert werden soll.

## Voraussetzungen

Ermittle soweit verfügbar:

- `athlete_id`, Zeitzone, Sportart und Disziplin,
- Geburtsdatum oder belastbare Altersangabe,
- Trainingsalter und technische Erfahrung,
- aktuelle Leistungs- und Wettkampfhistorie,
- verfügbare Trainingstage, typische Dauer und Equipment,
- bekannte Verletzungen, Erkrankungen und dokumentierte Restriktionen,
- relevante Präferenzen und No-Go-Übungen,
- optional und nur bei freiwilliger Angabe: sex-at-birth, Zyklus-/Kontrazeptions- oder peri-/postmenopausaler Kontext.

Gesundheitsnahe Daten nur erfassen, wenn sie für Trainingssteuerung erforderlich sind. Fehlende optionale Felder bleiben unbekannt.

## Ablauf

1. **Identität trennen.** Verwende eine stabile `athlete_id`; vermeide unnötige personenbezogene Details.
2. **Trainingskontext normalisieren.** Sport, Disziplin, Trainingsalter, Verfügbarkeit, Equipment und Umgebungsbedingungen strukturiert erfassen.
3. **Altersband ableiten.** Alter aus Datum/Referenzdatum berechnen, wenn möglich. `20-30`, `50+` oder anderes Band kennzeichnen, ohne daraus automatisch Trainingsrestriktionen abzuleiten.
4. **Leistungshistorie sichern.** PBs, Benchmarktests und relevante Vergleichswerte mit Datum und Quelle aufnehmen.
5. **Health constraints trennen.** Quellenbefund, dokumentierte Restriktion und sportwissenschaftliche Konsequenz nicht vermischen.
6. **Sex-spezifischen Kontext optionalisieren.** Zyklus-/Menopauseinformationen nur symptom- und entscheidungsbezogen führen; keine starre Phasenperiodisierung ableiten.
7. **Versionieren.** Änderungen mit `profile_version`, `valid_from`, `source_refs`, Unsicherheiten und Sicherheitsflags ausgeben.

## Alters- und Geschlechtsregeln

- Alter >50 ist kein Grund, Intensität, schwere Kraftarbeit oder Power pauschal zu entfernen.
- Recovery-Annahmen werden anhand beobachteter Reaktion angepasst, nicht allein anhand des Alters.
- Weibliche Athleten erhalten keine automatische Trainingssteuerung nach Kalender-Zyklusphase.
- Männliche Athleten bleiben für niedrige Energieverfügbarkeit, Schlaf-, Stress- und Gesundheitsprobleme gleichwertig im Risikomodell.

## Prüfungen

- Sind Pflichtfelder von optionalen/consented Feldern getrennt?
- Ist jede medizinische Einschränkung auf eine Quelle oder ausdrückliche Athletenangabe zurückführbar?
- Wurden unbekannte Werte nicht erfunden?
- Ist Alter ein Modifier statt eine pauschale Leistungsgrenze?
- Sind optionale sex-spezifische Daten datensparsam erfasst?

## Sicherheitsgrenzen

Keine Diagnose, kein medizinisches Clearance und keine psychologische Klassifikation erzeugen. Red-Flag-Angaben als `safety_flags` weiterreichen.

## Fehlerbehandlung

- **Geburtsdatum fehlt:** Altersband als `unknown` führen.
- **Widersprüchliche Angaben:** beide Quellen mit Unsicherheit erhalten und keine stillschweigende Auswahl treffen.
- **Unklare medizinische Restriktion:** keine Belastungsfreigabe erfinden; Klärungsbedarf markieren.
- **Optionale sensible Daten fehlen:** Planung darf trotzdem funktionieren und Unsicherheit sichtbar halten.

## Übergabe

Primärer Output ist `athlete-profile.json` gemäß `$defs.athleteProfile` in `schemas/sport-athlete-management-v1.schema.json`. Nachgelagerte Skills referenzieren das Profil über `athlete_id` und Version statt mutable Profildaten zu kopieren.

## Abschlusskriterien

Der Skill ist abgeschlossen, wenn ein minimaler, versionierter und quellenklarer Athletenkontext vorliegt, fehlende Daten sichtbar sind und keine alters-, geschlechts- oder medizinisch unbegründeten Annahmen eingeführt wurden.
