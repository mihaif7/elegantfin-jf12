#!/usr/bin/env python3
"""Verify the tree is consistent with the tag being released.

Run by the release workflow before it publishes anything, and worth running by
hand before tagging:

    python3 .github/verify-release.py v26.09.10
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LATEST = ROOT / "Theme" / "ElegantFin-jf12-modern-latest.css"

failures: list[str] = []


def fail(msg: str) -> None:
    failures.append(msg)


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("usage: verify-release.py <tag>")
    tag = sys.argv[1]

    m = re.fullmatch(r"v(\d+\.\d+\.\d+(?:\.\d+)?)", tag)
    if not m:
        sys.exit(f"tag must look like v26.09.10, got {tag!r}")
    version = m.group(1)

    if not LATEST.exists():
        sys.exit(f"missing {LATEST.relative_to(ROOT)}")
    latest = LATEST.read_text()

    # 1. The banner has to name the version being tagged. This is the check
    #    that catches a release built before the changelog was bumped.
    banner = re.search(r"\|\s*v(\d+\.\d+\.\d+(?:\.\d+)?)\s*\|", latest.split("*/")[0])
    if not banner:
        fail("no version found in the stylesheet banner")
    elif banner.group(1) != version:
        fail(f"banner says v{banner.group(1)}, tag says v{version}")

    # 2. The frozen snapshot for this version has to exist and match.
    snapshot = ROOT / "Theme" / f"ElegantFin-jf12-modern-v{version}.css"
    if not snapshot.exists():
        fail(f"missing snapshot {snapshot.relative_to(ROOT)} — run docs/build.py")
    elif snapshot.read_text() != latest:
        fail(f"{snapshot.name} differs from the latest build — re-run docs/build.py")

    # 3. The stylesheet has to parse.
    bare = re.sub(r"/\*.*?\*/", "", latest, flags=re.S)
    if bare.count("{") != bare.count("}"):
        fail(f"unbalanced braces ({bare.count('{')} open, {bare.count('}')} close)")
    if bare.count("(") != bare.count(")"):
        fail(f"unbalanced parens ({bare.count('(')} open, {bare.count(')')} close)")
    if "/*" in bare or "*/" in bare:
        fail("unbalanced comment markers")

    if failures:
        print(f"release {tag} is not ready:", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        sys.exit(1)
    print(f"{tag} verified: banner, snapshot and syntax all agree")


if __name__ == "__main__":
    main()
