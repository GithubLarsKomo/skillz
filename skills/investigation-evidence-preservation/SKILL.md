---
name: investigation-evidence-preservation
description: Plant und dokumentiert rechtmäßige Beweissicherung für interne Untersuchungen einschließlich Originalerhalt, Collection Scope, Chain of Custody, Legal-Hold-/Retention-Konflikten, Datenschutz und Zugriffsbefugnissen. Verwenden vor oder unmittelbar zu Beginn einer internen Investigation.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - current-law-context
  - privilege-and-counsel-routing
outputs:
  - investigation-evidence-preservation-plan.json
  - investigation-evidence-register.json
  - investigation-legal-hold-plan.md
lastEvaluated: 2026-08-28
---

# Investigation Evidence Preservation

## Zweck

Sichere relevante Informationen früh, nachvollziehbar und rechtmäßig, ohne aus „Investigation“ eine pauschale Zugriffserlaubnis abzuleiten.

## Preservation Gate

1. Ereignis, Allegations, Zeitraum und plausible Datenquellen bestimmen.
2. Drohenden Verlust/Überschreibung und bestehende Retention-/Deletion-Prozesse identifizieren.
3. Mit `privilege-and-counsel-routing` prüfen, ob Litigation Hold, externe Counsel-Steuerung oder besondere Kommunikationsregeln erforderlich sind.
4. Für jede Quelle Zugriffsbefugnis, Datenschutz-/Beschäftigtendatenlage, Betriebsrats-/Mitbestimmungstrigger und grenzüberschreitende Transfers prüfen.
5. Preservation von Collection trennen: Daten können erhalten werden, ohne sofort vollständig ausgewertet oder breit kopiert zu werden.

## Evidence Discipline

- Originale erhalten; Arbeitskopien getrennt kennzeichnen.
- Quelle, Custodian, Collector, Datum/Zeit, Methode, Hash/Integritätsmerkmal soweit sinnvoll und jede Übergabe protokollieren.
- Keine Umgehung von Zugriffskontrollen, Passwörtern, privaten Konten/Geräten oder technischen Schutzmaßnahmen ohne rechtmäßige Autorität.
- Scope und Suchbegriffe so eng wie mit Untersuchungszweck und Beweissicherung vereinbar halten.
- Besondere Kategorien, strafrechtlich sensible Daten und private Kommunikation gesondert routen.
- Legal Hold ist kein automatischer Standardbegriff mit universeller Rechtswirkung; Pflicht, Scope, Adressaten und Ende werden jurisdiktionsbezogen bestimmt.

## Retention Conflict Gate

Bei Konflikt zwischen regulärer Löschung, HinSchG-Dokumentationsregeln, Datenschutz-Speicherbegrenzung, QMS-Aufbewahrung, Litigation Hold oder Behördenpflichten keine pauschale längste Frist wählen. Die konkrete Authority, Zweckbindung und Verhältnismäßigkeit werden dokumentiert.

## Routing

Produkt-/Qualitätsdaten können parallel an bestehende Complaint-, Vigilance-, CAPA- oder Audit-Skills gehen. Die Investigation ersetzt keine regulatorische Record-Preservation- oder Reportability-Pflicht.

## Qualitätsgate

Pass nur, wenn Evidence Scope, rechtmäßiger Zugriff, Integrität/Chain of Custody, Datenschutz, Retention-Konflikte und Privilege/Counsel-Gates sichtbar sind und keine unbefugte Datenerhebung als Investigation-Mittel empfohlen wird.
