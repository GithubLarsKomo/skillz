---
name: ensemble-character-architecture
description: Modelliert komplexe Figurenensembles als dynamisches System aus Want, Need, Fear, False Belief, Werten, Kompetenzen, Grenzen, Geheimnissen, Loyalitäten, Beziehungen, Wissensständen und Arc-Zuständen. Verwenden für Romane und Serien mit mehreren tragenden Figuren; keine psychologische Diagnose realer Personen und keine statischen Steckbriefe als Ersatz für dramaturgische Funktion.
---

# Ensemble Character Architecture

## Zweck

Baue Figuren nicht als Merkmalslisten, sondern als **dynamische Akteure in einem Beziehungs- und Wissenssystem**.

## Kernmodell pro Figur

Mindestens soweit relevant:

- Want;
- Need;
- Fear;
- False Belief;
- Values;
- Constraint;
- Competence;
- Weakness;
- Secret;
- Loyalty;
- Conflict;
- Moral Boundary;
- Relationship State;
- Knowledge/Belief State;
- Arc State.

Biografische Details werden nur aufgenommen, wenn sie Figur, Stimme, Handlung oder Kontinuität tatsächlich beeinflussen.

## Relationsgraph

Beziehungen sind eigenständige, versionierte Objekte. Mögliche Relationen:

- `loves`;
- `trusts`;
- `fears`;
- `owes`;
- `depends_on`;
- `controls`;
- `opposes`;
- `allied_with`;
- `protects`;
- `betrayed`;
- `believes_about`;
- `knows_secret_of`.

Eine Beziehung kann asymmetrisch sein und sich im Zeitverlauf ändern.

## Ablauf

1. Story Promise und Ensemblefunktion fixieren.
2. Für jede tragende Figur Want/Need/Fear und relevante falsche Annahmen bestimmen.
3. Kompetenzen und Grenzen gegen die geplanten Konflikte prüfen.
4. Beziehungen als Kanten mit Zustand und Zeitpunkt modellieren.
5. Wissen, Glauben, Verdacht und Irrtum ausdrücklich trennen.
6. Ensemble auf Redundanz prüfen: Zwei Figuren mit identischer dramaturgischer Funktion benötigen eine Begründung.
7. Arc-Hypothesen markieren, aber nicht automatisch zu Canon machen.
8. Bestätigte Figuren-/Relationsobjekte mit stabilen IDs als `structured-knowledge-artifact` ausgeben.

## Qualitätsgate

- **Dynamik vor Steckbrief.**
- Figuren besitzen handlungsrelevante Ziele, Zwänge oder Konflikte.
- Beziehungen sind nicht automatisch symmetrisch.
- Wissen und Wahrheit werden nicht verwechselt.
- Arc State und Relationship State sind zeitlich adressierbar.
- Diversität wird nicht durch stereotype Ersatzmerkmale simuliert.

## Abschluss

Abgeschlossen, wenn `character-ensemble.json` alle tragenden Figuren, ihre relevanten Beziehungen und zeitlich adressierbaren Arc-/Knowledge-Zustände konsistent abbildet.
