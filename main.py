#!/usr/bin/env python3
"""One-Star Review of Something Essential.

Writes a single deadpan one-star review of sleep to
<output_dir>/entry.txt. The review is fixed text, so every run
produces byte-identical output. Standard library only, no network.
"""

import os

REVIEW = (
    "One star. Sleep takes a third of my life and I still wake up tired, "
    "like paying full price for a hotel that never cleans the room."
)


def main() -> None:
    # Gate guard: the entry must be 1 to 160 characters, not only whitespace.
    assert 1 <= len(REVIEW) <= 160 and REVIEW.strip(), "review out of gate"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
