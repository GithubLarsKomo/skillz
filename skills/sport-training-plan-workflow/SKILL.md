---
name: sport-training-plan-workflow
description: Orchestriert einen einmaligen ausführbaren Trainingsplan aus Athletenprofil, Ziel-/Performance-Modell, Saison-/Meso-/Mikroplanung und den spezialisierten Kraft-/Power- und Ausdauer-Prescriptions. Verwenden für konkrete Wochen-/Blockpläne ohne longitudinalen Athlete-Management-State; Fachlogik bleibt in den spezialisierten Sport-Skills.
userFacing: true
implicitInvocation: true
category: workflow
discoverability: public
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - sport-athlete-profile
  - sport-performance-diagnostics
  - sport-goal-performance-model
  - sport-season-periodization
  - sport-mesocycle-planning
  - sport-microcycle-planning
  - sport-strength-power-programming
  - sport-endurance-programming
consumes:
  - athlete-profile.json
  - sport-diagnostics.json
  - sport-performance-model.json
  - sport-season-plan.json
  - sport-mesocycle.json
  - sport-microcycle.json
  - strength-power-plan.json
  - endurance-plan.json
outputs:
  - sport-training-plan.json
lastEvaluated: 2026-08-28
---

# Sport Training Plan Workflow

## Zweck

Erzeuge einen **einmaligen kanonischen Trainingsplan**, ohne die Fachlogik der modernen Sport-Planungsschicht in einem Monolithen zu duplizieren. Das Zielmodell bestimmt die Prioritäten; Saison/Meso/Mikro bestimmen die zeitliche Struktur; Kraft/Power und Ausdauer besitzen ihre jeweilige Detail-Prescription.

Für longitudinale Steuerung mit Daily Monitoring und Adaptation weiterhin `sport-athlete-management` verwenden.

## Trigger

Nutze diesen Workflow für:

- konkrete Wochen- oder Blockplanung aus Ziel und Leistungsstand;
- Kraft-/Power- plus Ausdauerintegration mit sportartspezifischen Schlüsselreizen;
- kurze Peak-/Taperplanung vor einem Wettkampf;
- Ableitung eines Plans aus Diagnostik, Verfügbarkeit und Belastungsgrenzen;
- einen ausführbaren Plan, ohne einen persistenten Athlete-Management-State aufzubauen.

Nicht verwenden als medizinische Rehabilitationsfreigabe oder als Ersatz für longitudinale Adaptationssteuerung.

## Voraussetzungen

Mindestens erforderlich:

- Athletenprofil oder ausreichend Daten, um `sport-athlete-profile` zu erzeugen;
- Ziel, Zieltermin soweit bekannt und Sport-/Disziplinkontext;
- Trainingshistorie und reale Wochenverfügbarkeit;
- relevante Diagnostik/Leistungsreferenzen oder explizit markierte Unsicherheit;
- Equipment und Umgebungsbedingungen;
- dokumentierte Health-/Injury-Constraints.

Fehlende Schwellen oder 1RM/e1RM werden nicht erfunden. Ersatzsteuerung über RPE/RIR, Technik, Pace/Power-Bandbreiten oder konservative Referenzen bleibt als solche gekennzeichnet.

## Ablauf

1. **Profil fixieren.** `sport-athlete-profile` als Kontextbasis verwenden; vorhandene valide Profile referenzieren statt neu zu erfinden.
2. **Zielmodell erzeugen.** `sport-goal-performance-model` trennt Outcome-, Performance- und Prozessziele und priorisiert Limiter/KPIs.
3. **Planungshorizont wählen.** Bei Wettkampf-/Saisonbezug `sport-season-periodization` verwenden; bei kurzem Horizont darf die Saisonlogik einen reduzierten Makro-/Taperkontext liefern statt künstlicher Jahresplanung.
4. **Mesoziel festlegen.** `sport-mesocycle-planning` definiert Primäradaptation, Erhaltungsqualitäten, Lastkorridor sowie Entry-/Exit-Kriterien.
5. **Mikrozyklus bauen.** `sport-microcycle-planning` platziert Schlüsselreize, High/Low-Logik, Recovery-Abstände, Flexpunkte und Session-Slots.
6. **Kraft/Power spezialisieren.** Falls erforderlich `sport-strength-power-programming` für Übungen, Sätze, Wiederholungen, Last-/RIR-/RPE-Regeln, Pausen und Qualitäts-/Stop-Regeln verwenden.
7. **Ausdauer spezialisieren.** Falls erforderlich `sport-endurance-programming` für Intensitätsdomänen, Intervallstruktur, Pace/Power/HF/RPE-Ziele und Stop-/Anpassungsregeln verwenden. Verwendete Diagnostik bleibt referenziert.
8. **Interferenz reconciliieren.** Wenn Spezialprescriptions konkurrieren, entscheidet die Ziel-/Meso-/Mikro-Hierarchie über Platzierung und Priorität. Der Orchestrator erfindet keine dritte Fach-Prescription.
9. **Kanonischen Plan assemblieren.** `sport-training-plan.json` referenziert die Fachartefakte und enthält eine ausführbare, terminierbare Sicht auf Wochen/Sessions, Regeln, Unsicherheiten und Safety-Grenzen.
10. **Konsistenz-Gate.** Ziele, Zeitachsen, Zonen, Lasten, RIR/RPE, Stop-Regeln und Taperlogik gegen die referenzierten Fachartefakte prüfen.

## Output-Vertrag

`sport-training-plan.json` ist der einzige kanonische One-shot-Plan-Output dieses Workflows. Er enthält mindestens:

```json
{
  "profileRef": "athlete-profile.json",
  "performanceModelRef": "sport-performance-model.json",
  "seasonPlanRef": "sport-season-plan.json|reduced-context",
  "mesocycleRef": "sport-mesocycle.json",
  "microcycleRef": "sport-microcycle.json",
  "strengthPowerRef": "strength-power-plan.json|not_required",
  "enduranceRef": "endurance-plan.json|not_required",
  "weeks": [],
  "progressionRules": [],
  "taperRules": [],
  "safetyRules": [],
  "uncertainties": []
}
```

Die referenzierten Fachartefakte bleiben in Ownership ihrer Producer. Der Orchestrator darf ihre Werte nicht stillschweigend neu interpretieren.

## Prüfungen

Vor PASS prüfen:

- Ist jedes Plansegment auf Ziel-, Meso-/Mikro- oder Spezialartefakte zurückführbar?
- Sind Schlüsselreize und Recovery-Abstände plausibel und terminierbar?
- Enthält jede Detail-Prescription eine Quelle/Steuerungslogik statt erfundener Präzision?
- Bleiben Kraft/Power- und Ausdauer-Fachlogik bei ihren spezialisierten Skills?
- Werden Taper/Deload regelbasiert und zielbezogen angewendet?
- Sind Health-/Safety-Constraints erhalten?
- Gibt es genau einen Producer für `sport-training-plan.json`?

## Fehlerbehandlung

- **Kein Zieltermin:** offenen Entwicklungsblock mit Re-Evaluation erzeugen; keinen künstlichen Taper einbauen.
- **Diagnostik unzureichend:** konservative, explizit unsichere Steuerung verwenden und Retest-Bedarf markieren.
- **Zu wenig Trainingszeit:** sekundäre Reize reduzieren; Schlüsselreize nach Performance-Modell priorisieren.
- **Kraft/Ausdauer-Konflikt:** Mikrozyklus nach Primäradaptation neu ordnen statt beide Prescriptions zu verwässern.
- **Red Flag oder nicht freigegebene Bewegung:** aggressive Progression stoppen und geeignetes Health-/Medical-Routing priorisieren.
- **Widersprüchliche Fachartefakte:** keinen Hybridwert erfinden; zurück an den zuständigen Producer geben.

## Übergabe

Primärer Output ist `sport-training-plan.json`. Report-Workflows können diesen Plan konsumieren, ohne die Trainingslogik neu zu autorieren. Für fortlaufendes Monitoring und Planrevision wird an `sport-athlete-management` übergeben.

## Abschlusskriterien

Der Workflow ist abgeschlossen, wenn ein konsistenter, ausführbarer One-shot-Plan vorliegt, alle spezialisierten Prescriptions und Unsicherheiten referenziert bleiben, Schlüsselreize/Recovery geschützt sind, Safety-Grenzen erhalten wurden und `sport-training-plan.json` die einzige kanonische Trainingsplan-Ownership besitzt.
