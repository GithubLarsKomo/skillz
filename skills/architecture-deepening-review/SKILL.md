---
name: architecture-deepening-review
description: Prüft bestehende Softwarearchitektur evidenzbasiert auf flache Modulgrenzen, versehentliche Kopplung, duplizierte Domänenregeln und Infrastrukturleckagen. Verwenden, wenn ein Repository gezielt vertieft werden soll, ohne aus Dateilayout oder Stilpräferenzen spekulative Rewrite-Empfehlungen abzuleiten.
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - disciplined-diagnosis
  - iterate-software-projects
outputs:
  - architecture-review.md
  - architecture-findings.json
  - deepening-handoff.json
lastEvaluated: 2026-08-01
---

# Architecture Deepening Review

## Trigger

Diesen Skill verwenden, wenn die Änderbarkeit, Domänenklarheit oder Kopplung eines bestehenden Systems überprüft und genau ein kleiner, hochwirksamer Architekturvertiefungsschritt abgeleitet werden soll.

## Voraussetzungen

Erfasse Repositorystruktur, relevante Laufzeit- und Abhängigkeitspfade, zentrale Domänenbegriffe und Invarianten, jüngste Änderungen, bekannte Architekturgrenzen, vorhandene Tests sowie Lieferdruck und bewusste Einfachheitsentscheidungen. Dateinamen, Ordner oder Framework-Konventionen allein belegen keine architektonische Schwäche.

## Begriffe

Trenne konsequent Beobachtung, Symptom, Hypothese, verifizierten Befund und Vertiefungsschritt. Ein Befund ist erst verifiziert, wenn konkrete Abhängigkeits-, Domänen- oder Änderungsevidenz naheliegende Alternativen unterscheidet.

## Ablauf

### 1. Änderungsdruck und Hotspots bestimmen

Identifiziere Bereiche mit häufigen Änderungen, Defekten, Konflikten, langen Testketten oder wiederholten fachlichen Anpassungen. Prüfe, ob der Aufwand tatsächlich aus Kopplung oder fehlender Domänenklarheit entsteht.

### 2. Abhängigkeiten und Verantwortungen belegen

Untersuche Import-, Aufruf-, Daten- und Persistenzpfade. Suche nach überladenen Anwendungsdiensten, direkten Infrastrukturzugriffen aus Domänenlogik, zyklischen oder schichtübergreifenden Abhängigkeiten, duplizierten Invarianten und instabilen Schnittstellen. Nutze konkrete Pfade, Symbole, Aufrufe, Tests oder Änderungsverläufe als Evidenz.

### 3. Domänengrenzen prüfen

Leite Grenzen aus fachlichen Begriffen, Invarianten, Zustandsübergängen und Änderungsgründen ab, nicht aus Ordnernamen. Prüfe, welche Regeln zusammengehören und welche unabhängig geändert werden müssen.

### 4. Hypothesen unterscheiden

Formuliere zu jedem Kandidaten beobachtete Evidenz, vermutete Ursache, Gegenprobe, Ergebnis und Status `verified`, `plausible`, `rejected` oder `insufficient-evidence`.

### 5. Absichtlich einfache Architektur respektieren

Ist das System klein, stabil und leicht änderbar, dokumentiere flache Struktur ohne zusätzliche Schichten zu empfehlen. Abstraktionen benötigen aktuellen Änderungsdruck, nachgewiesene Regelduplikation oder eine instabile Grenze.

### 6. Einen Vertiefungsschritt priorisieren

Wähle höchstens einen ausführbaren Schritt. Er enthält betroffenen Pfad, Nicht-Ziele, erwarteten Nutzen, Verhaltens- und Kompatibilitätsinvarianten, Test- und Akzeptanzevidenz, Risiko, Rollback, Aufwand und Abhängigkeiten. Bevorzuge eine kleine Extraktion einer stabilen Domänenregel oder eines Ports an einer belegten Infrastrukturgrenze gegenüber einer repositoryweiten Neuschichtung.

### 7. Umsetzung übergeben

Übergib an `spec-to-vertical-issues`, wenn mehrere abnehmbare Slices nötig sind, an `test-driven-vertical-slice` für einen kleinen direkt umsetzbaren Schritt, an `disciplined-diagnosis` bei unklarer Ursache oder an `iterate-software-projects` bei weiterem Explorationsbedarf.

## Prüfungen

Vor Abschluss müssen Beobachtungen und Hypothesen getrennt, Abhängigkeits- und Domänenevidenz vorhanden, bewusste Einfachheit geprüft und Stilpräferenzen ausgeschlossen sein. Jede Empfehlung enthält Nutzen, Scope, Risiko, Rollback und Verifikation; höchstens ein nächster Schritt ist ausführbar.

## Fehlerbehandlung

Lehne Bewertungen ab, die allein aus Dateilayout eine Zielarchitektur ableiten, pauschal Clean Architecture, DDD oder ein neues Framework fordern, repositoryweite Umschreibungen empfehlen, Delivery-, Sicherheits- oder Migrationsgrenzen ignorieren, Symptome als Ursachen ausgeben oder mehrere Refactorings gleichzeitig freigeben.

## Übergabeformat

```json
{
  "scope": {"paths": ["..."], "constraints": ["..."], "nonGoals": ["..."]},
  "observations": [{"statement": "...", "evidence": ["..."]}],
  "hypotheses": [{"statement": "...", "status": "verified|plausible|rejected|insufficient-evidence", "evidence": ["..."]}],
  "findings": [{"finding": "...", "status": "verified|observation-only", "impact": "...", "affectedPaths": ["..."]}],
  "recommendations": [{"action": "...", "executable": true, "expectedBenefit": "...", "scope": ["..."], "risks": ["..."], "rollback": "...", "verification": ["..."]}],
  "nextSkill": "spec-to-vertical-issues|test-driven-vertical-slice|disciplined-diagnosis|iterate-software-projects"
}
```

## Abschlusskriterien

Die Prüfung ist abgeschlossen, wenn belastbare Evidenz und Domänenkontext vorliegen, spekulative Architekturpräferenzen ausgeschlossen wurden und entweder genau ein kleiner Vertiefungsschritt mit Verifikation übergeben oder begründet keine Strukturänderung empfohlen wird.
