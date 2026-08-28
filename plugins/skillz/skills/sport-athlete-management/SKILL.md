---
name: sport-athlete-management
description: Orchestriert den geschlossenen Sport-Trainingsregelkreis von Athletenprofil und Zielmodell über Saison-, Meso- und Mikroplanung zu Daily Monitoring, spezialisierten Kraft-/Ausdauer-/Recovery-/Fueling-/Health-, Psychologie- und Umweltmodulen und auditierbarer Adaptation. Verwenden für longitudinale Trainingssteuerung über mehrere Ebenen; Fachlogik der Spezialskills nicht duplizieren.
---

# Sport Athlete Management

Koordiniere die Sport-Skills als persistenten Regelkreis. Strukturierte Artefakte sind die fachliche Wahrheit; Reports und Web-UIs sind abgeleitete Ansichten.

## Trigger

Nutze diesen Orchestrator, wenn nicht nur ein einmaliger Trainingsplan, sondern fortlaufende Zielsetzung, Planung, tägliche Rückmeldung und Anpassung verlangt werden.

Für reine Testauswertung weiterhin `sport-performance-diagnostics`; für einen einmaligen Plan `sport-training-plan-workflow` verwenden. `sport-training-programming` bleibt nur als explizite Compatibility-Fassade für Legacy-Aufrufer erhalten.

## Voraussetzungen

Mindestens Athletenidentität und Ziel müssen bekannt sein. Für laufende Steuerung werden die jeweils aktuellen Versionen von Profil, Performance-Modell, Saison/Meso/Mikro, Monitoring, relevanten P1-Spezialartefakten, optionalen P2-Kontextartefakten und Adaptationsentscheidungen referenziert.

## Ablauf

1. **State laden.** Aktuelle IDs und Versionen der kanonischen Sport-Artefakte bestimmen.
2. **Fehlende Ebene routen.** Profil → Zielmodell → Saison → Meso → Mikro nur dort erzeugen, wo Zustand fehlt oder abgelaufen ist.
3. **P1-Fachmodule selektiv routen.** Je nach Ziel und Sessiontyp `sport-strength-power-programming` und/oder `sport-endurance-programming` verwenden; Recovery/Fueling/Testplanung nur bei fachlichem Bedarf aktualisieren.
4. **Health Routing priorisieren.** Dokumentierte Verletzung → `sport-injury-rehabilitation`; Rückkehr nach akuter Erkrankung → `sport-return-after-illness`. Diese Module erzeugen Kriterien und Grenzen, keine Diagnose oder medizinische Freigabe.
5. **P2-Kontextmodule selektiv routen.** Performance-Psychologie nur bei konkreter Performance-Frage, Musik nur bei gewünschter Nutzung, Umwelt/Reise nur bei realer Exposition. P2-Artefakte informieren den Kontext, verändern aber keinen Trainingsplan direkt.
6. **Mental-Health-Grenze prüfen.** Bei möglicher klinisch relevanter psychischer Belastung `sport-mental-health-routing` vor Performance-Psychologie verwenden. `urgent` verlässt normale Performance-Optimierung und priorisiert unmittelbares qualifiziertes Support-/Safety-Routing.
7. **Heute bestimmen.** Geplante Session, jüngsten Morning Check und relevante aktuelle Recovery-/Health-/P2-Kontextartefakte zusammenführen.
8. **Training protokollieren.** Completed Session und sRPE über `sport-daily-athlete-monitoring` erfassen.
9. **Trend analysieren.** Bei ausreichender longitudinaler Datenbasis `sport-adaptation-analysis` verwenden; Einzelmetriken nicht als Regler behandeln.
10. **Adaptation ausführen.** `sport-training-adaptation-engine` nur bei relevantem Checkpoint oder Mismatch aufrufen. P1-Spezialisten und P2-Kontextmodule liefern Evidenz, Grenzen und Optionen; die Engine besitzt die übergreifende Proceed/Modify/Recover/Review-Entscheidung.
11. **Versioniert revidieren.** Betroffene Fach- und Mikro-/Meso-/Saisonobjekte über ihre Eigentümer-Skills neu erzeugen; alte Version behalten. P2-Artefakte dürfen keine direkte Planmutation enthalten.
12. **State fortschreiben.** Nächste Entscheidung, offene Unsicherheiten, Safety Flags und nächste Re-Evaluation zusammenfassen.

## P1-Routingregeln

- **Kraft/Power:** `sport-strength-power-programming` besitzt Satz-/Wiederholungs-/Last-/RIR-/Power-Prescription. 50+ ist kein automatischer Grund, Power oder hohe Intensität zu entfernen.
- **Ausdauer:** `sport-endurance-programming` besitzt Intensitätsdomänen, Intervallstruktur und Pace/Power/HR-Regeln. HRV allein darf die Prescription nicht steuern.
- **Recovery:** `sport-recovery-sleep` interpretiert Schlaf, Fatigue und Kontext mehrdimensional und liefert keinen opaken Readiness-Score.
- **Fueling:** `sport-nutrition-fueling` unterstützt Leistungsversorgung und RED-S-Risikoerkennung für alle Geschlechter, ersetzt aber keine klinische Ernährungsmedizin.
- **Rehabilitation:** `sport-injury-rehabilitation` arbeitet nur auf dokumentierten medizinischen/physiotherapeutischen Constraints und kriteriumsorientiert, nicht kalenderbasiert.
- **Illness return:** `sport-return-after-illness` stoppt normale Progression bei kardio-pulmonalen/systemischen Red Flags und routet medizinische Abklärung.
- **Testing:** `sport-testing-battery` wählt minimale, entscheidungsrelevante Testbatterien nach Sport, Ziel und Saisonphase.
- **Longitudinale Analyse:** `sport-adaptation-analysis` trennt beobachtete Signale, Unsicherheit und Missing-Data-Effekte; ACWR ist kein kausaler Verletzungsprädiktor.

## P2-Routingregeln

- **Performance-Psychologie:** `sport-performance-psychology` besitzt Performance-Frage, trainierbare psychologische Fertigkeiten, Praxisdosis, Cues, Transfer und Monitoring. Der Skill diagnostiziert oder therapiert keine psychische Erkrankung.
- **Mental Health:** `sport-mental-health-routing` trennt Performance-Unterstützung von `monitor`, `professional_review` und `urgent`. Bei `urgent` darf Performance-Optimierung Safety-/Support-Routing nicht verzögern.
- **Trainingsmusik:** `sport-training-music` besitzt Präferenzen, Ausschlüsse, Zweck, Timing und Auswahlregeln. BPM ist höchstens deskriptiver Kontext und kein Ersatz für Power, Herzfrequenz, Pace oder RPE.
- **Umwelt/Reise:** `sport-environment-travel` trennt Hitze, Kälte, Höhe/Hypoxie, Travel Fatigue und Jetlag mechanistisch. Circadiane Planung, Akklimatisation und Umwelt-Safety werden nur bei tatsächlicher Exposition erzeugt.
- **Keine direkte Planmutation:** Kein P2-Artefakt besitzt `revised_plan`, `plan_patch` oder eine autonome Trainingsänderung. Änderungen laufen weiterhin über die zentrale Adaptationsentscheidung und die Eigentümer des betroffenen Plans.

## Systemgrenzen

Die WebApp und relationale Datenbank leben in einem separaten Produkt-Repository. `skillz` besitzt Fachlogik und JSON-Verträge, aber keine produktive Web-/DB-Implementierung. Die Produkt-App darf diese Verträge konsumieren und persistieren.

## Alters- und Geschlechtsregeln

Alle nachgelagerten Entscheidungen verwenden Alter und Geschlecht als Kontextmodifier. Individuelle Trainingsreaktion bleibt primär; keine pauschale Masters-Abwertung und keine starre Zyklusperiodisierung. Optionale menstruelle/peri-/postmenopausale Kontexte werden symptom- und evidenzbasiert behandelt. Psychologie, Musik und Umweltplanung verwenden keine demografischen Stereotype als automatische Controller.

## Prüfungen

- Ist jede Ebene über IDs/Versionen statt impliziten Chat-Kontext verbunden?
- Besitzt jede Fachentscheidung genau einen verantwortlichen Skill?
- Informieren P1-Spezialisten und P2-Kontextmodule die zentrale Adaptation, ohne deren Entscheidungslogik zu duplizieren?
- Bleibt Mental-Health-Routing klar von Performance-Psychologie getrennt?
- Kann `urgent` Performance-Optimierung explizit verlassen?
- Bleiben BPM, Alter, Geschlecht, HRV oder Umweltkontext Kontext statt magische Einzelregler?
- Sind Reports/UI nicht Source of Truth?
- Bleiben Audit Trail und Vorversionen erhalten?
- Können fehlende Daten ohne erfundene Werte weitergereicht werden?
- Werden Health/Medical/Mental-Health-Red-Flags vor Performance-Optimierung geroutet?

## Fehlerbehandlung

- **Unvollständiger State:** nur fehlende Ebene erzeugen und Abhängigkeiten erhalten.
- **Widersprüchliche Versionen:** keine stille Überschreibung; Konflikt als Reconciliation-Bedarf markieren.
- **Safety Red Flag:** Performance-Orchestrierung unterbrechen und Health/Medical/Mental-Health-Routing priorisieren.
- **P1-/P2-Artefakt fehlt:** nicht erfinden; Unsicherheit markieren und nur dann erzeugen, wenn die Entscheidung oder der reale Kontext es benötigt.
- **Psychische Belastung unklar:** keine Diagnose; konservativ an `sport-mental-health-routing` geben.
- **Produkt-App nicht verfügbar:** Fachartefakte bleiben als JSON unabhängig nutzbar.

## Übergabe

P0-Vertragsdefinition bleibt `schemas/sport-athlete-management-v1.schema.json`. P1-Spezialartefakte verwenden `schemas/sport-athlete-management-p1-v1.schema.json`. P2-Kontextartefakte verwenden `schemas/sport-athlete-management-p2-v1.schema.json`. Dadurch können Produktintegrationen jede Ebene bewusst und versioniert übernehmen. Das separate WebApp-Repository konsumiert diese Verträge über versionierte API-/Persistenzmodelle; Report-Workflows können dieselben Artefakte lesen.

## Abschlusskriterien

Der Orchestrator ist abgeschlossen, wenn der aktuelle Athlete-Management-State konsistent ist, die nächste Trainingsentscheidung eindeutig referenziert wird, erforderliche P1- und P2-Artefakte aktuell oder bewusst als fehlend markiert sind, Safety-/Mental-Health-Routing Vorrang behält, nötige Revisionen versioniert sind und keine Fachlogik aus Spezialskills dupliziert wurde.
