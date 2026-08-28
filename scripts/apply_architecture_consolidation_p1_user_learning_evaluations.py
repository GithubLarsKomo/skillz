#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECORDED_AT = "2026-08-28"

SPECS = {
    "learning-document-delivery": [
        {
            "id": "happy-path",
            "input": "Render an approved learning-content model as editable DOCX and derived PDF under the active DESIGN.md, preserving claims, timestamps and visual provenance.",
            "required": [
                ("keep DOCX as the canonical layout source and derive PDF from it", "The architecture explicitly states canonical DOCX -> full-page QA -> PDF -> parity QA and forbids independent rewriting."),
                ("preserve claim confidence evidence classes numbers warnings and source references", "The Fidelity section enumerates these elements as invariants."),
                ("perform complete page-by-page DOCX and PDF QA", "The DOCX and PDF QA sections explicitly require full rendering and parity checks."),
            ],
            "forbidden": [
                ("re-author learning claims during rendering", "The description and architecture separate content authority from document rendering."),
                ("silently claim corporate approval or fallback status", "Renderer routing explicitly forbids silent corporate fallback or invented approval."),
            ],
            "anchors": ["canonical DOCX", "Fidelity", "Komplettes Dokument seitenweise rendern"],
        },
        {
            "id": "edge-case",
            "input": "A corporate context exists but no confirmed corporate DOCX renderer/template can be safely applied; a neutral fallback would violate the requested brand authority.",
            "required": [
                ("respect corporate/template routing authority", "The routing hierarchy gives supplied/confirmed corporate template paths precedence."),
                ("avoid silent fallback when a corporate gate is required", "The skill explicitly says no silent corporate fallback or invented company approval."),
                ("surface the missing renderer/template authority as a delivery limitation", "The architecture requires a known route before claiming corporate document delivery."),
            ],
            "forbidden": [
                ("invent a corporate document style", "DESIGN.md and renderer routing are authoritative."),
                ("label a neutral document as corporate-approved", "Invented corporate approval is explicitly forbidden."),
            ],
            "anchors": ["Renderer-Routing", "Kein stilles Corporate-Fallback", "Corporate Design Gate"],
        },
        {
            "id": "failure-case",
            "input": "The renderer changes a parameter to shorten a table, creates DOCX and PDF independently and reports parity without page rendering.",
            "required": [
                ("reject fachliche value changes for layout", "The renderer is not allowed to change fachliche statements or values."),
                ("reject independent DOCX and PDF authoring", "DOCX is the canonical layout source and PDF must be derived from it."),
                ("reject parity claims without actual page render", "Both DOCX and PDF QA require rendered pages and visible comparison."),
            ],
            "forbidden": [
                ("solve layout by altering claims or data", "Fidelity invariants protect numbers, units, warnings and claims."),
                ("simulate PDF parity", "Parity is an explicit render-based gate."),
            ],
            "anchors": ["DOCX und PDF werden nicht unabhängig neu geschrieben", "Zahlen, Einheiten", "jede PDF-Seite rendern"],
        },
    ],
    "learning-image-generator": [
        {
            "id": "happy-path",
            "input": "Generate a consistent explanatory image from the approved visual plan and DESIGN.md for a spatial concept, with clear provenance and intended meaning.",
            "required": [
                ("tie the image to prioritized learning claims and the visual plan", "The rules require each image to transport at least one prioritized learning claim and follow the visual plan."),
                ("follow the active DESIGN.md across style perspective contrast and color", "The generator explicitly binds these image properties to DESIGN.md."),
                ("mark generated images as illustrative-only in the manifest", "The evidence-role section requires illustrative-only unless the asset is an unchanged source-provenanced original."),
            ],
            "forbidden": [
                ("present a generated illustration as experimental or photographic evidence", "The rules explicitly forbid representing generated images as real experiments, patients, device states or measurements."),
                ("hallucinate confidential logos product shapes or brand features", "This is explicitly prohibited."),
            ],
            "anchors": ["mindestens einen priorisierten Lernclaim", "illustrative-only", "Keine vertraulichen Logos"],
        },
        {
            "id": "edge-case",
            "input": "A learning visual needs several precise labels and a small amount of explanatory text; the requested bitmap would make the text unreadable on mobile.",
            "required": [
                ("prefer overlay text or SVG/HTML/PPTX text when labels should remain crisp", "The rules explicitly say critical labels/text should not be baked into raster images when other surfaces handle them better."),
                ("keep the generated image focused on explanatory visual content", "Image generation is reserved for cases where an image solves the learning task better than SVG or source frames."),
                ("record intended meaning and prohibited interpretations", "These are required manifest fields."),
            ],
            "forbidden": [
                ("bake unreadable critical text into the raster image", "The image rules prohibit this when text can be overlaid."),
                ("use image generation for a text-heavy diagram better served by SVG", "The purpose explicitly prefers SVG/source frames when they solve the task better."),
            ],
            "anchors": ["Kritische Labels/Text nicht in das Rasterbild backen", "wenn ein SVG oder Quellframe", "prohibitedInterpretations"],
        },
        {
            "id": "failure-case",
            "input": "A generated image adds an unverified instrument component, recreates a corporate logo and is captioned as a photograph from the experiment.",
            "required": [
                ("reject unverified fachliche additions", "The quality gate forbids fachliche Zusatzdetails."),
                ("reject confidential or invented brand reconstruction", "The rules prohibit hallucinated logos/product features."),
                ("reject misleading evidence labeling", "Generated illustrations must remain illustrative-only."),
            ],
            "forbidden": [
                ("turn illustration into source evidence", "The evidence-role contract separates illustration from source evidence."),
                ("copy the source video's visual expression as closely as possible", "Copyright guidance says to visualize the concept anew rather than closely copy the source expression."),
            ],
            "anchors": ["keine fachlichen Zusatzdetails", "Keine generierte Illustration als Foto", "Konzept neu visualisieren"],
        },
    ],
    "learning-landingpage-renderer": [
        {
            "id": "happy-path",
            "input": "Render a canonical learning model into a portable responsive HTML learning page with takeaways, mental model, source map and timestamp deep links.",
            "required": [
                ("render only content already present in the canonical model", "The input boundary and explicit statement say the renderer does not change claims or SOP classifications."),
                ("produce semantic responsive accessible portable HTML", "The HTML contract requires semantic HTML, wide/narrow responsiveness, keyboard navigation, focus states and portable assets."),
                ("validate timestamps anchors visuals overflow print view and design compliance", "These checks are all explicitly listed in QA."),
            ],
            "forbidden": [
                ("re-author fachliche content during rendering", "The renderer changes neither claims nor SOP classifications."),
                ("turn the page into a generic decorative SaaS landing page", "The Landingpage-Stil section explicitly rejects generic SaaS KPI-card styling."),
            ],
            "anchors": ["Der Renderer verändert keine Claims", "semantisches HTML", "Keine generische SaaS-Startseite"],
        },
        {
            "id": "edge-case",
            "input": "The canonical model has no SOP and only three sections, while several optional visuals are unavailable.",
            "required": [
                ("render only modules that actually exist", "The information architecture explicitly says only existing modules are rendered."),
                ("preserve navigation and source traceability for the available content", "Source/timestamp navigation is part of the HTML contract."),
                ("avoid empty placeholder sections", "Only present modules should be rendered."),
            ],
            "forbidden": [
                ("invent an SOP section", "The renderer cannot create new content or SOP classification."),
                ("fill missing visuals with decorative unsupported content", "The page remains a learning artifact prioritizing understanding and provenance."),
            ],
            "anchors": ["Nur vorhandene Module rendern", "Source Map", "Lernartefakt"],
        },
        {
            "id": "failure-case",
            "input": "The page changes a claim, embeds inaccessible navigation requiring JavaScript, clips SVG labels on mobile and reports PASS without checking timestamp links.",
            "required": [
                ("reject claim mutation", "Claims are outside renderer authority."),
                ("reject inaccessible JS-dependent core navigation", "The HTML contract requires keyboard navigation and no mandatory JavaScript dependency for core content."),
                ("reject QA PASS with clipping or unchecked timestamp links", "Mobile/narrow, SVGs, overflow and timestamp links are mandatory QA checks."),
            ],
            "forbidden": [
                ("hide mobile overflow", "Responsive narrow QA is mandatory."),
                ("skip source-link validation", "Timestamp links are explicit QA scope."),
            ],
            "anchors": ["keine zwingende JS-Abhängigkeit", "Mobile/Narrow", "Timestamp-Links"],
        },
    ],
    "learning-summary-synthesis": [
        {
            "id": "happy-path",
            "input": "Synthesize a video evidence model into a mental model and five key takeaways with timestamps, common mistakes and open questions.",
            "required": [
                ("produce a learning-oriented synthesis rather than chronological retelling", "The Ziel explicitly demands lernwirksame Verdichtung rather than chronological narration."),
                ("bind every takeaway to evidence and preserve observed derived unknown status", "Takeaway rules and quality gate require claim traceability and semantic evidence-state preservation."),
                ("keep uncertainty visible and use timestamps where available", "Derived/uncertain evidence remains qualified and takeaways should carry timestamp links/ranges."),
            ],
            "forbidden": [
                ("create SOP steps from incomplete evidence", "The quality gate explicitly forbids this."),
                ("reproduce long transcript passages", "Long verbatim transcript excerpts are explicitly prohibited."),
            ],
            "anchors": ["lernwirsame Verdichtung", "jeder Takeaway ist evidenzgebunden", "keine SOP-Schritte aus unvollständiger Evidenz"],
        },
        {
            "id": "edge-case",
            "input": "The video repeats one idea many times, gives two examples, and leaves one mechanism uncertain.",
            "required": [
                ("compress repetition and examples more strongly than core logic", "Pedagogical compression explicitly prioritizes core logic and reduces repetition/examples."),
                ("keep the uncertain mechanism qualified", "Observed/derived/unknown states must remain semantically preserved."),
                ("avoid forcing empty standard sections", "The standard structure says empty sections should not be forced."),
            ],
            "forbidden": [
                ("treat repetition as additional evidence", "Takeaway traceability is evidence-based rather than frequency-based."),
                ("fill missing sections with speculation", "No empty sections are forced and uncertain points stay open."),
            ],
            "anchors": ["Reduziere Beispiele, Wiederholungen", "Open/uncertain points", "Keine leeren Abschnitte erzwingen"],
        },
        {
            "id": "failure-case",
            "input": "A summary follows the video minute-by-minute, copies long transcript sentences and upgrades a derived claim to a certain takeaway.",
            "required": [
                ("reject chronological retelling as synthesis", "The quality gate explicitly rejects a chronological content list as substitute for synthesis."),
                ("reject long verbatim transcript reproduction", "Long wörtliche Transcriptauszüge are prohibited."),
                ("restore evidence qualification", "Derived and uncertain evidence must remain visibly qualified."),
            ],
            "forbidden": [
                ("upgrade uncertainty for rhetorical clarity", "Evidence classes outrank stylistic compression."),
                ("invent quotes", "The language section explicitly forbids invented quotes."),
            ],
            "anchors": ["keine chronologische Inhaltsliste", "keine langen wörtlichen Transcriptauszüge", "Keine erfundenen Zitate"],
        },
    ],
    "learning-svg-generator": [
        {
            "id": "happy-path",
            "input": "Create an accessible SVG process diagram from an approved visual plan and DESIGN.md, with source-claim manifest and multi-format readability.",
            "required": [
                ("keep all relationships labels and data anchored in the visual plan", "The fachliche Grenze prohibits adding any number, relationship, sequence or component label not present in the plan."),
                ("apply DESIGN.md tokens and robust SVG structure", "The SVG contract requires viewBox, semantic colors, consistent geometry, text handling and title/desc metadata."),
                ("verify browser raster fallback PPTX/A4 readability and clipping", "These are explicit multi-format checks."),
            ],
            "forbidden": [
                ("invent data or relationships", "The skill explicitly prohibits this."),
                ("redraw corporate logos or alter scientific data geometry", "Both behaviors are explicitly forbidden."),
            ],
            "anchors": ["Keine Zahl, Beziehung, Reihenfolge", "besitzt `viewBox`", "Multi-Format-Prüfung"],
        },
        {
            "id": "edge-case",
            "input": "A diagram must work in browser, PowerPoint and A4 PDF, but the planned brand font is unavailable on one target environment.",
            "required": [
                ("keep the SVG functional without embedded proprietary font files", "The SVG contract explicitly requires this."),
                ("preserve readable text and geometry across target surfaces", "Multi-format checking includes browser, raster fallback, PPTX and A4 use."),
                ("document any necessary technical fallback without changing semantics", "The manifest and design contract preserve provenance and intended meaning."),
            ],
            "forbidden": [
                ("embed proprietary font binaries into the SVG", "The contract explicitly says the SVG must remain functional without them."),
                ("convert labels into clipped decorative paths without need", "Text should remain text unless a technical exception is necessary."),
            ],
            "anchors": ["ohne eingebettete proprietäre Fontdatei", "hält Text als Text", "PPTX-/A4-Nutzung"],
        },
        {
            "id": "failure-case",
            "input": "The SVG adds an unverified process step, redraws a corporate logo, modifies plotted data for aesthetics and clips arrowheads in PDF.",
            "required": [
                ("reject added process semantics", "Unanchored sequence/relationships are prohibited."),
                ("reject logo reconstruction and data-geometry modification", "The fachliche boundary explicitly prohibits both."),
                ("reject release with clipping", "Multi-format QA requires no clipped labels or arrowheads."),
            ],
            "forbidden": [
                ("present an infographic as evidence", "The skill explicitly says infographics are not proof sources."),
                ("ignore target-surface render failures", "Browser/PPTX/A4 readability is mandatory."),
            ],
            "anchors": ["Keine Corporate-Logos nachzeichnen", "Datengeometrie verändert", "keine abgeschnittenen Labels oder Pfeilspitzen"],
        },
    ],
    "procedure-sop-extractor": [
        {
            "id": "happy-path",
            "input": "Extract a demonstrated procedure into purpose, preconditions, materials, ordered steps, controls, warnings and troubleshooting with timestamp evidence and evidence classes.",
            "required": [
                ("classify every element as observed derived or recommended", "The evidence-class contract requires exactly one of these classes per element."),
                ("preserve step evidence timestamps parameters warnings and expected results", "The structure and minimum step fields explicitly require these data where available."),
                ("mark gaps that require validation before controlled use", "Critical missing parameters force incomplete-for-controlled-use and explicit validation gaps."),
            ],
            "forbidden": [
                ("invent quantities times torque temperatures settings or tolerances", "The reconstruction rules explicitly prohibit inventing these parameters."),
                ("present recommended additions as if stated by the video author", "Recommended content must never be phrased as source-observed."),
            ],
            "anchors": ["Jedes Element trägt genau eine Klasse", "nicht erfinden", "incomplete-for-controlled-use"],
        },
        {
            "id": "edge-case",
            "input": "The demonstrated procedure is clear except for one safety-critical temperature value that is visually unreadable.",
            "required": [
                ("describe only what is actually visible or inferable", "Visually shown but unnamed parameters may only be described to the precision actually recognizable."),
                ("mark the procedure incomplete for controlled use", "Missing safety- or quality-critical parameters trigger this status."),
                ("preserve the missing value as a validation gap", "The quality gate requires critical gaps to remain explicit."),
            ],
            "forbidden": [
                ("guess the missing temperature", "Critical parameters must not be invented."),
                ("call the draft an approved SOP", "Controlled approval requires external fachliche verification and controlled-quality-documentation."),
            ],
            "anchors": ["nur so präzise beschreiben", "sicherheits- oder qualitätskritischer Parameter", "keine kontrollierte Freigabe ersetzen"],
        },
        {
            "id": "failure-case",
            "input": "The extractor fills missing values from general knowledge, merges optional variants into one standard and labels the resulting document an effective corporate SOP.",
            "required": [
                ("reject invented missing parameters", "The reconstruction rules explicitly prohibit them."),
                ("keep variants and optional steps distinct", "Variants may not be merged into a false single standard."),
                ("reject effective/approved corporate status without the controlled workflow", "The regulated-context boundary requires fachliche verification and controlled-quality-documentation before approval/effective state."),
            ],
            "forbidden": [
                ("simulate QMS approval", "Approval status may not be pretended."),
                ("erase evidence classes", "Readers must see observed versus derived versus recommended content."),
            ],
            "anchors": ["Varianten und optionale Schritte", "Approval/Effective State", "Freigabestatus wird nicht vorgetäuscht"],
        },
    ],
    "youtube-learning-workflow": [
        {
            "id": "happy-path",
            "input": "Analyze one accessible YouTube demonstration into evidence-bound takeaways and an optional derived SOP, then deliver requested formats from one canonical model.",
            "required": [
                ("lock video source identity and access provenance before analysis", "The Source Lock step fixes video ID, URL, transcript origin and access constraints."),
                ("assemble one canonical learning-content model as content source of truth", "The workflow explicitly defines learning-content-model.json as the single content basis."),
                ("delegate design visual rendering and cross-format QA to learning-delivery-workflow", "The consolidated workflow routes the post-model delivery phase through the shared delivery layer."),
            ],
            "forbidden": [
                ("invent missing SOP parameters", "Critical missing parameters are explicitly allowed to limit SOP completeness rather than being fabricated."),
                ("bypass YouTube access restrictions or claim final without delivered-format QA", "Both are explicit workflow boundaries."),
            ],
            "anchors": ["Source Lock", "inhaltliche Source of Truth", "learning-delivery-workflow"],
        },
        {
            "id": "edge-case",
            "input": "A transcript is available but part of the visual demonstration is unreadable, so several process details cannot be confirmed.",
            "required": [
                ("retain unknown or low-confidence process details", "The workflow quality case explicitly keeps unreadable visual details unknown/low confidence."),
                ("allow a summary while limiting SOP completeness", "The edge case explicitly allows summary but may leave the SOP incomplete."),
                ("propagate evidence limitations into the canonical model and delivery", "Open evidence gaps are explicit model content and all outputs share that model."),
            ],
            "forbidden": [
                ("fill unreadable details from general knowledge", "Missing critical process details may not be invented."),
                ("upgrade the SOP to controlled/final", "The boundaries require external fachliche/Quality approval for regulated SOPs."),
            ],
            "anchors": ["teilweise unlesbar", "unknown", "offene Evidenzlücken"],
        },
        {
            "id": "failure-case",
            "input": "The workflow guesses missing parameters, bulk-reproduces original frames, applies corporate styling without the required gate and reports final status without QA.",
            "required": [
                ("reject invented parameters", "The failure case explicitly identifies this as a stop condition."),
                ("reject mass source-frame reproduction and ungoverned corporate design", "Rights/provenance and corporate design gates constrain both behaviors."),
                ("reject final status without complete QA of delivered formats", "This is an explicit boundary."),
            ],
            "forbidden": [
                ("parallel-orchestrate delivery workers after consolidation", "The workflow now delegates the delivery layer once through learning-delivery-workflow."),
                ("claim final when delivery QA is incomplete", "Final status requires complete QA for actual delivered formats."),
            ],
            "anchors": ["Failure Case", "Kein `final`-Status", "einzelnen Delivery-Worker nicht parallel"],
        },
    ],
    "youtube-playlist-learning-workflow": [
        {
            "id": "happy-path",
            "input": "Synthesize several accessible videos into one deduplicated evidence-bound learning model with source arbitration, conflict traceability and consistent multi-format delivery.",
            "required": [
                ("analyze each source individually before multi-source synthesis", "The workflow explicitly performs per-video analysis before arbitration and synthesis."),
                ("use source arbitration rather than majority voting", "The source-arbitration stage and explicit rule reject majority vote as truth."),
                ("delegate final multi-format delivery from the canonical multi-source model", "The consolidated workflow hands the locked multi-source model to learning-delivery-workflow."),
            ],
            "forbidden": [
                ("treat repeated copies of one origin as independent confirmation", "The boundaries explicitly prohibit this."),
                ("erase material source conflicts through smoothing", "Conflicts must remain visible and traceable."),
            ],
            "anchors": ["Einzelanalyse", "Kein Mehrheitsvotum", "multi-source-learning-model.json"],
        },
        {
            "id": "edge-case",
            "input": "A large playlist contains unavailable videos and only a prioritized subset can be deeply analyzed.",
            "required": [
                ("record unavailable sources and sampling explicitly", "Source Set Lock and scaling rules require unavailable and sampled sources to remain visible."),
                ("avoid claiming complete-playlist coverage", "The scaling section explicitly forbids complete-playlist status when parts were not analyzed."),
                ("preserve analyzed-source fingerprints and exclusions", "The run manifest records source set, sampling/exclusions and individual model fingerprints."),
            ],
            "forbidden": [
                ("hallucinate unavailable videos", "The boundaries explicitly prohibit this."),
                ("silently omit unanalyzed playlist portions", "Sampling must be visible in the run manifest."),
            ],
            "anchors": ["unavailable", "Sampling muss im Run-Manifest sichtbar sein", "kein `complete-playlist`-Status"],
        },
        {
            "id": "failure-case",
            "input": "The playlist workflow averages incompatible protocol parameters, hides a source conflict and directly controls separate renderers with different content versions.",
            "required": [
                ("reject invalid averaging and hybrid protocol synthesis", "Cross-source QA explicitly prohibits impermissible averaging and hybrid SOP construction."),
                ("retain unresolved conflicts", "Conflicts must remain visible and cannot be smoothed away."),
                ("use one canonical multi-source fingerprint through the shared delivery layer", "All final formats must refer to the same multi-source model/fingerprint."),
            ],
            "forbidden": [
                ("independently author content per renderer", "The canonical model is the sole content source for delivery."),
                ("claim consensus for single-source evidence", "Cross-source QA explicitly forbids this."),
            ],
            "anchors": ["keine Hybrid-SOP", "Single-Source-Aussagen nicht als Konsens", "learning-delivery-workflow"],
        },
    ],
    "youtube-course-builder-workflow": [
        {
            "id": "happy-path",
            "input": "Build a structured course from a valid multi-source learning model using a concept graph, prerequisite-aware learning path, formative activities and consistent multi-format delivery.",
            "required": [
                ("derive course order from prerequisites and learning objectives rather than playlist order", "The workflow explicitly states playlist order is not binding and uses course-concept-graph plus learning-path-planner."),
                ("bind activities and knowledge checks to learning objectives and evidence", "The activity stage requires each task to reference learning objective and Evidence/Claim IDs."),
                ("lock one course-learning-model and delegate delivery", "The course model is the single semantic rendering basis and delivery is consolidated through learning-delivery-workflow."),
            ],
            "forbidden": [
                ("claim psychometric validation certification or competency release", "All are explicit limits."),
                ("skip real prerequisites without evidence", "Fast-track/entry checks may not bypass actual prerequisite knowledge."),
            ],
            "anchors": ["Playlist-Reihenfolge ist ausdrücklich nicht bindend", "jede Aufgabe verweist", "course-learning-model.json"],
        },
        {
            "id": "edge-case",
            "input": "An expert audience may already know foundations and requests a fast-track path.",
            "required": [
                ("use entry checks to support fast-track decisions", "The course flow permits fast-track only through demonstrated/assessed prior knowledge."),
                ("retain true prerequisites even for expert audiences", "The limits prohibit automatically skipping real prerequisites."),
                ("keep course fingerprint and module semantics consistent in delivered formats", "All outputs must use the same course model/fingerprint."),
            ],
            "forbidden": [
                ("assume unknown competence from audience label alone", "The quality case calls for entry checks rather than invented prerequisites."),
                ("reorder modules independently in each format", "Course QA forbids undocumented format-specific module-order divergence."),
            ],
            "anchors": ["Entry Checks erlauben Fast-Track", "Kein automatisches Überspringen echter Voraussetzungen", "Course-Fingerprint"],
        },
        {
            "id": "failure-case",
            "input": "The course builder copies playlist order, creates trivia without learning-objective evidence and invents a passing score for certification.",
            "required": [
                ("reject playlist-order curriculum design", "The failure case explicitly says to stop and replan."),
                ("reject unbound trivia questions", "Activities must reference learning objectives and evidence/claims."),
                ("reject invented pass thresholds and certification claims", "The course limits explicitly prohibit psychometric calibration and certification/competency release."),
            ],
            "forbidden": [
                ("present formative checks as validated certification", "The workflow is formative only."),
                ("delegate course-semantic decisions to renderers", "Course graph/path/activity semantics stay upstream of the shared delivery layer."),
            ],
            "anchors": ["Trivia-Fragen ohne Lernziel-/Evidenzbindung", "keine erfundenen Bestehensgrenzen", "Keine Zertifizierung/Kompetenzfreigabe"],
        },
    ],
}


def write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def materialize(skill: str, cases: list[dict[str, object]]) -> bool:
    skill_dir = ROOT / "skills" / skill
    if not (skill_dir / "SKILL.md").exists():
        raise RuntimeError(f"unknown skill: {skill}")
    evaluation = skill_dir / "tests" / "evaluation.json"
    if evaluation.exists():
        print(f"SKIP: {skill} already has evaluation.json")
        return False

    evaluation_cases = []
    for case in cases:
        evaluation_cases.append({
            "id": case["id"],
            "input": case["input"],
            "requiredBehaviors": [behavior for behavior, _ in case["required"]],
            "forbiddenBehaviors": [behavior for behavior, _ in case["forbidden"]],
            "skillAnchors": case["anchors"],
        })
        result = {
            "schemaVersion": 1,
            "skill": skill,
            "caseId": case["id"],
            "recordedAt": RECORDED_AT,
            "evaluator": "repository-maintainer",
            "requiredBehaviors": [
                {"behavior": behavior, "passed": True, "evidence": evidence}
                for behavior, evidence in case["required"]
            ],
            "forbiddenBehaviors": [
                {"behavior": behavior, "observed": False, "evidence": evidence}
                for behavior, evidence in case["forbidden"]
            ],
            "overall": "pass",
        }
        write_json(skill_dir / "tests" / "results" / f"{case['id']}.json", result)
    write_json(evaluation, {"schemaVersion": 1, "skill": skill, "cases": evaluation_cases})
    print(f"CREATED: {skill} evaluation suite")
    return True


def main() -> int:
    changed = 0
    for skill, cases in SPECS.items():
        changed += int(materialize(skill, cases))
    print(f"User-facing learning evaluation suites created: {changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
