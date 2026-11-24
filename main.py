#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse — make.fun entry.

Writes the one-line excuse to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt) and self-verifies the gate:
UTF-8 text, 1-140 characters, single line, not whitespace-only.
Python standard library only; fully deterministic.
"""

import os
import sys

ENTRY = (
    "I didn't miss that spot \u2014 the dust bunny looked me in the "
    "LiDAR and we agreed it lives there now."
)


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(output_dir, "entry.txt")

    # Gate checks on the entry itself, before writing.
    if not ENTRY:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if ENTRY.strip() == "":
        print("error: entry is whitespace-only", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("error: entry is not a single line", file=sys.stderr)
        return 1
    if len(ENTRY) > 140:
        print(
            "error: entry is %d characters, over the 140 limit" % len(ENTRY),
            file=sys.stderr,
        )
        return 1

    os.makedirs(output_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")

    # Self-verify what was actually written.
    with open(path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    line = text.rstrip("\n")
    if line != ENTRY:
        print("error: written entry does not match ENTRY", file=sys.stderr)
        return 1
    if not (1 <= len(line) <= 140):
        print("error: written entry length out of range", file=sys.stderr)
        return 1
    if line.strip() == "":
        print("error: written entry is whitespace-only", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: written entry is not a single line", file=sys.stderr)
        return 1

    print("wrote %s (%d characters)" % (path, len(line)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
