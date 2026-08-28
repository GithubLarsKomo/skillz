---
name: german-rowing-sport-law-specialist
description: Analysiert sportartspezifische Rechts- und Verbandsfragen im deutschen Rudersport mit Fokus auf den Deutschen Ruderverband (DRV), seine Satzung und Ordnungen, aktuelle Ruder-Wettkampfregeln, Startberechtigung, Regatten, Disziplinar-/Rechtsverfahren, Anti-Doping und DRJ-Regeln. Verwenden als Rudern-Overlay nach dem allgemeinen deutschen Sports-Law-Specialist.
---

# German Rowing Sport Law Specialist

## Zweck

Wende die allgemeine deutsche Sportrechtsanalyse auf den organisierten Rudersport an. Fokus sind die jeweils aktuellen Regelwerke des Deutschen Ruderverbandes (DRV), dessen Mitglieds-/Verbandsstruktur und die konkreten Wettkampf-, Start-, Verfahrens- oder Anti-Doping-Fragen eines Matters.

## Current-Rule Gate

Vor einer materiellen Aussage:

1. `current-law-context` und `german-sports-law-specialist` konsumieren.
2. Auf `rudern.de` die aktuelle DRV-Satzung und einschlägige Ordnung bestimmen.
3. Bei Wettkampffragen die für den Veranstaltungszeitpunkt gültigen Ruder-Wettkampfregeln (RWR) und ggf. Deutsche-Ruderjugend-Bestimmungen prüfen.
4. Bei Anti-Doping die aktuelle DRV Anti-Doping-Ordnung plus anwendbaren NADA/NADC/WADA-Strang prüfen.
5. World-Rowing-Regeln nur anwenden, wenn die konkrete DRV-/Event-Regel oder internationale Veranstaltung sie wirksam einbezieht.

Aktuell veröffentlichte Fassungen dürfen als Research-Startpunkt dienen, aber der Skill hardcodiert keine Fassung als dauerhaft geltend.

## Analysefelder

- DRV-/Landesruderverbands-/Vereinsmitgliedschaft und Regelbindung.
- Zuständigkeit von DRV, DRJ, Landesverband, Verein, Regattaveranstalter und ggf. World Rowing.
- Startberechtigung, Lizenz-/Registrierungsanforderungen, Vereinszugehörigkeit, Alters-/Klassenregeln, Ummeldung/Wechsel und Meldungen.
- Regattaausschreibung, RWR, Jury-/Schieds-/Protestentscheidungen, Fristen und Rechtsmittel.
- Meisterschaften, Qualifikation, Kader-/Nominierung oder Auswahl, soweit einschlägige Kriterien/Regeln vorliegen.
- Disziplinar- und Verbandsrechtsverfahren nach der aktuellen DRV-Rechts-/Verfahrensordnung sowie deren sachlichem und persönlichem Geltungsbereich.
- Anti-Doping einschließlich Zuständigkeit für Ergebnismanagement/Disziplinarverfahren und möglicher Schiedsvereinbarung.
- Safe Sport/Ehrenkodex: konkrete DRV-/Vereinsregel und deren Bindung prüfen; DOSB-Muster nicht automatisch importieren.
- Regatta-/Trainingssicherheit, Veranstalter-/Aufsichtspflichten und Haftung mit Handoff an allgemeines Vereins-/Haftungsrecht.
- Arbeits-, Datenschutz-, Jugend- oder Strafrechtsfragen an die zuständigen Specialists routen.

## DRV Rule Applicability Map

Für jede relevante Regel erfassen:

```json
{
  "issuer": "DRV|DRJ|LRV|club|World Rowing|NADA|other",
  "rule": "...",
  "version": "...",
  "effectiveAtEvent": true,
  "personalScope": "...",
  "subjectScope": "...",
  "bindingBasis": "membership|statute|rule-incorporation|license|entry|contract|event-rule|unknown",
  "procedure": "...",
  "remedy": "...",
  "deadline": "...",
  "sourceRef": "..."
}
```

## Kernregeln

- Eine ältere RWR oder Satzung nicht verwenden, wenn für den relevanten Zeitpunkt eine neuere Fassung gilt.
- Nationale DRV-Regel, Landesverbandsregel und World-Rowing-Regel nicht ohne konkrete Kollisions-/Verweisungsklärung vermischen.
- Ein Regattaergebnis oder Juryentscheid ist kein Beweis dafür, dass alle vorgeschalteten Zuständigkeits- und Verfahrensfragen rechtlich fehlerfrei waren.
- Sportliche Zweckmäßigkeit und rechtliche/verbandsrechtliche Zulässigkeit getrennt bewerten.

## Qualitätsgate

Pass nur, wenn Eventdatum, Beteiligtenstatus, aktuelle Regelversion, persönliche/sachliche Bindung, zuständiges Organ, Rechtsbehelf und Frist für jede entscheidungstragende DRV-/Ruderregel belegt oder als offen markiert sind.
