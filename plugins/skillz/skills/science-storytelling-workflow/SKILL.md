---
name: science-storytelling-workflow
description: Überführt belastbare wissenschaftliche Evidenz in eine narrative, für Nichtwissenschaftler verständliche Darstellung mit explizitem Audience Model, Explanation Model, Analogiegrenzen, Creative Workshop, Revision und abschließendem Fidelity-Recheck. Verwenden für populärwissenschaftliche Artikel, Buchkapitel, Essays oder erzählerische Erklärungen; keine wissenschaftlichen Claims zur Dramatisierung erfinden oder stärker darstellen als die Evidenz trägt.
---

# Science Storytelling Workflow

## Zweck

Mache Wissenschaft verständlich, ohne sie in eine falsche Geschichte zu verwandeln. Dieser Workflow verbindet Science Writing mit Creative-Writing-Handwerk, während `research-to-evidence-note` Eigentümer der wissenschaftlichen Claims bleibt.

## Eingänge

- bestätigtes Zielpublikum und gewünschte Wirkung;
- `evidence-note.json`;
- optional `mentor-craft-model.json`;
- gewünschtes Format und Länge.

## Audience Model

Vor dem Drafting fixieren:

- vermutetes Vorwissen;
- notwendige Begriffe;
- typische Fehlvorstellungen;
- gewünschte Tiefe;
- Motivation/Interesse;
- welche Details bewusst ausgelassen werden dürfen.

## Explanation Model

Für jedes schwierige Kernkonzept mindestens:

```json
{
  "concept": "...",
  "essentialUnderstanding": "...",
  "audienceAssumption": "...",
  "analogy": "...",
  "analogyWorksBecause": [],
  "analogyBreaksDownAt": [],
  "misconceptionRisk": [],
  "evidenceRefs": []
}
```

**Jede Analogie braucht eine dokumentierte Bruchkante.**

## Narrative Design

Definiere:

- zentrale Leserfrage;
- Reader Promise;
- narrative Bewegung;
- Reihenfolge der Erklärungen;
- konkrete Personen/Situationen nur soweit belegt oder klar fiktionalisiert;
- Spannungsquelle ohne künstliche Übertreibung;
- gewünschte Schlussfolgerung.

## Ablauf

1. Evidence Note und Audience Model fixieren.
2. Explanation Model erzeugen.
3. Optional Mentor-Craft-Muster als Mechanismen übernehmen.
4. Narrative Struktur entwerfen.
5. Draft schreiben.
6. `creative-writing-workshop` mit `mode=lay-reader-science` ausführen.
7. `creative-prose-revision` nur auf autorisierte Findings anwenden.
8. `precision-writing-revision` als finalen Fidelity-Recheck gegen Evidence Claims ausführen.
9. Bei Claim Drift zurück in Revision; nicht durch Umformulierung kaschieren.
10. `science-story.md` und Run Manifest ausgeben.

## Lay-Reader Gate

Der Cold Read rekonstruiert ausdrücklich:

- Was würde ein interessierter Nichtwissenschaftler nach dem Abschnitt vermutlich für wahr halten?
- Welche Kausalität würde er wiedergeben?
- Welche Analogie könnte er überdehnen?

Wenn diese Rekonstruktion dem Evidence-/Explanation-Modell widerspricht, gilt der Abschnitt als revisionspflichtig, auch wenn die Sätze leicht lesbar sind.

## Qualitätsgate

- **Verständlichkeit ohne Claim Drift.**
- Jeder fachlich relevante Satz bleibt auf Evidence Claims oder klar markierte Illustration zurückführbar.
- Analogiegrenzen sind intern dokumentiert und werden bei realem Missverständnisrisiko im Text sichtbar gemacht.
- Unsicherheit und Modalität werden nicht zugunsten einer stärkeren Pointe entfernt.
- Zahlen und Kausalitäten bleiben korrekt.
- Der finale Fidelity-Recheck muss `pass` sein.

## Output

`science-storytelling-run.json` enthält mindestens:

- evidenceRef;
- audience model version;
- explanation model version;
- workshop status;
- creative revision status;
- fidelity status;
- unresolved scientific questions;
- next delivery recommendation.

## Abschluss

Abgeschlossen, wenn ein verständlicher narrativer Text vorliegt, der den Lay-Reader-Test und den finalen wissenschaftlichen Fidelity-Recheck bestanden hat.
