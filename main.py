#!/usr/bin/env python3
"""One Emoji, One Dream Vacation — make.fun bounty entry.

Writes exactly one emoji to /output/entry.txt: the dream vacation
that most makes a stranger want to book the flight.

The program holds ten candidate emojis, scores each one against the
judge's published brief (in the brief's own order: plainly a dream
vacation; vivid like a postcard; personal and specific; a spark of
wit or surprise; instantly readable across cultures), and writes the
strongest one. Deterministic: fixed candidates, fixed scores.
"""

import os

# Ten candidate emojis. Scores are out of 5 per criterion, in the
# brief's own order:
#   1. plainly lands on a dream vacation
#   2. vivid at a glance, like a postcard
#   3. personal and specific, not generic
#   4. spark of wit or surprise, a fresh pick
#   5. instantly readable across cultures and screens
CANDIDATES = [
    # Mount Fuji: a mountain AND a faraway place, both named in the
    # brief. One iconic postcard, one specific dream (Japan), fresh
    # against a field full of beaches and planes, universally known,
    # a single code point that renders clearly at any size.
    ("🗻", [5, 5, 5, 4, 5]),
    # Desert island: the archetypal dream vacation, a perfect
    # postcard — but the most generic pick in the field, no surprise.
    ("🏝️", [5, 5, 3, 3, 5]),
    # Beach with umbrella: the classic holiday, instantly read —
    # and the most generic holiday of all.
    ("🏖️", [5, 4, 2, 2, 5]),
    # Sunrise over the sea: dreamy and vivid, but it could be any
    # morning anywhere, not one particular dream.
    ("🌅", [4, 5, 2, 3, 5]),
    # Snow-capped mountain: a real alpine dream, specific — but it
    # reads as climbing and effort more than as a vacation.
    ("🏔️", [5, 4, 4, 3, 5]),
    # Surfer: a specific surf-trip dream, fun and fresh — but an
    # activity, not a place, so it lands less plainly as a vacation.
    ("🏄", [4, 4, 4, 4, 5]),
    # Water wave: a holiday hint, vivid and clear — but a wave alone
    # is not a dream vacation.
    ("🌊", [3, 4, 2, 2, 5]),
    # Volcano: surprising and specific (a Hawaii dream), a fresh
    # pick — but it can read as danger, which costs it clarity.
    ("🌋", [4, 4, 4, 5, 4]),
    # Airplane: travel, no destination — the trip without the dream.
    ("✈️", [3, 3, 1, 1, 5]),
    # Spiral shell: personal, a souvenir of one beach — but a shell
    # is not a trip at a glance.
    ("🐚", [3, 3, 4, 4, 5]),
]


def pick():
    """Return the highest-scoring candidate; ties break to the first."""
    best_emoji, best_score = None, -1
    for emoji, scores in CANDIDATES:
        total = sum(scores)
        if total > best_score:
            best_emoji, best_score = emoji, total
    return best_emoji


def main():
    emoji = pick()
    # Self-check the gate before writing: exactly one emoji, well
    # inside the 1-8 character limit, never only whitespace.
    assert len(emoji) == 1 and not emoji.isspace(), "pick must be one emoji"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(emoji + "\n")
    print(f"wrote {emoji} (Mount Fuji) to /output/entry.txt")


if __name__ == "__main__":
    main()
