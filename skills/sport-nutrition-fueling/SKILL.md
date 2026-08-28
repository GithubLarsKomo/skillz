---
name: sport-nutrition-fueling
description: Plant leistungsorientiertes Fueling, Proteinverteilung, Flüssigkeit und Wettkampfernährung und erkennt Hinweise auf niedrige Energieverfügbarkeit/RED-S unter Einbezug methodenbewusster Body-/Gewichtstrends. Verwenden für Trainings- und Wettkampfernährung; nicht als klinische Diätetik, autonome RED-S-Diagnose oder Interpretation proprietärer Metabolic-/Longevity-Scores.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - sport-athlete-profile
  - sport-mesocycle-planning
  - sport-microcycle-planning
  - sport-daily-athlete-monitoring
outputs:
  - sport-fueling-plan.json
  - energy-availability-risk.json
lastEvaluated: 2026-08-28
---

# Sport Nutrition Fueling

Unterstütze Training und Regeneration durch belastungsabhängige Ernährung. Der Skill optimiert Fueling und erkennt Risikosignale; klinische Diagnostik und individuelle Therapie gehören zu qualifizierter Ernährungs-/Medizinbetreuung.

## Ablauf

1. **Belastungsbedarf erfassen.** Sport, Trainingsdauer/-intensität, Tagesdoppel, Wettkampf, Körpermassen-/Gewichtsziel und Umweltkontext strukturieren.
2. **Body-/Messkontext prüfen.** Körpermasse, Taille und Body-Composition-Trends nur mit Methode, Gerät/Quelle, Qualitätsklasse und `comparable_series_id` interpretieren. BIA, DXA, Waage und Tape werden nicht still zusammengeführt.
3. **Energieverfügbarkeit schützen.** Restriktion, unbeabsichtigter methodenkompatibler Gewichtsverlust, Leistungseinbruch, Recovery-Verschlechterung, wiederkehrende Verletzung/Erkrankung und relevante hormonelle/menstruelle Hinweise als Risikosignale erfassen – bei allen Geschlechtern.
4. **Mehrsignalregel anwenden.** Körpergewicht oder BIA-Body-Fat allein begründen weder RED-S noch eine Fueling-/Trainingsintervention. Gewicht/Body-Composition werden mit Intake-/Fueling-Kontext, Trainingslast, Performance, Recovery, Symptomen und gegebenenfalls klinischen Informationen zusammen bewertet.
5. **Kohlenhydrate periodisieren.** Verfügbarkeit an Schlüsselreize und lange/harde Einheiten koppeln; nicht pauschal maximal oder minimal zuführen.
6. **Protein verteilen.** Tagesmenge und Mahlzeitenverteilung auf Trainings-/Regenerationsbedarf abstimmen; spezielle klinische Einschränkungen routen.
7. **Hydration individualisieren.** Dauer, Temperatur, Schweißverlust und praktische Verträglichkeit einbeziehen; Übertrinken vermeiden.
8. **Pre/during/post konkretisieren.** Timing, Menge als sinnvoller Bereich, Lebensmittel-/Getränkeoptionen und GI-Verträglichkeit angeben.
9. **Race fueling testen.** Wettkampfstrategie im Training erproben; keine neuen Produkte/hohen Mengen am Hauptwettkampf improvisieren.
10. **Risiko routen.** Bei RED-S-/Essstörungs-/medizinischen Warnsignalen keine reine Performance-Optimierung fortsetzen.

## Body Composition und Messmethoden

Consumer-BIA kann unter standardisierten Bedingungen als Trendkontext dienen, bleibt aber eine Schätzung. BIA-Fett-/Lean-Mass-Werte werden nicht als DXA-äquivalent behandelt; BIA-„bone density“ ist keine gemessene Bone Mineral Density. DXA- oder andere Referenzmessungen bleiben separate Serien und überschreiben Consumer-Schätzungen nicht.

Kurzfristige Gewichtsänderungen können Flüssigkeit, Glykogen, GI-Inhalt oder Messbedingungen widerspiegeln. Deshalb werden akute Schwankungen nicht automatisch als Änderung von Fettmasse oder Energieverfügbarkeit interpretiert.

## Gewichtsmanagement

Keine aggressive Energierestriktion, Dehydrierung oder leistungsgefährdende Crash-Diät automatisieren. Körpergewicht ist nicht der alleinige Leistungs- oder Gesundheitsindikator. Bei Gewichtsänderungszielen werden Zeitraum, Trainingsqualität, Recovery, methodenkompatible Trends und Energieverfügbarkeitsrisiko gemeinsam betrachtet.

## Provider-Scores

Biological Age, Pace of Aging, Lifespan-/„days gained“-Angaben, Metabolic Capacity/Momentum oder analoge Hume-/Vendor-Konstrukte sind keine validierten Energy-Availability- oder Fueling-Endpunkte und werden nicht als Risikobeleg verwendet. Garmin-/andere Provider-Scores können höchstens Kontext liefern, wenn ihre Provenance klar ist; direkte Signale und strukturierter Athletenkontext haben Vorrang.

## Geschlecht und 50+

RED-S betrifft alle Geschlechter. Bei weiblichen Athleten können Menstruationsstörungen, Knochenkontext oder peri-/menopausale Symptome zusätzliche freiwillige Risikoinformation liefern. Bei 50+ sind Protein-/Krafttrainingskontext, Regeneration und ggf. Knochen-/medizinische Faktoren relevant, ohne pauschale Sonderdiät.

## Safety

Verdacht auf RED-S, Essstörung, relevante Gewichtsabnahme, persistierende GI-Probleme, Nieren-/Stoffwechselerkrankung oder andere klinische Risiken an Arzt bzw. qualifizierte Sporternährungsfachkraft übergeben. Ein günstiger Fitness-/Recovery-/Metabolic-Score darf solche Signale nicht überstimmen.

## Übergabe

`sport-fueling-plan.json` enthält Belastungskontext, Tages-/Session-Fueling, Hydration, Proteinstrategie, Wettkampfpraxis und Re-Evaluation. `energy-availability-risk.json` enthält Risikosignale, einen methodenbewussten `body_energy_context`, Unsicherheit und Routing – keine autonome Diagnose.

## Evidenzanker

IOC RED-S 2023/2024 und etablierte Sporternährungs-Positionspapiere stützen individualisierte Energie-/Makronährstoffversorgung und klinisches Routing bei Risikosignalen. Consumer-Body-Composition-Daten werden methodenbewusst und primär longitudinal interpretiert.

## Abschlusskriterien

Fueling ist belastungsbezogen, praktisch testbar und sicher; Energieverfügbarkeitsrisiken bleiben geschlechtsunabhängig sichtbar, Body-/Gewichtstrends sind methodenbewusst und keine proprietäre Longevity-/Metabolic-Zahl wird als physiologischer Endpunkt missverstanden.
