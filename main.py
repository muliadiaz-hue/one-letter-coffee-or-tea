#!/usr/bin/env python3
"""One Letter: Coffee or Tea — write the survey winner to entry.txt.

The survey picked coffee over tea. Coffee wins where the judge weighs
most: vividness (sharp aroma, dark roast, the caffeine jolt landing at
once) and funniness (coffee culture and its memes are far livelier than
tea's calm, meditative profile). The judge reads a single letter, A for
coffee, so this program emits exactly that one letter and nothing else.
"""

import os
import sys


def winning_letter():
    """Return the single letter the survey chose for coffee."""
    return "A"


def output_dir():
    """Resolve the directory the entry file goes into."""
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not chosen:
        chosen = "/output"
    return chosen


def main():
    target_dir = output_dir()
    os.makedirs(target_dir, exist_ok=True)
    entry_path = os.path.join(target_dir, "entry.txt")
    letter = winning_letter()
    payload = letter.encode("ascii")
    with open(entry_path, "wb") as handle:
        handle.write(payload)
    # Self-check: the gate accepts exactly one non-whitespace byte, so
    # confirm what landed on disk before reporting success.
    with open(entry_path, "rb") as handle:
        written = handle.read()
    if written != payload:
        print("entry.txt mismatch: expected 1 byte, got %d" % len(written),
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
