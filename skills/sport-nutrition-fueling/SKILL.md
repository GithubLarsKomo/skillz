---
name: sport-nutrition-fueling
description: Plant leistungsorientiertes Fueling, Proteinverteilung, Flüssigkeit und Wettkampfernährung und erkennt Hinweise auf niedrige Energieverfügbarkeit/RED-S. Verwenden für Trainings- und Wettkampfernährung; nicht als klinische Diätetik oder autonome Diagnose von RED-S.
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
lastEvaluated: 2026-08-22
---

# Sport Nutrition Fueling

Unterstütze Training und Regeneration durch belastungsabhängige Ernährung. Der Skill optimiert Fueling und erkennt Risikosignale; klinische Diagnostik und individuelle Therapie gehören zu qualifizierter Ernährungs-/Medizinbetreuung.

## Ablauf

1. **Belastungsbedarf erfassen.** Sport, Trainingsdauer/-intensität, Tagesdoppel, Wettkampf, Körpermassen-/Gewichtsziel und Umweltkontext strukturieren.
2. **Energieverfügbarkeit schützen.** Restriktion, unbeabsichtigter Gewichtsverlust, Leistungseinbruch, wiederkehrende Verletzung/Erkrankung und relevante hormonelle/menstruelle Hinweise als Risikosignale erfassen – bei allen Geschlechtern.
3. **Kohlenhydrate periodisieren.** Verfügbarkeit an Schlüsselreize und lange/harde Einheiten koppeln; nicht pauschal maximal oder minimal zuführen.
4. **Protein verteilen.** Tagesmenge und Mahlzeitenverteilung auf Trainings-/Regenerationsbedarf abstimmen; spezielle klinische Einschränkungen routen.
5. **Hydration individualisieren.** Dauer, Temperatur, Schweißverlust und praktische Verträglichkeit einbeziehen; Übertrinken vermeiden.
6. **Pre/during/post konkretisieren.** Timing, Menge als sinnvoller Bereich, Lebensmittel-/Getränkeoptionen und GI-Verträglichkeit angeben.
7. **Race fueling testen.** Wettkampfstrategie im Training erproben; keine neuen Produkte/hohen Mengen am Hauptwettkampf improvisieren.
8. **Risiko routen.** Bei RED-S-/Essstörungs-/medizinischen Warnsignalen keine reine Performance-Optimierung fortsetzen.

## Gewichtsmanagement

Keine aggressive Energierestriktion, Dehydrierung oder leistungsgefährdende Crash-Diät automatisieren. Körpergewicht ist nicht der alleinige Leistungsindikator. Bei Gewichtsänderungszielen werden Zeitraum, Trainingsqualität und Energieverfügbarkeitsrisiko gemeinsam betrachtet.

## Geschlecht und 50+

RED-S betrifft alle Geschlechter. Bei weiblichen Athleten können Menstruationsstörungen, Knochenkontext oder peri-/menopausale Symptome zusätzliche freiwillige Risikoinformation liefern. Bei 50+ sind Protein-/Krafttrainingskontext, Regeneration und ggf. Knochen-/medizinische Faktoren relevant, ohne pauschale Sonderdiät.

## Safety

Verdacht auf RED-S, Essstörung, relevante Gewichtsabnahme, persistierende GI-Probleme, Nieren-/Stoffwechselerkrankung oder andere klinische Risiken an Arzt bzw. qualifizierte Sporternährungsfachkraft übergeben.

## Übergabe

`sport-fueling-plan.json` enthält Belastungskontext, Tages-/Session-Fueling, Hydration, Proteinstrategie, Wettkampfpraxis und Re-Evaluation. `energy-availability-risk.json` enthält nur Risikosignale, Unsicherheit und Routing – keine autonome Diagnose.

## Evidenzanker

IOC RED-S 2023/2024 und etablierte Sporternährungs-Positionspapiere stützen individualisierte Energie-/Makronährstoffversorgung und klinisches Routing bei Risikosignalen.

## Abschlusskriterien

Fueling ist belastungsbezogen, praktisch testbar und sicher; Energieverfügbarkeitsrisiken bleiben geschlechtsunabhängig sichtbar.