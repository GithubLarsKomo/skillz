from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import run_live_provider_validation as live
from score_capability_interpretations import load_json


class LiveProviderValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.benchmark = load_json(ROOT / "benchmarks" / "capability-interpretation-v1.json")
        cls.baseline = load_json(ROOT / "benchmarks" / "capability-interpretation-baseline-v1.json")
        cls.index = load_json(ROOT / "docs" / "skill-capability-index.json")
        cls.proposals_by_case = {row["caseId"]: row["proposal"] for row in cls.baseline["proposals"]}
        cls.case_by_source = {case["sourceText"]: case["id"] for case in cls.benchmark["cases"]}

    def transport(self, endpoint, body, headers, timeout):
        self.assertEqual(endpoint, "https://provider.example/v1/chat/completions")
        self.assertEqual(headers["Authorization"], "Bearer top-secret-token")
        self.assertEqual(timeout, 30)
        request_body = json.loads(body.decode("utf-8"))
        interpretation_request = json.loads(request_body["messages"][1]["content"])
        case_id = self.case_by_source[interpretation_request["sourceText"]]
        response = {
            "choices": [
                {"message": {"content": json.dumps(self.proposals_by_case[case_id], sort_keys=True)}}
            ]
        }
        return json.dumps(response).encode("utf-8")

    def run_live_case(self, mode="qualify", case_id=None, transport=None, environ=None):
        return live.run_live(
            mode,
            "live-test-provider",
            "https://provider.example/v1/chat/completions",
            "live-test-model",
            self.benchmark,
            self.index,
            case_id=case_id,
            api_key_env="TEST_PROVIDER_KEY",
            timeout_seconds=30,
            transport=transport or self.transport,
            environ={"TEST_PROVIDER_KEY": "top-secret-token"} if environ is None else environ,
        )

    def test_full_baseline_qualifies(self):
        summary, qualification = self.run_live_case()
        expected_count = len(self.benchmark["cases"])
        self.assertEqual(summary["status"], "qualified")
        self.assertTrue(summary["qualified"])
        self.assertEqual(summary["caseCount"], expected_count)
        self.assertEqual(summary["passedCount"], expected_count)
        self.assertEqual(summary["failedCount"], 0)
        self.assertTrue(qualification["qualified"])

    def test_smoke_only_runs_one_case_without_qualification(self):
        summary, qualification = self.run_live_case("smoke-only", "exact-review-output")
        self.assertEqual(summary["status"], "passed")
        self.assertIsNone(summary["qualified"])
        self.assertEqual(summary["completedCaseIds"], ["exact-review-output"])
        self.assertIsNone(qualification)

    def test_transport_failure_is_redacted_and_stage_specific(self):
        def broken_transport(endpoint, body, headers, timeout):
            raise ValueError("provider HTTP error: 503")

        summary, qualification = self.run_live_case(transport=broken_transport)
        self.assertEqual(summary["status"], "failed")
        self.assertEqual(summary["failedStage"], "provider-collection")
        self.assertIn("503", summary["error"])
        self.assertIsNone(qualification)

    def test_missing_secret_fails_without_exposing_secret_name_value(self):
        summary, qualification = self.run_live_case(environ={})
        self.assertEqual(summary["failedStage"], "provider-collection")
        rendered = live.canonical_json(summary)
        self.assertNotIn("top-secret-token", rendered)
        self.assertIn("TEST_PROVIDER_KEY", rendered)
        self.assertIsNone(qualification)

    def test_summary_never_contains_response_or_secret(self):
        summary, _ = self.run_live_case()
        rendered = live.canonical_json(summary)
        self.assertNotIn("top-secret-token", rendered)
        self.assertNotIn("choices", rendered)
        self.assertNotIn("confidenceBasis", rendered)
        self.assertNotIn("proposal", rendered)

    def test_repeated_summary_is_byte_stable(self):
        first = live.canonical_json(self.run_live_case()[0])
        second = live.canonical_json(self.run_live_case()[0])
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
