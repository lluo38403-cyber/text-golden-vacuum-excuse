"""The Robot Vacuum's Best Excuse — make.fun entry.

Writes one excuse to /output/entry.txt: a single line, at most 140
characters, the funniest excuse a robot vacuum could offer for missing
a spot. The vacuum does not admit failure — it reframes the missed spot
as a kindness, leaving the human something to feel needed for.
"""

import os

ENTRY = (
    "I didn't miss that spot — I left it there so you would still feel needed."
)

MAX_CHARS = 140


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
