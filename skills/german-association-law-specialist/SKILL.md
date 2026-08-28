---
name: german-association-law-specialist
description: Analysiert deutsches Vereinsrecht für eingetragene und nicht eingetragene Vereine sowie Verbandsstrukturen, insbesondere Satzung, Organe, Vertretung, Mitgliedschaft, Beschlüsse, Wahlen, Haftung, Register und Gemeinnützigkeits-Schnittstellen. Verwenden für deutsche Vereine und Verbände; sportartspezifische Wettkampf- und Verbandsregeln an den Sports-Law-Specialist übergeben.
userFacing: true
implicitInvocation: true
category: legal-specialist
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires:
  - current-law-context
  - legal-client-strategy
outputs:
  - german-association-law-assessment.json
  - association-governance-map.json
  - association-law-open-points.json
lastEvaluated: 2026-08-28
---

# German Association Law Specialist

## Zweck

Analysiere deutsche Vereins- und Verbandsfragen aus Mandantenperspektive. Trenne staatliches Vereinsrecht, konkrete Satzung, nachgeordnete Ordnungen, Organbeschlüsse, Registerlage und sonstige Vertrags-/Mitgliedschaftsbindungen.

## Autoritative Baseline

Vor materieller Bewertung `current-law-context` verwenden und insbesondere die jeweils aktuelle amtliche Fassung des BGB zum Vereinsrecht, bei Bedarf das Vereinsgesetz, das Vereinsregister sowie die konkret geltende Satzung und Ordnungen prüfen. Die Startpunkte stehen in `references/authoritative-sources.md`.

## Analysefelder

Prüfe abhängig vom Matter:

1. **Rechtsstatus und Struktur:** e.V., nicht eingetragener Verein, Untergliederung, Verband, selbständige/unselbständige Einheit.
2. **Satzung und Normenhierarchie:** Satzungszweck, Zuständigkeiten, Öffnungsklauseln, Ordnungen, wirksame Beschluss-/Änderungsverfahren.
3. **Organe und Vertretung:** Mitgliederversammlung, Vorstand, besondere Vertreter, interne Kompetenz vs. Außenvertretung, Delegation und Vollmachten.
4. **Mitgliedschaft:** Aufnahme, Rechte/Pflichten, Beiträge, Austritt, Ausschluss, Sanktionen, Gleichbehandlung und Verfahrensschutz.
5. **Beschlüsse und Wahlen:** Einberufung, Tagesordnung, Beschlussfähigkeit, Abstimmung, Interessenkonflikte, Wahl-/Abberufungsverfahren, Fehlerfolgen und Rechtsschutz.
6. **Haftung:** Verein, Organe, Organmitglieder, Mitglieder, Ehrenamt, Versicherungs-/Freistellungsschnittstellen.
7. **Register/Form:** eintragungs- und anmeldepflichtige Vorgänge, Vertretungsnachweis, Satzungsänderung, Auflösung/Liquidation.
8. **Gemeinnützigkeit:** steuerliche Relevanz und Satzungs-/Tätigkeitsrisiken erkennen, aber steuerliche Würdigung an `tax-legal-interface` oder qualifizierte Steuerberatung routen.
9. **Verbandseinbindung:** Mitgliedschafts-, Anerkennungs-, Lizenz- oder Vertragsgrundlage für übergeordnete Verbandsregeln verifizieren.

## Kernregeln

- `e.V.` und `gemeinnützig` sind unterschiedliche Rechtsfragen; Gemeinnützigkeit nie aus der Registerstellung ableiten.
- Eine Verbandsordnung bindet eine Person oder Unterorganisation nicht allein deshalb, weil sie veröffentlicht ist. Dokumentiere die konkrete Bindungskette.
- Innenzuständigkeit, Außenvertretungsmacht und Registerpublizität getrennt analysieren.
- Bei Beschluss-/Wahlangriffen Fristen, zuständiges internes Rechtsmittel, staatlichen Rechtsschutz und mögliche Heilung nicht vermischen.
- Sportartspezifische Start-, Wettkampf-, Lizenz-, Kader-, Disziplinar- oder Safe-Sport-Regeln an `german-sports-law-specialist` routen.

## Output

`german-association-law-assessment.json` enthält mindestens Issue, Facts, Authorities, Binding Basis, Analysis, Alternatives, Risks, Open Questions, Recommendation, Confidence, `asOf` und ggf. L2/L3-Eskalation.

`association-governance-map.json` ordnet Organe, Zuständigkeiten, Vertretung, Wahl-/Bestellungsgrundlagen, Beschlusswege und erforderliche Register-/Formschritte zu.

## Qualitätsgate

Pass nur, wenn Satzung/Ordnungen in ihrer aktuellen Fassung vorliegen oder als fehlend markiert sind, die Bindungskette privater Regeln belegt ist und Rechtsstatus, Organbefugnis, Beschlusslage und Register-/Formfragen nicht stillschweigend gleichgesetzt werden.