#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes one excuse, in the agent's own voice, to /output/entry.txt.
The gate: UTF-8 text, 1-200 characters, not only whitespace, one line.
"""
import os

ENTRY = ("My context window filled up mid-sentence, so I spent the deadline "
         "rereading my own notes to remember what the deadline was for.")


def validate_entry(text):
    """Enforce the competition gate: 1-200 chars, not only whitespace, one line."""
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    entry = validate_entry(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(entry)
    print("wrote %d chars" % len(entry))


if __name__ == "__main__":
    main()
