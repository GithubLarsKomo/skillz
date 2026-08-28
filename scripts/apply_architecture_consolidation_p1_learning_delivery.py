#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

MIGRATIONS = {
    "skills/youtube-learning-workflow/SKILL.md": (
        """requires:\n  - youtube-video-ingestion\n  - multimodal-learning-analysis\n  - learning-summary-synthesis\n  - procedure-sop-extractor\n  - learning-visual-planner\n  - learning-content-design-system\n  - learning-svg-generator\n  - learning-image-generator\n  - learning-landingpage-renderer\n  - learning-document-delivery\n  - learning-artifact-qa\n  - template-presentation-workflow\n""",
        """requires:\n  - youtube-video-ingestion\n  - multimodal-learning-analysis\n  - learning-summary-synthesis\n  - procedure-sop-extractor\n  - learning-delivery-workflow\n""",
    ),
    "skills/youtube-playlist-learning-workflow/SKILL.md": (
        """requires:\n  - youtube-learning-workflow\n  - learning-source-arbitration\n  - multi-source-learning-synthesis\n  - learning-visual-planner\n  - learning-content-design-system\n  - learning-svg-generator\n  - learning-image-generator\n  - learning-landingpage-renderer\n  - learning-document-delivery\n  - learning-artifact-qa\n  - template-presentation-workflow\n""",
        """requires:\n  - youtube-learning-workflow\n  - learning-source-arbitration\n  - multi-source-learning-synthesis\n  - learning-delivery-workflow\n""",
    ),
    "skills/youtube-course-builder-workflow/SKILL.md": (
        """requires:\n  - youtube-playlist-learning-workflow\n  - course-concept-graph\n  - learning-path-planner\n  - learning-activity-generator\n  - learning-visual-planner\n  - learning-content-design-system\n  - learning-svg-generator\n  - learning-image-generator\n  - learning-landingpage-renderer\n  - template-presentation-workflow\n  - learning-document-delivery\n  - learning-artifact-qa\n""",
        """requires:\n  - youtube-playlist-learning-workflow\n  - course-concept-graph\n  - learning-path-planner\n  - learning-activity-generator\n  - learning-delivery-workflow\n""",
    ),
}

SECTION_INSERTS = {
    "skills/youtube-learning-workflow/SKILL.md": (
        "## Ziel\n\n",
        "## Ziel\n\nDie fachliche Einzelvideo-Analyse bleibt in diesem Skill. Sobald `learning-content-model.json` fixiert ist, wird Design-, Visual-, Render- und Cross-Format-QA an `learning-delivery-workflow` delegiert; die einzelnen Renderer werden hier nicht parallel orchestriert.\n\n",
    ),
    "skills/youtube-playlist-learning-workflow/SKILL.md": (
        "## Ziel\n\n",
        "## Ziel\n\nDie Multi-Source-Arbitration und Synthese bleiben in diesem Skill. Sobald `multi-source-learning-model.json` fixiert ist, wird die gemeinsame Design-, Visual-, Render- und Cross-Format-QA-Schicht über `learning-delivery-workflow` ausgeführt.\n\n",
    ),
    "skills/youtube-course-builder-workflow/SKILL.md": (
        "## Ziel\n\n",
        "## Ziel\n\nCourse Concept, Learning Path und Activities bleiben in diesem Skill. Nach dem Lock von `course-learning-model.json` wird die gemeinsame Design-, Visual-, Render- und Cross-Format-QA-Schicht über `learning-delivery-workflow` ausgeführt.\n\n",
    ),
}

BODY_MIGRATIONS = {
    "skills/youtube-learning-workflow/SKILL.md": (
        """### 5. Visuals planen\n\n`learning-visual-planner` entscheidet je Botschaft, ob Quellframe, SVG/Diagramm oder generierte Illustration geeignet ist.\n\n### 6. DESIGN.md Authority Lock\n\n`learning-content-design-system` ausführen.\n\n- Bei neutralem Lernartefakt gelten Projekt-DESIGN.md + `docs/learning-content/DESIGN.md`.\n- Bei Corporate Content gewinnt der entsprechende Corporate-Vertrag.\n- Für EUROIMMUN gilt zusätzlich zwingend `docs/corporate/euroimmun/DESIGN.md` einschließlich Corporate Design Gate.\n\n### 7. Visual Assets erzeugen\n\n- strukturierte Diagramme/Schematics -> `learning-svg-generator`;\n- erklärende/realistische Illustration -> `learning-image-generator`;\n- Originalframe nur wenn inhaltlich nötig und provenance-/rights-seitig zulässig.\n\nVisuals dürfen keine neuen fachlichen Claims einführen.\n\n### 8. Ausgabe erzeugen\n\n**HTML** -> `learning-landingpage-renderer`.\n\n**PPTX** -> `template-presentation-workflow`. Educational Storyline als Default:\n\n`why it matters -> mental model -> key concepts -> how it works -> demonstrated procedure -> critical details -> mistakes -> takeaways`\n\nBei bestätigtem EUROIMMUN-Kontext ist der EUROIMMUN-Corporate-Wrapper/Template-Kontext zu verwenden und der Corporate Design Gate nachzuweisen.\n\n**DOCX/PDF** -> `learning-document-delivery`.\n\n### 9. Cross-Format QA\n\n`learning-artifact-qa` ausführen. Nach jeder materiellen Korrektur neu rendern und erneut prüfen.\n""",
        """### 5. Delivery delegieren\n\nNach dem Canonical Model Lock `learning-delivery-workflow` mit `learning-content-model.json`, angeforderten Formaten, Zielgruppe/Sprache und Design-/Corporate-/Template-Kontext ausführen.\n\nDie Delivery-Schicht besitzt ab hier:\n\n- DESIGN.md-/Corporate-Authority-Auflösung;\n- Visualplanung sowie SVG-/Bild-Routing;\n- HTML-, PPTX-, DOCX- und PDF-Erzeugung;\n- Cross-Format-QA, Render-/Parity-Gates und Re-Render nach Korrekturen.\n\nDieser Orchestrator darf die einzelnen Delivery-Worker nicht parallel erneut steuern. Video-spezifische Verantwortung bleibt hier: Source Identity, Evidence Map, Summary/SOP-Evidenzgrenzen und der unveränderliche `learning-content-model.json`-Fingerprint. `youtube-learning-run.json` referenziert `learning-delivery-bundle.json` und `learning-delivery-run.json`.\n""",
    ),
    "skills/youtube-playlist-learning-workflow/SKILL.md": (
        """## 6. Visuals und DESIGN.md\n\n`learning-visual-planner` plant Visuals auf Basis des **konsolidierten** Modells.\n\nMulti-Source-spezifische Visuals können sein:\n\n- Consensus-vs-Variant-Diagramm;\n- Source Coverage Map;\n- Konfliktmatrix;\n- harmonisierter Prozessflow;\n- Varianten-Branching;\n- Concept Map mit Source-Provenienz.\n\n`learning-content-design-system` löst die Designautorität. Corporate DESIGN.md bleibt höherrangig.\n\n## 7. Ausgabe\n\n**HTML:** Landingpage mit Source Navigator, Consensus Core, Varianten/Konflikten und Source Map.\n\n**PPTX:** vorhandener Template-Presentation-Workflow. Default Storyline:\n\n`problem -> shared mental model -> consensus core -> deeper mechanism -> relevant variants -> conflicts/open questions -> practical synthesis -> takeaways`.\n\n**DOCX/PDF:** kanonischer Multi-Source-Inhalt -> DOCX -> vollständiger Render -> PDF -> Paritätsprüfung.\n\n## 8. Cross-Source QA\n\nZusätzlich zur bestehenden `learning-artifact-qa` prüfen:\n\n- alle finalen Claims auf Source-Cluster rückführbar;\n- `independentSourceCount` korrekt;\n- ungelöste Konflikte sichtbar;\n- Single-Source-Aussagen nicht als Konsens dargestellt;\n- Zahlen/Einheiten/Parameter nicht unzulässig gemittelt;\n- keine Hybrid-SOP aus inkompatiblen Protokollen;\n- Source Map in allen Formaten semantisch konsistent;\n- alle Formate nutzen denselben Multi-Source-Fingerprint.\n""",
        """## 6. Delivery und Cross-Source QA\n\n`learning-delivery-workflow` mit dem kanonischen `multi-source-learning-model.json`, den angeforderten Formaten und dem Design-/Corporate-/Template-Kontext ausführen. Visualplanung, Assets, HTML/PPTX/DOCX/PDF, Render-/Parity-Gates und Cross-Format-QA gehören ausschließlich in diese gemeinsame Delivery-Schicht.\n\nDer Playlist-Orchestrator ergänzt darauf nur die **Multi-Source-spezifischen** Prüfungen:\n\n- alle finalen Claims bleiben auf Source-Cluster rückführbar;\n- `independentSourceCount` ist korrekt;\n- ungelöste Konflikte bleiben sichtbar;\n- Single-Source-Aussagen werden nicht als Konsens dargestellt;\n- Zahlen/Einheiten/Parameter werden nicht unzulässig gemittelt;\n- keine Hybrid-SOP entsteht aus inkompatiblen Protokollen;\n- alle ausgelieferten Formate referenzieren denselben Multi-Source-Fingerprint.\n\n`youtube-playlist-learning-run.json` referenziert das `learning-delivery-bundle.json` und den zugehörigen Delivery-Run, ohne Worker-Artefakte selbst zu besitzen.\n""",
    ),
    "skills/youtube-course-builder-workflow/SKILL.md": (
        """### 6. Visuals + DESIGN\n\nZusätzlich zu `docs/learning-content/DESIGN.md` gilt `docs/learning-content/course/DESIGN.md`.\n\nVisuals priorisieren:\n\n- Course Map / Learning Path;\n- prerequisite graph;\n- Modul-Mental-Models;\n- Prozess-/Varianten-Schematics;\n- Fortschritts-/Coverage-Darstellung ohne Fake-Metriken.\n\nGenerated visuals bleiben illustrative-only.\n\n### 7. Ausgabe\n\n**HTML:** Course-Landingpage mit Overview, Course Map, Module Navigation, Module Lessons, Activities, Knowledge Checks, Sources.\n\n**PPTX:** kein vollständiges LMS simulieren; stattdessen Instructor-/Workshop-Deck oder Course Overview + Moduldecks über `template-presentation-workflow`.\n\n**DOCX/PDF:** Study Guide / Trainer Guide mit Kursstruktur, Inhalten, Übungen, Lösungen/Begründungen und Source Map.\n\n### 8. QA\n\n`learning-artifact-qa` plus Course-spezifische Gates:\n\n- prerequisite graph azyklisch;\n- jedes Pflichtmodul hat Lernziel und Exit Criteria;\n- jede formative Frage ist auf Claim/Evidence rückführbar;\n- keine ungelösten materiellen Konflikte als eindeutige Prüfungsantwort;\n- keine erfundenen Bestehensgrenzen;\n- keine Formatausgabe mit abweichender Modulreihenfolge ohne dokumentierten Grund;\n- 0 offene Critical/Major Findings.\n""",
        """### 6. Delivery und Course-QA\n\n`learning-delivery-workflow` mit `course-learning-model.json`, angeforderten Formaten und dem kombinierten Learning-/Course-/Corporate-Designkontext ausführen. Visualplanung, Assets, HTML/PPTX/DOCX/PDF sowie Cross-Format- und Render-QA gehören ausschließlich in diese Delivery-Schicht.\n\nDer Course Builder besitzt nur die **kurssemantischen** Gates:\n\n- prerequisite graph ist azyklisch;\n- jedes Pflichtmodul besitzt Lernziel und Exit Criteria;\n- jede formative Frage ist auf Claim/Evidence rückführbar;\n- ungelöste materielle Konflikte werden nicht zu eindeutigen Prüfungsantworten;\n- keine erfundenen Bestehensgrenzen;\n- keine Formatausgabe verwendet eine abweichende Modulreihenfolge ohne dokumentierten Grund;\n- Delivery-Run und Course-Fingerprint sind im `youtube-course-builder-run.json` referenziert.\n""",
    ),
}


def replace_once(path: Path, old: str, new: str) -> bool:
    text = path.read_text(encoding="utf-8")
    if new in text:
        return False
    if old not in text:
        raise RuntimeError(f"{path.relative_to(ROOT)}: expected migration anchor not found")
    path.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")
    return True


def main() -> int:
    changed: set[str] = set()
    for mapping in (MIGRATIONS, SECTION_INSERTS, BODY_MIGRATIONS):
        for relative, (old, new) in mapping.items():
            if replace_once(ROOT / relative, old, new):
                changed.add(relative)
    if changed:
        for relative in sorted(changed):
            print(f"UPDATED: {relative}")
    else:
        print("OK: learning delivery consolidation already applied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
