---
name: speculative-worldbuilding
description: Entwickelt Science-Fiction- oder Fantasy-Welten als kausales System aus Grundannahmen, Natur-/Magie-/Technologieregeln, Ressourcen, Grenzen, Zugang, Institutionen, Kulturen, Machtfolgen und Konflikten und verpackt bestätigte Weltelemente als adressierbare Knowledge Artifacts. Verwenden für belastbares Worldbuilding; keine Enzyklopädie um ihrer selbst willen erzeugen und Ideen nicht automatisch zu Canon erklären.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - structured-knowledge-artifact
outputs:
  - world-model.json
  - world-bible.md
  - structured world artifacts
lastEvaluated: 2026-09-06
---

# Speculative Worldbuilding

## Zweck

Baue eine Welt, die Geschichten **verursacht**, statt nur Hintergrund zu liefern.

## Kausalkette

```text
Grundannahme
 -> Regel / Naturgesetz / Technologie / Magie
 -> Kosten und Grenzen
 -> Ressourcen
 -> Zugang
 -> Kontrolle
 -> Institutionen
 -> Gewinner und Verlierer
 -> kulturelle Normen
 -> Konflikte
 -> erzählbare Konsequenzen
```

## Domänen

Nach Bedarf:

- Physik/Ökologie;
- Technologie;
- Magie;
- Ökonomie;
- Politik und Recht;
- Religion/Mythologie;
- Kultur/Sprache;
- Demographie/Spezies;
- Infrastruktur;
- Geographie;
- Geschichte.

## Canon-Zustände

Jedes Element ist:

- `idea`;
- `planned`;
- `draft-canon`;
- `approved-canon`;
- `published-hard-canon`.

**Idee ist nicht Canon.**

## Ablauf

1. Story Promise und zentrale Weltannahme bestimmen.
2. Regeln, Kosten und Grenzen definieren.
3. First-order consequences ableiten.
4. Second-order institutionelle und kulturelle Folgen prüfen.
5. Konfliktpotenzial und Story Relevance bewerten.
6. Inkonsistenzen und unbeantwortete Systemfragen sichtbar halten.
7. Bestätigte Elemente als `structured-knowledge-artifact` mit stabilen IDs ausgeben.

## Science Fiction

Reale wissenschaftliche Behauptungen und spekulative Setzungen ausdrücklich unterscheiden. Plausibilität kann recherchiert werden; Fiktion darf darüber hinausgehen, muss den Übergang aber sichtbar markieren.

## Fantasy

Magie wird mindestens nach Zugang, Kontrolle, Kosten, Grenzen, Lernbarkeit und gesellschaftlicher Machtwirkung betrachtet, sofern das Projekt kein bewusst mythisch-unklares System verlangt.

## Qualitätsgate

- **Weltlogik vor Lore-Menge.**
- Kein Canon ohne expliziten Lifecycle-State.
- Regeln besitzen Kosten, Grenzen oder bewusst dokumentierte Unbestimmtheit.
- Institutionen und Kultur folgen nicht automatisch modernen Standardannahmen.
- Weltbau erzeugt konkrete Möglichkeiten und Zwänge für Figuren und Handlung.

## Abschluss

Abgeschlossen, wenn ein referenziell konsistentes `world-model.json` mit offenen Fragen, Canon-State und story-relevanten Konsequenzen vorliegt.
