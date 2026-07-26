---
name: central-skill-repository-curation
description: Erkennt wiederverwendbare Arbeitsabläufe aus Projekten und Gesprächen, konsolidiert sie als versionierte Skills und pflegt sie im zentralen Repository GithubLarsKomo/skillz einschließlich Katalog, Herkunft und Aktualisierungsregeln. Ausdrücklich bestätigte neue oder geänderte Skills werden im selben Arbeitsgang zentral aktualisiert, geprüft, committed und gepusht.
---

# Zentrale Skill-Repository-Pflege

## Zweck

Dieses Skill beschreibt das verbindliche Vorgehen, um wiederverwendbare Arbeitsabläufe aus Projekten, erfolgreichen Problemlösungen und ausdrücklich als Skill bezeichneten Verfahren dauerhaft im Repository `GithubLarsKomo/skillz` zu sichern.

Das zentrale Repository ist die maßgebliche Sammlung. Projektrepositories dürfen lokale Kopien enthalten, aber fachliche Weiterentwicklungen werden zusätzlich im zentralen Skill aktualisiert.

## Auslöser

Der Skill wird angewendet, wenn mindestens eine der folgenden Situationen eintritt:

- Der Nutzer sagt ausdrücklich, ein Vorgehen solle gelernt oder als Skill gespeichert werden.
- Ein wiederverwendbarer Ablauf wurde erfolgreich praktisch erprobt.
- In einem Projekt entsteht eine `SKILL.md`, die auch außerhalb dieses Projekts nutzbar ist.
- Ein bestehender Skill wird fachlich erweitert, korrigiert oder durch neue Betriebserfahrung präzisiert.
- Der Nutzer verlangt, alle bisher erzeugten Skills zentral zu pflegen.

Eine ausdrückliche Bestätigung wie „lerne das“, „ergänze den Skill“, „merke dir das als Skill“ oder eine sinngleiche Formulierung ist zugleich der Auftrag, die zentrale Fassung im selben Arbeitsgang zu aktualisieren und zu veröffentlichen, sofern Repository und Schreibzugriff verfügbar sind. Eine bloße Beschreibung oder ein Vorschlag der Änderung genügt dann nicht.

## Zielstruktur

Jeder Skill erhält ein eigenes Verzeichnis:

```text
skills/
  <skill-slug>/
    SKILL.md
```

Optional zulässige Begleitdateien:

```text
examples/
templates/
schemas/
tests/
CHANGELOG.md
```

Begleitdateien werden nur angelegt, wenn sie für die Wiederverwendung notwendig sind.

## Namensregeln

- englischer, kleingeschriebener Slug
- Wörter mit Bindestrichen trennen
- Name beschreibt die Fähigkeit, nicht ein einzelnes Projekt
- keine Versionsnummer im Verzeichnisnamen
- keine Personen-, Kunden- oder Unternehmensgeheimnisse im Namen

## Mindestinhalt jeder SKILL.md

Jede Datei enthält YAML-Frontmatter mit mindestens:

```yaml
---
name: <skill-slug>
description: <präzise Beschreibung von Trigger, Zweck und Ergebnis>
---
```

Der Hauptteil beschreibt mindestens:

1. Zweck und Abgrenzung
2. Auslöser
3. Voraussetzungen
4. verbindlichen Ablauf
5. Prüfungen und Erfolgskriterien
6. Fehlerbehandlung
7. Sicherheits- und Datenschutzgrenzen
8. Abschlusszustand

## Konsolidierungsablauf

### 1. Skill-Kandidat erkennen

Prüfen, ob das Verfahren:

- wiederholbar ist,
- über ein einzelnes Projekt hinaus nützlich ist,
- einen klaren Auslöser und Abschluss besitzt,
- ausreichend erprobt oder fachlich begründet ist.

Ein einmaliger Code-Fix ohne übertragbaren Ablauf ist kein eigener Skill.

### 2. Quellen erfassen

Mögliche Quellen sind:

- bestehende `SKILL.md` in anderen Repositories,
- erfolgreich ausgeführte Befehlsfolgen,
- dokumentierte Troubleshooting-Verfahren,
- Grilling-Reports und freigegebene Spezifikationen,
- ausdrücklich bestätigte Arbeitsweisen aus dem Gespräch.

Die Herkunft wird in README, Skill oder Changelog nachvollziehbar beschrieben, ohne vertrauliche Gesprächsinhalte zu kopieren.

### 3. Fachlich abstrahieren

Projektgebundene Angaben werden in wiederverwendbare Regeln überführt:

- konkrete Repository-Namen nur behalten, wenn sie Teil des verbindlichen Systems sind,
- Tokens, Passwörter, lokale Pfade und personenbezogene Daten entfernen,
- produktspezifische Schritte als Beispiele kennzeichnen,
- stabile Prinzipien von austauschbaren Implementierungsdetails trennen.

### 4. Duplikate prüfen

Vor dem Anlegen eines neuen Skills prüfen:

- existiert bereits ein Skill mit gleichem Ziel,
- ist die neue Erkenntnis nur eine Erweiterung,
- sollten zwei überlappende Skills zusammengeführt werden,
- bleibt ein projektspezifischer Spezialfall besser als Unterabschnitt erhalten.

Bei fachlicher Überschneidung wird bevorzugt der bestehende Skill aktualisiert statt ein nahezu identischer Skill angelegt.

### 5. Skill schreiben oder aktualisieren

- neuen Skill unter `skills/<slug>/SKILL.md` anlegen,
- bei Aktualisierung zuerst den aktuellen Stand lesen,
- bestehende bewährte Inhalte erhalten,
- neue Regeln widerspruchsfrei integrieren,
- unsichere oder noch nicht erprobte Schritte ausdrücklich kennzeichnen.

### 6. Zentralen Katalog aktualisieren

Die `README.md` des Repositories enthält für jeden Skill:

- Link zur `SKILL.md`,
- kurze Zweckbeschreibung,
- Herkunft oder Entstehungskontext.

Neue Skills und Umbenennungen müssen dort im selben Arbeitsgang eingetragen werden. Bei wesentlichen fachlichen Erweiterungen ist zusätzlich zu prüfen, ob die Kurzbeschreibung im Katalog angepasst werden muss.

### 7. Versionieren und veröffentlichen

Commit-Nachrichten folgen bevorzugt Conventional Commits:

```text
feat(skill): add <skill-name>
docs(skill): refine <skill-name>
fix(skill): correct <skill-name> workflow
refactor(skill): consolidate overlapping skills
```

Ein Commit soll einen logisch zusammenhängenden Skill-Schritt enthalten. Skill-Datei und zugehöriger Katalogeintrag dürfen in getrennten Commits erfolgen, müssen aber am Ende konsistent sein.

Bei ausdrücklich bestätigten Skill-Lern- oder Erweiterungsaufträgen umfasst der Abschluss standardmäßig:

1. zentrale Skill-Datei lesen,
2. Änderung integrieren,
3. Katalogkonsistenz prüfen und gegebenenfalls aktualisieren,
4. Sicherheits- und Qualitätsprüfung durchführen,
5. committen,
6. auf das zentrale GitHub-Repository pushen,
7. Commit-Hash und betroffene Dateien berichten.

Es wird nicht erneut nach einer Push-Freigabe gefragt, wenn der Nutzer die Skill-Übernahme oder -Erweiterung bereits ausdrücklich beauftragt hat und Schreibzugriff vorhanden ist.

### 8. Ergebnis prüfen

Vor Abschluss kontrollieren:

- YAML-Frontmatter ist gültig,
- Verzeichnisname und `name` stimmen überein,
- README-Link zeigt auf den richtigen Pfad,
- keine Zugangsdaten oder vertraulichen Inhalte wurden übernommen,
- Ablauf besitzt klare Erfolgskriterien,
- vorhandene Skills wurden nicht widersprüchlich dupliziert,
- die veröffentlichte Fassung enthält die bestätigte fachliche Änderung vollständig.

## Laufende Pflege

Nach jeder künftig ausdrücklich bestätigten Skill-Lernentscheidung wird geprüft, ob:

1. ein neuer Skill angelegt werden muss,
2. ein bestehender Skill erweitert werden muss,
3. lediglich ein projektspezifisches Beispiel ergänzt wird,
4. der zentrale README-Katalog angepasst werden muss.

Diese Prüfung ist kein rein gedanklicher Nachlauf. Liegt ein zentral relevanter Änderungsbedarf vor und besteht Schreibzugriff, wird die Änderung unmittelbar im Repository umgesetzt, committed und gepusht.

Das zentrale Repository wird nicht nur als Archiv, sondern als maßgebliche, fortlaufend gepflegte Wissensbasis behandelt.

## Umgang mit lokalen Skill-Kopien

Besteht ein Skill zusätzlich in einem Projektrepository:

- wird die vollständigere und aktuellere Fassung ermittelt,
- werden allgemein gültige Änderungen nach `skillz` übernommen,
- bleiben projektspezifische Betriebsdetails im Projekt,
- wird eine bewusste Abweichung dokumentiert,
- werden lokale Kopien nicht ungeprüft überschrieben.

## Fehlerbehandlung

### Repository oder Schreibzugriff fehlt

- Repository und Berechtigungen prüfen,
- keine erfolgreiche Speicherung behaupten,
- den fertigen Skill-Inhalt lokal oder im Chat bereitstellen, bis der Push möglich ist.

### Skill existiert bereits

- vorhandene Datei lesen,
- Unterschiede fachlich bewerten,
- aktualisieren oder bewusst nicht ändern,
- keine parallele Dublette mit leicht verändertem Namen erzeugen.

### Quellen widersprechen sich

- den zuletzt erfolgreich erprobten und bestätigten Ablauf bevorzugen,
- relevante Unterschiede transparent dokumentieren,
- destructive oder sicherheitsrelevante Änderungen nicht stillschweigend übernehmen.

## Sicherheitsgrenzen

Nicht in das Repository gehören:

- Passwörter, API-Schlüssel und Zugriffstokens,
- private Schlüssel oder Zertifikate,
- personenbezogene Daten,
- interne vertrauliche Dokumentinhalte,
- temporäre Zuganglinks,
- ungeprüfte Schadcode- oder Umgehungsanweisungen.

Beispielwerte müssen eindeutig als Platzhalter erkennbar sein.

## Abschlusskriterien

Die Pflege ist abgeschlossen, wenn:

- der Skill im zentralen Repository angelegt oder aktualisiert ist,
- der README-Katalog konsistent ist,
- die Änderungen committed und auf GitHub veröffentlicht wurden,
- Commit-Hash und betroffene Dateien berichtet wurden,
- zukünftige Anwendungen auf diesen zentralen Skill Bezug nehmen können.