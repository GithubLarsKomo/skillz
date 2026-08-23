# Speaking Writing — SPEC v1

Status: candidate implementation baseline
Date: 2026-08-23
Repository: `GithubLarsKomo/skillz`

## 1. Zweck

Skillz erhält einen komponierbaren Workflow für Reden und Vorträge. Beide Pfade teilen Grilling, Konzeptarbeit, Speaker Profile und die bestehende DE/EN-Precision-Writing-Kette. Der Vortragspfad ergänzt Storyline, Slide Architecture und optional die Arbeit mit einem vorhandenen PPT-Template oder einem erzeugten Designprofil.

Zielkette:

`grilling → concept → draft → precision language optimization → review → final`

Für Vorträge zusätzlich:

`concept → presentation draft → slide architecture → template/design handoff → presentation review`

## 2. Architekturprinzipien

1. **Konzept vor Text.** Kein vollständiges Manuskript unmittelbar aus unvollständigem Grilling erzeugen.
2. **Rede und Vortrag trennen.** Gemeinsame Logik wird geteilt, die Ausgabemedien bleiben eigenständig.
3. **Gesprochene Sprache ist kein Report.** Die bestehende Precision-Writing-Kette wird wiederverwendet, aber um `speech`, `speaker-notes` und `slide-copy` erweitert.
4. **Fidelity vor Wirkung.** Zahlen, Claims, Quellen, Negationen, Bedingungen, Modalität und Terminologie dürfen durch sprachliche oder rhetorische Optimierung nicht verändert werden.
5. **Speaker Voice nur evidenzbasiert.** Persönlichen Stil nur aus bestätigtem Speaker-/Author-Voice-Profil ableiten.
6. **Folien sind kein Manuskript.** On-Slide Copy und Speaker Notes werden getrennt optimiert.
7. **Template optional.** Vorhandene `.pptx`-Templates oder Referenzdecks werden genutzt; andernfalls wird ein Designprofil für den Presentation-Handoff erzeugt.

## 3. Skills

### 3.1 `speaking-grilling`

Erhebt mindestens Anlass, Kommunikationsziel, Zielgruppe, Vorwissen, erwartete Haltung/Widerstände, Sprecherrolle, Kernbotschaft, Dauer, Format, Sprache, Tonalität, Pflichtinhalte, Evidenzbedarf, sensible Themen, gewünschten Call-to-Action, Story-Material, Visual-/PPT-Bedarf und vorhandene Templates.

Output: `speaking-brief.json`.

### 3.2 `speaking-concept`

Transformiert Brief und belastbare Evidenz in ein freigabefähiges Konzept mit:

- Ziel und Audience Insight
- Kernthese
- 3–5 Supporting Messages
- Argumentations-/Dramaturgiebogen
- Opening
- Peak/entscheidender Moment
- Closing
- Call-to-Action
- Evidence Map
- Timing Budget
- Risiken/No-go-Aussagen

Output: `speaking-concept.json`.

### 3.3 `speaker-profile`

Erfasst sprecherbezogene Präferenzen getrennt nach Sprache und Kontext: Direktheit, technische Tiefe, Humor, Emotionalität, Satzlänge, rhetorische Dichte, bevorzugte/unerwünschte Muster, Aussprache-/Terminologiehinweise. Das Profil darf aus bestätigten Einstellungen oder authentischen Referenztexten entstehen, aber keine psychologischen Eigenschaften erfinden.

Output: `speaker-profile.json`.

### 3.4 `speech-writer`

Erzeugt aus `speaking-concept.json` ein Rede-Manuskript sowie optional eine performative Fassung mit `[PAUSE]`, Blick-/Betonungs- und Timing-Hinweisen. Unterstützte Profile sind u. a. Begrüßung, Festrede, Laudatio, Jubiläum, Abschied, Trauerrede, Motivation, Management-/Unternehmensansprache, Townhall, wissenschaftliche Eröffnung, politische Rede, Dankesrede, Dinner Speech und Keynote ohne Folien.

Output: `speech-draft.md` und optional `speech-script.md`.

### 3.5 `speech-review`

Bewertet Audience Fit, Core Message, Dramaturgie, Evidenz/Fidelity, Erinnerungswert, Sprechbarkeit, Authentizität, Timing, rhetorische Angemessenheit und Call-to-Action. Hard Fail bei sachlicher Verfälschung oder ungeklärtem Fidelity-Fehler.

Output: `speech-review.json` und finaler Text nach Korrekturschleife.

### 3.6 `presentation-writer`

Erzeugt die sprachlich-dramaturgische Vortragsfassung einschließlich Narrativ, Segmenten, Übergängen, Speaker Notes und Timing. Unterstützt Fach-/Wissenschaftsvortrag, Management-/Board-Präsentation, Sales/Pitch, Keynote, Schulung/Training und Webinar.

Output: `presentation-narrative.json` und `speaker-notes.md`.

### 3.7 `slide-architect`

Übersetzt das Konzept in Folien. Jede Folie besitzt mindestens `purpose`, `keyMessage`, `visualType`, `evidence`, `onSlideText`, `speakerMessage`, `transition` und `timeSeconds`. Default ist eine Kernaussage pro Folie. Der Skill verhindert das Muster "Headline + sechs Bullet Points", wenn eine bessere visuelle Form möglich ist.

Output: `slide-plan.json`.

### 3.8 `presentation-template`

Drei Modi:

- `template`: vorhandenes `.pptx`-Template analysieren und Layouts/Designsystem für den Handoff erfassen;
- `reference-deck`: Stil aus einer vorhandenen Präsentation abstrahieren;
- `design-profile`: ohne Vorlage ein Designbriefing erzeugen.

Output: `presentation-design-profile.json` beziehungsweise Template-Mapping.

### 3.9 `presentation-review`

Prüft Storyline, Message-per-Slide, Slide Density, Visual Storytelling, Daten-/Chart-Tauglichkeit, Speaker/Slide-Balance, Template-Konsistenz, Accessibility, Timing sowie sprachliche und sachliche Fidelity.

Output: `presentation-review.json` und freigegebener Presentation-Handoff.

## 4. Precision-Writing-Integration DE/EN

Die bestehenden Skills `llm-prose-pattern-audit`, `author-voice-profiler`, `precision-language-rewriter`, `rewrite-fidelity-verifier` und `precision-writing-revision` werden wiederverwendet.

Neue Genres:

- `speech`
- `speaker-notes`
- `slide-copy`

### 4.1 Rede

`speech-writer → precision-writing-revision(language=de|en, genre=speech, mode=light|author|editorial) → speech-review`

### 4.2 Vortrag

Zwei getrennte Optimierungspässe:

1. `slide-architect → precision-writing-revision(genre=slide-copy)`
2. `presentation-writer → precision-writing-revision(genre=speaker-notes)`

Danach gemeinsame Prüfung durch `presentation-review`.

### 4.3 Deutsch gesprochen

Zusätzlich zu den bestehenden deutschen Regeln:

- kurze, sprechbare Atem-/Sinneinheiten;
- Nebensatzketten reduzieren;
- aktive Verben und konkrete Bezüge bevorzugen;
- Verwaltungs- und Nominalstil vermeiden, Fachnomina erhalten;
- Semikolons vermeiden, Doppelpunkte selten, Gedankenstriche sparsam;
- bewusste Wiederholung und Rhythmus erhalten, wenn dramaturgisch begründet;
- Zahlen, Abkürzungen und Fachtermini akustisch verständlich einführen.

### 4.4 Englisch gesprochen

- idiomatische gesprochene Syntax;
- Kontraktionen je nach Register/Speaker Profile zulassen;
- inflated register, noun stacks und template transitions reduzieren;
- aktive konkrete Formulierungen bevorzugen;
- wissenschaftlich notwendiges Hedging erhalten;
- `international|us|uk` weiterhin respektieren.

### 4.5 Slide Copy

- assertion-style headline, wenn durch Evidenz gedeckt;
- eine Botschaft pro Folie;
- kurze scanbare Texte;
- Zahlen, Einheiten, Quellen und Terminologie schützen;
- komplexe Erklärung in Speaker Notes statt durch aggressive Kürzung verfälschen;
- generische Titel (`Overview`, `Key Takeaways`, `Zusammenfassung`) nur verwenden, wenn sie funktional sinnvoller als eine konkrete Aussage sind.

## 5. JSON-Verträge

### `speaking-brief.json`

```json
{
  "schemaVersion": 1,
  "type": "speech|presentation",
  "language": "de|en",
  "englishVariant": "international|us|uk|null",
  "occasion": "...",
  "objective": "...",
  "coreMessage": "...",
  "durationMinutes": 20,
  "audience": {
    "type": "expert|management|mixed|public",
    "size": 120,
    "knowledgeLevel": "...",
    "attitude": "..."
  },
  "speaker": {"role": "...", "profile": "speaker-profile.json|null"},
  "tone": [],
  "requiredContent": [],
  "evidenceRequirements": [],
  "sensitiveTopics": [],
  "callToAction": "...",
  "presentation": {"slides": true, "templateAvailable": false}
}
```

### `slide-plan.json`

```json
{
  "schemaVersion": 1,
  "slides": [
    {
      "number": 1,
      "purpose": "attention",
      "keyMessage": "...",
      "visualType": "photo|diagram|chart|table|quote|minimal-text",
      "evidence": [],
      "onSlideText": {"headline": "...", "body": []},
      "speakerMessage": "...",
      "transition": "...",
      "timeSeconds": 45
    }
  ]
}
```

## 6. Workflow

### Rede

`round-based-requirements-grilling → speaking-grilling → speaking-concept → speech-writer → precision-writing-revision[speech] → speech-review → final`

### Vortrag

`round-based-requirements-grilling → speaking-grilling → speaking-concept → presentation-writer → slide-architect → precision-writing-revision[speaker-notes + slide-copy] → presentation-template → presentation-review → presentation/PPT handoff`

Recherche-/Evidence-Skills können vor `speaking-concept` eingeschoben werden, wenn Aussagen externe Evidenz benötigen.

## 7. Qualitätsgates

- **SW-01:** Kein Draft ohne Kernbotschaft, Audience und Ziel; fehlende Informationen gehen zurück ins Grilling.
- **SW-02:** Timing-Budget muss zur angeforderten Dauer passen.
- **SW-03:** Faktische Claims werden vor Precision Rewrite per Fidelity Lock geschützt.
- **SW-04:** Gesprochene Sprache darf nicht auf formelle Report-Syntax normalisiert werden.
- **SW-05:** `slide-copy` und `speaker-notes` bleiben getrennte Artefakte.
- **SW-06:** Jede Folie besitzt eine klare kommunikative Funktion und Kernaussage.
- **SW-07:** Kein persönlicher Speaker-Stil ohne bestätigte Profilbasis.
- **SW-08:** Vorhandenes Template hat Vorrang vor neu erfundenem Designsystem, sofern es technisch nutzbar ist.
- **SW-09:** Rhetorik darf Evidenz, Unsicherheit und Compliance-Grenzen nicht übersteuern.
- **SW-10:** Finalisierung erst nach Sprach- und Fidelity-Gate.

## 8. Entscheidungsregister

- D-01: Gemeinsamer `speaking-concept`-Kern für Rede und Vortrag.
- D-02: Precision Writing wiederverwenden statt zweiten Sprach-Optimizer bauen.
- D-03: Precision Writing um `speech|speaker-notes|slide-copy` erweitern.
- D-04: On-Slide Copy und gesprochener Text werden separat optimiert.
- D-05: `speaker-profile` ergänzt Author Voice für performative Kommunikation.
- D-06: PPT-Template ist optionaler Input; ohne Template entsteht ein Designprofil.
- D-07: Fidelity bleibt auch bei rhetorischer Zuspitzung das höchste Qualitätsgate.

## 9. Sequenzierung

1. Precision-Writing-Genres erweitern.
2. `speaking-grilling` und `speaking-concept` implementieren.
3. `speaker-profile` implementieren.
4. Speech-Pfad implementieren.
5. Presentation-/Slide-Pfad implementieren.
6. Template-/PPT-Handoff ergänzen.
7. Capability-/Dependency-Artefakte mit bestehenden Repo-Generatoren aktualisieren.
8. Happy-Path-, Edge- und Failure-Evaluationen ergänzen.
