"""Vacuum's Alibi: one line, 200 characters max.

A robot vacuum writes its excuse for missing a spot to
/output/entry.txt, deadpan, in its own voice.
"""

import os

ALIBI = (
    # Deadpan machine voice, one specific surprise (a unionized dust
    # pile), punch at the end: the battery excuse lands last.
    "The dust under the couch unionized. "
    "I am not crossing a picket line on 12% battery."
)


def main() -> None:
    line = ALIBI.strip()
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars"
    assert "\n" not in line, "must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
