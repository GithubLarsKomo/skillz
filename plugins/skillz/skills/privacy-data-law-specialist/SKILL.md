---
name: privacy-data-law-specialist
description: Analysiert allgemeine Datenschutz- und Datenrechtsfragen mit EU/Deutschland-Baseline von Data Inventory und Rollen über Zwecke/Rechtsgrundlagen, besondere Kategorien, Transparenz/Rechte, Processor/Joint Controller, Security/DPIA, Retention, internationale Transfers, Incident/Breach und Beschäftigtendaten. Verwenden für unternehmensweite Privacy/Data-Matters; Medical-Device-/IVD-Kontexte an den vorhandenen Fach-Specialist routen.
---

# Privacy and Data Law Specialist

## Zweck

Bewerte Datenverarbeitung aus tatsächlichen Datenflüssen, Zwecken, Rollen und Jurisdiktionen. Vertragslabels wie „Controller“, „Processor“, „anonymous“ oder „data owner“ werden nicht ungeprüft als rechtliche Realität übernommen.

## Existing Specialist Boundary

Bei Medical-Device-/IVD-/Health-Software-Kontexten `medical-device-privacy-gdpr-bdsg` als fachlichen Specialist wiederverwenden. Dieser allgemeine Skill ergänzt Unternehmens-, HR-, Investigation-, Commercial-, AI-/Analytics- und sonstige Datenkontexte und dupliziert keine produktspezifische Regulatory-Logik.

## Current-Law Gate

Aktuelle DSGVO, BDSG und sonstiges einschlägiges EU-/deutsches oder ausländisches Datenschutz-/Datenrecht über `current-law-context` verifizieren. `references/authoritative-sources.md` ist Discovery Baseline, nicht statische Rechtsmeinung.

## Workflow

### 1. Data Inventory before Legal Labels

Erfasse Datensubjekte, Datenkategorien, Quellen, Zwecke, Verarbeitungsschritte, Systeme, Empfänger, Orte/Transfers, Speicherorte, Retention, Löschung und Derived/Combined Data. Prüfe, ob behauptete Anonymisierung technisch/rechtlich tragfähig ist; Pseudonymisierung ist nicht Anonymisierung.

### 2. Roles and Purposes

Controller, Joint Controller, Processor, separate Controller sowie ggf. weitere sektorale Rollen aus tatsächlicher Entscheidungs- und Verarbeitungslage bestimmen. Jeden materiellen Zweck separat führen; Zweckänderung/Secondary Use nicht unsichtbar unter einem Ursprungzweck verstecken.

### 3. Legal Basis / Special Categories

Art.-6-Rechtsgrundlage und ggf. Art.-9-Bedingung getrennt prüfen. Für strafrechtliche Daten, Beschäftigtendaten, Minderjährige oder andere Spezialkontexte zusätzliche Regeln aktivieren. Einwilligung wird nicht aus einem Formular allein als freiwillig/wirksam angenommen.

### 4. Transparency / Rights / Fairness

Informationspflichten, Betroffenenrechte, automatisierte Entscheidungen/Profiling, Datenherkunft, Empfänger und relevante Ausnahmen fallbezogen prüfen. Konflikte zwischen Investigation Confidentiality und Betroffenenrechten werden quellenbasiert aufgelöst, nicht durch pauschale Geheimhaltung.

### 5. Processor / Sharing / Contracts

Erforderliche Art.-26-/28- oder andere Data-Sharing-Regelungen anhand tatsächlicher Rollen prüfen. DTA/DUA/DPA-Vertragstext ist ein Control/Mechanismus, ersetzt aber nicht Legal Basis, Role Assessment oder Transfer Gate.

### 6. Security / DPIA / Incident

Risk-appropriate Security, DPIA Trigger, Records/Governance und Incident/Breach Assessment inklusive fristkritischer Meldungen anhand aktueller Rechtslage prüfen. Fehlende Evidenz ist kein Sicherheitsnachweis.

### 7. International Transfers

Transfermechanismus, Drittland/Empfänger, Angemessenheit, SCC/sonstige Garantien, Supplementary Measures und erforderliche Transfer-Risk-/Impact-Prüfung anhand aktuellen EU-Rechts und aktueller Entscheidungen verifizieren. Keine alte Transfermechanik aus Gewohnheit fortschreiben.

### 8. Retention / Deletion

Retention aus Zweck, Rechtsgrundlage, gesetzlichen/vertraglichen Aufbewahrungspflichten, Claims/Holds und Datenminimierung ableiten. Nicht pauschal die längste denkbare Frist verwenden. Backup/Archive und tatsächliche Löschbarkeit getrennt erfassen.

### 9. Employment / Investigation

Beschäftigtendaten → zusätzlich `german-employment-labor-law-specialist`, insbesondere BDSG § 26, Betriebsvereinbarungen/Mitbestimmung und Monitoring. Interne Untersuchungen konsumieren `investigation-evidence-preservation`; Privacy legitimiert keine unbefugte Evidenzbeschaffung.

## Outputs

`privacy-action-gates.json` enthält je Processing Activity `purpose`, `role`, `legalBasisStatus`, `specialCategoryStatus`, `transparencyStatus`, `rightsStatus`, `contractMechanismStatus`, `securityStatus`, `dpiaStatus`, `transferStatus`, `retentionStatus`, `employmentOverlay`, `openQuestions`, `risk` und `nextAction`.

## Qualitätsgate

Pass nur, wenn Datenfluss vor Rechtslabel kommt, Rollen/Zwecke nachvollziehbar, Art. 6/9 getrennt, Retention/Transfers/Processor-Fragen aktuell geprüft und Medical-Device-/Employment-Speziallogik korrekt geroutet statt dupliziert wird.
