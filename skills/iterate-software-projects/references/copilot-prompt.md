# Schablone für einen Coding-Agent-Auftrag

Die Felder projektspezifisch ausfüllen und irrelevante Punkte entfernen.

```text
Du arbeitest als [Rolle] im Repository [Repository/Pfad].

Ziel dieser Iteration
[Ein fachlich kohärentes, überprüfbares Ergebnis.]

Belegter Ausgangsstand
- [Branch/Commit/letzte abgeschlossene Funktion]
- [relevante Architektur und Schnittstellen]
- [bekannte Restfehler oder Testergebnisse]

Bestätigte Entscheidungen und Annahmen
- Entschieden: [Nutzerentscheidung und Konsequenz]
- Angenommen: [reversible Vorgabe und Grund]
- Noch offen: [nur nicht blockierende Punkte für spätere Iterationen]

Arbeitsweise
1. Lies zuerst [Projektregeln, SPEC, relevante Dateien].
2. Prüfe den Ist-Zustand; passe Details an belegte Repository-Fakten an.
3. Frage nicht nach Fakten, die im Repository oder in der Laufzeitumgebung feststellbar sind.
4. Stoppe und berichte, falls eine neue, weitreichende Entscheidung nötig wird, die den bestätigten Scope verändert; triff sie nicht stillschweigend.
5. Behebe zuerst Restfehler der vorherigen Iteration.
6. Implementiere das Inkrement vollständig einschließlich Tests und Dokumentation.
7. Führe die unten genannten Nachweise aus und korrigiere gefundene Fehler.

Scope
- [Anforderung]
- [Anforderung]

Nicht im Scope
- [bewusst ausgeschlossene Erweiterung]
- Keine sachfremden Refactorings oder Abhängigkeits-Upgrades.

Technische Leitplanken
- [Kompatibilitätsgrenzen]
- [vorhandene Komponenten wiederverwenden]
- [Sicherheits-, Daten- oder Quellenanforderungen]
- Provisorische Laufzeitfixes dauerhaft und reproduzierbar verankern.

Tests und Funktionsnachweise
- [Unit-/Integrations-/Migrationstest]
- [Build/Lint/Typprüfung]
- [Health-/API-/Ende-zu-Ende-Aufruf mit erwartetem Ergebnis]
- Prüfe den finalen Diff auf unbeabsichtigte Änderungen und Whitespace-Fehler.

Definition of Done
- [beobachtbares Nutzer- oder Systemverhalten]
- Alle relevanten Tests sind erfolgreich.
- Dokumentation, Konfiguration und Migrationen stimmen mit der Implementierung überein.
- Es verbleiben keine stillen Provisorien oder unbelegten Erfolgsaussagen.

Abschluss
Berichte knapp:
- geänderte Dateien und Zweck,
- ausgeführte Befehle und Ergebnisse,
- Laufzeitnachweise,
- verbleibende Risiken oder bewusst vertagte Punkte.
- neu aufgetauchte Entscheidungen und verwendete reversible Annahmen.

[Optional und nur beauftragt: Stage ausschließlich die zu dieser Iteration gehörenden Änderungen, committe sie mit einer präzisen Nachricht und pushe den aktuellen Branch.]
```

## Anpassung nach Aufgabentyp

- **Fehlerbehebung:** Reproduktion, Ursache, minimaler Fix und Regressionstest verlangen.
- **Feature:** Nutzerverhalten, API-/Datenvertrag, Negativfälle und Migration festlegen.
- **Docker/Integration:** Service-Namen, Netzwerke, Ports, Healthchecks, Persistenz und echte Containeraufrufe nennen.
- **RAG/KI:** Quellenbindung, Trennung generierter Inhalte, Retrieval-Nachweis, Auditierbarkeit und Fehlverhalten ohne Quellen definieren.
- **PR/Review-Fix:** Jeden Befund auflösen oder begründet zurückweisen; bestehende grüne Checks erhalten.
