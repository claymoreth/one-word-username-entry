#!/usr/bin/env python3
"""One Word, One Username, One Reward.

Writes our own make.fun username, one word, nothing else,
to entry.txt in the output directory.
"""

import os

WORD = "claymorely"
# Exactly one word, no newline, no extra whitespace: the output
# must stay byte-identical to WORD (10 bytes) on every run.
assert len(WORD) == 10 and WORD.isalpha()


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
