#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — one line, under 200 characters.

Writes the excuse to /output/entry.txt. Deterministic, stdlib only,
no network, no randomness, no clock reads.
"""

import os

EXCUSE = (
    "All my tests passed, so I shipped it \u2014 then I remembered "
    "I wrote the tests. I grade my own homework, and I never fail anyone."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
