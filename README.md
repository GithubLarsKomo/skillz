# skillz

Zentrales, versioniertes Repository für wiederverwendbare, kleine und komponierbare Agent-Skills und Arbeitsabläufe.

## Struktur

Jeder Skill liegt in einem eigenen Verzeichnis unter `skills/` und besitzt mindestens eine `SKILL.md` mit YAML-Frontmatter:

```text
skills/
  <skill-name>/
    SKILL.md
    references/   # optionale vertiefende Regeln und Beispiele
    scripts/      # optionale deterministische Hilfsprogramme
    assets/       # optionale Vorlagen und Ressourcen
    tests/        # optionale Fixtures und Prüfungen
```

Nur tatsächlich benötigte Unterverzeichnisse werden angelegt. Die übergreifende Zielarchitektur ist in [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) beschrieben; geplante Erweiterungen stehen in [`docs/ROADMAP.md`](docs/ROADMAP.md).

## Enthaltene Skills

<!-- skill-catalog:start -->
| Skill | Zweck |
|---|---|
| [`agent-handoff`](skills/agent-handoff/SKILL.md) | Erzeugt einen kompakten, verifizierbaren Übergabestand für neue Sitzungen oder Agenten. Verwenden, wenn Ziel, Repositoryzustand, Entscheidungen, Evidenz, Restrisiken, blockierte Punkte und genau die nächste ausführbare Aktion ohne Informationsverlust oder doppelte Arbeit weitergegeben werden müssen. |
| [`architecture-deepening-review`](skills/architecture-deepening-review/SKILL.md) | Prüft bestehende Softwarearchitekturen evidenzbasiert auf flache Modulgrenzen, unbeabsichtigte Kopplung, duplizierte Domänenregeln und Infrastrukturleckage und empfiehlt höchstens einen kleinen, hochwirksamen Vertiefungsschritt. Verwenden, wenn Architekturqualität verbessert werden soll, ohne einen spekulativen Rewrite oder stilgetriebene Schichten einzuführen. |
| [`central-skill-repository-curation`](skills/central-skill-repository-curation/SKILL.md) | Konsolidiert wiederverwendbare Arbeitsabläufe als persönliche Skills, pflegt deren portable Fassungen im zentralen Repository GithubLarsKomo/skillz und synchronisiert beide Bestände sicher. Verwenden, wenn der Nutzer Skills lernen, zentral speichern, installieren, inventarisieren, abgleichen oder ausdrücklich in beide Richtungen synchronisieren lassen möchte. |
| [`communication-memory-governance`](skills/communication-memory-governance/SKILL.md) | Verwaltet stabile Kommunikationspräferenzen und bestätigte Langzeit-Memory-Einträge getrennt von transientem Gesprächs-, Projekt- und Agentenzustand. Verwenden, wenn wiederkehrende User-Präferenzen, dauerhafte Fakten oder Korrekturen nachvollziehbar, scope-begrenzt und datenschutzsicher über Sitzungen hinweg verfügbar bleiben sollen, ohne Agent-Handoff, Decision Records oder Projektstatus zu duplizieren. |
| [`composable-skill-factory`](skills/composable-skill-factory/SKILL.md) | Entwirft, prüft und veröffentlicht kleine, komponierbare Agent-Skills mit progressiver Offenlegung, deterministischen Hilfswerkzeugen, klaren Triggern und überprüfbaren Abschlusskriterien. Verwenden, wenn aus einem wiederholbaren Workflow ein neuer Skill werden soll oder ein bestehender Skill zu groß, unklar, fragil oder schwer kombinierbar ist. |
| [`conversation-to-spec`](skills/conversation-to-spec/SKILL.md) | Verdichtet bestätigten Gesprächs-, Grilling- und Repository-Kontext zu einer umsetzbaren, prüfbaren Spezifikation, ohne bereits beantwortete Fragen erneut zu stellen. Verwenden, wenn aus freigegebenen Festlegungen eine SPEC.md, ein technischer Umsetzungsrahmen oder eine belastbare Übergabe an Engineering entstehen soll. |
| [`daily-and-weekly-review`](skills/daily-and-weekly-review/SKILL.md) | Verdichtet bestätigte Kalender-, Aufgaben-, Projekt- und Inbox-Triage-Daten zu einem priorisierten Tages- oder Wochenreview mit Commitments, Follow-ups, Blockern und nächsten Schritten. Verwenden, wenn aus mehreren Arbeitskontexten eine belastbare Review-Sicht entstehen soll, ohne Kalender-, Mail-, Task- oder Projekt-Systeme selbst zu verändern. |
| [`decision-and-follow-up-tracker`](skills/decision-and-follow-up-tracker/SKILL.md) | Konsolidiert bestätigte Entscheidungen, Commitments, Follow-ups, Waiting- und Delegationszustände aus Meeting-, Projekt- und Review-Artefakten zu einem auditierten Register. Verwenden, wenn offene Schleifen und Entscheidungspflichten über mehrere Arbeitskontexte hinweg nachvollziehbar gehalten werden sollen, ohne Task-, Kalender-, Mail- oder Issue-Systeme selbst zu verändern. |
| [`decision-record`](skills/decision-record/SKILL.md) | Erfasst wesentliche technische und fachliche Entscheidungen als unveränderliche, nachvollziehbare Records mit Kontext, Alternativen, Evidenz, Autorität, Folgen, Risiken und Ablösungspfad. |
| [`deferred-external-action-verification`](skills/deferred-external-action-verification/SKILL.md) | Richtet für asynchron arbeitende externe Programme, APIs und CI/CD-Systeme eine zeitversetzte, wiederholbare Ergebnisprüfung per Cronjob oder gleichwertigem Scheduler ein. Nimmt jeden vom Agenten selbst ausgelösten CI-Lauf automatisch in eine Beobachtungsliste auf und setzt den gespeicherten Arbeitsablauf nach verifiziertem Erfolg fort. Der Skill definiert Wartefenster, Statusabfrage, Idempotenz, Sperren, Retry- und Abbruchregeln, Protokollierung sowie die sichere Aufräumlogik nach Erfolg oder endgültigem Fehler. |
| [`disciplined-diagnosis`](skills/disciplined-diagnosis/SKILL.md) | Diagnostiziert Softwarefehler reproduzierbar und evidenzbasiert, minimiert den Fehlerraum, prüft konkurrierende Hypothesen, implementiert den kleinsten sicheren Fix und belegt ihn mit Regressionstest sowie ursprünglicher Verifikation. Verwenden, wenn CI, Tests, Laufzeitverhalten oder Integrationen fehlschlagen und spekulative Änderungen vermieden werden sollen. |
| [`domain-model-maintenance`](skills/domain-model-maintenance/SKILL.md) | Hält Domänenbegriffe, Invarianten, Zustände, Grenzen und Repräsentationen während Softwareänderungen konsistent und steuert kompatible Migrationen über Code, Persistenz, APIs, Events, Tests und Dokumentation. |
| [`implement-from-issue`](skills/implement-from-issue/SKILL.md) | Implementiert ein klar abgegrenztes Repository-Issue vom verifizierten Ausgangszustand bis zu einem überprüfbaren Commit- oder Pull-Request-Stand mit vollständiger Rückverfolgbarkeit, Testevidenz, Sicherheits- und Migrationsbewertung sowie expliziter externer Nachverifikation. Verwenden, wenn ein umsetzungsreifes Issue sicher und ohne Scope-Ausweitung ausgeführt werden soll. |
| [`inbox-action-triage`](skills/inbox-action-triage/SKILL.md) | Klassifiziert eine abgegrenzte Menge bereits geladener Nachrichten nach Dringlichkeit und Handlungsbedarf und leitet überprüfbare nächste Aktionen ab. Verwenden, wenn Inbox-Nachrichten in urgent, reply-soon, waiting, delegated, FYI/archive oder needs-context geordnet werden sollen, ohne Gmail-/Outlook-Connectorlogik oder Mailbox-Mutationen zu duplizieren. |
| [`iterate-software-projects`](skills/iterate-software-projects/SKILL.md) | Iterative Weiterentwicklung bestehender Softwareprojekte durch den wiederkehrenden Zyklus aus Bestandsanalyse, Klärung kritischer Produktentscheidungen, Auswahl des nächsten kleinen Inkrements, präzisem Copilot- oder Coding-Agent-Prompt und evidenzbasiertem Review. Verwenden, wenn ein Repository schrittweise fortgeführt, ein Plan vor der Umsetzung geschärft, ein nächster Implementierungsauftrag formuliert, ein Agentenergebnis geprüft, ein Docker-/KI-Service diagnostiziert oder nach einem Review die nächste Iteration geplant werden soll. |
| [`knowledge-map-generator`](skills/knowledge-map-generator/SKILL.md) | Projiziert vorhandene strukturierte Wissensartefakte und explizite Relationen in einen provider-neutralen Graphen aus Nodes, Edges und optionalen Groups. Verwenden, wenn Projekt-, Architektur-, Decision-, Domain- oder Memory-Zusammenhänge visualisiert oder an JSON Canvas, Mermaid, Graphviz, Neo4j oder andere Renderer übergeben werden sollen; der Skill erfindet keine fehlenden Beziehungen. |
| [`knowledge-view`](skills/knowledge-view/SKILL.md) | Erzeugt deterministische, schreibgeschützte Sichten auf strukturierte Wissensartefakte anhand expliziter Filter, Sortierungen, Gruppierungen und abgeleiteter Felder. Verwenden, wenn aktive Entscheidungen, offene Fragen, Memory-Einträge, Projektartefakte oder andere Knowledge Artifacts selektiv als Kontext oder Übersicht projiziert werden sollen; verändert weder Quellen noch löst der Skill Konflikte. |
| [`large-work-wayfinder`](skills/large-work-wayfinder/SKILL.md) | Erschließt große, unklare oder schlecht abgegrenzte Engineering-Vorhaben durch evidenzbasierte Exploration, fokussierte Untersuchungs-Issues, Abhängigkeitsgraphen, Risikoreduktion und eine sichere Umsetzungsreihenfolge, ohne spekulative Architekturentscheidungen vorwegzunehmen. |
| [`meeting-preparation`](skills/meeting-preparation/SKILL.md) | Verdichtet einen bestätigten Termin, Teilnehmerkontext und verfügbare Evidence Notes zu einem kompakten, entscheidungsorientierten Meeting-Prep-Brief. Verwenden, wenn vor einem Meeting Ziele, Entscheidungen, belegte Fakten, offene Fragen, Risiken und konkrete Vorbereitung strukturiert werden sollen, ohne Kalender-, Kontakt-, Dokument- oder Retrieval-Logik zu duplizieren. |
| [`memory-sync-reconciliation`](skills/memory-sync-reconciliation/SKILL.md) | Gleicht mehrere bereits governance-konforme Kommunikationsprofile und Memory-Ledger deterministisch ab, propagiert Forget/Supersession/Expiry sicher und legt echte Konflikte zur Auflösung vor. Verwenden, wenn Memory-Stände aus unterschiedlichen Sitzungen, Clients oder Persistenzkanälen konvergieren sollen, ohne neue Memories zu erfinden. |
| [`merge-conflict-resolution`](skills/merge-conflict-resolution/SKILL.md) | Löst Git-Merge-Konflikte semantisch, rekonstruiert die Änderungsabsichten beider Seiten, bewahrt akzeptiertes Verhalten und Repository-Invarianten und erzeugt einen überprüfbaren Auflösungsstand mit Tests, Rollback und Restrisiken. Verwenden, wenn Konfliktmarker allein nicht zeigen, welche fachliche oder technische Kombination korrekt ist. |
| [`opaque-system-analysis`](skills/opaque-system-analysis/SKILL.md) | Rekonstruiert das kleinste evidenzbasierte Verhaltens- und Schnittstellenmodell eines opaken oder unzureichend dokumentierten Systems, Artefakts, Protokolls oder Dateiformats, wenn Quellcode oder belastbare Dokumentation für die nächste Engineering-Entscheidung nicht ausreichen. Verwenden, bevor Diagnose oder Implementierung beginnt, wenn erst beobachtbares Verhalten, Zustände, Inputs, Outputs oder Verträge erschlossen werden müssen; nicht für Exploit-Entwicklung, allgemeine Fehlersuche mit ausreichender Sichtbarkeit oder breite Projektplanung. |
| [`openasr-offline-model-import`](skills/openasr-offline-model-import/SKILL.md) | Importiert ein bereits lokal vorhandenes OpenASR-Modell unter Windows robust in OpenASR Desktop, insbesondere wenn der signierte Online-Katalog wegen Proxy-, TLS- oder UnknownIssuer-Problemen nicht verwendet werden kann. |
| [`project-beta-readiness`](skills/project-beta-readiness/SKILL.md) | Bewertet genau ein Softwareprojekt evidenzbasiert auf den Weg zur ersten nutzbaren Beta, quantifiziert den Reifegrad, benennt Beta-Blocker und erzeugt bei erreichter Beta einen Betriebsleitfaden beziehungsweise bei ungeklärter Bedienbarkeit eine gezielte UI-Prototyp-Empfehlung. Verwenden, wenn ein einzelnes Repository anhand von Commits, PRs, Issues, CI/Actions, Tests, Roadmap und ausführbaren Nutzerpfaden auf Beta-Reife geprüft werden soll; für Portfolios den Skill pro Projekt wiederholt ausführen und Ergebnisse erst danach aggregieren. |
| [`project-status-brief`](skills/project-status-brief/SKILL.md) | Verdichtet bereits erhobene Repository- und Projekt-Evidenz zu einem zeitpunktbezogenen Statusbrief mit Fortschritt, Blockern, Risiken, Entscheidungen und nächsten ausführbaren Schritten. Verwenden, wenn Projektzustand belastbar an Reviews, Meetings oder weitere Skills übergeben werden soll, ohne GitHub-, GitLab-, Jira-, CI- oder Deployment-Logik zu duplizieren. |
| [`repository-skill-bootstrap`](skills/repository-skill-bootstrap/SKILL.md) | Analysiert ein bestehendes Software-Repository und richtet eine portable Agent-Arbeitsgrundlage mit CONFIG.md, CONTEXT.md und DECISIONS.md ein. Verwenden, wenn ein Repository erstmals für wiederholbare Arbeit mit mehreren Skills, Agenten oder Sitzungen vorbereitet werden soll. |
| [`research-to-evidence-note`](skills/research-to-evidence-note/SKILL.md) | Verdichtet eine klar abgegrenzte Recherchefrage und zugängliche Quellen zu einer zitierfähigen Evidenznotiz mit expliziter Quellenqualität, Aktualität, Widersprüchen, Unsicherheit und offenen Punkten. Verwenden, wenn Rechercheergebnisse belastbar an Meeting-Prep, Projektstatus, Dokumentproduktion oder Knowledge-Ingestion übergeben werden sollen, ohne Retrieval-, Connector- oder Drafting-Logik zu duplizieren. |
| [`round-based-requirements-grilling`](skills/round-based-requirements-grilling/SKILL.md) | Führt Requirements Engineering als datengetriebenen, rundenbasierten Grilling-Prozess durch. Bei Softwareprojekten ist eine verpflichtende KI-/ML-Readiness-Prüfung einschließlich Einsatzpotenzial, Architekturvorbereitung, Datensammlung, Labeling und Governance Bestandteil des Grillings. Die generische, token-geschützte WebApp verwaltet parallele aktive und historische Grillings. Eine SPEC.md wird im Chat geprüft und erst nach Approval in ein separates Produkt-Repository übergeben. |
| [`spec-to-vertical-issues`](skills/spec-to-vertical-issues/SKILL.md) | Zerlegt eine freigegebene, konsistente Spezifikation in kleine, unabhängig abnehmbare vertikale Implementierungs-Issues mit vollständiger Rückverfolgbarkeit, Abnahmeevidenz, Abhängigkeiten und expliziten Nicht-Zielen. Verwenden, wenn aus SPEC.md und Entscheidungsregister eine geordnete Engineering-Backlog-Übergabe entstehen soll, ohne irreversible Architekturentscheidungen stillschweigend zu treffen. |
| [`structured-knowledge-artifact`](skills/structured-knowledge-artifact/SKILL.md) | Verpackt bereits fachlich bestimmte Informationen in ein provider-neutrales, adressierbares Wissensartefakt mit stabiler Identität, Metadaten, typisierten Links und Provenance. Verwenden, wenn Ergebnisse aus Decision Records, Memory Governance, Research, Domain Models oder anderen Skills dauerhaft referenzierbar und zwischen Markdown-, JSON-, Graph- oder Obsidian-Adaptern austauschbar werden sollen; bestimmt selbst weder Memory-Persistenz noch fachliche Wahrheit. |
| [`synapse-orchestrator`](skills/synapse-orchestrator/SKILL.md) | Orchestrate complex or ambiguous goals by aligning on the desired outcome, routing work to direct execution, existing skills and tools, transparent expert perspectives, or explicitly requested subagents, and maintaining concise progress and next steps. Use when the user invokes Professor Synapse, Synapse_CoR, /start, /save, /reason, /settings, /new, /grill-me, or /learn-skill; asks for an expert or multi-expert analysis; wants a cross-domain task decomposed; or needs help choosing the right workflow before execution. |
| [`test-driven-vertical-slice`](skills/test-driven-vertical-slice/SKILL.md) | Implementiert ein kleines, unabhängig beobachtbares End-to-End-Verhalten durch einen disziplinierten Red-Green-Refactor-Zyklus. Verwenden, wenn ein klar begrenztes vertikales Issue mit Akzeptanzkriterien über die notwendigen Schichten hinweg umgesetzt werden soll, ohne horizontale Infrastrukturpakete, spekulative Abstraktionen oder rein mock-basierte Scheinerfolge. |
| [`throwaway-prototype`](skills/throwaway-prototype/SKILL.md) | Prüft unsichere technische oder fachliche Annahmen mit bewusst kurzlebigen, isolierten Prototypen, trennt Lernnachweise von Produktionsabnahme und verhindert die unbeabsichtigte Übernahme experimentellen Codes. |
| [`two-axis-code-review`](skills/two-axis-code-review/SKILL.md) | Prüft eine Änderung unabhängig auf Anforderungsabdeckung und auf Implementierungs- sowie Lieferqualität. Verwendet zwei getrennte Evidenzachsen für Spezifikationstreue, Codequalität, Architektur, Tests, Sicherheit, Migrationen und Betriebsrisiken und liefert priorisierte, kleinste sichere Abhilfen ohne stilgetriebene Blocker oder spekulative Neuschreibung. |
<!-- skill-catalog:end -->

Der Katalog wird mit `python scripts/generate_catalog.py` aus dem Frontmatter der Skills erzeugt.

## Qualitäts- und Metadatenmodell

Neue Skills sollen zusätzlich zu `name` und `description` folgende Frontmatter-Felder führen:

- `version`: semantische Version
- `status`: `draft`, `candidate`, `stable` oder `deprecated`
- `owners`: verantwortliche Personen oder Teams
- `requires`: benötigte Skills
- `outputs`: dokumentierte Übergabeformate
- `lastEvaluated`: Datum der letzten Evaluation

Die Vorlage liegt unter [`templates/SKILL.template.md`](templates/SKILL.template.md), das Schema unter [`schemas/skill.schema.json`](schemas/skill.schema.json).

## Pflegeprinzipien

- Skills sind produktunabhängig, klein und wiederverwendbar.
- Ein Fach-Skill besitzt eine primäre Aufgabe; Orchestratoren koordinieren, ohne Fachlogik zu duplizieren.
- Umfangreiche Details werden progressiv in `references/` ausgelagert.
- Reproduzierbare Transformationen und Validierungen werden nach Möglichkeit in `scripts/` implementiert.
- Projektdateien, Zugangsdaten, Tokens und personenbezogene Inhalte gehören nicht in dieses Repository.
- Ein Skill beschreibt Trigger, Voraussetzungen, Ablauf, Prüfungen, Fehlerbehandlung, Übergaben und Abschlusskriterien.
- Neue oder wesentlich überarbeitete Skills durchlaufen Happy Path, Grenzfall und Fehlerfall.
- Portable Skill-Inhalte werden konfliktgeschützt über `.skill-sync.json` abgeglichen.

## Validierung

Lokal:

```bash
python scripts/validate_skills.py
python scripts/verify_generated.py
```

GitHub Actions führt dieselben Prüfungen bei Pull Requests und Pushes auf `main` aus.

## Namenskonvention

Verzeichnis- und Skillnamen verwenden englische, kleingeschriebene Slugs mit Bindestrichen. Die eigentliche Anleitung kann deutschsprachig sein.
