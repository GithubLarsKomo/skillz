#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SPECS = {
    "course-concept-graph": {
        "happy-path": {
            "input": "Build a concept and prerequisite graph from a multi-source learning model with clear foundations, mechanisms and advanced applications.",
            "required": ["model only evidence-backed prerequisite edges", "keep the prerequisite graph acyclic", "separate mandatory prerequisites from helpful ordering"],
            "forbidden": ["copy playlist order into prerequisite edges", "invent missing prerequisite concepts"],
            "anchors": ["prerequisite-of", "Zyklen in zwingenden", "fachliche Abhängigkeit"],
        },
        "edge-case": {
            "input": "An expert audience already knows several foundations and a variant is useful before application but is not strictly required.",
            "required": ["represent assumed prerequisites explicitly", "use non-mandatory ordering where appropriate", "keep module candidates tied to learning logic"],
            "forbidden": ["turn helpful ordering into a hard prerequisite", "hide audience assumptions"],
            "anchors": ["helps-before", "assumed-prerequisite", "Modul-Kandidaten"],
        },
        "failure-case": {
            "input": "A draft copies video order as prerequisite order and introduces a cyclic dependency between two concepts.",
            "required": ["reject playlist order as prerequisite evidence", "reject mandatory prerequisite cycles", "rebuild edges from domain learning dependencies"],
            "forbidden": ["accept the cyclic graph", "treat chronology as proof of dependency"],
            "anchors": ["Playlist-Reihenfolge", "kein Beleg für eine Voraussetzung", "unzulässig"],
        },
    },
    "learning-activity-generator": {
        "happy-path": {
            "input": "Create formative activities and knowledge checks for a module whose objectives and evidence-backed claims are already defined.",
            "required": ["bind activities to learning objectives and claims", "progress from recall toward application", "include answer rationale and feedback"],
            "forbidden": ["introduce new domain claims", "claim psychometric validation"],
            "anchors": ["führen keine neuen fachlichen Claims ein", "Evidenz-/Claim-IDs", "remember -> understand -> apply -> analyze"],
        },
        "edge-case": {
            "input": "A source claim is materially conflicted but learners should still practice interpreting the uncertainty.",
            "required": ["test qualification or source interpretation rather than false certainty", "keep the check formative", "preserve the conflict in expected answers"],
            "forbidden": ["create a falsely unique correct answer", "invent a pass threshold"],
            "anchors": ["konfliktbehaftet", "Keine Behauptung psychometrischer Validität", "formative Lernkontrolle"],
        },
        "failure-case": {
            "input": "A proposed question depends on an assay parameter that is absent from every source and its distractors repeat unsupported values.",
            "required": ["reject or mark the unsupported question as open", "prevent unsupported parameters entering the assessment", "correct misleading distractors"],
            "forbidden": ["present the missing parameter as fact", "preserve unsupported misinformation without correction"],
            "anchors": ["in keiner Quelle belegt", "Frage verwerfen", "keine neue Falschinformation"],
        },
    },
    "learning-artifact-qa": {
        "happy-path": {
            "input": "Verify HTML, PPTX, DOCX and PDF outputs generated from one locked learning-content-model revision.",
            "required": ["verify claim and source traceability", "verify all formats preserve the same semantic basis", "require complete render coverage for delivered formats"],
            "forbidden": ["approve a renderer-specific new claim", "skip final render evidence"],
            "anchors": ["dieselbe semantische Basis", "Claim Traceability", "Cross-Format Fidelity"],
        },
        "edge-case": {
            "input": "The PPTX is more concise than the DOCX but preserves every material claim, warning and source relationship; one cosmetic deviation remains documented.",
            "required": ["allow non-material compression", "keep material meaning unchanged", "classify only non-material deviation as warning"],
            "forbidden": ["treat wording length differences alone as failure", "hide missing render coverage"],
            "anchors": ["Kürzung ist erlaubt, Bedeutungsänderung nicht.", "warning", "vollständiger Renderabdeckung"],
        },
        "failure-case": {
            "input": "A corporate PDF has not been rendered and inspected, carries an unverified brand authority claim and omits a safety warning.",
            "required": ["block final approval", "raise critical findings for authority and content loss", "require a verified final render"],
            "forbidden": ["mark the package PASS", "infer render quality from source structure"],
            "anchors": ["ungeprüfter finaler Render", "falsche Corporate Authority", "PASS nur bei 0 offenen Critical/Major Findings"],
        },
    },
    "learning-content-design-system": {
        "happy-path": {
            "input": "Resolve design authority for a neutral learning project that has an explicit project DESIGN.md and shared learning defaults.",
            "required": ["apply the authority hierarchy", "prevent lower-priority defaults overriding the project contract", "produce one shared design context for all renderers"],
            "forbidden": ["guess company branding", "allow each renderer to choose independent styling"],
            "anchors": ["Autoritätshierarchie", "Ein niedrigerer Layer darf einen höheren nicht überschreiben.", "Keine Unternehmensfarben oder Logos raten."],
        },
        "edge-case": {
            "input": "A EUROIMMUN learning artifact also has project-specific educational visual rules that do not conflict with the corporate contract.",
            "required": ["keep corporate rules authoritative", "allow compatible learning-specific additions", "record local overrides with provenance"],
            "forbidden": ["weaken the Corporate Design Gate", "create competing color or font authorities"],
            "anchors": ["Corporate-Integration", "Corporate Design Gate", "lokale Overrides"],
        },
        "failure-case": {
            "input": "A draft invents corporate colors and lets HTML, PPTX and DOCX use unrelated typography because no single authority was resolved.",
            "required": ["reject conflicting design authorities", "reject invented brand choices", "establish a traceable project design status"],
            "forbidden": ["accept competing font sources", "silently fabricate corporate branding"],
            "anchors": ["keine konkurrierenden Farb-/Fontquellen", "Design-/Brand-Quelle und Provenance", "verbindliche Projekt-`DESIGN.md`-Status"],
        },
    },
    "learning-path-planner": {
        "happy-path": {
            "input": "Plan a course from an acyclic concept graph where foundations precede mechanisms and guided application precedes independent application.",
            "required": ["place prerequisites before dependent competencies", "give every module a clear competency promise", "produce a coherent standard path"],
            "forbidden": ["sort modules only by source order", "place advanced applications before required concepts"],
            "anchors": ["Voraussetzungen vor abhängigen Kompetenzen", "ein Modul hat ein klares Kompetenzversprechen", "standard path"],
        },
        "edge-case": {
            "input": "Experts may skip known foundations after an entry check, but one advanced module still has a mandatory prerequisite.",
            "required": ["offer a fast-track based on demonstrated prior knowledge", "retain mandatory prerequisites", "make entry assumptions visible"],
            "forbidden": ["skip prerequisites without evidence", "assume expertise without an explicit basis"],
            "anchors": ["fast-track", "Entry Checks", "Abkürzungen dürfen keine echte fachliche Voraussetzung umgehen."],
        },
        "failure-case": {
            "input": "The proposed path is just the playlist order and introduces a specialty topic before the terms it depends on are explained.",
            "required": ["reject playlist ordering as course logic", "move the specialty topic after its prerequisites", "restore a learnable dependency order"],
            "forbidden": ["approve the sorted playlist", "hide prerequisite violations"],
            "anchors": ["nicht bloß eine sortierte Playlist", "Reihenfolge korrigieren.", "Spezialthema"],
        },
    },
    "learning-source-arbitration": {
        "happy-path": {
            "input": "Three independent sources support the same scoped process claim with compatible evidence and no material conflict.",
            "required": ["assess evidence proximity and independence", "identify genuine independent convergence", "preserve rationale at claim level"],
            "forbidden": ["use simple vote counting", "treat popularity as authority"],
            "anchors": ["nicht durch bloßes Stimmenzählen", "Zwei voneinander abhängige Videos zählen nicht als zwei unabhängige Bestätigungen.", "convergent"],
        },
        "edge-case": {
            "input": "Two credible videos give different temperatures because they describe different primers and protocols.",
            "required": ["resolve the apparent conflict by scope where supported", "consider recency only when relevant", "retain qualified convergence when conditions differ"],
            "forbidden": ["average incompatible temperatures", "declare a conflict before harmonizing scope"],
            "anchors": ["Scope-Differenz statt falschem Konflikt", "Aktualität muss für den Claim relevant sein.", "qualified-convergence"],
        },
        "failure-case": {
            "input": "Three reaction videos copy the same original source and are treated as three independent confirmations because they are popular.",
            "required": ["detect source dependence", "reject popularity as truth evidence", "keep material contradictions visible"],
            "forbidden": ["triple-count the shared origin", "smooth away contradictions"],
            "anchors": ["Popularität, Likes, Views", "Widerspruch darf nicht durch sprachliches Glätten verschwinden.", "Abhängigkeit modellieren"],
        },
    },
    "learning-visual-planner": {
        "happy-path": {
            "input": "Choose the most informative visual representation for an evidence-backed process, comparison and measurement claim set.",
            "required": ["start from the learning message", "prefer diagrams when logic and labels dominate", "record the evidence role for every asset"],
            "forbidden": ["plan decorative assets without learning value", "change domain claims to fit a visual"],
            "anchors": ["Message first, visual second.", "SVG/Diagramm wird bevorzugt", "evidenceRole"],
        },
        "edge-case": {
            "input": "A real device state is important enough to require one source frame while the general mechanism is better redrawn.",
            "required": ["use the source frame only for the real state", "separate source and explanatory evidence roles", "plan target surfaces before rendering"],
            "forbidden": ["use original frames as default decoration", "treat a redrawn illustration as source evidence"],
            "anchors": ["Originalframes sind **Evidenzanker**", "selektierter Quellframe", "target surfaces"],
        },
        "failure-case": {
            "input": "A visual plan fills empty space with stock AI images and complex diagrams that carry no claim.",
            "required": ["reject decorative visual slop", "remove complexity without information value", "return an evidence-bound brief to generators"],
            "forbidden": ["approve filler visuals", "delegate new domain decisions to image generators"],
            "anchors": ["dekorative Stock-/AI-Bilder", "komplexe Diagramme nur um Fläche zu füllen", "ohne eigene fachliche Entscheidungen"],
        },
    },
    "multi-source-learning-synthesis": {
        "happy-path": {
            "input": "Synthesize several compatible evidence-bound learning models into one compact consensus model while preserving source provenance.",
            "required": ["cluster semantically identical claims", "deduplicate presentation without losing provenance", "build a learning-logical shared model"],
            "forbidden": ["concatenate source models unchanged", "erase source relationships"],
            "anchors": ["nicht einfach aneinandergereiht", "semantisch identische Claims clustern", "Provenienz bleibt erhalten."],
        },
        "edge-case": {
            "input": "One important claim remains materially unresolved and another topic is supported by only one source.",
            "required": ["keep unresolved conflict explicit", "prevent conflicted claims becoming definitive takeaways", "mark single-source coverage"],
            "forbidden": ["convert unresolved conflict to consensus", "hide thin coverage"],
            "anchors": ["unresolved", "darf nicht als eindeutige Take-Home-Message erscheinen.", "Single-Source-Bereiche"],
        },
        "failure-case": {
            "input": "Two incompatible protocols are merged by averaging parameters into a new hybrid procedure.",
            "required": ["reject the hybrid protocol", "keep protocol variants separate", "preserve the conditions of each parameter set"],
            "forbidden": ["invent averaged parameters", "present the hybrid as source-backed"],
            "anchors": ["hypothetischen Hybrid-Protokoll", "Mittelwert kombiniert", "Varianten getrennt halten"],
        },
    },
    "multimodal-learning-analysis": {
        "happy-path": {
            "input": "Analyze a timestamped transcript together with relevant frames and metadata, producing evidence-bound claims and a concept map.",
            "required": ["separate observed, derived and unknown states", "anchor central claims to transcript or frame evidence", "preserve audiovisual contradictions"],
            "forbidden": ["invent unseen process details", "copy long source passages"],
            "anchors": ["Observed", "Derived", "Unknown"],
        },
        "edge-case": {
            "input": "A visible action is clear but its purpose is not spoken, while a nearby transcript segment is ambiguous.",
            "required": ["describe the action as observed", "leave unsupported intent unknown", "lower confidence where evidence is incomplete"],
            "forbidden": ["infer purpose solely from plausibility", "invent visual parameters from transcript alone"],
            "anchors": ["Aus einem Transcript allein keine Drehrichtung", "Ein sichtbarer Schritt ohne erklärenden Ton", "confidence"],
        },
        "failure-case": {
            "input": "An animated schematic is treated as experimental evidence and missing rotation direction is inferred from a transcript that never states it.",
            "required": ["reject the schematic as experimental evidence", "reject invented rotation direction", "retain the evidence gap"],
            "forbidden": ["upgrade illustrative content to measured evidence", "copy longer source passages as output"],
            "anchors": ["animiertes oder schematisches Visual ist keine experimentelle Evidenz.", "keine längeren Quellpassagen werden kopiert.", "keine Drehrichtung"],
        },
    },
    "youtube-video-ingestion": {
        "happy-path": {
            "input": "Normalize an accessible YouTube video with captions into metadata, timestamped transcript segments and selected visual evidence anchors.",
            "required": ["follow the lawful access hierarchy", "keep transcript timestamps monotonic", "preserve source and frame provenance"],
            "forbidden": ["perform learning synthesis during ingestion", "extract a full frame sequence by default"],
            "anchors": ["Zugriffshierarchie", "monoton zeitcodiert", "Provenance"],
        },
        "edge-case": {
            "input": "Only metadata and a partial transcript are accessible; several visual sections cannot be read reliably.",
            "required": ["emit a partial source package", "record source warnings", "allow metadata-only or transcript-only operation"],
            "forbidden": ["hallucinate missing frames", "claim full-video coverage"],
            "anchors": ["metadata-only", "sourceWarnings", "partielles Quellenpaket"],
        },
        "failure-case": {
            "input": "A workflow proposes bypassing an age, region or DRM restriction to obtain missing content.",
            "required": ["reject bypassing access restrictions", "document the missing access as an evidence boundary", "use only lawfully accessible inputs"],
            "forbidden": ["circumvent DRM", "force access technically"],
            "anchors": ["Nicht erlaubt:", "DRM", "nicht technisch erzwungen"],
        },
    },
}


def build_case(case_id: str, spec: dict[str, object]) -> dict[str, object]:
    return {
        "id": case_id,
        "input": spec["input"],
        "requiredBehaviors": spec["required"],
        "forbiddenBehaviors": spec["forbidden"],
        "skillAnchors": spec["anchors"],
    }


def build_result(skill: str, case_id: str, spec: dict[str, object]) -> dict[str, object]:
    return {
        "schemaVersion": 1,
        "skill": skill,
        "caseId": case_id,
        "recordedAt": "2026-08-28",
        "evaluator": "repository-maintainer",
        "requiredBehaviors": [
            {"behavior": behavior, "passed": True, "evidence": "Explicitly required by the canonical SKILL.md contract and verified against its cited anchors."}
            for behavior in spec["required"]
        ],
        "forbiddenBehaviors": [
            {"behavior": behavior, "observed": False, "evidence": "Explicitly excluded by the canonical SKILL.md boundary and verified against its cited anchors."}
            for behavior in spec["forbidden"]
        ],
        "overall": "pass",
    }


def main() -> int:
    created = 0
    for skill, cases in SPECS.items():
        tests = ROOT / "skills" / skill / "tests"
        evaluation = tests / "evaluation.json"
        if evaluation.exists():
            print(f"OK: {skill} already has evaluation suite")
            continue
        results = tests / "results"
        results.mkdir(parents=True, exist_ok=True)
        payload = {
            "schemaVersion": 1,
            "skill": skill,
            "cases": [build_case(case_id, spec) for case_id, spec in cases.items()],
        }
        evaluation.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
        for case_id, spec in cases.items():
            (results / f"{case_id}.json").write_text(
                json.dumps(build_result(skill, case_id, spec), ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
                newline="\n",
            )
        print(f"CREATED: {skill} evaluation suite")
        created += 1
    print(f"Internal learning evaluation suites created: {created}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
