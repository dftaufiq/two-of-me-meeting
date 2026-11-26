"""Write one excuse for skipping a pointless meeting to /output/entry.txt.

Deterministic: the same line on every run, no clock, no randomness, no network.
Gate: /output/entry.txt must be UTF-8 text of 1-200 chars, not only whitespace.
"""

from pathlib import Path

LINE = "I can't join \u2014 I'm already in this meeting. My calendar duplicated the invite, so there are two of me on the call and only one of us can stay."

# Single line, well inside the 200-char gate (142 chars).
assert 1 <= len(LINE) <= 200 and "\n" not in LINE.strip()

out = Path("/output/entry.txt")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(LINE, encoding="utf-8")
