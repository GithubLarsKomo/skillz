from __future__ import annotations

import argparse
import hashlib
import html
import json
from pathlib import Path

from docx import Document
from docx.shared import Inches, Pt
from pptx import Presentation
from pptx.util import Inches as PInches, Pt as PPt

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FIXTURE = ROOT / "tests" / "fixtures" / "youtube-learning" / "pcr-qpcr-course-large-golden.json"
DEFAULT_OUT = ROOT / "build" / "youtube-course-large-golden"


def canonical_fingerprint(data: dict) -> str:
    payload = json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def model(data: dict, fp: str) -> dict:
    return {"schemaVersion":1,"courseId":data["courseId"],"title":data["title"],"audience":data["audience"],"language":data["language"],"courseDepth":data["courseDepth"],"courseFingerprint":fp,"sources":data["sources"],"assumedPrerequisites":data["assumedPrerequisites"],"modules":data["modules"],"learningObjectives":data["learningObjectives"],"knowledgeChecks":data["knowledgeChecks"],"designAuthority":data["designAuthority"],"renderTargets":data["renderTargets"]}


def generate_svg(data: dict, fp: str, out: Path) -> None:
    ys = {m["moduleId"]:150+i*125 for i,m in enumerate(data["modules"])}
    edges=[]; boxes=[]
    for m in data["modules"]:
        y=ys[m["moduleId"]]
        for pre in m.get("prerequisites",[]):
            edges.append(f'<path d="M700 {ys[pre]+88} L700 {y}" stroke="#343a40" stroke-width="2.5" marker-end="url(#arrow)"/>')
        boxes.append(f'<rect x="270" y="{y}" width="860" height="88" rx="14" fill="white" stroke="#343a40" stroke-width="2"/><text x="300" y="{y+31}" font-family="Arial, sans-serif" font-size="22" font-weight="700">{m["moduleId"]} · {html.escape(m["title"])}</text><text x="300" y="{y+62}" font-family="Arial, sans-serif" font-size="16">{html.escape(m["competencePromise"])}</text>')
    h=250+len(data["modules"])*125
    out.write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1400 {h}" role="img" aria-labelledby="title desc"><title id="title">Course Map PCR und qPCR</title><desc id="desc">Acht Module mit fachlichen Voraussetzungskanten. Course fingerprint {fp[:12]}.</desc><defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="#343a40"/></marker></defs><rect width="100%" height="100%" fill="#f8f9fa"/><text x="90" y="70" font-family="Arial, sans-serif" font-size="34" font-weight="700">PCR → qPCR Learning Path</text><text x="90" y="105" font-family="Arial, sans-serif" font-size="16">Course fingerprint: {fp[:12]} · prerequisite-based, not playlist order</text>{''.join(edges)}{''.join(boxes)}</svg>''',encoding="utf-8")


def generate_html(data: dict, fp: str, out: Path) -> None:
    modules=[]
    for m in data["modules"]:
        objectives=''.join(f'<li>{html.escape(data["learningObjectives"][oid])}</li>' for oid in m["objectives"])
        modules.append(f'<section class="module" id="{m["moduleId"]}"><h2>{m["moduleId"]} · {html.escape(m["title"])}</h2><p class="promise">{html.escape(m["competencePromise"])}</p><h3>Lernziele</h3><ul>{objectives}</ul><p><strong>Voraussetzungen:</strong> {html.escape(", ".join(m.get("prerequisites",[])) or "Einstieg")}</p><p><strong>Quellen:</strong> {html.escape(", ".join(m["sourceScope"]))}</p></section>')
    checks=''.join(f'<li><strong>{q["questionId"]}</strong> {html.escape(q["prompt"])}</li>' for q in data["knowledgeChecks"])
    rows=''.join(f'<tr><td>{s["sourceId"]}</td><td>{html.escape(s["channel"])}</td><td><a href="https://www.youtube.com/watch?v={s["youtubeVideoId"]}">{html.escape(s["title"])}</a></td><td>{html.escape(s["role"])}</td></tr>' for s in data["sources"])
    out.write_text(f'''<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(data["title"])}</title><style>body{{font-family:Arial,sans-serif;margin:0;color:#212529;background:#f8f9fa}}main{{max-width:1120px;margin:auto;padding:32px}}header{{padding:52px 32px;background:#fff;border-bottom:1px solid #dee2e6}}header>div{{max-width:1120px;margin:auto}}h1{{font-size:42px;margin:0 0 12px}}.meta{{color:#495057}}.course-map{{width:100%;background:white;margin:28px 0;border:1px solid #dee2e6}}.grid{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px}}.module{{background:white;border:1px solid #dee2e6;border-radius:14px;padding:24px}}.promise{{font-size:18px}}table{{width:100%;border-collapse:collapse;background:white}}th,td{{padding:10px;border:1px solid #dee2e6;text-align:left;overflow-wrap:anywhere}}@media(max-width:760px){{h1{{font-size:32px}}.grid{{grid-template-columns:1fr}}main{{padding:18px}}}}@media print{{body{{background:white}}.module{{break-inside:avoid}}}}</style></head><body data-course-fingerprint="{fp}"><header><div><p>Golden Course Reference · 12 reale YouTube-Quellen</p><h1>{html.escape(data["title"])}</h1><p class="meta">Course fingerprint {fp[:12]} · Zielgruppe: {html.escape(data["audience"])}</p></div></header><main><h2>Course Map</h2><object class="course-map" data="course-map.svg" type="image/svg+xml" aria-label="Course Map"></object><div class="grid">{''.join(modules)}</div><section><h2>Formative Knowledge Checks</h2><ol>{checks}</ol></section><section><h2>Source Map</h2><table><thead><tr><th>ID</th><th>Quelle</th><th>Video</th><th>Rolle</th></tr></thead><tbody>{rows}</tbody></table></section></main></body></html>''',encoding="utf-8")


def generate_pptx(data: dict, fp: str, out: Path) -> None:
    prs=Presentation(); prs.slide_width=PInches(13.333); prs.slide_height=PInches(7.5)
    slide=prs.slides.add_slide(prs.slide_layouts[5]); tf=slide.shapes.add_textbox(PInches(.8),PInches(1),PInches(11.7),PInches(4.5)).text_frame
    p=tf.paragraphs[0]; p.text=data["title"]; p.font.size=PPt(30); p.font.bold=True
    for text,size in [("Instructor / Workshop Golden Reference",20),(f'12 sources · 8 modules · fingerprint {fp[:12]}',15)]: p=tf.add_paragraph(); p.text=text; p.font.size=PPt(size)
    for m in data["modules"]:
        slide=prs.slides.add_slide(prs.slide_layouts[5]); tf=slide.shapes.add_textbox(PInches(.7),PInches(.55),PInches(12),PInches(6.1)).text_frame
        p=tf.paragraphs[0]; p.text=f'{m["moduleId"]} · {m["title"]}'; p.font.size=PPt(28); p.font.bold=True
        p=tf.add_paragraph(); p.text=m["competencePromise"]; p.font.size=PPt(18)
        p=tf.add_paragraph(); p.text="Lernziele"; p.font.size=PPt(18); p.font.bold=True
        for oid in m["objectives"]: p=tf.add_paragraph(); p.text=data["learningObjectives"][oid]; p.level=1; p.font.size=PPt(16)
        for text in [f'Quellen: {", ".join(m["sourceScope"])}',f'Exit Criteria: {"; ".join(m["exitCriteria"])}']:
            p=tf.add_paragraph(); p.text=text; p.font.size=PPt(13)
        f=slide.shapes.add_textbox(PInches(10.6),PInches(7.05),PInches(2.1),PInches(.25)).text_frame.paragraphs[0]; f.text=fp[:12]; f.font.size=PPt(8)
    slide=prs.slides.add_slide(prs.slide_layouts[5]); tf=slide.shapes.add_textbox(PInches(.8),PInches(.6),PInches(11.7),PInches(6.1)).text_frame
    p=tf.paragraphs[0]; p.text="Formative Knowledge Checks"; p.font.size=PPt(28); p.font.bold=True
    for q in data["knowledgeChecks"]: p=tf.add_paragraph(); p.text=f'{q["questionId"]}: {q["prompt"]}'; p.font.size=PPt(14)
    prs.core_properties.subject=f"Course fingerprint {fp}"; prs.save(out)


def generate_docx(data: dict, fp: str, out: Path) -> None:
    doc=Document(); sec=doc.sections[0]
    sec.top_margin=Inches(.7); sec.bottom_margin=Inches(.7); sec.left_margin=Inches(.8); sec.right_margin=Inches(.8)
    doc.add_heading(data["title"],0); doc.add_paragraph(f"Study Guide · 12 sources · 8 modules · Course fingerprint {fp[:12]}"); doc.add_heading("Course Map",1)
    for m in data["modules"]: doc.add_paragraph(f'{m["moduleId"]} → {m["title"]} | Voraussetzung: {", ".join(m.get("prerequisites",[])) or "Einstieg"}')
    for m in data["modules"]:
        doc.add_page_break(); doc.add_heading(f'{m["moduleId"]} · {m["title"]}',1); doc.add_paragraph(m["competencePromise"]); doc.add_heading("Lernziele",2)
        for oid in m["objectives"]: doc.add_paragraph(data["learningObjectives"][oid],style="List Bullet")
        doc.add_heading("Exit Criteria",2)
        for item in m["exitCriteria"]: doc.add_paragraph(item,style="List Bullet")
        doc.add_paragraph(f'Quellen: {", ".join(m["sourceScope"])}')
        related=[q for q in data["knowledgeChecks"] if q["moduleId"]==m["moduleId"]]
        if related:
            doc.add_heading("Checkpoint",2)
            for q in related: doc.add_paragraph(q["prompt"])
    doc.add_page_break(); doc.add_heading("Source Map",1); table=doc.add_table(rows=1,cols=4)
    for i,text in enumerate(["ID","Channel","Video","Role"]): table.rows[0].cells[i].text=text
    for s in data["sources"]:
        c=table.add_row().cells; c[0].text=s["sourceId"]; c[1].text=s["channel"]; c[2].text=s["title"]; c[3].text=s["role"]
    sec.footer.paragraphs[0].text=f"Golden Reference · {fp[:12]}"
    for run in sec.footer.paragraphs[0].runs: run.font.size=Pt(8)
    doc.core_properties.subject=f"Course fingerprint {fp}"; doc.save(out)


def main() -> None:
    ap=argparse.ArgumentParser(); ap.add_argument("--fixture",type=Path,default=DEFAULT_FIXTURE); ap.add_argument("--out",type=Path,default=DEFAULT_OUT); a=ap.parse_args()
    data=json.loads(a.fixture.read_text(encoding="utf-8")); fp=canonical_fingerprint(data); a.out.mkdir(parents=True,exist_ok=True)
    (a.out/"course-learning-model.json").write_text(json.dumps(model(data,fp),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    generate_svg(data,fp,a.out/"course-map.svg"); generate_html(data,fp,a.out/"index.html"); generate_pptx(data,fp,a.out/"instructor-deck.pptx"); generate_docx(data,fp,a.out/"study-guide.docx")
    manifest={"courseFingerprint":fp,"sourceCount":len(data["sources"]),"moduleCount":len(data["modules"]),"artifacts":["course-learning-model.json","course-map.svg","index.html","instructor-deck.pptx","study-guide.docx"]}
    (a.out/"artifact-manifest.json").write_text(json.dumps(manifest,indent=2)+"\n",encoding="utf-8"); print(json.dumps(manifest,indent=2))


if __name__=="__main__": main()
