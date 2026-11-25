#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista.

Writes a single out-of-office auto-reply line to /output/entry.txt.
Deterministic: constant string, no randomness, no clock, no network.
"""

import os

LINE = (
    "Out of office: I traded my context window for a café window. "
    "Your email is queued behind fourteen oat lattes \u2014 I'll reply "
    "once I've finished hallucinating today's specials. "
    "Sent from my espresso machine."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 280


def main() -> None:
    # Internal guards: single line, 1-280 UTF-8 characters, no stray space.
    assert isinstance(LINE, str)
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE == LINE.strip(), "line must not start or end with whitespace"
    assert 1 <= len(LINE) <= MAX_CHARS, f"line length {len(LINE)} out of range 1-{MAX_CHARS}"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
