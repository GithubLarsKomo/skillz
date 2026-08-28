---
name: privilege-and-counsel-routing
description: Bewertet für einen Legal Matter Schutz-, Vertraulichkeits- und Eskalationsbedarf, ohne pauschal anwaltliches Privileg zu behaupten, und routet Fragen nach interner Bearbeitung, qualifiziertem externem Counsel, Behörde, Notar oder sonstiger zwingender Autorität. Verwenden früh im Matter und erneut vor irreversiblen Rechtsentscheidungen.
userFacing: true
implicitInvocation: true
category: workflow
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - legal-matter-intake
outputs:
  - privilege-routing.json
  - counsel-scope.json
  - external-counsel-brief.md
lastEvaluated: 2026-08-28
---

# Privilege and Counsel Routing

## Zweck

Schütze sensible Legal-Arbeit und verhindere, dass Skillz Befugnisse oder Schutzwirkungen simuliert, die nur qualifizierte Berufsträger, Gerichte, Behörden, Notare oder andere Stellen erzeugen können.

## Kernregeln

- Legal Privilege, anwaltliche Verschwiegenheit, Beschlagnahmeschutz und Work-Product-Schutz sind jurisdiktions- und rollenspezifisch; keine US-artige Schutzwirkung pauschal auf In-house-Kommunikation übertragen.
- Vertraulichkeit ist nicht automatisch Privileg.
- Litigation Hold, Beweissicherung und Kommunikationsdisziplin werden bei Streit-/Investigation-Risiko früh geprüft.
- Externer Counsel wird nicht für jede Frage verlangt: Skillz soll Facts, Quellen, Alternativen und die verbleibende Fachfrage maximal vorbereiten.

## Eskalationsstufen

- `L0 autonomous`: vorbereitende Analyse ohne besondere Freigabe.
- `L1 executive-authorization`: Unternehmens-/Organentscheidung oder akzeptiertes wesentliches Restrisiko erforderlich.
- `L2 specialist-validation`: qualifizierte interne Fachfunktion oder benannter Specialist muss validieren.
- `L3 external-authority`: externer Rechtsanwalt, Patentanwalt, Notar, Steuerberater, Gericht, Behörde oder andere rechtlich erforderliche Stelle.

## Workflow

1. Matter-Typ, Jurisdiktion, Streit-/Investigationsnähe und Sensitivität prüfen.
2. Schutzstatus und Dokumentations-/Kommunikationsregeln bestimmen.
3. Materielle Fragen nach L0-L3 klassifizieren.
4. Bei L3 eine enge Frage mit Facts, Sources, Uncertainties und gewünschter Entscheidung formulieren.
5. `privilege-routing.json`, `counsel-scope.json` und bei Bedarf `external-counsel-brief.md` ausgeben.

## Qualitätsgate

Pass nur, wenn keine Schutzwirkung erfunden, L3-Fragen eng formuliert und interne Analyse trotz Eskalation soweit sinnvoll fortgeführt wird.