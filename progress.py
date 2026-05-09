#!/usr/bin/env python3
"""Run every challenge file and print a progress summary."""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CHALLENGES = ROOT / "challenges"
SUMMARY_RE = re.compile(r"(\d+)/(\d+) tests passed\.")


def run_one(py_file: Path) -> tuple[int, int]:
    result = subprocess.run(
        [sys.executable, str(py_file)],
        capture_output=True,
        text=True,
    )
    match = SUMMARY_RE.search(result.stdout)
    if match is None:
        return (0, 0)
    return (int(match.group(1)), int(match.group(2)))


def main() -> None:
    if not CHALLENGES.is_dir():
        print(f"No challenges/ directory at {CHALLENGES}")
        return

    grand_passed = 0
    grand_total = 0

    print()
    topics = sorted(p for p in CHALLENGES.iterdir() if p.is_dir())
    for topic in topics:
        topic_passed = 0
        topic_total = 0
        for difficulty in ("easy", "medium", "hard"):
            d = topic / difficulty
            if not d.is_dir():
                continue
            for f in sorted(d.glob("*.py")):
                p, t = run_one(f)
                topic_passed += p
                topic_total += t

        if topic_total == 0:
            continue

        grand_passed += topic_passed
        grand_total += topic_total
        marker = "OK" if topic_passed == topic_total else "  "
        print(f"  {topic.name:30s}  {topic_passed:3d}/{topic_total:<3d}  {marker}")

    print()
    if grand_total == 0:
        print("No challenges found yet.")
    else:
        print(f"Total: {grand_passed}/{grand_total} tests passed across all challenges.")


if __name__ == "__main__":
    main()
