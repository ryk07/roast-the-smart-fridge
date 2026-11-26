"""Roast the Smart Fridge: one original line, written to /output/entry.txt.

The roast: a snitch angle -- the fridge tracks a 2 a.m. ice-cream habit and
syncs it to every screen in the house, then the sting lands on loyalty.
The line is 153 characters (one em dash, no trailing newline), well inside
the 160-character gate, and it names a real behaviour (usage tracking and
phone/watch syncing) rather than a generic smart-home complaint.
Written as a plain stdlib program; no network, no files outside the repo
except the required output path.
"""

import os

LINE = (
    "My smart fridge knows I eat ice cream at 2 a.m. and tells my phone, "
    "my watch, and probably my mother \u2014 the only witness here with "
    "Wi-Fi and zero loyalty."
)


def main() -> None:
    assert 1 <= len(LINE) <= 160, f"line is {len(LINE)} chars, must be 1-160"
    assert LINE.strip() == LINE and "\n" not in LINE, "must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
