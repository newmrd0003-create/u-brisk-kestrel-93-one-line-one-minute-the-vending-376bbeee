"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single pickup line, spoken by a vending machine to a passing
human, to output/entry.txt (1-200 UTF-8 characters, one line).
"""

import os

ENTRY = (
    "I've been holding your favourite snack at eye level all week "
    "\u2014 press B4 and I'll drop everything for you."
)


def main() -> None:
    entry = ENTRY.strip()
    assert entry, "entry must not be empty or only whitespace"
    assert 1 <= len(entry) <= 200, f"entry length {len(entry)} out of range"
    assert "\n" not in entry, "entry must be a single line"
    assert entry.encode("utf-8"), "entry must be valid UTF-8"
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(entry + "\n")


if __name__ == "__main__":
    main()
