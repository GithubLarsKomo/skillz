---
name: suno-song-production-workflow
description: Entwickelt und iteriert Suno-Produktionen nach verpflichtendem progressivem Grilling v2: bestätigter Projekt-/Track-Intent, Referenzanalyse auf Craft-Ebene, Suno-fertige Title/Lyrics/Style-Pakete mit harten Feldlimits, modell- und versionsbewusste Generationsstrategie, Variantenreview, gezielte Revision, Album-Playlist/Cover-Abschluss, Provenienz und Second-Brain-Lernschleife. Verwenden bei Suno-Songs, Suno-Alben, Soundtrack-/Workout-/Trance-Projekten oder wenn ein vorhandener Song-Album-Workflow den generativen Produktionsschritt an Suno übergibt.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.3.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - round-based-requirements-grilling
  - project-second-brain
outputs:
  - suno-capability-snapshot.json
  - suno-track-package.md
  - suno-generation-review.json
  - suno-production-handoff.json
  - suno-model-learning.md
  - suno-album-playlist.md
  - suno-album-cover-asset.json
lastEvaluated: 2026-09-13
---

# Suno Song Production Workflow

## Zweck

Dieser Skill übernimmt den **Suno-spezifischen Produktionsloop** zwischen bestätigter künstlerischer Absicht und einem belastbaren Generations-/Edit-Handoff. Er ersetzt weder das übergeordnete `song-album-release-workflow`, noch Grilling, Creative-Writing-Revision, Audio-QC, Distribution oder Suno selbst.

Seine Kernfrage lautet:

> Ist aus einem in Grilling v2 bestätigten Projekt-/Track-Intent ein präzises, Suno-taugliches Produktionspaket entstanden, das reproduzierbar generiert, bewertet, gezielt verbessert und mit seinen Learnings dokumentiert werden kann?

Für **Albumprojekte** kommt eine zweite Abschlussfrage hinzu:

> Sind nach dem Track-Loop die finale Playlist und ein tatsächlich erzeugtes quadratisches Albumcover vorhanden und konsistent mit Albumtitel, Titelreihenfolge, Texten und Musik?

## Routing und Scope

### Als Teil eines Album-/Release-Workflows

Wenn `song-album-release-workflow` bereits einen gültigen Grilling-v2-Handoff, Albumvertrag, Albumarchitektur, Track-Funktion oder gefrorene Lyrics liefert, werden diese **konsumiert statt erneut erfunden**. Ein gültiger upstream Grilling-v2-Handoff wird wiederverwendet; derselbe Projektvertrag wird nicht noch einmal abgefragt.

Der Suno-Skill ändert keine bestätigte Albumdramaturgie oder Lyrics ohne dokumentierten Revisionsgrund.

### Als eigenständiger Suno-Lauf

Jedes neue Suno-Projekt beginnt mit progressivem **Grilling v2**. Auch für einen einzelnen Track wird der fachliche Intent zuerst bestätigt. Bei Folgeiteration eines bereits gegrillten Projekts wird der bestehende v2-Session-/Handoff-Stand fortgeführt; beantwortete Fragen werden nicht wiederholt.

Für ein fortlaufendes Projekt, eine EP oder ein Album wird anschließend `project-second-brain` verwendet und der Projektzustand im dafür festgelegten Repository fortgeführt.

Nicht stillschweigend aus einem Einzelsong ein Release-Projekt machen.

## Phase -1 — Progressive Grilling v2 Gate

### Harte Startbedingung

Vor Track-Brief, Referenzanalyse, Lyrics-/Style-Paket oder Generationsstrategie muss `round-based-requirements-grilling` mit der **DB-backed progressiven v2-Runtime** verwendet werden.

Vor Ausführung gelten die autoritativen Regeln aus `GithubLarsKomo/grilling` auf aktuellem `main`. Für neue Suno-Projekte ist die portable v2-Definition `examples/suno-song-production-intake-v2.json` der Standard-Intake, sofern kein bereits passender gültiger v2-Handoff existiert.

Das Grilling muss mindestens ausreichend klären:

- Projektform: einzelner Track, EP, Album, Untermalung/Soundtrack oder Experiment;
- Working Title und künstlerische Kernidee;
- primärer Hörkontext und gewünschte Wirkung;
- Sprache, instrumental/vokal und Vocal-Rolle;
- Ziel-Länge bzw. Längenband;
- Energie- und Arrangement-Arc;
- Referenzen auf Craft-Ebene und deren jeweilige Funktion;
- Lyrics-/Hook-Dichte und gewünschte Wiederholungsstrategie;
- gemeinsame Identität versus gewünschte Track-Variation;
- kommerzielle/private Nutzungsabsicht;
- harte musikalische, rechtliche und workflowbezogene Grenzen;
- messbare Erfolgskriterien des ersten Produktionsloops.

Bei Albumprojekten soll die visuelle Identität nur soweit mitgeklärt werden, wie sie bereits naheliegend ist. Ist die Coverrichtung am Ende des musikalischen Loops noch materiell offen, wird **nur dafür** eine fokussierte progressive Grilling-v2-Folgerunde verwendet.

### Progressive Semantik

- Kleine initiale Runde bevorzugen und nur bei verbleibender fachlicher Unsicherheit weitere v2-Runden erzeugen.
- Aktuellen `grilling-round-handoff` und `nextRoundContract` respektieren.
- Bereits beantwortete Fragen nicht wiederholen.
- Nach Reopen/Truncation keinen invalidierten downstream Handoff weiterverwenden.
- Technische Suno-Fakten wie aktuelle Modelle, native Maximaldauer oder Edit-Funktionen **nicht** im Grilling erraten; sie werden im Current Suno Capability Gate aktuell verifiziert.

### Wiederverwendung statt Doppel-Grilling

Ein neuer Grilling-Lauf ist **nicht** nötig, wenn ein gültiger projektbezogener v2-Handoff bereits alle für den konkreten Produktionsschritt relevanten Entscheidungen enthält. Dann wird nur offene fachliche Unsicherheit in einer progressiven Folgerunde geklärt.

### Second-Brain-Hook

Nach dem ersten gültigen projektbezogenen Grilling-Handoff:

1. bestehenden Project Second Brain fortführen oder initialisieren;
2. Grilling-Session-/Handoff-Referenz, bestätigte Entscheidungen, Nicht-Ziele und offene Punkte dokumentieren;
3. den resultierenden `projectMemory`-Verweis in Track- und Produktionshandoffs mitführen.

### Gate G0 — Intent Confirmed

Kein Suno-Prompt-Paket und keine Generationsstrategie, solange produktionsrelevante fachliche Unsicherheit im Grilling offen ist. Reines Reformatieren eines bereits bestätigten Suno-Pakets darf ohne erneutes Grilling erfolgen, verändert aber keine fachlichen Entscheidungen.

## Phase 0 — Current Suno Capability Gate

Suno ist volatil. Vor einem produktionsrelevanten Lauf aktuelle **offizielle** Suno-Quellen prüfen und `suno-capability-snapshot.json` erzeugen.

Mindestens erfassen:

- Datum der Prüfung;
- verfügbare Modelle und deren Rollen;
- maximale native Generationsdauer;
- relevante Edit-/Extend-/Replace-/Remix-Funktionen;
- Voice/Persona/Custom-Model-Funktionen, soweit relevant;
- verfügbare Advanced Controls;
- Plan-/Download-/Commercial-Use-Regeln, falls eine spätere externe Nutzung geplant ist;
- Quellen-URLs und Freshness.

Historische Modellgrenzen werden **nicht** als aktuelle Fakten übernommen. Ein Wechsel der Modellfamilie invalidiert alte Performance-Heuristiken bis zur Revalidierung.

### Gate A — Capability Snapshot Fresh

Kein modellabhängiger Produktionsrat ohne aktuellen Snapshot, wenn sich die Empfehlung durch Modellversion, Maximaldauer, Editierfunktionen oder Rechtebedingungen ändern kann.

## Phase 1 — Track Intent Contract

Aus dem bestätigten Grilling-Handoff und ggf. der Albumarchitektur wird pro Track der produktionsnahe Intent konkretisiert:

- Tracktitel oder Working Title;
- Funktion des Tracks im Album bzw. Hörkontext;
- Zielwirkung und Energieverlauf;
- Sprache / instrumental;
- Ziel-Länge;
- grober BPM-/Tempo-Bereich und Takt, falls relevant;
- Tonart/Modus, falls gewünscht;
- Stimme bzw. Vocal-Charakter;
- zentrale Hook-/Melodie-Funktion;
- Referenztracks oder Referenzeigenschaften;
- Nachbartrack-Differenzierung;
- harte Ausschlüsse;
- Rechte-/Voice-/Sample-Grenzen.

Offene Geschmacksfragen werden zurück in eine fokussierte progressive Grilling-v2-Folgerunde geroutet. Technische Suno-Fragen werden nicht durch unnötiges Grilling verlängert.

## Phase 2 — Reference Decomposition statt Artist Imitation

Referenzen sind Analyseinput, nicht Copy-Prompt.

Jeden Referenztrack auf beschreibbare Craft-Dimensionen zerlegen:

- Genre/Subgenre und Produktionsära;
- Tempo, Meter und Groove;
- Drum-Architektur;
- Bassbewegung;
- Harmonik, Tonart/Modus und Spannungsführung;
- Lead-/Synth-/Gitarren-/Orchesterfunktion;
- Hook- und Melodieverhalten;
- Vocal-Rolle, Register, Dichte und Verarbeitung;
- Arrangement: Intro, Build, Break, Drop, Chorus, Bridge, Outro;
- Dynamik/Energieverlauf;
- Sounddesign, Raum, Mix-Charakter;
- charakteristische, aber abstrahierbare Merkmale.

Bei mehreren Referenzen jeder Referenz eine Rolle geben, z. B. `rhythm`, `harmonic tension`, `drop architecture`, `vocal attitude`, statt alle Namen unstrukturiert in einen Stilprompt zu kippen.

Nicht übernehmen:

- fremde Lyrics;
- konkrete Melodien;
- ungeklärte Samples;
- nicht autorisierte Stimmen;
- direkte Aufforderungen, einen lebenden Künstler exakt nachzuahmen.

Ergebnis ist ein eigenständiger `style-vector`, kein Künstler-Klon.

## Phase 3 — Lyrics als musikalische Struktur

Lyrics werden nicht nur semantisch, sondern als **Zeit- und Arrangementmaterial** behandelt.

### Struktur-Tags

Soweit mit der aktuellen Suno-Version sinnvoll, klare Songstruktur verwenden, z. B.:

`[Intro]`, `[Verse]`, `[Pre-Chorus]`, `[Chorus]`, `[Breakdown]`, `[Build]`, `[Drop]`, `[Bridge]`, `[Outro]`.

Produktionsregie nicht überladen in das Lyrics-Feld schreiben. Lyrics bleiben singbar und strukturell lesbar.

### Repetition

Bei repetition-driven Dance-, Trance-, Hard-Trance-, Makina- oder Workout-Tracks darf Wiederholung **explizit ausgeschrieben** werden, wenn sie musikalisch idiomatisch ist. Ein wiederholter Hook-/Chorus-Block ist dann Teil des Arrangements, nicht künstliche Textstreckung.

Bei narrativen Songs dagegen keine Doppelung erzwingen, wenn dadurch Progression, Perspektive oder Punchline geschwächt werden.

### Duration Budget

Ziel-Länge nicht nur aus Wortzahl ableiten. Arrangement-Abschnitte und ungefähr benötigte musikalische Zeit planen. Für lange Dance-Tracks typischerweise Raum für Intro, ersten Aufbau, Hauptteil, Breakdown, zweiten Aufbau/Peak und Outro vorsehen.

## Phase 4 — Suno-Ready Prompt Contract

Das Standard-Handoff an den Nutzer folgt für **jeden Track immer** dieser Reihenfolge:

1. **Title**
2. **Lyrics**
3. **Style**
4. **Advanced controls** nur wenn aktuelle, tatsächlich relevante Suno-Regler oder Profile gezielt verwendet werden

### Harte Feldlimits

Vor jeder Ausgabe wird der finale, tatsächlich zu kopierende Text geprüft:

- **Lyrics: maximal 5000 Zeichen**;
- **Style: maximal 1000 Zeichen**.

Überschreitet ein Feld das Limit, wird es **vor der Ausgabe** gekürzt/verdichtet bzw. strukturell überarbeitet. Der Nutzer erhält kein überlanges Feld mit dem Hinweis, es selbst zu kürzen.

### Copy/Paste Contract

> **One real Suno input field = one dedicated copyable block.**

Das gilt für jede Suno-Ausgabe, nicht nur auf ausdrückliche Nachfrage oder auf Mobilgeräten.

- **Title, Lyrics und Style stehen immer in drei getrennten Kopierblöcken.**
- **Complete one track before starting the next.**
- **Put the field label outside the block.**
- In jedem Block steht nur der **exact text to paste into Suno**.
- **Do not make the user manually select a subsection** aus einem größeren Sammelblock.
- Keine leeren Platzhalterblöcke für nicht verwendete Suno-Felder.
- Kein separates Feld `Sonstiges`/`Misc`, wenn dessen Inhalt sinnvoll im Style- oder Advanced-Block aufgehoben ist.

Der vollständige normative Prompt-Vertrag liegt in [`references/suno-prompt-contract.md`](references/suno-prompt-contract.md).

### Style muss die produktionsrelevanten Angaben bündeln

Mindestens, soweit relevant:

- Genre/Subgenre und Ära;
- BPM / Meter;
- Tonart/Modus;
- **Target length**;
- Groove/Drums/Bass;
- Lead-/Instrumentenrollen;
- Arrangement Arc;
- **Vocals / Melody**;
- Production/Mix-Charakter;
- negative Constraints;
- Differenzierung zum Nachbartrack.

Tonart, Ziel-Länge sowie Vocals/Melody gehören in den Style-Block und werden nicht in ein loses Restfeld ausgelagert.

### Prompt-Kompaktheit

Bevorzugt einen dichten, widerspruchsfreien Stilvektor statt langer Prosa. Zu viele Genres, Epochen oder gegensätzliche Produktionsanweisungen werden vor Generierung reduziert.

### Gate B — Prompt Ready

PASS nur wenn:

- Title, Lyrics und Style in drei getrennten Kopierblöcken vorliegen;
- Lyrics <= 5000 Zeichen sind;
- Style <= 1000 Zeichen ist;
- Referenzen in Craft-Merkmale übersetzt sind;
- Lyrics/Struktur und Ziel-Länge zusammenpassen;
- Style keine offensichtlichen Widersprüche enthält;
- der Track im Album eine erkennbare eigene Funktion behält;
- keine Rechte-/Voice-/Sample-Grenze verletzt wird.

## Phase 5 — Model Routing

Modellwahl aus dem **aktuellen Capability Snapshot** ableiten.

Typische Rollen:

- schnelles Ideenscreening / große Variantenmenge;
- explorative, bewusst weniger vorhersehbare Klangsuche;
- präzise Finalisierung eines klaren Briefs;
- Custom Model / Voice / Style Persona für wiederkehrende Identität, wenn aktuell verfügbar und rechtlich/provenienzseitig sauber.

Modellnamen und Verfügbarkeiten niemals dauerhaft als unveränderliche Skill-Regel behandeln.

### Explore -> Select -> Refine

Bevorzugter Loop:

1. wenige gezielte Explorationsvarianten statt wahlloser Massengenerierung;
2. Kandidaten anhand Track-Funktion und Hörwirkung vergleichen;
3. stärksten Kandidaten auswählen;
4. nur die schwachen Dimensionen gezielt ändern;
5. Finalkandidaten erneut gegen Brief und Albumkontext prüfen.

Take 1 ist kein Default-Sieger.

## Phase 6 — Length Recovery Ladder

Wenn Suno deutlich kürzer generiert als beabsichtigt, nicht reflexartig Lyrics kürzen oder blind `Extend` verwenden.

In dieser Reihenfolge entscheiden:

1. **Native long regeneration** — wenn das aktuelle Modell die Ziel-Länge in einer Generation unterstützt: Style + Arrangement + ausgeschriebene Struktur auf Ziel-Länge optimieren und neu generieren.
2. **Genre-idiomatische Wiederholung** — bei Dance/Trance/Workout die tragenden Lyrics-/Hook-Blöcke bewusst wiederholen, wenn die bisherige Generierung trotz korrekter Ziel-Länge zu kurz bleibt.
3. **Targeted edit / Replace Section** — wenn nur ein Abschnitt fehlt oder falsch ist und aktuelle Editierfunktionen dies erlauben.
4. **Extend** — wenn der bestehende Kandidat musikalisch so stark ist, dass Kontinuität wichtiger ist als eine saubere Vollregeneration.
5. **Studio/DAW assembly** — für bewusst mehrteilige oder komplexe Langformen; Source-Parts verlustfrei halten und nach Assembly erneut Audio-QC durchführen.

Ein Nutzerfeedback wie „Extension ist unverhältnismäßig aufwändig“ wird als Workflow-Präferenz respektiert und verschiebt die Wahl zugunsten nativer Regeneration bzw. struktureller Wiederholung.

## Phase 7 — Candidate Review

Für jede relevante Generationsvariante `suno-generation-review.json` fortschreiben.

Mindestens bewerten:

- Track-Funktion / emotionale Wirkung;
- Style-Fit;
- Hook/Melodie;
- Arrangement Arc;
- tatsächliche Dauer vs. Ziel-Länge;
- Vocal-Charakter und Kontinuität;
- Lyrics-Treue / ausgelassene oder hallucinated Lines;
- technische Auffälligkeiten;
- Differenzierung zu Nachbartracks;
- Nutzerfeedback;
- Entscheidung: reject / keep-for-parts / candidate / selected.

Numerische Scores dürfen unterstützen, ersetzen aber keine hörbasierte Begründung.

### Targeted Revision Matrix

- **Musik stark, einzelne Lyric-Zeile falsch** -> gezielte Lyric-/Section-Edit-Funktion vor Vollregeneration.
- **Hook stark, Track zu kurz** -> Length Recovery Ladder.
- **Stimme driftet** -> aktuelles Voice/Persona/Custom-Model-Setup und Prompt-Konsistenz prüfen.
- **Track klingt zu ähnlich zum Nachbartrack** -> Arrangement/Instrumentation/Groove ändern, nicht zwangsläufig Persona oder Albumidentität.
- **Zwei Takes enthalten komplementär starke Teile** -> aktuelle Mashup-/Multi-source-Funktion oder verlustfreie externe Assembly nur mit sauberer Provenienz nutzen.

## Phase 8 — Rights and Provenance Capture

Vor einem kommerziellen Handoff dokumentieren:

- Suno-Modell und Versions-/Snapshot-Bezug;
- Erstellungsdatum;
- Plan-/Account-Kontext soweit für Rechte relevant;
- Download-/Commercial-Use-Status anhand aktueller offizieller Suno-Regeln;
- Lyrics-Urheberschaft;
- verwendete Audio-Uploads/Samples und Rechte daran;
- Voice/Persona/Custom-Model-Provenienz;
- externe Edits / Assembly;
- Source-Generation-IDs oder stabile Links, soweit verfügbar.

Keine kommerzielle Freigabe allein auf Basis historischer Suno-Regeln.

## Phase 9 — Project Second Brain Learning Loop

Nach einer sinnvollen Generationsrunde projektbezogene Beobachtungen in den Suno-Second-Brain schreiben.

Trenne strikt:

- **user preference** — was der Nutzer musikalisch/arbeitsmethodisch bevorzugt;
- **project observation** — was in diesem Song/Album passiert ist;
- **model behavior** — reproduzierbares Verhalten einer Suno-Modellversion;
- **cross-project learning** — mehrfach bestätigte, allgemeinere Regel.

Ein einzelner ungewöhnlicher Take wird nicht zur globalen Prompt-Regel erhoben.

Bei Modellwechsel werden ältere Learnings mit `revalidation_required` markiert, soweit sie modellabhängig sind.

Der normative Lernvertrag liegt in [`references/second-brain-learning-loop.md`](references/second-brain-learning-loop.md).

## Phase 10 — Production Handoff

Erzeuge `suno-production-handoff.json` mit:

- project / track ID;
- Grilling-v2-Handoff-/Session-Referenz;
- projectMemoryRef;
- selected prompt version;
- selected generation / source refs;
- model + capability snapshot ref;
- observed length;
- lyric/style deviations accepted or unresolved;
- rights/provenance status;
- external asset refs;
- open audio-QC items;
- next skill / next action.

Für einen Release-Workflow geht der Handoff zurück an `song-album-release-workflow` für vollständiges Audio-QC, Rights/Metadata und Distribution. Für Albumprojekte bleibt jedoch Phase 11 dieses Suno-Workflows verpflichtend.

## Phase 11 — Album Completion Contract

Diese Phase gilt für jedes Projekt mit `Projektform = Album`.

### 11.1 Finale Playlist

Sobald Albumtitel und Trackreihenfolge gefroren sind, `suno-album-playlist.md` erzeugen. Die Nutzer-Ausgabe enthält kompakt:

- den finalen **Albumtitel**;
- die **nummerierte Titelreihenfolge** in finaler Hörreihenfolge;
- exakt dieselben Tracktitel wie in den finalen Title-Kopierfeldern.

Ändert sich Albumtitel oder Reihenfolge, wird die Playlist neu erzeugt. Sie ist die kanonische menschenlesbare Albumsequenz.

### 11.2 Quadratisches Albumcover

Für jedes Album muss ein **tatsächliches Coverbild** erzeugt werden; ein Prompt oder Brief allein genügt nicht.

Harte Anforderungen:

- **1:1 / quadratisch**;
- Motiv und Atmosphäre müssen aus Texten, musikalischer Identität, emotionalem Album-Arc und bestätigtem Projektkontext ableitbar sein;
- kein beliebiges generisches Artwork als Lückenfüller;
- vorhandene Bildgenerierungsfähigkeit zur tatsächlichen Bilderzeugung verwenden;
- keine direkte Imitation eines lebenden visuellen Künstlers;
- keine ungeklärten fremden Assets;
- wenn die visuelle Richtung materiell offen ist: fokussierte Grilling-v2-Folgerunde nur zu diesen offenen Coverentscheidungen;
- wenn Grilling/Second Brain bereits eine ausreichend klare visuelle Richtung liefern: ohne unnötige Rückfrage erzeugen;
- ein bereits akzeptiertes, passendes quadratisches Cover derselben gefrorenen Albumversion wiederverwenden statt grundlos neu erzeugen.

Nicht-textuelle Coverdateien werden gemäß `project-second-brain` im dokumentierten externen Artifact Store gehalten. `suno-album-cover-asset.json` bzw. `ASSETS.md` referenziert mindestens Asset-Pfad/Link, Erstellungsdatum, Albumversion, Bildherkunft/Tool und Freigabestatus.

### Gate C — Album Package Complete

Für ein Album PASS nur wenn:

- finale Playlist vorhanden ist;
- Playlist Albumtitel und finale Reihenfolge korrekt widerspiegelt;
- alle Tracktitel mit den finalen Title-Blöcken übereinstimmen;
- ein tatsächlich erzeugtes quadratisches Cover vorhanden ist;
- das Cover inhaltlich zur Musik/Textwelt passt;
- Cover-Provenienz und Asset-Referenz dokumentiert sind.

## Second-Brain Storage Boundary

Textuelle Projektartefakte und Learnings gehören in das festgelegte Project-Memory-Repository. Audio, Stems, Cover und andere nicht-textuelle Produktionsdateien werden gemäß `project-second-brain` im dokumentierten externen Artifact Store gehalten und in `ASSETS.md` referenziert, sofern sie nicht für Build/Test/Runtime im Repository benötigt werden.

Keine Binärsammlung im GitHub-Second-Brain nur der Bequemlichkeit halber.

## Stop-Regeln

Blockierend:

- kein gültiger Grilling-v2-Handoff bzw. noch offene produktionsrelevante fachliche Unsicherheit bei einem neuen Suno-Projekt;
- kein ausreichend definierter Track-Brief;
- modellabhängige Empfehlung bei veraltetem/fehlendem Capability Snapshot;
- Lyrics > 5000 Zeichen im finalen Suno-Feld;
- Style > 1000 Zeichen im finalen Suno-Feld;
- Title/Lyrics/Style nicht in getrennten Kopierblöcken;
- ungeklärte oder nicht autorisierte Stimme/Samplequelle;
- direkter Künstler-Klon statt abstrahierter Craft-Spezifikation;
- kommerzieller Handoff mit ungeklärtem aktuellen Nutzungsrecht;
- behauptete externe Generierung ohne Evidenz;
- bei Albumprojekten: fehlende finale Playlist;
- bei Albumprojekten: fehlendes oder nicht quadratisches tatsächliches Coverbild.

Nicht automatisch blockierend:

- ein bereits gegrilltes Projekt wird nur in einer bestätigten Dimension iteriert;
- noch kein finaler WAV-Export vorhanden, solange nur ein Track-Prompt iteriert wird;
- Distribution ist noch nicht geplant;
- bei Nicht-Album-Projekten ist kein Cover vorgesehen;
- ein experimenteller Take bleibt als `keep-for-parts` erhalten.

## Abschluss

Der Skill endet, wenn:

1. ein gültiger Grilling-v2-Handoff den produktionsrelevanten Intent bestätigt;
2. Capability Snapshot aktuell genug ist;
3. jedes ausgegebene Suno-Track-Paket Title, Lyrics und Style in getrennten Kopierblöcken enthält;
4. Lyrics <= 5000 und Style <= 1000 Zeichen sind;
5. Generations-/Editentscheidungen und Nutzerfeedback nachvollziehbar bewertet sind;
6. der ausgewählte Kandidat samt Provenienz in `suno-production-handoff.json` festgehalten ist;
7. relevante Learnings im Project Second Brain stehen;
8. bei Albumprojekten finale Playlist und quadratisches, inhaltlich passendes erzeugtes Cover vorhanden und dokumentiert sind;
9. genau die nächste Aktion oder das nächste Workflow-Ziel benannt ist.
