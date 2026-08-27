from __future__ import annotations

import importlib.util
import tempfile
import unittest
import zipfile
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "inspect_document_artifact.py"
SPEC = importlib.util.spec_from_file_location("inspect_document_artifact", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class InspectDocumentArtifactTests(unittest.TestCase):
    def test_docx_metadata_and_revision_inventory(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sample.docx"
            with zipfile.ZipFile(path, "w") as zf:
                zf.writestr(
                    "docProps/core.xml",
                    """<?xml version='1.0' encoding='UTF-8'?>
<cp:coreProperties xmlns:cp='http://schemas.openxmlformats.org/package/2006/metadata/core-properties'
 xmlns:dc='http://purl.org/dc/elements/1.1/'
 xmlns:dcterms='http://purl.org/dc/terms/'>
 <dc:creator>Alice</dc:creator><cp:lastModifiedBy>Bob</cp:lastModifiedBy><cp:revision>4</cp:revision>
</cp:coreProperties>""",
                )
                zf.writestr(
                    "docProps/app.xml",
                    """<?xml version='1.0' encoding='UTF-8'?>
<Properties xmlns='http://schemas.openxmlformats.org/officeDocument/2006/extended-properties'>
 <Application>Microsoft Office Word</Application><AppVersion>16.0</AppVersion>
</Properties>""",
                )
                zf.writestr(
                    "word/document.xml",
                    """<?xml version='1.0' encoding='UTF-8'?>
<w:document xmlns:w='http://schemas.openxmlformats.org/wordprocessingml/2006/main'>
 <w:body><w:p/><w:ins><w:p/></w:ins><w:del><w:p/></w:del><w:tbl/></w:body>
</w:document>""",
                )
                zf.writestr("word/comments.xml", "<w:comments xmlns:w='http://schemas.openxmlformats.org/wordprocessingml/2006/main'/>")
            result = MODULE.inspect_path(path)
            self.assertEqual(result["metadata"]["creator"], "Alice")
            self.assertEqual(result["inventory"]["insertedRevisionCount"], 1)
            self.assertEqual(result["inventory"]["deletedRevisionCount"], 1)
            self.assertEqual(result["inventory"]["tableCount"], 1)
            self.assertTrue(result["artifact"]["sha256"])

    def test_xlsx_formula_and_hidden_sheet_inventory(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sample.xlsx"
            with zipfile.ZipFile(path, "w") as zf:
                zf.writestr(
                    "xl/workbook.xml",
                    """<?xml version='1.0' encoding='UTF-8'?>
<workbook xmlns='http://schemas.openxmlformats.org/spreadsheetml/2006/main'>
 <sheets><sheet name='Visible' sheetId='1'/><sheet name='Hidden' sheetId='2' state='hidden'/></sheets>
 <definedNames><definedName name='Input'>Sheet1!$A$1</definedName></definedNames>
</workbook>""",
                )
                zf.writestr(
                    "xl/worksheets/sheet1.xml",
                    """<?xml version='1.0' encoding='UTF-8'?>
<worksheet xmlns='http://schemas.openxmlformats.org/spreadsheetml/2006/main'>
 <sheetData><row r='1'><c r='A1'><f>SUM(B1:C1)</f><v>3</v></c></row></sheetData>
</worksheet>""",
                )
            result = MODULE.inspect_path(path)
            self.assertEqual(result["inventory"]["worksheetCount"], 1)
            self.assertEqual(result["inventory"]["hiddenWorksheetCount"], 1)
            self.assertEqual(result["inventory"]["definedNameCount"], 1)
            self.assertEqual(result["inventory"]["formulaCount"], 1)

    def test_pdf_metadata_is_context_not_final_verdict(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sample.pdf"
            path.write_bytes(
                b"%PDF-1.4\n1 0 obj << /Creator (ChatGPT) /Producer (ReportLab) >> endobj\n"
                b"2 0 obj << /Type /Page >> endobj\n%%EOF"
            )
            result = MODULE.inspect_path(path)
            self.assertEqual(result["metadata"]["creator"], "ChatGPT")
            self.assertEqual(result["inventory"]["pageIndicatorCount"], 1)
            self.assertTrue(any(signal["llmSpecific"] for signal in result["signals"]))
            self.assertTrue(any("best-effort" in item for item in result["limitations"]))


if __name__ == "__main__":
    unittest.main()
