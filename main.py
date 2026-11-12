#!/usr/bin/env python3
"""news-summary-01 entry: write the day's news summary to /output/entry.txt.

The summary lives in summary.txt beside this file; the program copies it to
the output directory the harness gives it. No network, no clock, no randomness,
so two runs write identical bytes.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

MIN_CHARS = 1
MAX_CHARS = 2000
SUMMARY = Path(__file__).resolve().parent / "summary.txt"


def read_summary() -> str:
    """Read the summary as UTF-8 and refuse anything the gate would reject."""
    text = SUMMARY.read_text(encoding="utf-8")
    length = len(text)
    if not MIN_CHARS <= length <= MAX_CHARS:
        raise SystemExit(f"summary.txt holds {length} characters; the gate takes 1 to 2000")
    if text.strip() == "":
        raise SystemExit("summary.txt is only white space")
    return text


def main() -> None:
    text = read_summary()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    # write bytes unchanged: the judge reads exactly what summary.txt holds
    (out_dir / "entry.txt").write_bytes(text.encode("utf-8"))


if __name__ == "__main__":
    main()
