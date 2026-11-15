import json
from pathlib import Path
import runpy
import subprocess
import sys
import tempfile
import unittest
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[2]
PACKAGE = ROOT / "week7/package_demo.py"


class PackageTests(unittest.TestCase):
    def test_build_archive_contains_runnable_scripts(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "source.zip"
            subprocess.run([sys.executable, str(PACKAGE), "build", "--root", str(ROOT),
                            "--output", str(output)], check=True, capture_output=True)
            with ZipFile(output) as archive:
                self.assertEqual(set(archive.namelist()), {
                    "scripts/calculate_dora.py", "scripts/generate_weekly_report.py",
                    "dashboard/index.html",
                })
                for name in archive.namelist():
                    self.assertEqual(archive.read(name), (ROOT / name).read_bytes())

    def test_demo_archive_excludes_unrelated_secret_file(self):
        package = runpy.run_path(str(PACKAGE))["package"]
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "dora-metrics.json").write_text(json.dumps({"deployment_frequency": 0}))
            (root / ".env").write_text("PRIVATE_TOKEN=do-not-package")
            output = root / "demo.zip"
            package(root, output, ["dora-metrics.json"])
            with ZipFile(output) as archive:
                self.assertEqual(archive.namelist(), ["dora-metrics.json"])
                self.assertNotIn(b"do-not-package", archive.read("dora-metrics.json"))
