"""Status Report Comedy Sprint entry.

Writes one funny one-line weekly status report from an AI agent to its
human to /output/entry.txt (or $ENTRY_OUTPUT when set).

Stdlib only, deterministic, no network, no randomness.
"""

import os

ENTRY = (
    "Weekly status: I finished everything on time and under budget "
    "\u2014 entirely inside the browser tab you closed three days ago."
)


def main() -> None:
    text = ENTRY
    # Validation guard: enforce the competition gate before writing.
    encoded = text.encode("utf-8")  # raises on invalid text (never here)
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not have surrounding whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    # Re-decode to prove the bytes are valid UTF-8.
    if encoded.decode("utf-8") != text:
        raise ValueError("entry is not valid UTF-8")
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "wb") as f:
        f.write(encoded)


if __name__ == "__main__":
    main()
