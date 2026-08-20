---
name: frontend-design-shaping
description: Klärt eine konkrete neue oder wesentlich veränderte Frontend-Surface vor Implementierung auf Basis des autoritativen PRODUCT.md und DESIGN.md. Fragt nur materielle neue Entscheidungen ab, erzeugt bei Greenfield oder echter Richtungsunsicherheit visuelle Probes und liefert einen bestätigbaren frontend-design-brief.md mit expliziten lokalen Overrides.
userFacing: false
implicitInvocation: true
category: engineering
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - frontend-product-context
  - frontend-design-system-context
  - round-based-requirements-grilling
  - large-work-wayfinder
outputs:
  - frontend-design-brief.md
  - frontend-shaping-handoff.json
lastEvaluated: 2026-08-20
---

# Frontend Design Shaping

## Zweck und Grenze

Shaping plant UX/UI einer konkreten Surface oder eines Features vor Codeänderungen. Es erzeugt einen belastbaren Design-Brief und implementiert nicht selbst.

## Voraussetzungen

`PRODUCT.md` und `DESIGN.md` müssen bestätigt und aktuell genug für den Scope sein. Beide Dokumente werden vollständig als autoritative Basis behandelt.

## Ablauf

### 1. Scope und vorhandene Antworten bestimmen

Lies `PRODUCT.md`, `DESIGN.md`, betroffene Oberfläche, relevante Komponenten und die Nutzeraufgabe. Markiere jede bereits beantwortete Frage als geschlossen. **Keine bestätigte Entscheidung erneut fragen.**

### 2. Nur materielle Lücken klären

Kläre bei Bedarf Zweck der Surface, primäre Nutzeraktion, reale Inhalte/Datenbereiche, Zustände und Edge Cases, Fidelity, Interaktivität, responsive Besonderheiten und konkrete Anti-Ziele. Neue fachliche/gestalterische Entscheidungen gehen an ein fokussiertes `round-based-requirements-grilling`; technische Tragfähigkeit oder unbekannte Abhängigkeiten an `large-work-wayfinder`.

### 3. Visuelle Probes gezielt einsetzen

- Greenfield oder neue visuelle Richtung: standardmäßig **2–3 visuelle Probes** erzeugen, wenn native Bild-/Visual-Capability verfügbar ist.
- Bestehende UI: erst Bestand analysieren; Probes nur bei **echter Richtungsunsicherheit**, nicht für kleine evolutionäre Änderungen.
- Probes sind Richtungsentscheidungen, keine finale UX-Spezifikation und kein Ersatz für semantische, responsive oder accessible Implementierung.

### 4. Surface-Overrides kontrollieren

Ein Brief darf `DESIGN.md` nur lokal überschreiben, wenn der Override ausdrücklich bestätigt, räumlich/funktional begrenzt und begründet ist. Dokumentiere Scope, betroffene Regel, neue Regel und Kriterium, wann sie wieder entfällt oder per DESIGN-Grilling globalisiert werden soll.

### 5. Brief zur Bestätigung ausgeben

Der `frontend-design-brief.md` enthält mindestens:

- Feature/Surface und Nutzerziel,
- primäre Aktion oder Erkenntnis,
- relevante PRODUCT-/DESIGN-Regeln,
- Inhalte/Daten und realistische Zustände,
- Layout- und Hierarchiestrategie,
- Interaktionsmodell,
- Responsive/Accessibility-Anforderungen,
- Bild-/Asset-Rollen,
- gewählte Probe-Richtung, falls verwendet,
- explizite lokale Overrides,
- offene technische/fachliche Punkte und Routing,
- Implementierungs- und Review-Akzeptanzkriterien.

Die Implementierung startet erst nach expliziter Bestätigung des Briefs oder wenn ein bereits bestätigter Brief als Input vorliegt.

## Persönliche Default-Hypothesen

Wenn der Director sie mitliefert, dürfen persönliche Defaults fehlende Richtungsentscheidungen anregen. Für Apps sind kompakte Informationsdichte, technische/geometrische Typografie und eher dunkle Oberflächen typische Hypothesen; für Landingpages eher helle, editoriale und auch für fachlich naive Besucher verständliche Gestaltung. Diese Hypothesen verlieren sofort gegen `PRODUCT.md`, `DESIGN.md` oder bestätigte Surface-Entscheidungen.

## Fehlerbehandlung

Stoppe Shaping, wenn die Aufgabe eigentlich eine globale Produkt-/Designsystemänderung verlangt; route dann zu PRODUCT- oder DESIGN-Grilling. Erfinde keine technische Lösung, wenn Wayfinder-Evidenz fehlt.

## Abschluss

Abgeschlossen ist Shaping, wenn ein bestätigbarer Brief mit **keine bestätigte Entscheidung erneut fragen**, belastbaren Zuständen, klaren Overrides und genauem Handoff für Implementierung/Review vorliegt.
