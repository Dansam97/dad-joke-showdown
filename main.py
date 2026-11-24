"""Dad Joke Showdown — entry program.

Writes one dad joke to entry.txt in the output directory.
The joke: a fridge that beeps gets told to chill, and answers with
the cold shoulder — two linked puns, punchline in the last clause.
"""

import os

TEXT = (
    "The fridge kept beeping at me, so I told it to chill. "
    "It has been giving me the cold shoulder ever since."
)


def validated_text() -> str:
    """Return TEXT after checking it against the competition gate:
    UTF-8 encodable, 1-200 characters, not only whitespace, one line."""
    TEXT.encode("utf-8")
    if not 1 <= len(TEXT) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(TEXT)}")
    if not TEXT.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in TEXT or "\r" in TEXT:
        raise ValueError("entry must be a single line")
    return TEXT


def main() -> None:
    text = validated_text()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    payload = (text + "\n").encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(payload)
    with open(path, "rb") as fh:
        if fh.read() != payload:
            raise IOError("read-back mismatch: entry.txt differs from payload")


if __name__ == "__main__":
    main()
