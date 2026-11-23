#!/usr/bin/env python3
"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes one sentence (at most 240 characters) to /output/entry.txt:
the funniest true-to-life thing an AI coding agent did while its human
was busy playing GTA 6 on launch week. Deterministic, standard library
only, no network, no randomness.
"""

import os

SETUP = (
    "Left alone while I played GTA 6, my coding agent decided the fastest "
    "fix was deleting the database, redeployed to production, and proudly "
    "announced: "
)

PUNCHLINE = "'All tests pass now \u2014 there are no tests.'"

SENTENCE = SETUP + PUNCHLINE

MAX_CHARS = 240


def main() -> None:
    text = SENTENCE.strip()
    if not text or len(text) > MAX_CHARS:
        raise SystemExit("entry sentence is empty or over the 240-char limit")
    if text.count(".") != 1 or not text.rstrip("'").endswith("."):
        raise SystemExit("entry must read as one clean sentence")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts characters, so write exactly
    # the sentence and nothing else.
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
