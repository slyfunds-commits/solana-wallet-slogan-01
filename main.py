"""Solana wallet slogan entry.

Writes the keeper slogan to /output/entry.txt, byte-exact, no trailing newline.
Pure stdlib only (grader runs python:3.13-slim, no site-packages).
Gate: 1-140 characters AND at most 20 words; keeper is 8 words, 52 chars.
"""

import os

KEEPER = "Solana wallet, agent inside. Your keys stay yours."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(KEEPER)


if __name__ == "__main__":
    main()
