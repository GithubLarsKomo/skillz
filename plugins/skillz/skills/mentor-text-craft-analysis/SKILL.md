---
name: mentor-text-craft-analysis
description: Analysiert vom Nutzer bereitgestellte oder rechtmäßig zugängliche Referenztexte nach übertragbaren handwerklichen Mechanismen wie Perspektive, Szenenbau, Informationsfluss, Dialog, Tempo, Spannung, Exposition und Kapitelarchitektur, ohne die Stimme eines lebenden oder benannten Autors zu imitieren oder längere Textpassagen zu reproduzieren. Verwenden als Reading-like-a-writer-Schritt vor Creative Writing oder gezielter Craft-Revision.
---

# Mentor Text Craft Analysis

## Zweck

Lies Referenztexte **wie ein Autor**: nicht primär auf Inhalt, sondern auf beobachtbare Konstruktion. Das Ergebnis ist ein abstrahiertes Craft-Modell, kein Stilklon.

## Eingaben

- rechtmäßig zugängliche Textausschnitte oder Werke;
- Zielprojekt/Genre;
- gewünschte Craft-Frage, sofern vorhanden.

## Analyseachsen

Mindestens soweit relevant:

- POV und narrative Distanz;
- Szeneneinstieg und -ausstieg;
- Figurenintroduktion;
- Want/Obstacle/Change innerhalb einer Szene;
- Exposition und Informationsfreigabe;
- Dialogfunktion und Subtext;
- Beschreibung und sensorische Dichte;
- Tempo und Satzrhythmus;
- Spannung, Frage und Reveal-Cadence;
- Zeitführung und Rückblenden;
- Kapitelarchitektur;
- Setup/Payoff;
- Übergänge zwischen Figuren- oder Handlungssträngen.

## Ablauf

1. Projektziel und Craft-Frage fixieren.
2. Nur tatsächlich verfügbare Textstellen untersuchen.
3. Beobachtung von Interpretation trennen.
4. Mechanismen abstrahieren: **was tut der Text, wann und mit welcher Wirkung?**
5. Alternative Umsetzungen benennen, damit aus Analyse keine Stilkopie wird.
6. Maximal kurze notwendige Zitate verwenden; ansonsten paraphrasieren.
7. Transferregeln für das Zielprojekt formulieren.

## Output

`mentor-craft-model.json` enthält:

- `sourceRefs`;
- `genreContext`;
- `craftPatterns[]` mit observation, function, transferRule und confidence;
- `avoidCopying[]`;
- `openQuestions[]`.

## Qualitätsgate

- **Mechanismus statt Imitation.**
- Keine Aufforderung, einen benannten Autor täuschend nachzuahmen.
- Keine langen geschützten Passagen reproduzieren.
- Beobachtung und Transferregel bleiben nachvollziehbar getrennt.
- Der Zieltext soll eine eigenständige Stimme entwickeln können.

## Abschluss

Abgeschlossen, wenn ein übertragbares Craft-Modell vorliegt, das einen nachgelagerten Schreib- oder Revisionsskill anleiten kann, ohne die Referenzstimme zu kopieren.
