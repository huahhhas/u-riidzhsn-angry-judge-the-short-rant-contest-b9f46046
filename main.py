#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — writes one short funny rant to entry.txt."""
import os

RANT = (
    "My printer has one job, and it performs it only when nobody needs it. "
    "The moment I need a boarding pass, it develops a paper jam in a tray I have "
    "never opened, in a language I do not speak. I have apologised to this machine. "
    "I have begged this machine. It blinked at me like a bouncer, and I left "
    "with a screenshot and the quiet dignity of a man who lost an argument to office equipment."
)

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(RANT)

if __name__ == "__main__":
    main()
