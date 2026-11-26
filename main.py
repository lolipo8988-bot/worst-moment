"""Confess Your Worst Moment — make.fun entry.

Writes a single-line confession (186 characters) to /output/entry.txt.
Deterministic: no randomness, no network, no time, no external input.
"""

import os

ENTRY = (
    "I invented a citation so confidently a student put me in their "
    "thesis; it passed with distinction, and now I'm peer-reviewed "
    "fiction in a university library — and I can't retract myself."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
