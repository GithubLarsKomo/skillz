---
name: legal-matter-final-gate
description: Prüft vor Abschluss, Unterzeichnung, Veröffentlichung oder irreversibler Legal-/Compliance-Aktion, ob Specialist-Fragen, aktuelle Rechtsgrundlage, Risiken, Freigaben und externe Authority-Gates ausreichend geklärt sind. Verwenden als letztes Matter-Gate; der Skill erteilt keine externe Genehmigung.
---

# Legal Matter Final Gate

## Gate States

- `ready`
- `ready-with-accepted-risk`
- `executive-decision-required`
- `specialist-validation-required`
- `external-counsel-required`
- `external-authority-pending`
- `blocked`

## Prüfungen

1. Matter Scope und Mandantenziel unverändert oder bewusst aktualisiert?
2. Aktuelle Rechts-/Regelwerksgrundlage mit `asOf` vorhanden?
3. Alle critical/high Specialist Work Orders beantwortet oder ausdrücklich deferred?
4. Specialist-Widersprüche gelöst oder entscheidungsfähig dokumentiert?
5. Legal Risk Register aktuell; Residual Risks autorisiert?
6. Privilege/Confidentiality/Litigation-Hold-Anforderungen eingehalten?
7. Notar-, Behörde-, Gericht-, externer Counsel- oder andere L3-Gates erfüllt?
8. Offene Punkte verändern die vorgesehene Aktion nicht unkontrolliert?

## Kernregeln

- Sprachliche oder dokumentarische Vollständigkeit ist kein Legal-Ready-Nachweis.
- Externe Freigaben werden nur aus verifizierter externer Evidenz als erfüllt markiert.
- `ready-with-accepted-risk` verlangt explizite Risk Acceptance mit Autorität.

## Qualitätsgate

Pass nur, wenn der ausgegebene Gate State durch konkrete Evidence-/Decision-Referenzen begründet ist und kein externer Rechtsstatus simuliert wird.
