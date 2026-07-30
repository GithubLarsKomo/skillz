---
name: conversation-to-spec
description: Verdichtet bestätigten Gesprächs-, Grilling- und Repository-Kontext zu einer umsetzbaren, prüfbaren Spezifikation, ohne bereits beantwortete Fragen erneut zu stellen. Verwenden, wenn aus freigegebenen Festlegungen eine SPEC.md, ein technischer Umsetzungsrahmen oder eine belastbare Übergabe an Engineering entstehen soll.
---

# Conversation to Spec

Erzeuge aus bestätigtem Kontext eine vollständige Spezifikation. Dieser Skill führt kein neues Requirements-Interview durch, solange vorhandene Quellen die Entscheidung bereits tragen.

## Eingaben

Nutze in dieser Reihenfolge:

1. ausdrücklich bestätigte Nutzerentscheidungen und freigegebene Grilling-Reports,
2. vorhandene `SPEC.md`, `README.md`, Architektur- und Agent-Dokumente,
3. ADRs, Aufgabenlisten, Issues und bestehende Implementierung,
4. begründete Annahmen nur für nicht entscheidungskritische Lücken.

Kennzeichne Widersprüche und Unsicherheiten. Überschreibe keine bestätigte Festlegung durch eine spätere bloße Vermutung.

## Kernregeln

- Stelle keine Frage erneut, deren Antwort in den Quellen eindeutig vorliegt.
- Trenne Anforderungen, Entscheidungen, Annahmen und offene Punkte.
- Formuliere beobachtbares Verhalten und prüfbare Akzeptanzkriterien.
- Bewahre Domänensprache, Invarianten und Architekturgrenzen des Ziel-Repositories.
- Erfinde keine APIs, Rollen, Datenfelder oder Betriebszusagen ohne fachliche Grundlage.
- Halte das MVP ohne unvalidierte KI sicher nutzbar; dokumentiere KI-/ML-Vorbereitung separat.
- Verweise auf ADR-pflichtige Entscheidungen, statt sie unbemerkt in der Spezifikation zu treffen.

## Workflow

### 1. Quellen inventarisieren

Erfasse je Quelle:

- Status: bestätigt, bindend, informativ oder veraltet,
- behandelte Themen,
- relevante Entscheidungen,
- erkennbare Widersprüche,
- offenen Geltungsbereich.

Bei Repository-Arbeit zuerst `docs/agents/CONFIG.md`, `CONTEXT.md` und `DECISIONS.md` lesen, sofern vorhanden.

### 2. Entscheidungsregister bilden

Konsolidiere jede Festlegung als:

- stabile ID,
- Thema,
- Entscheidung,
- Quelle,
- Status,
- betroffene Anforderungen und Risiken.

Bei Konflikten gilt nicht automatisch die jüngste Quelle. Bevorzuge ausdrücklich freigegebene, fachlich höherrangige oder durch Tests belegte Festlegungen.

### 3. Lücken klassifizieren

Ordne fehlende Angaben ein:

- **blockierend:** verhindert eine sichere oder eindeutige Umsetzung,
- **ADR-pflichtig:** verändert Architektur oder Invarianten,
- **später entscheidbar:** kann mit einer stabilen Schnittstelle vertagt werden,
- **sicher annehmbar:** besitzt eine risikoarme Standardannahme.

Erstelle keine künstlichen Blocker. Nutze sichere Annahmen mit klarer Kennzeichnung.

### 4. Spezifikation erzeugen

Eine Software-Spezifikation enthält mindestens:

1. Zweck, Zielbild und Nicht-Ziele,
2. Nutzer, Rollen und zentrale Abläufe,
3. funktionale Anforderungen mit IDs,
4. Domänenmodell und Invarianten,
5. Zustände, Fehlerfälle und Wiederaufnahme,
6. Datenmodell, Datenschutz und Aufbewahrung,
7. Autorisierung, Audit und Sicherheitsgrenzen,
8. Schnittstellen und Integrationen,
9. Offline-, Synchronisations- und Konfliktverhalten, falls relevant,
10. Qualitätsanforderungen und Observability,
11. KI-/ML-Architektur und Datenstrategie, falls Software betroffen ist,
12. Migration, Deployment und Betrieb,
13. Akzeptanzkriterien und Release-Gates,
14. Risiken, Annahmen und offene Entscheidungen,
15. Umsetzungsreihenfolge in vertikalen Schnitten.

Nicht relevante Abschnitte werden kurz als nicht anwendbar begründet statt still ausgelassen.

### 5. Rückverfolgbarkeit prüfen

Jede Muss-Anforderung benötigt mindestens eine Quelle oder eine ausdrücklich markierte Annahme. Jedes Akzeptanzkriterium muss auf eine Anforderung verweisen. Offene Punkte dürfen nicht als bereits entschiedene Anforderungen erscheinen.

### 6. Konsistenzprüfung

Prüfe mindestens:

- Rollen gegen Berechtigungen,
- Zustandsübergänge gegen Fehler- und Wiederaufnahmefälle,
- Datenfelder gegen Datenschutz und Export/Löschung,
- Offline-Verhalten gegen Idempotenz und Konfliktregeln,
- Architektur gegen Repository-Invarianten,
- Release-Gates gegen die beschriebenen Tests,
- KI-Funktionen gegen Fallback, Ground Truth, Evaluation und Governance.

### 7. Ausgabe und Übergabe

Liefere:

- die vollständige Spezifikation,
- ein kurzes Entscheidungsregister,
- offene Blocker und ADR-Bedarf,
- empfohlene nächste vertikale Schnitte,
- einen Abschlussnachweis der Konsistenzprüfung.

Speichere oder veröffentliche die Spezifikation nur im ausdrücklich bestimmten Produkt-Repository. Der Grilling- oder Skill-Katalog ist kein Ablageort für projektspezifische Spezifikationen.

## Qualitätsfälle

### Happy Path

Mehrere freigegebene Grilling-Reports und Repository-Dokumente sind konsistent. Ergebnis ist eine vollständige Spezifikation ohne erneutes Interview.

### Grenzfall

Eine Detailfrage ist offen, aber durch eine austauschbare Schnittstelle vertagbar. Die Spezifikation dokumentiert Annahme, Grenze und späteren Entscheidungspunkt.

### Fehlerfall

Zwei bindende Quellen widersprechen sich bei einer Sicherheits-, Compliance- oder Architekturentscheidung. Stoppe die betroffene Festlegung, dokumentiere den Konflikt und liefere den übrigen konsistenten Teil weiter.

## Abschlusskriterien

Der Skill ist abgeschlossen, wenn:

- alle relevanten Quellen klassifiziert wurden,
- bestätigte Entscheidungen rückverfolgbar enthalten sind,
- keine bereits beantwortete Frage erneut gestellt wurde,
- Anforderungen und Akzeptanzkriterien prüfbar sind,
- Annahmen und offene Punkte sichtbar getrennt sind,
- Architektur- und Sicherheitsinvarianten konsistent bleiben,
- der nächste Umsetzungsschritt eindeutig ableitbar ist.
