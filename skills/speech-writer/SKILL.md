---
name: speech-writer
description: Schreibt auf Basis eines freigegebenen Speaking-Konzepts deutsche oder englische Reden als sprechbares Manuskript und optionales Speaker Script. Unterstützt Anlass-, Fest-, Management-, wissenschaftliche, motivierende und andere Redetypen und respektiert Speaker Profile, Evidenz und Timing.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - speaking-concept
  - speaker-profile
outputs:
  - speech-draft.md
  - speech-script.md
lastEvaluated: 2026-08-23
---

# Speech Writer

## Input

`speaking-concept.json`, optional `speaker-profile.json`, Evidence/Fidelity Lock.

## Unterstützte Profile

Begrüßung, Festrede, Laudatio, Jubiläum, Abschied, Trauerrede, Motivation, Unternehmens-/Managementansprache, Townhall, wissenschaftliche Eröffnung, politische Rede, Dankesrede, Dinner Speech und Keynote ohne Folien. Profile steuern Regeln; sie sind keine separaten Skills.

## Schreibregeln

- für das Ohr statt für die Seite schreiben;
- Kernbotschaft und Dramaturgie des Konzepts erhalten;
- Sätze und Übergänge sprechbar halten;
- bewusste Wiederholung, Kontrast, Metapher und Dreierfigur nur gezielt einsetzen;
- keine künstlichen rhetorischen Fragen oder generischen Motivationsfloskeln ergänzen;
- Fachclaims, Zahlen, Quellen, Negationen und Unsicherheit schützen;
- Timing pro Abschnitt gegen das Konzept prüfen.

## Speaker Script

Optional Performance-Hinweise wie `[PAUSE]`, `[BETONUNG]`, `[BLICK]` und Zeitmarken hinzufügen. Hinweise sparsam einsetzen und nicht mit Inhalt vermischen.

## Handoff

Der Draft ist **nicht final**. Nächster Pflichtschritt:

`precision-writing-revision(genre=speech, language=de|en) → speech-review`.
