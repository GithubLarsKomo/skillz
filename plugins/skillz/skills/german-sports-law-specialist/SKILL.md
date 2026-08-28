---
name: german-sports-law-specialist
description: Analysiert deutsches Sportrecht an der Schnittstelle von staatlichem Recht und autonomem Verbandsrecht, insbesondere DOSB-Strukturen, Lizenzen/Startrechte, Disziplinar- und Rechtsbehelfsverfahren, Safe Sport, Anti-Doping, Athleten-/Trainer-/Vereinsbeziehungen, Veranstaltung, Haftung und Datenschutz-/Arbeitsrechts-Handoffs. Verwenden für Sportmatters in Deutschland; sportartspezifische Regeln an den zuständigen Fachverbands-Specialist übergeben.
---

# German Sports Law Specialist

## Zweck

Analysiere deutsche Sportrechtsfragen als Mehrschichtsystem aus staatlichem Recht, Satzungs-/Verbandsautonomie, Mitgliedschaft, Lizenz-/Vertragsbindung und sportartspezifischen Regeln. Der DOSB ist keine staatliche Gesetzgebungsinstanz; seine Regelwerke werden nach ihrer konkreten Bindungsgrundlage bewertet.

## Autoritative Baseline

Nutze `current-law-context`. Startpunkte für DOSB, Safe Sport, NADA/NADC, AntiDopG und staatliches Recht stehen in `references/authoritative-sources.md`. Für sportartspezifische Fragen ist zusätzlich die aktuelle Regelwerksfassung des zuständigen Spitzenfachverbandes erforderlich.

## Analysefelder

1. **Regelwerksschichten und Bindung:** staatliches Recht, Vereinssatzung, Landes-/Spitzenverband, DOSB, Lizenz/Startpass, Athleten-/Trainervertrag, Veranstaltungsausschreibung und sportartspezifische Regeln.
2. **Teilnahme und Status:** Mitgliedschaft, Lizenz, Startberechtigung, Vereins-/Verbandswechsel, Kader-/Nominierungsentscheidungen, Auswahlkriterien und Gleichbehandlung.
3. **Disziplinar- und Verbandsverfahren:** Tatbestand, Regelzuständigkeit, persönliche/sachliche Bindung, Verfahrensgrundlage, Anhörung, Befangenheit, Sanktion, Begründung, Fristen und Rechtsbehelf.
4. **Safe Sport:** prüfen, welches Schutz-/Disziplinarregelwerk die konkrete Organisation tatsächlich wirksam eingeführt hat und welche Personen daran gebunden sind. DOSB-Mustertexte nicht automatisch als unmittelbar geltend behandeln.
5. **Anti-Doping:** NADA/NADC, WADA/WADC, AntiDopG und verbandseigene Anti-Doping-Regeln als getrennte Ebenen behandeln; Ergebnismanagement, Disziplinarweg und Schiedsvereinbarung konkret verifizieren.
6. **Athleten, Trainer und Organisation:** Vertrag, Vergütung/Förderung, Sponsoring, Bild-/Medienrechte, Pflichten, Auswahlentscheidungen; arbeitsrechtliche Fragen an Employment/Labor routen.
7. **Veranstaltung, Sicherheit und Haftung:** Veranstalterpflichten, Verkehrssicherung, Aufsicht/Minderjährige, Versicherungen, Einwilligung und Risikozuweisung.
8. **Daten und Gesundheit:** Athleten-, Leistungs-, Gesundheits- und Anti-Doping-Daten an Privacy/Data routen, wenn eine eigenständige Datenschutzanalyse erforderlich ist.

## DOSB Safe Sport Gate

Vor Anwendung des DOSB Safe Sport Code explizit prüfen:

- Hat der konkrete Verband/Verein den Code oder eine angepasste Fassung wirksam in Satzung/Ordnung übernommen?
- Welche Personen sind unmittelbar Mitglied und welche benötigen Vertrags-/Lizenzbindung?
- Welche Untersuchungs-, Sanktions- und Rechtsbehelfsorgane wurden tatsächlich bestimmt?
- Welche Fassung galt zum relevanten Zeitpunkt?

Fehlt diese Bindung, darf der Muster-Code nicht als automatisch anwendbare Sanktionsgrundlage behandelt werden.

## Safe Sport Investigation Gate

Bei Vorwürfen oder Meldungen kann `internal-investigation-workflow` als Fact-Finding-Verfahren eingesetzt werden. Dabei:

- akute Schutzbedarfe insbesondere bei Minderjährigen zuerst triagieren,
- tatsächlich bindende Vereins-/Verbandsverfahrensregeln separat feststellen,
- HinSchG nur anwenden, wenn persönlicher/sachlicher Anwendungsbereich tatsächlich erfüllt ist,
- staatliche Straf-/Zivil-/Arbeits-/Datenschutzfragen und private Sport-Sanktionen getrennt halten,
- Untersuchung, Disziplinarentscheidung und Rechtsbehelf nicht in einer unkontrollierten Rolle vermischen.

## Rechtsweg und Eskalation

Interne Verbandsrechtswege, Schiedsvereinbarungen und staatlicher Rechtsschutz getrennt erfassen. Nicht pauschal CAS-Zuständigkeit oder Ausschluss staatlicher Gerichte annehmen. Strafrechtliche, arbeitsrechtliche oder hochstreitige Fragen bei Bedarf über `privilege-and-counsel-routing` eskalieren.

## Qualitätsgate

Pass nur, wenn staatliches Recht und Verbandsrecht getrennt, die persönliche und sachliche Bindung jeder privaten Regel nachgewiesen, die aktuelle Fassung geprüft und vorhandene Rechtsbehelfe/Fristen sichtbar sind.
