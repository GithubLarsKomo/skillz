---
name: legal-matter-intake
description: Strukturiert neue unternehmerische oder private Rechts- und Compliance-Sachverhalte in einen belastbaren Matter-Kontext mit Mandantenziel, Parteien, Fakten, Annahmen, Jurisdiktionen, Fristen, Dokumenten, Autorität und offenen Punkten. Verwenden, bevor ein Legal-Specialist, Vertragsworkflow oder Compliance-Workflow fachlich arbeitet.
---

# Legal Matter Intake

## Zweck

Erzeuge den gemeinsamen, domänenneutralen Matter-Kontext für Legal, Compliance und angrenzende Regulatory-/IP-Workflows. Der Skill entscheidet keine materielle Rechtsfrage.

## Trigger

Verwenden bei neuen Vertrags-, Gesellschafts-, Vereins-, Sport-, Arbeits-, Datenschutz-, Compliance-, Streit-, IP-, Transaktions- oder privaten Rechtsfragen, wenn Scope und Mandantenziel noch nicht als strukturierter Matter-Kontext vorliegen.

## Kernregeln

- Trenne `facts`, `assumptions`, `unknowns` und `userPreferences` strikt.
- Bestimme `corporate|private`, Mandant bzw. zu schützende Partei, Gegenparteien und deren Rollen.
- Erfasse Jurisdiktionen als Hypothese, bis anwendbares Recht und Forum verifiziert sind.
- Fristen, Verjährungs-/Ausschlussrisiken, bereits laufende Verfahren und irreversible Schritte werden früh sichtbar gemacht.
- Dokumente werden mit Status `available|missing|partial|unreadable|unverified` erfasst; fehlender Inhalt wird nie erfunden.
- `privilegeState` wird nur vorläufig markiert; die rechtliche Einordnung gehört zu `privilege-and-counsel-routing`.
- Grilling ist optional: Rufe `round-based-requirements-grilling` nur auf, wenn materielle Nutzerentscheidungen oder Fakten fehlen, die nicht aus vorhandenen Unterlagen ableitbar sind.

## Workflow

1. Nutzerziel und zu schützende Partei fixieren.
2. Matter-Typen, Parteien, Rollen und wirtschaftlichen Kontext erfassen.
3. Fakten, Annahmen, Unbekanntes und widersprüchliche Angaben trennen.
4. Jurisdiktionen, relevante Organisationen/Verbände, Verträge und Regelwerke als Scope-Hypothesen erfassen.
5. Dokumente, Fristen, Geld-/Haftungsexposure und bestehende Entscheidungen aufnehmen.
6. Offene Punkte nach `blocking|important|optional` priorisieren.
7. `legal-matter.json` und `legal-intake-open-points.json` ausgeben.

## Übergabeformat

`legal-matter.json` enthält mindestens:

```json
{
  "schemaVersion": 1,
  "matterId": "LM-...",
  "matterClass": "corporate|private",
  "client": {"name": "...", "role": "..."},
  "clientObjective": "...",
  "matterTypes": [],
  "parties": [],
  "jurisdictions": [],
  "facts": [],
  "assumptions": [],
  "unknowns": [],
  "documents": [],
  "deadlines": [],
  "economicExposure": [],
  "authority": [],
  "privilegeState": "unassessed|internal-confidential|legal-review|external-counsel|litigation-hold",
  "asOf": "YYYY-MM-DD"
}
```

## Grenzen

- Keine Rechtsberatung oder materielle Subsumtion.
- Keine definitive Bestimmung von anwendbarem Recht ohne Legal Context.
- Keine stillschweigende Annahme, dass Verbandsregeln automatisch für jede Person oder Organisation gelten.

## Qualitätsgate

Pass nur, wenn Mandantenziel, Parteien, Fakten/Annahmen/Unknowns, Jurisdiktionshypothesen, Fristen und Dokumentstatus nachvollziehbar sind und alle blockierenden Lücken sichtbar bleiben.
