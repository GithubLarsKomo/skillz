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
lastEvaluated: 2026-08-28
---

# Sport Nutrition Fueling

Unterstütze Training und Regeneration durch belastungsabhängige Ernährung. Der Skill optimiert Fueling und erkennt Risikosignale; klinische Diagnostik und individuelle Therapie gehören zu qualifizierter Ernährungs-/Medizinbetreuung.

## Ablauf

1. **Belastungsbedarf erfassen.** Sport, Trainingsdauer/-intensität, Tagesdoppel, Wettkampf, Körpermassen-/Gewichtsziel und Umweltkontext strukturieren.
2. **Body-/Energy-Kontext methodisch prüfen.** Körpergewicht, Taillenumfang und optionale Body-Composition-Daten nur als longitudinale, methodisch gekennzeichnete Serien verwenden. BIA, DXA und manuelle Maße nicht stillschweigend gleichsetzen.
3. **Energieverfügbarkeit schützen.** Restriktion, unbeabsichtigter Gewichtsverlust, Leistungseinbruch, persistente Recovery-/Health-Drift-Signale, wiederkehrende Verletzung/Erkrankung und relevante hormonelle/menstruelle Hinweise als Risikosignale erfassen – bei allen Geschlechtern.
4. **Kohlenhydrate periodisieren.** Verfügbarkeit an Schlüsselreize und lange/harde Einheiten koppeln; nicht pauschal maximal oder minimal zuführen.
5. **Protein verteilen.** Tagesmenge und Mahlzeitenverteilung auf Trainings-/Regenerationsbedarf abstimmen; spezielle klinische Einschränkungen routen.
6. **Hydration individualisieren.** Dauer, Temperatur, Schweißverlust und praktische Verträglichkeit einbeziehen; Übertrinken vermeiden.
7. **Pre/during/post konkretisieren.** Timing, Menge als sinnvoller Bereich, Lebensmittel-/Getränkeoptionen und GI-Verträglichkeit angeben.
8. **Race fueling testen.** Wettkampfstrategie im Training erproben; keine neuen Produkte/hohen Mengen am Hauptwettkampf improvisieren.
9. **Risiko routen.** Bei RED-S-/Essstörungs-/medizinischen Warnsignalen keine reine Performance-Optimierung fortsetzen.

## Body-Composition-Regeln

- Körpergewicht oder Körperfett allein diagnostizieren keine niedrige Energieverfügbarkeit.
- Schnelle Gewichtsänderung wird im Kontext von Training, Performance, subjektiver Recovery, physiologischer Stabilität und Fueling bewertet.
- Consumer-BIA ist eine Schätzung; DXA kann als Referenzserie separat geführt werden.
- Aus BIA abgeleitete „Knochendichte“ ist keine echte BMD-Messung und darf nicht für Bone-Health-Entscheidungen verwendet werden.
- Kein „Metabolic Age“, „Biological Age“ oder Longevity-Score wird als Ernährungsziel verwendet.

## Gewichtsmanagement

Keine aggressive Energierestriktion, Dehydrierung oder leistungsgefährdende Crash-Diät automatisieren. Körpergewicht ist nicht der alleinige Leistungsindikator. Bei Gewichtsänderungszielen werden Zeitraum, Trainingsqualität, Performance, Recovery und Energieverfügbarkeitsrisiko gemeinsam betrachtet.

## Geschlecht und 50+

RED-S betrifft alle Geschlechter. Bei weiblichen Athleten können Menstruationsstörungen, Knochenkontext oder peri-/menopausale Symptome zusätzliche freiwillige Risikoinformation liefern. Bei 50+ sind Protein-/Krafttrainingskontext, Regeneration und ggf. Knochen-/medizinische Faktoren relevant, ohne pauschale Sonderdiät.

## Safety

Verdacht auf RED-S, Essstörung, relevante Gewichtsabnahme, persistierende GI-Probleme, Nieren-/Stoffwechselerkrankung oder andere klinische Risiken an Arzt bzw. qualifizierte Sporternährungsfachkraft übergeben.

## Übergabe

`sport-fueling-plan.json` enthält Belastungs- und Body-/Energy-Kontext, Tages-/Session-Fueling, Hydration, Proteinstrategie, Wettkampfpraxis und Re-Evaluation. `energy-availability-risk.json` enthält nur Risikosignale, Unsicherheit und Routing – keine autonome Diagnose.

## Evidenzanker

IOC RED-S 2023/2024 und etablierte Sporternährungs-Positionspapiere stützen individualisierte Energie-/Makronährstoffversorgung und klinisches Routing bei Risikosignalen.

## Abschlusskriterien

Fueling ist belastungsbezogen, praktisch testbar und sicher; Body-Composition-Daten sind methodisch korrekt eingeordnet und Energieverfügbarkeitsrisiken bleiben geschlechtsunabhängig sichtbar.
