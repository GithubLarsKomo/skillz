---
name: role-requirements-grilling
description: Klärt den tatsächlichen Bedarf an einer Führungs-, Experten- oder Schlüsselrolle durch fokussiertes Grilling von Auftrag, Ergebnissen, Entscheidungsrechten, Schnittstellen, Kontext, Muss-Kriterien und bewusst ausgeschlossenen Anforderungen. Verwenden, bevor eine Role Architecture oder Stellenbeschreibung entworfen wird.
---

# Role Requirements Grilling

## Trigger

Verwenden, wenn Zweck, Outcomes, Entscheidungsrechte, Scope, Schnittstellen, Capability-Anforderungen oder Nicht-Ziele einer Führungs-, Experten- oder Schlüsselrolle noch nicht ausreichend geklärt sind. Dieser Skill ist die domänenspezifische Fassade für Rollen- und Stellenklärung auf Basis des autoritativen `round-based-requirements-grilling` und beantwortet: **Welche Rolle braucht die Organisation tatsächlich und welche Entscheidungen müssen dazu noch getroffen werden?**

Er entwirft noch keine normative Role Architecture, schreibt keine Stellenanzeige und bewertet keine Kandidaten. Die Grilling-Runtime, Runden- und Statuslogik bleibt ausschließlich beim autoritativen Grilling. Wegen dieser zwingenden Delegation ist `implicitInvocation: false` bewusst gesetzt.

## Voraussetzungen

Erforderlich ist ein konkreter Rollen- oder Besetzungsanlass mit mindestens einem identifizierbaren Stakeholder oder einer nachvollziehbaren Organisationsentscheidung. Vorhandene Stellenprofile, Organigramme, Zielbilder, Suchaufträge, HR-Grading-/Package-Angaben, Reporting-Lines, Standort-/Hybrid-/Reiseregeln, Sprachvorgaben oder Corporate-Templates sind **Evidenz**, aber keine automatisch gültige Rollenarchitektur.

Trenne dabei früh zwischen:

- **rollenbestimmenden Organisationsfakten** wie Reporting Line, tatsächlichem funktionalem Scope, Standort-/Mobilitätsanforderungen, zwingender Sprache oder Entscheidungsrechten,
- **Such-/Kommunikationsmetadaten** wie Package, Bonus, Job Family, gewünschter Dokumentaufbau, Corporate Wording, Branding oder Publikationssprache,
- **historischem Template-Inhalt**, der nur übernommen werden darf, wenn er mit den neu bestätigten Rollenanforderungen übereinstimmt.

Verwende keine geschützten oder sachfremden persönlichen Merkmale als Auswahlkriterien. Formuliere Anforderungen funktionsbezogen und begründe harte Kriterien durch den tatsächlichen Rollenauftrag.

## Ablauf

### Grilling-Dimensionen

Frage bevorzugt nach beobachtbaren Ergebnissen statt nach Wunschprofilen:

1. Warum existiert die Rolle?
2. Welche drei bis fünf Ergebnisse müssen sichtbar werden?
3. Welche Entscheidungen muss die Person selbst treffen dürfen?
4. Welche Ressourcen, Informationen und Eskalationswege braucht sie?
5. Welche Schnittstellen und strukturellen Widerstände prägen die Rolle?
6. Welche Fähigkeiten sind kausal nötig, welche nur historische Proxys?
7. Welche Erfahrungen sind zwingend, trainierbar oder irrelevant?
8. Welche Arbeitsweise passt zum Kontext, ohne Persönlichkeit zu stereotypisieren?
9. Was gehört ausdrücklich nicht zur Rolle?
10. Welche offenen Entscheidungen blockieren die Rollenarchitektur?
11. Welche bestätigten Organisationsfakten müssen später in interner Stellenbeschreibung, Search Brief oder Ausschreibung erscheinen, und welche Angaben sind lediglich HR-/Kommunikationsmetadaten?
12. Gibt es bestehende Corporate-Templates, Organigramme, Sprachfassungen oder Stilvorgaben, deren **Form** übernommen werden soll, ohne veraltete Inhalte ungeprüft zu erben?

Trenne bestätigte Organisationsfakten, Stakeholder-Präferenzen, Annahmen und Hypothesen. Ungeklärte Entscheidungspunkte bleiben sichtbar und werden nicht durch vermeintlich naheliegende Antworten ersetzt.

### Kommunikationskontext ohne Rollenverfälschung

Ein bestehendes Posting oder Briefing darf zwei Arten wertvoller Information liefern:

- **inhaltliche Organisationsfakten**, die nach Stakeholder-Bestätigung in Handoff/Role Architecture gehören;
- **Darstellungs- und HR-Kontext**, der später `job-description-authoring` steuert, aber keine neue Capability oder Auswahlhürde erzeugt.

Ein Titel, Package, Bonus, Job Family oder eine Corporate-Formulierung ist nicht allein deshalb normativ, weil sie in einer bestehenden Ausschreibung steht. Umgekehrt dürfen bestätigte Reporting-, Standort-, Mobilitäts-, Sprach- oder Funktionsscope-Fakten nicht später als bloße Copy-Details behandelt oder wieder zu Platzhaltern degradiert werden.

### Artefaktvertrag

`role-requirements-handoff.json` enthält mindestens `schemaVersion`, `handoffId`, `version`, `status`, Rollenauftrag, Kontext, Outcomes, Entscheidungsrechte, Scope, Interfaces, Constraints, Must-haves, trainierbare Capabilities, Non-Requirements, Success Evidence, Open Decisions, Sources und bei Freigabe `approvedAt`/`approvalAuthority`.

Zusätzlich entsteht `role-requirements-report.md` als lesbare Fassung. Nicht-normative HR-/Template-/Sprachinformationen werden dort als **Kommunikationskontext** bzw. in den Quellen dokumentiert, sofern das Schema dafür kein eigenes Feld vorsieht; sie dürfen nicht künstlich als Capability oder Constraint umetikettiert werden.

### Lebenszyklus

Wird ein bereits verwendeter Requirements-Handoff fachlich geändert, erhält er eine neue Version. Eine frühere Version bleibt nachvollziehbar, wird aber `superseded`. Abgeleitete Role Architectures müssen ihre konkrete Quelle festhalten.

Reine Änderungen von Layout-, Branding- oder Kommunikationsmetadaten erfordern **keine neue normative Handoff-Version**, solange Rollenauftrag, Scope, Constraints, Capabilities oder Auswahlkriterien unverändert bleiben.

## Prüfungen

Prüfe vor Abschluss insbesondere:

- Rollenbestimmende Organisationsfakten sind von HR-/Kommunikationsmetadaten getrennt.
- Vorhandene Templates wurden als Evidenz behandelt und nicht als stillschweigende normative Quelle.
- Bekannte Angaben werden nicht als offene Platzhalter weitergereicht; echte unbekannte Angaben bleiben ausdrücklich offen und werden nicht erfunden.
- Must-haves sind von trainierbaren Fähigkeiten und bloßen Proxys getrennt.
- Keine blockierende Rollenentscheidung bleibt verborgen.

## Fehlerbehandlung

Bei widersprüchlichen Stakeholder-Aussagen den Konflikt explizit halten und eine weitere Grilling-Runde auslösen, statt selbst eine Entscheidung zu erfinden.

Widerspricht ein bestehendes Posting oder Corporate-Template den neu bestätigten Rollenanforderungen, hat die bestätigte Rollenentscheidung Vorrang. Die Abweichung wird für das spätere Authoring sichtbar dokumentiert; sie wird nicht durch Mittelung oder sprachliche Abschwächung kaschiert.

Ein bloßer Wunsch nach einer Stellenanzeige ist kein Grund, die normative Zwischenstufe zu überspringen. **Keine Job Description direkt** aus dem Grilling erzeugen.

## Übergabe

Nach Klärung an `role-architecture` übergeben. Zusätzlich darf bestätigter nicht-normativer Kommunikationskontext – Corporate-Template, gewünschte Dokumentstruktur, Package/Job-Family-Angaben, Sprachfassungen, Branding oder Organigramm – als **separate ergänzende Evidenz** an `job-description-authoring` weitergereicht werden. Dieser Kontext darf die Role Architecture nicht umgehen oder verändern.

## Abschlusskriterien

Abgeschlossen ist der Skill, wenn Rollenbedarf, kausale Fähigkeiten, blockierende Entscheidungen und die Grenze zwischen normativen Organisationsfakten und Kommunikationsmetadaten belastbar geklärt sind.