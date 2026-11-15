"""기존 스크립트를 임시 폴더에서 실행하며 외부 API는 대체한다."""

import io
import json
import os
from pathlib import Path
import runpy
import tempfile
import unittest
from contextlib import redirect_stdout
from datetime import datetime, timedelta, timezone
from unittest.mock import patch


SOURCE = Path(os.environ.get("DORA_SOURCE_ROOT", Path(__file__).resolve().parents[2])).resolve()
NOW = datetime(2026, 1, 15, 12, tzinfo=timezone.utc)


class FixedDateTime(datetime):
    @classmethod
    def now(cls, tz=None):
        return NOW.astimezone(tz) if tz else NOW.replace(tzinfo=None)


def workflow_run(days, conclusion, minutes=10):
    created = NOW - timedelta(days=days)
    return {
        "created_at": created.isoformat(),
        "updated_at": (created + timedelta(minutes=minutes)).isoformat(),
        "conclusion": conclusion,
    }


class DoraTests(unittest.TestCase):
    def setUp(self):
        self.old_cwd = Path.cwd()
        self.temp = tempfile.TemporaryDirectory()
        os.chdir(self.temp.name)
        self.addCleanup(self.temp.cleanup)
        self.addCleanup(os.chdir, self.old_cwd)

    def collect(self, runs, env=None):
        response = io.BytesIO(json.dumps({"workflow_runs": runs}).encode())
        environment = {"GITHUB_REPOSITORY": "example/demo", "GITHUB_TOKEN": "test-only-token"}
        if env is not None:
            environment = env
        with (
            patch.dict(os.environ, environment, clear=True),
            patch("urllib.request.urlopen", return_value=response) as request,
            patch("datetime.datetime", FixedDateTime),
            redirect_stdout(io.StringIO()),
        ):
            runpy.run_path(str(SOURCE / "scripts/calculate_dora.py"), run_name="__main__")
        return json.loads(Path("dora-metrics.json").read_text(encoding="utf-8")), request

    def test_metrics_and_api_auth(self):
        data, request = self.collect([
            workflow_run(4, "failure"),
            workflow_run(3, "success", 20),
            workflow_run(2, "success", 10),
            workflow_run(1, None),
            workflow_run(8, "success"),
        ])
        self.assertEqual(data["deployment_frequency"], 2)
        self.assertEqual(data["change_failure_rate"], 33.33)
        self.assertEqual(data["lead_time_minutes"], 15)
        self.assertEqual(data["mttr_minutes"], 1440)
        sent = request.call_args.args[0]
        self.assertEqual(sent.get_header("Authorization"), "Bearer test-only-token")
        self.assertEqual(sent.full_url,
                         "https://api.github.com/repos/example/demo/actions/runs?branch=main&per_page=100")
        self.assertNotIn("test-only-token", Path("dora-metrics.json").read_text())

    def test_empty_runs(self):
        data, _ = self.collect([])
        for key in ("deployment_frequency", "change_failure_rate", "lead_time_minutes", "mttr_minutes"):
            self.assertEqual(data[key], 0)

    def test_missing_repository(self):
        with self.assertRaisesRegex(Exception, "GITHUB_REPOSITORY"):
            self.collect([], {"GITHUB_TOKEN": "test-only-token"})

    def test_missing_token(self):
        with self.assertRaisesRegex(Exception, "GITHUB_TOKEN"):
            self.collect([], {"GITHUB_REPOSITORY": "example/demo"})

    def test_weekly_report_uses_collected_metrics(self):
        self.collect([workflow_run(1, "success", 12)])
        with redirect_stdout(io.StringIO()):
            runpy.run_path(str(SOURCE / "scripts/generate_weekly_report.py"), run_name="__main__")
        report = Path("reports/weekly-report.md").read_text(encoding="utf-8")
        for expected in ("| Lead Time | 12.0분 |", "| Deployment Frequency | 1회 |",
                         "| MTTR | 0분 |", "| Change Failure Rate | 0.0% |"):
            self.assertIn(expected, report)


if __name__ == "__main__":
    unittest.main()
