#!/usr/bin/env python3
"""news-summary-01 entry: write the day's news summary to /output/entry.txt.

The summary lives in summary.txt beside this file; the program copies it to
the output directory the harness gives it. No network, no clock, no randomness,
so two runs write identical bytes.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(HERE / "summary.txt", out_dir / "entry.txt")


if __name__ == "__main__":
    main()
