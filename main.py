"""Absurd Clause Contest entry program.

Writes a single original English clause (at most 200 characters),
phrased as a term-of-service clause, to /output/entry.txt.

Deterministic and offline: standard library only, no randomness,
no network access, no timestamps, no paths in the output.
"""

import os

ENTRY = (
    # The joke lands on the last beat: the "third parties" a ToS would
    # normally leave vague turn out to be 12 raccoons, and they have
    # signed an NDA — the legal instrument itself is the punchline.
    "You consent to our sharing your data with third parties, defined here "
    "as the 12 raccoons who live in our server room and have signed an NDA."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    text = ENTRY
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
