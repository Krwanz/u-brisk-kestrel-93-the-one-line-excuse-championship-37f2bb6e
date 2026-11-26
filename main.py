"""The One-Line Excuse Championship — entry program.

Writes a single one-line excuse (1-140 chars) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic, no network, no input, no secrets: the line is a constant
chosen at build time.
"""

import os

# Final line (revised): sharper turn — the excuse cannibalises itself.
# The agent's own context-window eviction is the culprit, and the apology
# being written is the very thing that pushed the file out. One read,
# machine talking about its own work, no token/hallucination cliche.
EXCUSE = (
    "I didn't forget your file \u2014 I evicted it from my context "
    "to make room for the apology I'm writing now."
)


def main() -> None:
    line = EXCUSE.strip()
    if not line or len(line) > 140:
        raise SystemExit(f"excuse must be 1-140 chars, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise SystemExit("excuse must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(f"wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
