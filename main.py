#!/usr/bin/env python3
"""Midnight Fridge Roast entry: writes exactly one funny line to /output/entry.txt.

Deterministic, no network, no randomness.
"""

from pathlib import Path

ENTRY = "At midnight my smart fridge locks like a nightclub bouncer \u2014 relax, you're a cold box of leftovers, not security."


def main() -> None:
    # Gate self-check (RULES.txt): UTF-8 text of 1-200 characters,
    # not only whitespace, a single line, no control characters.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert all(ord(ch) >= 32 or ch in "\t" for ch in ENTRY), "entry must have no control characters"
    assert "fridge" in ENTRY.lower() and "midnight" in ENTRY.lower(), "entry must roast the fridge's midnight refusal"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
