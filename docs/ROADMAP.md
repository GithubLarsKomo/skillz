# Roadmap

## Jetzt

- Bestehende Skills schrittweise auf das erweiterte Frontmatter migrieren.
- Evaluations-Fixtures für die drei zentralen Skills einführen.
- Synchronisationshashes für neuere Skills aktualisieren und künftig automatisch erzeugen.

## Als Nächstes

1. `spec-to-vertical-issues`: Spezifikationen in unabhängig umsetzbare vertikale Issues zerlegen.
2. `disciplined-diagnosis`: Fehler reproduzieren, minimieren, instrumentieren und mit Regressionstest beheben.
3. `test-driven-vertical-slice`: Red-Green-Refactor pro kleinem End-to-End-Schnitt.
4. `agent-handoff`: überprüfbaren Übergabestand für neue Sitzungen oder Agenten erzeugen.
5. `architecture-deepening-review`: flache Module, Kopplung und fehlende Domänengrenzen erkennen.

## Geschlossene Engineering Delivery Chain

Diese Ausbaustufe schließt die Lücke zwischen Spezifikation, Implementierung, Review und Integration. Die Skills sollen komponierbar sein und vorhandene Skills wie `conversation-to-spec`, `iterate-software-projects`, `disciplined-diagnosis`, `test-driven-vertical-slice` und `agent-handoff` wiederverwenden.

1. `implement-from-issue`: Ein klar abgegrenztes Issue vollständig umsetzen, relevante Dateien und Testseams bestimmen, Qualitätsprüfungen ausführen und einen überprüfbaren Commit- oder PR-Stand erzeugen.
2. `two-axis-code-review`: Änderungen getrennt gegen Spezifikation beziehungsweise Issue sowie gegen Codequalität, Architektur, Tests, Sicherheit, Migrationen und Betriebsrisiken prüfen.
3. `merge-conflict-resolution`: Konflikte semantisch auflösen, beide Änderungsabsichten erhalten, relevante Tests ausführen und die Auflösung nachvollziehbar dokumentieren.
4. `large-work-wayfinder`: Große oder unklare Vorhaben durch gezielte Exploration, Untersuchungs-Issues, Abhängigkeitsgraphen und eine belastbare Umsetzungsreihenfolge erschließen.
5. `throwaway-prototype`: Unsichere technische oder fachliche Annahmen mit bewusst kurzlebigen Prototypen prüfen und die gewonnenen Erkenntnisse ohne versehentliche Produktionsübernahme dokumentieren.
6. `domain-model-maintenance`: Domänenbegriffe, Invarianten, Zustände und Grenzen während der Implementierung konsistent halten und bei Änderungen kontrolliert migrieren.

### Abschlusskriterien

- Ein bestätigter Anforderungskontext kann ohne manuelle Prozesslücke in vertikale Issues, Implementierung, Tests, Review, Integration und Übergabe überführt werden.
- Jeder Skill besitzt Happy-Path-, Grenzfall- und Fehlerfall-Evaluationen.
- Gemeinsame Übergabeformate zwischen den Skills sind über `requires` und `outputs` maschinenlesbar dokumentiert.

## Productivity & Knowledge Work

Diese Ausbaustufe erweitert das Repository von einem Engineering-System zu einem allgemeinen Arbeits- und Wissenssystem. Die Skills sollen vorhandene Connectoren und lokale Werkzeuge nutzen, ohne personenbezogene Inhalte oder Zugangsdaten im Repository abzulegen.

1. `research-to-evidence-note`: Recherchefragen in belegte, zitierfähige Evidenznotizen mit Quellenqualität, Unsicherheiten und offenen Punkten überführen.
2. `meeting-preparation`: Termine, Teilnehmer, frühere Entscheidungen und relevante Unterlagen zu einem kompakten Vorbereitungsbrief zusammenführen.
3. `inbox-action-triage`: Nachrichten nach Dringlichkeit, Antwortbedarf, Delegation, Warten und reiner Information klassifizieren und konkrete nächste Aktionen ableiten.
4. `daily-and-weekly-review`: Aufgaben, Kalender, wartende Vorgänge, Projektstände und Prioritäten zu einem wiederholbaren Tages- beziehungsweise Wochenreview verdichten.
5. `decision-record`: Entscheidungen mit Kontext, Optionen, Begründung, Risiken, Gültigkeitsannahmen und Revisionsauslösern dokumentieren.
6. `knowledge-ingestion`: Dokumente und Medien kontrolliert extrahieren, strukturieren, verschlagworten, verknüpfen und an RAG-, Obsidian-, Affine- oder Graph-Systeme übergeben.
7. `project-status-brief`: Repository-, Issue-, CI-, Deployment- und Entscheidungsstand zu einem belastbaren Projektstatus mit Blockern und nächstem Inkrement zusammenführen.
8. `teach`: Lernmission, evidenzbasiertes Wissen, nachgewiesene Kompetenz und nächste Herausforderungen über mehrere Sitzungen orchestrieren; `exam-trainer-framework` dient dabei ohne Fork als gemeinsame Learning-, Spaced-Retrieval- und Assessment-Runtime, Anki als sicherer Content-Import. Architektur und Phasen sind in [`TEACH-INTEGRATION-SPEC.md`](TEACH-INTEGRATION-SPEC.md) festgelegt.
9. `document-production`: Aus bestätigten Fakten und Vorgaben konsistente Berichte, Memos, SOP-nahe Dokumente oder Präsentationsgrundlagen mit Review-Gates erstellen.

### Abschlusskriterien

- Wiederkehrende Wissens- und Produktivitätsabläufe können mit klaren Triggern, Eingaben, Ausgaben und Datenschutzgrenzen ausgeführt werden.
- Connector-abhängige Skills trennen portable Fachlogik von integrationsspezifischen Adaptern.
- Jeder Skill definiert, welche Inhalte persistent gespeichert werden dürfen und welche ausschließlich im jeweiligen Lauf verbleiben.

## Plattform, Evaluation und Distribution

- Maschinenlesbare Evaluationsrubriken und einen Evaluations-Runner einführen.
- Automatische Abhängigkeitsgraphen für `requires` und `outputs` erzeugen.
- Release-Prozess mit Skill-Versionen, Changelog und reproduzierbaren Skill-Bundles etablieren.
- Deprecation-, Kompatibilitäts- und Migrationsprüfungen ergänzen.
- Installation und Aktualisierung für neue Repositories mit einem einzelnen Bootstrap-Befehl ermöglichen.
- Frische Installationen in isolierten Test-Repositories automatisiert prüfen.
- Eine Coverage-Matrix für Engineering, Productivity, Knowledge Work und Operations pflegen.

## Später

- Domänenspezifische Skill-Pakete für Regulatory/IVD, lokale KI-Infrastruktur, RAG und Datenpipelines ergänzen.
- Skill-Komposition anhand erfolgreicher realer Abläufe messen und häufige Ketten als Orchestratoren verfügbar machen.
- Telemetrie ausschließlich als optionale, datensparsame lokale Evaluation vorsehen.
- Reifegrade von `draft` über `candidate` bis `stable` an nachweisbare Evaluationen und Nutzungserfahrung koppeln.
