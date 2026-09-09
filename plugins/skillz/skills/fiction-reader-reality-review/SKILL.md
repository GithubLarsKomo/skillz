---
name: fiction-reader-reality-review
description: Prüft längere Fiction in einem strikt isolierten Reader-Reality-Pass, friert Leserrekonstruktion vor Architekturzugriff ein und vergleicht erst danach Leserwirkung mit Autor-/Story-Intention. Verwenden für vollständige Acts oder Romane, wenn Motivation, Figurenbögen, Agency, Ambiguität und emotionale Kausalität ohne internes Projektwissen belastbar sein müssen.
---

# Fiction Reader Reality Review

## Zweck

Prüfe die dritte Wahrheitsebene eines Romans: **Was rekonstruiert ein Leser tatsächlich aus dem Text, wenn er Story Bible, Plot-Architektur, Autorintention und frühere Reviews nicht kennt?**

Der Skill trennt zwingend:

1. Architektur-Wahrheit — was intern beabsichtigt oder kanonisch ist;
2. Text-Wahrheit — was auf der Seite steht;
3. Leser-Wahrheit — welches Modell ein unvorbereiteter Leser daraus bildet.

Architektur darf Reader-Wirkung nicht nachträglich wegdefinieren.

## Scope

Geeignet für:

- abgeschlossene Acts, wenn Figuren- oder Wirkungsrisiken früh geprüft werden sollen;
- vollständige Romane vor Publication Freeze;
- gezielte Wiederholung nach einer materiellen Revision, wenn ein früherer Reader-Gate-Status invalidiert wurde.

Nicht als Kapitel-Lektorat verwenden; dafür zuerst creative-writing-workshop.

## Harte Isolation

Vor dem Reader Freeze darf der isolierte Leser ausschließlich erhalten:

- ein Clean-Manuscript-Paket in Lesereihenfolge;
- minimale neutrale Metadaten, die ein normaler Leser ebenfalls hätte, z. B. Titel, Genre und Bandnummer;
- den Reader-Review-Auftrag.

Vor Freeze verboten:

- Story Bible;
- World/Character/Series Architecture;
- Plot- oder Beat-Sheets;
- Reveal Budgets;
- Draft Contracts;
- frühere Reviews;
- Autorintention;
- Project Second Brain;
- Commit-/Dateinamen oder Manuskript-Metadaten, die spätere Kapitel, Revisionen oder interne Funktionen verraten.

Wenn Isolation verletzt wurde, ist der Blind-Pass **invalid** und darf nicht als Reader-Evidence verwendet werden.

## Phase A — Clean Reader Packet

Erzeuge oder verifiziere ein neutrales Lesepaket:

- fortlaufende Kapitel;
- keine internen Review-Kommentare;
- keine Versionshinweise im Fließtext;
- keine Architektur- oder Reveal-Labels;
- keine Links auf Projektartefakte.

Dokumentiere exakt, welche Dateien/Abschnitte der Reader sehen durfte.

## Phase B — Reader-Only Reconstruction

Der Reader protokolliert aus dem Manuskript allein:

### Emotional Ledger

Kapitel-/Abschnittsweise:

- Was fühle/verstehe ich über die tragenden Figuren?
- Was änderte sich?
- Welche Beziehung wurde stärker, schwächer oder ambivalenter?
- Welche Entscheidung wirkte teuer oder folgenlos?
- Welche Frage will ich beantwortet sehen?
- Wo fehlt mir Motivation, Orientierung oder emotionaler Übergang?

### Character Reconstruction

Für jede tragende Figur:

- vermutete Vorgeschichte;
- Want;
- Fear/Avoidance;
- Werte und Grenzen;
- wiederkehrendes Verhaltensmuster;
- wahrgenommener Arc;
- eine konkret sichtbare kostspielige veränderte Entscheidung;
- offene Widersprüche;
- autonome versus rein funktionale Wirkung.

Zusätzlich:

- sekundäre Figuren-Agency;
- nichtmenschliche Agency, falls relevant;
- politische/moralische Stakes;
- absichtlich offene Rätsel versus verwirrende Auslassungen;
- wahrgenommene Buchschlussfähigkeit ohne Fortsetzung;
- Stellen, an denen sichtbare Konzeptarchitektur menschliche Wirkung überlagert.

## Phase C — Freeze

Vor jedem Architekturzugriff müssen die Reader-only-Artefakte unveränderlich referenzierbar eingefroren werden:

- `reader-emotional-ledger.json`;
- `reader-character-reconstruction.md`;
- Liste aller zugelassenen Reader-Inputs;
- Isolation-Status.

Der Freeze muss einen stabilen Referenzpunkt besitzen, z. B. Commit SHA oder unveränderlichen Artefakt-Hash.

**Keine nachträgliche Korrektur der Blind-Rekonstruktion nach Architekturzugriff.**

## Phase D — Intent Reconciliation

Erst nach Freeze werden Architektur und Intent geöffnet.

Vergleiche Finding für Finding:

- Leserrekonstruktion versus intended arc;
- reader-visible cause versus hidden author cause;
- bewusste Ambiguität versus unbeabsichtigte Unklarheit;
- Sequel Reserve versus vergessener Faden;
- Designentscheidung versus Manuskriptproblem;
- intern wahre Mechanik versus auf der Seite über- oder untererklärte Mechanik.

Disposition:

- `manuscript-problem`;
- `intentional-design`;
- `justified-by-page-evidence`;
- `architecture-overclaims-page`;
- `reader-misread-but-page-fair`;
- `defer-with-gate`.

Intent darf nur relativieren, wenn die **Seite selbst** genügend Evidenz liefert.

## Findings und Severity

- `critical`: zentrale Figur/Entscheidung/Schlussfunktion nur mit verborgenem Projektwissen verständlich oder Isolation ungültig;
- `major`: wichtige Motivation/Arc/Agency/Payoff auf der Seite nicht tragfähig;
- `minor`: lokale oder geschmacksabhängige Wirkung mit begrenzter Tragweite;
- `intentional`: bewusst offene oder ambivalente Wirkung, die aus dem Text als solche lesbar ist.

Publication Freeze ist bei offenem Critical/Major Reader-Reality-Finding blockiert.

## Output Contract

### reader-reality-review.json

Enthält:

- scope;
- cleanPacket;
- allowedInputs;
- forbiddenInputs;
- isolationStatus;
- freezeReference;
- readerFindings;
- readerModelSummary;
- nextGate.

### reader-vs-architecture-comparison.json

Enthält ausschließlich den **post-freeze** Vergleich mit:

- intendedFunction;
- frozenReaderEffect;
- match/divergence;
- evidenceOnPage;
- disposition;
- severity;
- gateImpact.

### reader-reality-gate.json

Enthält:

- isolationValid;
- criticalOpen;
- majorOpen;
- minorOpen;
- invalidatedByRevision;
- gateStatus `pass|pass-with-watchpoints|revise|invalid`.

## Qualitätsregeln

- **Reader vor Intent.**
- **Freeze vor Architektur.**
- Reader-Evidence wird nicht rückwirkend redigiert.
- Ein interner Plot-/Canon-Beweis ist kein Beweis dafür, dass Leser ihn wahrnehmen.
- Figurenänderung muss im Text durch Entscheidungen, Kosten oder Verhalten rekonstruierbar sein.
- Offene Mysterien sind erlaubt; unlesbare Motivation ist nicht automatisch Mystery.
- Clean-Manuscript-Pakete enthalten keine verräterische Projekt-Metasprache.
- Nach materieller Revision entscheidet creative-revision-regression, ob dieser Gate-Status weiter gültig ist.

## Abschluss

Abgeschlossen, wenn ein valider isolierter Reader-Pass eingefroren, erst danach mit Architektur verglichen und jeder relevante Divergenzbefund dispositioniert wurde.
