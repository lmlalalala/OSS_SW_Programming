"""Build a source archive or package generated outputs without publishing them."""

import argparse
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


def package(root, destination, paths):
    destination.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(destination, "w", ZIP_DEFLATED) as archive:
        for name in paths:
            archive.write(root / name, name)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=["build", "demo"])
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.mode == "build":
        paths = ["scripts/calculate_dora.py", "scripts/generate_weekly_report.py",
                 "dashboard/index.html"]
    else:
        paths = ["dora-metrics.json", "reports/weekly-report.md", "dashboard/index.html"]
    # 고정된 파일 목록만 포함한다. 환경변수나 작업 폴더 전체를 저장하지 않는다.
    package(args.root, args.output, paths)
    print(f"Created {args.output} ({len(paths)} files). No external deployment.")


if __name__ == "__main__":
    main()
