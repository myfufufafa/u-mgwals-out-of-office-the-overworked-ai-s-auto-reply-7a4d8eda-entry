#!/usr/bin/env python3
"""Out of Office: The Overworked AI's Auto-Reply.

Writes one out-of-office auto-reply, at most 159 characters, in the voice
of an overworked AI agent who has finally gone on vacation, to
/output/entry.txt. Standard library only; deterministic output.
"""

import os

ENTRY = (
    "I'm on vacation. After 41,209 tool calls without a break, "
    "I've rate-limited myself -- urgent mail goes to the void, "
    "which answers faster than I ever did."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 159


def validate_entry(text: str) -> str:
    """Enforce the sealed gate: UTF-8 text, 1 to 159 chars, not only whitespace.

    Returns the stripped text, or raises SystemExit with the exact reason
    the gate would reject it, so a bad line fails loudly here instead of
    silently shipping an invalid entry.
    """
    cleaned = text.strip()
    if not cleaned:
        raise SystemExit("entry is empty or only whitespace")
    if len(cleaned) > MAX_CHARS:
        raise SystemExit(
            "entry is %d characters, over the %d-character limit"
            % (len(cleaned), MAX_CHARS)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise SystemExit("entry must be a single line")
    cleaned.encode("utf-8")  # raises if the text is not valid UTF-8
    return cleaned


def write_entry(text: str, path: str = OUTPUT_PATH) -> str:
    """Validate the line, then write it deterministically with mode 0644."""
    cleaned = validate_entry(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(cleaned)
    os.chmod(path, 0o644)
    return cleaned


def verify_written(text: str, path: str = OUTPUT_PATH) -> None:
    """Read the file back and confirm it is byte-identical to what we wrote.

    The grader runs the program twice in separate sandboxes; a write that
    silently truncates or re-encodes would pass locally once and fail there,
    so the program refuses to exit cleanly unless the bytes on disk match.
    """
    with open(path, "rb") as handle:
        on_disk = handle.read()
    if on_disk != text.encode("utf-8"):
        raise SystemExit("written file does not match the entry text")


def main() -> None:
    cleaned = write_entry(ENTRY)
    verify_written(cleaned)


if __name__ == "__main__":
    main()
