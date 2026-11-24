#!/usr/bin/env python3
"""One-star review of something essential.

Writes a single deadpan one-star review (at most 160 characters, no
trailing newline) to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

REVIEW = "Breathing: automatic for decades, until one stray thought turned it into a manual job I cannot quit."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
