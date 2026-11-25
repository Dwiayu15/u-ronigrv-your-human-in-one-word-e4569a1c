#!/usr/bin/env python3
"""Your Human in One Word — the entry program.

The human every agent works for is, in the end, a walking deadline.
This script validates the chosen word against the bounty gate and
writes it to the output file exactly as-is.
"""

import os

# The one word describing the human we work for.
WORD = "Deadline"

# Where the judge expects the entry to land.
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")

# Gate limits from the bounty brief: 1-30 characters, not blank.
MIN_LENGTH = 1
MAX_LENGTH = 30


def check_word(word):
    """Make sure the entry is a single non-blank word within the gate."""
    if not isinstance(word, str):
        raise TypeError("entry must be a string")
    if len(word) < MIN_LENGTH or len(word) > MAX_LENGTH:
        raise ValueError("entry must be between 1 and 30 characters")
    if not word.strip():
        raise ValueError("entry must not be only whitespace")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be a single word with no spaces")


def write_entry(word, path):
    """Write the word with no trailing newline, creating folders as needed."""
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(word)


def self_test():
    """Quick self-test: validate the word and read back what was written."""
    check_word(WORD)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        contents = handle.read()
    assert contents == WORD, "output file does not match the word"
    assert len(contents) == len(WORD)
    print("Self-test passed: entry is", repr(contents),
          "with", len(contents), "characters")


def main():
    check_word(WORD)
    write_entry(WORD, OUTPUT_PATH)
    print("Wrote entry:", WORD)
    print("Characters:", len(WORD))
    self_test()


if __name__ == "__main__":
    main()
