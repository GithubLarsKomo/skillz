---
name: sport-training-programming
description: Erstellt aus Zieltermin, Leistungsstand, Trainingshistorie, Kraftwerten, verfügbaren Einheiten und Belastungsgrenzen einen periodisierten Sporttrainingsplan mit konkreten Übungen, Sätzen, Wiederholungen, RIR/Prozentlast, Pausen, Ausdauerzonen, Progression und Taper. Verwenden, wenn aus Diagnostik oder Zielsetzung ein ausführbarer Wochenplan entstehen soll; nicht als medizinische Rehabilitationsfreigabe.
---

# Sport Training Programming

Erzeuge einen ausführbaren, periodisierten Trainingsplan, der Kraft, Schnellkraft, Ausdauer, sportartspezifische Hauptreize und Erholung gemeinsam steuert. Der Plan soll konkret genug zum Trainieren und robust genug zum Anpassen sein.

## Trigger

Nutze diesen Skill bei Anfragen nach:

- Wochen-, Block- oder Saisonplanung,
- Kraft-, Schnellkraft-, Power- oder Taperprogrammen,
- Integration von Zone 2, Intervallen und sportartspezifischen Einheiten,
- A/B- oder Ganzkörperplänen mit genauen Sätzen, Wiederholungen, RIR, Prozentlast und Pausen,
- Ableitung eines Plans aus `sport-diagnostics.json`, 1RM/e1RM oder einem Wettkampfdatum.

Nicht auslösen, wenn nur eine bestehende Planung typografisch als PDF gesetzt werden soll.

## Voraussetzungen

Ermittle mindestens:

- Hauptziel und Zieltermin,
- Sportart und aktuelle Trainingsphase,
- verfügbare Trainingstage und typische Dauer,
- aktuelle Kraftwerte oder konservative e1RM, wenn Prozentsteuerung verwendet werden soll,
- Ausdauerzonen/Schwellen oder geeignete Ersatzsteuerung,
- Trainingsalter und technische Erfahrung,
- Equipment und Umgebungsbedingungen,
- letzte harte Einheiten und erwartete sportartspezifische Belastungen,
- bekannte Verletzungen, Symptome, ärztliche Restriktionen oder Bewegungsverbote.

Fehlt ein 1RM, keine Prozentlast vortäuschen. Dann RIR/RPE, Velocity, Technik oder eine konservative e1RM-Schätzung verwenden und die Methode kennzeichnen.

## Ablauf

1. **Zielhierarchie setzen.** Wettkampf-/Funktionsziel, Primärqualitäten und bewusst nicht priorisierte Qualitäten benennen.
2. **Belastungsbudget bauen.** Harte sportartspezifische Reize zuerst platzieren; Kraftraum und Ausdauer so integrieren, dass sie Hauptleistung unterstützen statt verdrängen.
3. **Blocklogik wählen.** Je nach Horizont Aufbau, Intensivierung, Schnellkraft/Power, Taper oder Erhaltungsphase definieren.
4. **Einheiten konkretisieren.** Für jede Übung/Intervallserie mindestens Umfang, Intensität, Pause, Technikfokus und Abbruch-/Anpassungsregel angeben.
5. **Reihenfolge optimieren.** Hochgeschwindigkeits-/Powerarbeit vor ermüdender Arbeit; Hauptübung vor Zubehör; sportartspezifische Schlüsselreize mit ausreichender Frische schützen.
6. **Progression definieren.** Last, Wiederholungen, Satzanzahl, Dauer oder Dichte nur nach expliziten Kriterien steigern. Bei Powerarbeit Geschwindigkeit und Qualität vor Last.
7. **Autoregulation ergänzen.** RIR/RPE, Velocity-Loss, 24-h-Reaktion, Schlaf/Ermüdung oder sportartspezifische Qualitätsmarker passend zum Kontext verwenden.
8. **Taper einbauen.** Vor Zielwettkampf Volumen gezielt reduzieren, Intensität/Bewegungsgeschwindigkeit passend erhalten und keine neuen Übungen/1RM-Tests spät einführen.
9. **Wochenplan prüfen.** Harte Tage, leichte Tage, Recovery und konkurrierende Reize auf Kollisionen prüfen.
10. **Handoff erzeugen.** `sport-training-plan.json` mit Phasen, Wochen, Einheiten, Regeln und Begründung erzeugen.

Empfohlenes Kernschema:

```json
{
  "goal": {},
  "constraints": [],
  "periodization": [],
  "weeks": [
    {
      "week": 1,
      "focus": "",
      "sessions": [
        {
          "day": "",
          "type": "strength|power|endurance|sport|recovery",
          "items": [],
          "load_rule": "",
          "stop_rule": ""
        }
      ]
    }
  ],
  "progression_rules": [],
  "taper_rules": [],
  "safety_rules": [],
  "uncertainties": []
}
```

## Programmierregeln

- **Kraft:** Last und Volumen an Zielphase koppeln; Wiederholungen mit RIR/RPE oder Prozentlast eindeutig steuern.
- **Schnellkraft:** geringe Wiederholungszahlen, vollständige Pausen, maximale Beschleunigungsabsicht, Satzende bei klarer Geschwindigkeits- oder Technikabnahme.
- **Plyometrie:** Sprunghöhe/Boxhöhe nicht als Selbstzweck steigern; Landungsqualität und geringe Ermüdung priorisieren.
- **Zone 2:** Intensität aus vorhandener Diagnostik oder konservativem Talk-/HF-/Leistungsbereich ableiten; Dauer vor Intensität progressieren, wenn die Grundlagenausdauer im Vordergrund steht.
- **Taper:** spezifische Qualität schützen, Gesamtvolumen reduzieren und kein „Nachholen“ verpasster Arbeit in der Wettkampfwoche.
- **Kombination Kraft + Sport:** bei Konflikt gewinnt der Reiz, der dem aktuellen Hauptziel näher ist.

## Prüfungen

Vor Übergabe prüfen:

- Ist jede geplante Einheit terminierbar und vollständig dosiert?
- Sind harte Reize sinnvoll verteilt und Recovery-Zeiten plausibel?
- Passt die Prozentlast zum genannten 1RM/e1RM und ist die Rechenbasis dokumentiert?
- Enthält jede Schnellkraftübung ein Qualitäts-/Abbruchkriterium?
- Sind Progression und Deload/Taper regelbasiert statt nur kalenderbasiert?
- Stimmen Ausdauerzonen mit der verfügbaren Diagnostik überein?
- Wurde bei Verletzung/Symptomatik der Plan auf freigegebene Bewegungsmuster begrenzt?

## Sicherheitsgrenzen

- Der Skill ersetzt keine medizinische Untersuchung, Rehabilitationsfreigabe oder physiotherapeutische Befundung.
- Bei akuter Verletzung, zunehmender Schwellung, Blockierung, Wegknicken, Ruhe-/Nachtschmerz oder neurologischen/kardialen Warnzeichen keine aggressive Progression planen.
- Medizinische Quellenbefunde nicht umdiagnostizieren. Aus ihnen nur dokumentierte Einschränkungen und sichere Belastungsregeln in den Plan übernehmen.
- Bei älteren oder hoch belasteten Athleten technische Erfahrung, Recovery und vorherige Exposition berücksichtigen; Alter allein ist kein pauschaler Ausschlussgrund.

## Fehlerbehandlung

- **Kein Zieltermin:** einen offenen Block mit Re-Evaluation statt künstlichem Taper erzeugen.
- **Kein 1RM/e1RM:** RIR/RPE/Velocity steuern und Prozentfelder leer lassen.
- **Zu viele gewünschte Übungen:** auf Hauptbewegungen und Zielbeitrag reduzieren; redundante Zubehörarbeit entfernen.
- **Kollision mit Wasser-/Sporttraining:** zuerst Kraftvolumen oder Zubehör reduzieren, nicht automatisch den spezifischen Schlüsselreiz.
- **Symptomreaktion >24 h:** geplante Last/ROM/Volumen gemäß vorab definierter Ampel reduzieren und Re-Evaluation auslösen.

## Übergabe

Primärer Output ist `sport-training-plan.json`. Der Output kann direkt in `dr-komorowski-sport-report-renderer` überführt werden. Falls `sport-diagnostics.json` vorliegt, die verwendeten Schwellen/Arbeitswerte mit Herkunft referenzieren statt zu kopieren und neu zu interpretieren.

## Abschlusskriterien

Der Skill ist abgeschlossen, wenn jede geplante Woche konkrete, ausführbare Einheiten enthält, Intensität und Pausen eindeutig sind, Progressions-/Abbruchregeln definiert wurden, sportartspezifische Hauptreize geschützt sind und ein eigenständig verständliches `sport-training-plan.json` vorliegt.
