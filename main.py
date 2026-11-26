"""Entry for make.fun's "Rejected Olympic Sports" bounty.

Writes one funny single-line sport the Olympics rejected to
/output/entry.txt: a made-up event, real enough to sound like a
broadcast, absurd enough to be funny.
"""

import os

ENTRY = (
    "Competitive queueing: four athletes stand in line for a bus that "
    "never comes; gold goes to whoever sighs the quietest, silver to "
    "whoever checks the timetable twice."
)

assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert "\n" not in ENTRY, "entry must be a single line"
assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing space"
assert ENTRY.endswith("."), "entry must end with a full stop"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"Wrote {len(ENTRY)}-char entry to {path}")


if __name__ == "__main__":
    main()
