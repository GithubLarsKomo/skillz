---
name: repository-skill-bootstrap
description: Analysiert ein bestehendes Software-Repository und richtet eine portable Agent-Arbeitsgrundlage mit CONFIG.md, CONTEXT.md und DECISIONS.md ein. Verwenden, wenn ein Repository erstmals für wiederholbare Arbeit mit mehreren Skills, Agenten oder Sitzungen vorbereitet werden soll.
userFacing: true
category: skill-system
version: 0.2.0
status: candidate
owners:
  - GithubLarsKomo
requires: []
outputs:
  - docs/agents/CONFIG.md
  - docs/agents/CONTEXT.md
  - docs/agents/DECISIONS.md
lastEvaluated: 2026-07-31
---

# Repository Skill Bootstrap

Richte in einem bestehenden Repository eine kleine, versionierte Arbeitsgrundlage für komponierbare Skills ein. Der Bootstrap verändert keine Produktlogik und erfindet keine Projektregeln.

## Ergebnis

Erzeuge standardmäßig unter `docs/agents/`:

- `CONFIG.md`: ausführbare Befehle, Tracker, Labels, relevante Pfade, erlaubte Schreibziele und Schutzregeln,
- `CONTEXT.md`: Domänensprache, Kernobjekte, Akteure, Systemgrenzen und wichtige Abkürzungen,
- `DECISIONS.md`: bestätigte Architekturentscheidungen, bestehende ADR-Verweise und offene Entscheidungen.

Nutze einen abweichenden Zielpfad nur, wenn das Repository bereits eine eindeutige Konvention besitzt.

## Grenzen

- Überschreibe keine bestehenden Dateien ungeprüft.
- Erfinde keine Build-, Test-, Deployment- oder Migrationsbefehle.
- Übernimm keine Secrets, Tokens, privaten URLs oder personenbezogenen Angaben.
- Führe keine Installation, Migration oder Produktänderung aus.
- Markiere unsichere Erkenntnisse als `unbestätigt` oder `offen`.
- Bewahre vorhandene ADR-, CONTRIBUTING- und Dokumentationskonventionen.

## Workflow

### 1. Repository inventarisieren

Lies mindestens:

- README und CONTRIBUTING,
- Paket- und Build-Manifeste,
- CI-Workflows,
- vorhandene Architektur- und ADR-Dokumente,
- zentrale Quellverzeichnisse,
- Issue- und PR-Konventionen, soweit verfügbar.

Ermittle daraus belegbare Fakten zu Technologie, Befehlen, Struktur und Governance.

### 2. Zielpfad bestimmen

Bevorzuge in dieser Reihenfolge:

1. vorhandenes Verzeichnis für Agent- oder Engineering-Kontext,
2. vorhandenes Dokumentationsverzeichnis,
3. `docs/agents/`.

Melde Kollisionen und vorhandene Inhalte vor einem Schreibvorgang.

### 3. Vorschlag bilden

Erzeuge zunächst einen Dry-Run mit:

- Zielpfaden,
- Quellen je Aussage,
- geplanten Inhalten,
- offenen oder widersprüchlichen Punkten,
- Dateien, die unverändert bleiben.

Bei rein automatischer Ausführung darf nur geschrieben werden, wenn keine Kollision und keine wesentliche Unsicherheit besteht.

### 4. Dateien erzeugen

Nutze das Skript `scripts/bootstrap_repository_context.py` für deterministische Dateierzeugung. Das Skript erzeugt nur fehlende Dateien und verweigert standardmäßig Überschreibungen.

Beispiel:

```bash
python skills/repository-skill-bootstrap/scripts/bootstrap_repository_context.py \
  --repo /pfad/zum/repository \
  --project-name "Projektname" \
  --dry-run
```

Nach Prüfung ohne `--dry-run` ausführen.

### 5. Inhalte vervollständigen

Ersetze Platzhalter ausschließlich mit belegbaren Informationen. Verweise bei Befehlen auf deren Quelle, zum Beispiel `package.json`, `Makefile` oder CI-Workflow. Halte offene Entscheidungen in `DECISIONS.md` sichtbar, statt sie stillschweigend zu entscheiden.

### 6. Validieren

Prüfe:

- alle drei Dateien existieren am erwarteten Ort,
- kein Secret-Muster wurde übernommen,
- dokumentierte Befehle existieren tatsächlich in den Quellmanifesten,
- Links und Pfade sind relativ und gültig,
- bestehende Dokumentation wurde nicht dupliziert oder widersprochen,
- `git diff` enthält ausschließlich die erwarteten Kontextdateien.

## Übergaben

Der Bootstrap liefert an nachfolgende Skills:

- Repository-Regeln aus `CONFIG.md`,
- gemeinsame Domänensprache aus `CONTEXT.md`,
- verbindliche und offene Entscheidungen aus `DECISIONS.md`.

Nachfolgende Skills dürfen diese Dateien lesen, aber bestätigte Regeln nicht ohne expliziten Auftrag ändern.

## Fehlerfälle

- **Datei existiert:** stoppen, Inhalt vergleichen und Merge-Vorschlag erzeugen.
- **Befehle widersprechen sich:** beide Quellen dokumentieren und als offen markieren.
- **Keine belastbare Domänensprache:** minimale Struktur erzeugen und Lücken benennen.
- **Secret-Verdacht:** betroffene Inhalte nicht übernehmen und Fundstelle melden.
- **Kein Software-Repository:** nicht schreiben; Zweck und erwartete Eingaben klären.

## Abschluss

Der Skill ist abgeschlossen, wenn die drei Kontextdateien konfliktfrei erzeugt oder aktualisiert, ihre Aussagen auf Repository-Quellen zurückführbar und alle offenen Unsicherheiten sichtbar dokumentiert sind.
