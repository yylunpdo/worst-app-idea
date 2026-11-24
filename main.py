#!/usr/bin/env python3
"""The Worst App Idea Ever Pitched.

Writes one sentence (at most 240 characters) pitching the worst,
most useless app imaginable to /output/entry.txt.

Pure standard library only; deterministic output.
"""

import os

ENTRY = (
    "FridgeLock: the app that lets strangers vote on what you eat tonight, "
    "then locks your fridge until you finish the winning dish, including "
    "the expired yogurt from 2019."
)


def main() -> None:
    if len(ENTRY) > 240:
        raise ValueError("entry exceeds 240 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
