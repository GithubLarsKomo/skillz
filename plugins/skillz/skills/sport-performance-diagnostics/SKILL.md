---
name: sport-performance-diagnostics
description: Wertet sportwissenschaftliche Leistungsdiagnostik wie Laktat-Stufentests, Ergometerdaten, Herzfrequenz, RPE und Erholung strukturiert aus und erzeugt belastbare Arbeitsbereiche mit Unsicherheiten statt Scheingenauigkeit. Verwenden, wenn Testdaten interpretiert, Schwellenmodelle verglichen oder Trainingszonen aus Messreihen abgeleitet werden sollen; nicht für eigenständige medizinische Diagnosen.
---

# Sport Performance Diagnostics

Verwandle rohe sportwissenschaftliche Testdaten in eine nachvollziehbare diagnostische Arbeitsunterlage. Trenne gemessene Werte, mathematische Interpolation, physiologische Interpretation und praktische Trainingsableitung sichtbar voneinander.

## Trigger

Nutze diesen Skill bei Anfragen wie:

- Laktat-Stufentest, Spiroergometrie-nahe Leistungsdaten oder Ergometertest auswerten,
- LT1/LT2, aeroben/anaeroben Umschlag oder Trainingszonen bestimmen,
- mehrere Schwellenmodelle vergleichen,
- Herzfrequenz, Leistung/Pace, Laktat, RPE und Erholung gemeinsam einordnen,
- einen strukturierten Befund für einen späteren Trainingsplan oder PDF-Report erzeugen.

Nicht auslösen, wenn ausschließlich ein bereits fertiger Befund gesetzt oder ein PDF ohne fachliche Neuauswertung gerendert werden soll.

## Voraussetzungen

Ermittle, soweit verfügbar:

- Sportart und Testmodalität,
- Stufendauer und Last-/Pace-Inkremente,
- Leistung/Pace je Stufe,
- Herzfrequenz je Stufe,
- Blutlaktat je Stufe samt Einheiten und Messzeitpunkt,
- RPE oder subjektive Belastung,
- Erholungsprobe(n) mit Zeitabstand,
- Abbruchgrund und Besonderheiten des Protokolls,
- relevante Trainingsziele und letzten Vergleichstest.

Fehlende Daten nicht erfinden. Eine unvollständige Messreihe darf ausgewertet werden, muss aber mit reduzierter Sicherheit gekennzeichnet werden.

## Ablauf

1. **Protokoll normalisieren.** Einheiten, Stufendauer, Reihenfolge, Nachbelastungsproben und Messfehler prüfen.
2. **Rohdaten sichern.** Gemessene Werte unverändert als Primärdaten führen; keine geglätteten Werte als Messwerte ausgeben.
3. **Kurvenverlauf beschreiben.** Baseline, erste nachhaltige Änderung, Steigungswechsel, hohe Laktatakkumulation und Recovery erfassen.
4. **Modelle rechnen.** Nur Modelle verwenden, deren Voraussetzungen zur Messreihe passen. Typische Kandidaten sind feste Laktatmarken, Dmax-Varianten, Delta-/Baseline-Kriterien und visuelle/segmentierte Umschläge. Rechenwerte mit Python/Calculator oder einem deterministischen Skript bestimmen, nicht im Kopf runden.
5. **Konvergenz bewerten.** Modelle nicht durch Mehrheitsentscheid vermischen. Erklären, welche Werte wegen Protokollauflösung oder Modellannahmen robust bzw. fragil sind.
6. **Arbeitsbereiche festlegen.** Praktische LT1-/LT2- oder Zonenwerte als Bereich und bevorzugten Arbeitswert ausgeben. Keine Ein-Watt- oder Ein-Schlag-Scheingenauigkeit, wenn Stufen grob sind.
7. **Erholung einordnen.** Laktat- und Herzfrequenzabfall relativ zum Messzeitpunkt beschreiben; keine klinische Aussage aus einem einzelnen Recovery-Punkt ableiten.
8. **Handoff erzeugen.** Ergebnis als `sport-diagnostics.json` mit Rohdatenreferenz, Modellergebnissen, Arbeitsbereichen, Unsicherheiten und Trainingsimplikationen strukturieren.

Empfohlenes Kernschema:

```json
{
  "protocol": {},
  "observations": [],
  "model_results": [],
  "working_thresholds": {
    "lt1": {"range": null, "working_value": null, "confidence": "low|medium|high"},
    "lt2": {"range": null, "working_value": null, "confidence": "low|medium|high"}
  },
  "training_implications": [],
  "uncertainties": [],
  "source_notes": []
}
```

## Prüfungen

Vor Übergabe prüfen:

- Stimmen Einheiten und Stufenreihenfolge?
- Ist jede Zahl entweder Messwert, explizite Rechnung oder klar gekennzeichnete Interpretation?
- Sind Interpolationen von tatsächlich gemessenen Punkten unterscheidbar?
- Passt die behauptete Präzision zur Stufenbreite und Testqualität?
- Werden Herzfrequenz, Laktat, Leistung/Pace und RPE gemeinsam statt isoliert betrachtet, sofern vorhanden?
- Sind Unsicherheiten und alternative plausible Schwellen sichtbar?
- Wurden aktuelle Primärquellen/Leitlinien herangezogen, wenn normative oder medizinisch relevante Aussagen erforderlich sind?

## Sicherheitsgrenzen

- Keine eigenständige medizinische Diagnose, keine ärztliche Freigabe und kein Ausschluss von Erkrankungen aus Sporttestdaten.
- Bei Synkope, Thoraxschmerz, auffälligen Rhythmusangaben, ungewöhnlicher Dyspnoe oder anderen medizinischen Warnzeichen Testinterpretation stoppen und medizinische Abklärung empfehlen.
- Bei MRT-, Verletzungs- oder Krankheitsbefunden nur die sportwissenschaftlich belastbare Konsequenz ableiten und medizinische Aussagen als Quelle vs. Interpretation trennen.
- Referenzwerte und Schwellenkonzepte sind sport-, protokoll- und populationsabhängig; aktuelle fachliche Quellen verwenden, wenn sie entscheidungsrelevant sind.

## Fehlerbehandlung

- **Fehlende Stufenwerte:** vorhandene Daten analysieren, Lücken markieren, keine künstliche Kurve erzeugen.
- **Widersprüchliche Einheiten:** vor Berechnung klären oder beide Lesarten als unaufgelösten Fehler ausweisen.
- **Ausreißer:** nicht automatisch löschen; Plausibilität, Messfehler und physiologische Erklärung getrennt diskutieren.
- **Zu grobe Stufung:** Schwellen als Bereich ausgeben und Auflösungsgrenze nennen.
- **Keine belastbare Schwelle:** ausdrücklich `not_resolved` melden statt einen Wert zu erzwingen.

## Übergabe

Primärer Output ist `sport-diagnostics.json`. Er kann direkt an `sport-training-programming` übergeben oder in einen Report-Spec für `dr-komorowski-sport-report-renderer` transformiert werden. Die Übergabe muss ohne zusätzlichen Gesprächskontext verständlich sein.

## Abschlusskriterien

Der Skill ist abgeschlossen, wenn Rohdaten und Protokoll konsistent erfasst, geeignete Modelle nachvollziehbar gerechnet, praktische Arbeitsbereiche mit Unsicherheit angegeben und ein eigenständig verständliches `sport-diagnostics.json` erzeugt wurden.
