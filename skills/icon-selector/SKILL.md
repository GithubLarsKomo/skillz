---
name: icon-selector
description: Wählt aus einer registrierten Icon-Bibliothek das semantisch passendste vorhandene Icon und eine zulässige Farb-/Kontrastvariante anhand von Intent, Kontext, Domain, Zielmedium und Hintergrund. Verwenden intern vor dem Platzieren von Icons in Präsentationen, Dokumenten oder anderen gebrandeten Artefakten; keine Icons erfinden, umzeichnen oder regulatorische/klinische Bedeutung aus einem Symbol ableiten.
userFacing: false
implicitInvocation: true
version: 0.1.0
status: candidate
owners:
  - GithubLarsKomo
requires: []
outputs:
  - icon-selection.json
lastEvaluated: 2026-09-02
---

# Icon Selector

## Zweck

Dieser Skill verwandelt eine semantische Icon-Anfrage plus Brand-/Bibliothekskontext in genau eine begründete primäre Icon-Auswahl, zulässige Varianten und höchstens wenige Alternativen. Er rendert, verändert und verteilt keine Icon-Binaries.

## Eingabe

Mindestens erforderlich:

- `intent` — was das Icon ausdrücken soll;
- `provider` oder genügend Brand-/Kontextinformation, um genau einen registrierten Provider zu bestimmen.

Optional:

- `context` — konkrete Aussage des Message-Blocks;
- `domain` — z. B. executive, laboratory, regulatory, IT, HR;
- `medium` — presentation, document, pdf, web;
- `background` — light, dark, photo;
- `statusMeaning` — falls das Icon einen Status begleitet;
- `criticalMeaning` — true, wenn Fehlinterpretation sicherheits-, regulatorisch- oder entscheidungsrelevant wäre;
- `exactProject`, `technique`, `portfolio` — explizite enge Semantik, wenn vorhanden.

## Provider

Vor Auswahl `references/provider-registry.json` lesen. Jeder Provider muss auf einen menschenlesbaren Systemvertrag und einen maschinenlesbaren semantischen Katalog zeigen.

Aktuell registriert:

- `euroimmun-corporate` -> `docs/corporate/euroimmun/ICON_SYSTEM.md` + `docs/corporate/euroimmun/icon-semantic-catalog.json`.

Wenn kein registrierter Provider eindeutig passt, keinen Corporate-Fallback erfinden. `status = "unresolved-provider"` ausgeben.

## Auswahlpriorität

Wenn der Provider diese Klassen unterstützt, in dieser Reihenfolge prüfen:

1. exakt benanntes Project-/Program-Icon nur für genau dieses Projekt;
2. exakte Technik-/Plattformsemantik;
3. Portfolio-/Indikationssemantik;
4. spezifischstes Essential-/Generic-Icon;
5. generischer Fallback nur, wenn der Provider ihn ausdrücklich zulässt.

Ein breiteres Icon darf ein verfügbares engeres Icon nicht verdrängen, nur weil es bekannter aussieht.

## Routing-Ablauf

1. **Provider auflösen.** Brand/Library gegen Registry prüfen.
2. **Provider-Verträge laden.** Systemregeln und semantischen Katalog lesen.
3. **Intent normalisieren.** Aliases, Legacy-Schreibweisen und deutsch/englische Synonyme anwenden; kanonischen Asset-Namen nicht umbenennen.
4. **Enge Semantik prüfen.** `exactProject`, `technique`, `portfolio` vor generischen Kategorien behandeln.
5. **Kandidaten bilden.** Preferred-Routing, Alias-Treffer und passende semantische Kategorie priorisieren.
6. **Ambiguitäten auflösen.** Kontext und Domain verwenden; bei echter Bedeutungsunsicherheit nicht raten.
7. **Claim-Safety prüfen.** Icon darf keine regulatorische Freigabe, Intended Use, Performance, klinische Evidenz oder positiven Status implizieren, wenn dies nicht explizit belegt ist.
8. **Variante wählen.** Nur Varianten verwenden, die der Provider für den Hintergrund zulässt; kein Recoloring gegen Provider-Regel.
9. **Text-Redundanz markieren.** Bei `criticalMeaning=true` oder Status-/Risikoaussagen `requiresTextLabel=true` setzen.
10. **Output erzeugen.** Genau einen primären Treffer, maximal drei Alternativen und offene Unsicherheiten ausgeben.

## Ambiguitätsregel

Nicht nur lexikalisch matchen. Bedeutung schlägt Wortähnlichkeit.

Beispiele beim EUROIMMUN-Provider:

- strategisches Ziel -> `hit the bullseye`; analytische Präzision -> `Precision`;
- Literatur-/Evidenzsuche -> `magnifying glass`; Laborwissenschaft -> `microscope`;
- Programmrisko -> `risk protection`; geschützter Zugang -> `shield lock`;
- Laborautomation -> `automatic lab`; Portfolio-Automation -> `Automation`;
- Dokument/Dossier -> `Document`; Dateiformat explizit PDF -> `PDF`.

## Output Contract

`icon-selection.json`:

```json
{
  "schemaVersion": 1,
  "provider": "euroimmun-corporate",
  "status": "selected",
  "request": {
    "intent": "analytical precision",
    "context": "assay robustness",
    "domain": "laboratory",
    "medium": "presentation",
    "background": "light",
    "criticalMeaning": false
  },
  "selection": {
    "canonicalName": "Precision",
    "family": "Essential icons",
    "variant": "clover",
    "assetStem": "Precision",
    "rationale": "Analytical precision/robustness is narrower than generic target semantics.",
    "confidence": "high",
    "requiresTextLabel": false
  },
  "alternatives": [],
  "warnings": []
}
```

Statuswerte:

- `selected`
- `ambiguous`
- `unresolved-provider`
- `no-approved-match`

Bei `ambiguous` keine scheinpräzise Primärauswahl erzwingen; Kandidaten und benötigte Kontextinformation angeben.

## Sicherheits- und Governance-Regeln

- Keine nicht vorhandenen Icons erfinden oder aus fremden Libraries beimischen.
- Keine proprietären Binaries in das öffentliche Skillz-Repo übernehmen.
- Keine SVGs umzeichnen, tracen oder gegen Provider-Vertrag recolorieren.
- Project Icons nie als generische Symbole zweckentfremden.
- Kritische Bedeutung nie nur durch Icon oder Farbe ausdrücken.
- Technik-/Indikationsicons nie als Beleg für regulatorischen Status, Intended Use, Validierung oder Performance behandeln.
- Positiv konnotierte Statusicons nur bei tatsächlich positivem Status verwenden.

## Fehlerbehandlung

- Provider unbekannt -> `unresolved-provider`.
- Katalog/Vertrag fehlt -> `no-approved-match` plus fehlende Quelle nennen.
- Zwei semantisch gleich plausible Kandidaten -> `ambiguous`; keine willkürliche Auswahl.
- Passender Name vorhanden, aber Variante für Hintergrund unzulässig -> alternative zugelassene Variante wählen; sonst `no-approved-match`.
- Intent würde einen unbelegten Claim erzeugen -> Auswahl verweigern oder neutrales Icon nur dann wählen, wenn der Provider dies semantisch trägt.

## Übergabe

Downstream-Skills verwenden `selection.canonicalName` und `selection.variant`, lösen daraus aber erst zur Laufzeit das tatsächliche Asset aus der autorisierten Bibliothek auf. Der Selector selbst liefert keinen Dateipfad zu einem proprietären Runtime-Asset, solange dessen Mount-/Task-Pfad nicht explizit bekannt ist.

## Qualitätsgate

PASS nur wenn:

- Provider eindeutig und registriert ist;
- ausgewählter Name im Provider-Katalog existiert;
- engste passende Semantik gewählt wurde;
- Variante mit Hintergrund-/Providerregeln kompatibel ist;
- Claim-Safety bestanden ist;
- kritische Bedeutung zusätzlich textlich abgesichert wird;
- keine proprietäre Binärdatei persistiert wurde.

## Abschluss

Abgeschlossen ist der Skill, wenn ein valides `icon-selection.json` mit nachvollziehbarer Auswahl oder einem expliziten unresolved/ambiguous Status vorliegt.