---
name: thought-to-concept-flow
description: Orchestriert die Klärung eines Ziels per Grilling, die fortlaufende Sammlung unstrukturierter Gedanken, deren semantische Graphanalyse und die Ableitung eines strukturierten Zielkonzepts mit optionalem Obsidian- oder Mermaid-Export. Verwenden, wenn aus einer wachsenden Gedankensammlung ein belastbarer Plan, Vortrag, eine Rede, ein Projekt-, Strategie- oder sonstiges Umsetzungskonzept entstehen soll.
userFacing: true
implicitInvocation: false
category: workflow
version: 0.2.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - round-based-requirements-grilling
  - thought-capture-journal
  - thought-graph-extractor
  - knowledge-map-generator
outputs:
  - thought-journal.json
  - thought-graph.json
  - concept.md
  - concept-handoff.json
  - optional Obsidian vault projection
  - optional Mermaid map
lastEvaluated: 2026-08-23
---

# Thought to Concept Flow

## Ziel

Verwandle eine zunächst ungeordnete, über Stunden, Tage oder Wochen entstehende Gedankensammlung in ein zielgerichtetes Konzept, ohne frühe Ideen vorschnell in eine starre Gliederung zu pressen.

Der Flow trennt bewusst vier Ebenen:

1. **Ziel klären** – Was soll erreicht werden?
2. **Gedanken sammeln** – Was fällt dazu ungefiltert ein?
3. **Bedeutungsgraph bilden** – Wie hängen Ziele, Ideen, Argumente, Risiken, Fragen und Aktionen zusammen?
4. **Konzept ableiten** – Welche Struktur ist zur Zielerreichung geeignet?

## Phase 0 – Zielstellung per Grilling

Nutze `round-based-requirements-grilling`, bevor eine finale Konzeptlogik festgelegt wird. Bei einfachen Fällen genügt eine kurze fokussierte Runde; bei komplexen Vorhaben mehrere Runden.

Das Grilling soll mindestens klären:

- gewünschtes Ergebnis/Wirkung,
- Zielgruppe oder Stakeholder,
- Artefakttyp: z. B. Vortrag, Rede, Projekt, Strategie, Entscheidungsvorlage, Artikel,
- Umfang, Termin und harte Randbedingungen,
- Qualitätsmaßstab: Woran wäre Erfolg erkennbar?,
- Nicht-Ziele und Tabus,
- vorhandenes Material und noch offene Wissenslücken.

Ergebnis ist ein bestätigter Zielrahmen aus `GRILL-REPORT.md`/`requirements-handoff.json`. Bereits beantwortete Fragen nicht erneut stellen.

## Phase 1 – Gedankensammlung einrichten

Nutze `thought-capture-journal`.

### iPhone / iOS: bevorzugter Standard

Empfehle auf dem iPhone **Apple Kurzbefehle + iOS-Diktat + eine einzelne Markdown-Datei**. Der Nutzer soll für einen neuen Gedanken nicht erst Obsidian oder eine Notiz-App strukturieren müssen, sondern einen Kurzbefehl wie **Gedanke festhalten** starten können.

Empfohlener Ablauf des Kurzbefehls:

1. Gedanken diktieren.
2. `Aktuelles Datum` lesen.
3. mit `Datum formatieren` auf `yyyy-MM-dd HH:mm` bringen.
4. `\n## <Datum>\n<Gedanke>\n` erzeugen.
5. an `Thought Journal.md` anhängen.

Bei Obsidian-Nutzung liegt die Datei bevorzugt direkt unter:

`iCloud Drive/Obsidian/<Vault>/00 Inbox/Thought Journal.md`

Damit ist die Erfassungsdatei bereits native Obsidian-Quelle und kann auf dem Desktop ohne Importkopie verarbeitet werden. Start des Kurzbefehls kann je nach Gerät über Siri, Home-Screen/Widget, Kontrollzentrum oder Aktionstaste erfolgen.

### Android

Empfehle **Markor QuickNote** als Standard: eine einzelne frei wählbare Markdown-Datei, offline, Open Source, ohne proprietären Datenlock-in. Für jeden neuen Gedanken wird per Date/Time-Aktion ein Zeitstempel eingefügt; der Inhalt kann per Android-Tastatur diktiert werden.

### Gemeinsame Minimalroutine

1. Capture-Aktion öffnen/starten.
2. Zeitstempel `yyyy-MM-dd HH:mm` erzeugen.
3. Gedanken diktieren oder tippen.
4. Keine Tags/Ordner/Struktur erzwingen.
5. Nächsten Gedanken später einfach an dieselbe Datei anhängen.

Die kanonische Capture-Datei heißt bevorzugt `Thought Journal.md`; `thoughts.md` oder `QuickNote.md` bleiben kompatibel.

## Phase 2 – Journal normalisieren

Importiere die einzelne Datei mit `thought-capture-journal` zu `thought-journal.json`. Rohtext und Zeitbezug bleiben erhalten.

Bei wiederholten Läufen nur neue/geänderte Einträge verarbeiten, sofern stabile IDs erhalten werden können. Historische Einträge nicht ohne Grund neu identifizieren.

## Phase 3 – Thought Graph erzeugen

Nutze `thought-graph-extractor`.

Der Graph muss mindestens unterscheiden können:

- Ziele,
- Ideen/Ansätze,
- Aussagen/Argumente,
- Constraints,
- Risiken,
- offene Fragen,
- Aktionen,
- Entscheidungen,
- Stakeholder,
- Themencluster.

Erhalte zeitliche Entwicklung, Widersprüche und Confidence. Ein häufiger oder sprachlich dominanter Gedanke ist nicht automatisch wichtiger als ein seltener, aber zielkritischer Gedanke.

## Phase 4 – Graph visualisieren

Der Nutzer kann einen oder beide Wege wählen:

### A. Obsidian Universe / Vault

1. Thought-Graph-Einheiten als `structured-knowledge-artifact` bereitstellen.
2. `knowledge-map-generator` für den provider-neutralen Graphen nutzen.
3. `obsidian-adapter` für Markdown-Notes und optional JSON Canvas nutzen.
4. Für eine Universe-/Graph-Ansicht einen neuen Vault oder einen klar abgegrenzten Vault-Ordner erzeugen.

Empfohlene Vault-Struktur:

```text
Thought-Universe/
  00 Goal/
  10 Themes/
  20 Ideas/
  30 Claims/
  40 Questions/
  50 Risks/
  60 Actions/
  70 Decisions/
  90 Sources/
  INDEX.md
```

Jede Note enthält stabile ID, Typ, SourceRefs, Confidence, Links zu verbundenen Nodes und relevante Originalzitate/Paraphrasen. Ordner dienen der Orientierung; Semantik kommt aus Metadaten und Relationen.

### B. Mermaid

Nutze `mermaid-knowledge-map-renderer` für eine portable Markdown-Darstellung. Bei großen Graphen zusätzlich eine reduzierte Themen-/Zielansicht erzeugen.

## Phase 5 – Konzept aus dem Graphen ableiten

Erzeuge `concept.md` **nicht** als bloße Zusammenfassung aller Gedanken. Das Konzept ist eine zielorientierte Auswahl und Anordnung.

### Gemeinsamer Konzeptkern

1. Ziel und Erfolgskriterien,
2. Zielgruppe/Stakeholder,
3. Kernthese oder Leitidee,
4. priorisierte Teilziele,
5. ausgewählte tragende Gedanken aus dem Graphen,
6. Abhängigkeiten und notwendige Reihenfolge,
7. offene Fragen/Entscheidungen,
8. Risiken/Gegenargumente und Umgang damit,
9. konkrete nächste Schritte,
10. verworfene oder bewusst zurückgestellte Gedanken mit Begründung.

### Artefaktspezifische Projektionen

**Vortrag:** Dramaturgie, Kernbotschaften, Publikumseffekt, Folien-/Visual-Ideen, Timing, Übergänge, Q&A.

**Rede:** Anlass, Publikum, gewünschte emotionale/inhaltliche Wirkung, roter Faden, Geschichten/Beispiele, Pointen, Schlussbild/Call-to-action.

**Projekt:** Outcome, Scope/Nicht-Scope, Workstreams, Deliverables, Abhängigkeiten, Meilensteine, Risiken, Entscheidungen, nächste Schritte.

**Strategie:** Ausgangslage, Zielbild, Optionen, Trade-offs, Auswahlkriterien, strategische Entscheidungen, Initiativen, Messgrößen.

Für andere Artefakttypen das gleiche Prinzip anwenden: Graphelemente werden nach ihrer Funktion für die Zielerreichung ausgewählt und geordnet.

## Phase 6 – Übergabe an spezialisierte Downstream-Skills

Wenn ein spezialisierter Skill für den Zielartefakttyp existiert, `concept.md` und `concept-handoff.json` an diesen übergeben, statt dessen Fachlogik zu duplizieren. Beispiele: Vortrags-/Redenschreiber, Projektplanung, Strategy Memo, Präsentationserstellung oder Sprachrevision.

Für deutsche oder englische finale Prosa nach Möglichkeit den vorhandenen präzisen Sprach-/Voice-Revisionspfad verwenden, sofern der Nutzer eine ausformulierte Fassung verlangt.

## concept-handoff.json

```json
{
  "schemaVersion": 1,
  "artifactType": "presentation|speech|project|strategy|other",
  "goalRef": "goal-001",
  "successCriteria": [],
  "selectedNodeIds": [],
  "deferredNodeIds": [],
  "openQuestionIds": [],
  "riskIds": [],
  "recommendedNextSkill": null
}
```

## Iteration

Der Flow ist ausdrücklich zyklisch:

`capture -> graph update -> concept update -> neue Gedanken -> graph update`.

Neue Gedanken dürfen das Konzept verändern. Frühere Entscheidungen werden aber nur dann zurückgenommen, wenn neue Evidenz/Widersprüche dies rechtfertigen oder der Nutzer sie ändert.

## Qualitätsgate

- Zielrahmen ist bestätigt oder klar als vorläufig markiert.
- Kein Gedanke geht beim Import verloren; Rohquelle bleibt erhalten.
- Graphbeziehungen besitzen SourceRefs, inferierte Beziehungen zusätzlich Confidence/Rationale.
- Obsidian-/Mermaid-Darstellung fügt keine neue Semantik hinzu.
- Konzept erklärt sichtbar, warum bestimmte Gedanken ausgewählt, priorisiert oder zurückgestellt wurden.
- Offene Fragen und Widersprüche bleiben sichtbar.
- Ergebnis enthält ausführbare nächste Schritte und einen geeigneten Downstream-Handoff.

## Abschluss

Der Flow ist abgeschlossen, wenn ein nachvollziehbarer Thought Graph und ein strukturiertes, auf die bestätigte Zielstellung ausgerichtetes `concept.md` vorliegen und der Nutzer entweder mit dem Konzept weiterarbeiten oder es direkt an einen spezialisierten Produktions-Skill übergeben kann.
