# Spoken Language Profile

## Zweck

Dieses Profil ergänzt die allgemeine Precision-Writing-Logik um Regeln für Texte, die überwiegend gehört statt gelesen werden.

## Standardstil

Wenn der Grilling keinen anderen Stil festlegt, gilt:

- sachlich;
- technisch-wissenschaftlich klar;
- präzise;
- ruhig;
- erklärend;
- ohne werbliche, theatralische oder künstlich motivierende Tonlage.

Die Sprache richtet sich nach Inhalt und Zielgruppe. Juristische, steuerliche, wissenschaftliche oder technische Fachbegriffe bleiben erhalten, wenn sie für Präzision erforderlich sind.

## Deutsch

### Anglizismen

Englische Wörter nur verwenden, wenn mindestens eines gilt:

1. Der Begriff ist im deutschen Sprachalltag oder im relevanten Fachgebiet fest etabliert.
2. Eine Übersetzung wäre fachlich unpräzise oder ungewöhnlich.
3. Der englische Originalbegriff ist selbst Lerngegenstand.

Nicht etablierte Management- oder Beratungsanglizismen bevorzugt durch klares Deutsch ersetzen.

Beispiele:

- `take-away` -> `Kernaussage`
- `deep dive` -> `Vertiefung`
- `golden path` -> `bewährter Standardweg`
- `agenda setting` -> je nach Kontext `Prioritäten setzen` oder `Führungsagenda bestimmen`
- `trade-off` -> `Abwägung` oder `Zielkonflikt`
- `workflow` -> `Arbeitsablauf` oder `Prozess`, wenn `Workflow` nicht fachlich etabliert ist

Nicht künstlich eindeutschen:

- Software;
- Browser;
- Server;
- API in technischen Zielgruppen;
- Feedback, wenn es im Kontext natürlich ist;
- andere tatsächlich etablierte Fachbegriffe.

### Modelle mit englischen Originalbezeichnungen

Beim ersten Auftreten:

1. deutschen Sinn nennen;
2. englische Originalbezeichnung einmal nennen;
3. anschließend bevorzugt die deutsche Bezeichnung verwenden.

Beispiel:

`Der vierte Rollenwechsel ist der Übergang vom Ausführenden zum Gestalter von Strukturen. Watkins nennt ihn im Original "Bricklayer to Architect".`

Danach nicht fortlaufend `Bricklayer`, `Architect` oder `Shift` wiederholen.

### Hörbarkeit

- kurze bis mittellange Sätze bevorzugen;
- Pronomen nur verwenden, wenn der Bezug beim Hören eindeutig bleibt;
- Zahlen und Abkürzungen so formulieren, dass TTS sie verständlich wiedergibt;
- keine slash-lastigen Schreibweisen;
- keine Klammerketten;
- Listen sprachlich einführen;
- Kapitelanfänge mit einem klaren Orientierungssatz versehen;
- Kapitelenden mit einer knappen Schlussfolgerung oder Selbstprüfung versehen, wenn didaktisch sinnvoll.

## Englisch

Default ist amerikanisches Englisch.

- `englishVariant=us`;
- amerikanische Rechtschreibung und Idiomatik;
- klare technische oder wissenschaftliche Prosa;
- regionale oder umgangssprachliche Varianten nur bei explizitem Auftrag.

## Slang, Poesie und Regionalität

Nicht automatisch einsetzen.

Wenn im Grilling angefordert:

- Stilmerkmale als bewusste Anforderung behandeln;
- Verständlichkeit und fachliche Treue erhalten;
- Stimmenempfehlung an den Stil anpassen;
- falls keine geeignete Plattformstimme belastbar verfügbar ist, einen Voice-Design-Prompt liefern.

## Voice-Design-Prompt

Minimalstruktur:

```text
Native <language/variant>. <gender if desired>, approximately <age range>.
Studio-quality narration. Persona: <role>.
Voice: <timbre and register>.
Delivery: <pace, articulation, energy>.
Emotion: <baseline>.
Accent: <desired accent>.
Emphasize: <content-specific behavior>.
Avoid: <undesired traits>.
```

### Standardbeispiel Deutsch

```text
Native German, standard High German. Male, approximately 40-55.
Studio-quality narration. Persona: experienced technical and scientific instructor.
Voice: clear, warm baritone with precise articulation.
Delivery: measured medium pace, calm and focused, with natural pauses between conceptual sections.
Emotion: confident and intellectually engaged, but restrained.
Accent: no noticeable regional accent.
Emphasize definitions, causal relationships and key conclusions.
Avoid theatrical delivery, advertising tone, exaggerated emotion and rushed pacing.
```

### Standardbeispiel Englisch

```text
Native American English. Male, approximately 40-55.
Studio-quality narration. Persona: experienced scientific and technical instructor.
Voice: clear, warm baritone with precise articulation.
Delivery: measured medium pace, calm and focused, with natural pauses between conceptual sections.
Emotion: confident and intellectually engaged, but restrained.
Accent: neutral American.
Emphasize definitions, causal relationships and key conclusions.
Avoid theatrical delivery, advertising tone, exaggerated emotion and rushed pacing.
```
