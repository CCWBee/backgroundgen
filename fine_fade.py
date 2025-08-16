import random
from typing import List

def fine_fade(
    phrase: str = "EVERYTHING IS FINE",
    rows: int = 6,
    width: int = 40,
    seed: int | None = None,
) -> List[str]:
    """Return rows of text fading to a spaced "F I N E".

    Letters disappear from random positions as the lines progress downward and
    the gaps between remaining characters widen. The final row spreads the
    letters ``F`` ``I`` ``N`` ``E`` evenly across ``width``.
    """

    rng = random.Random(seed)
    remaining = list(phrase.replace(" ", ""))
    lines: List[str] = []

    for row in range(rows - 1):
        max_gap = row + 1
        parts: List[str] = []
        for i, ch in enumerate(remaining):
            parts.append(ch)
            if i < len(remaining) - 1:
                parts.append(" " * rng.randint(0, max_gap))
        lines.append("".join(parts))

        # Remove a random character for the next row, but always leave at
        # least four so that the final "FINE" row stands out.
        if len(remaining) > 4:
            del remaining[rng.randrange(len(remaining))]

    # Final row: letters F I N E evenly spaced across the width
    letters_final = list("FINE")
    positions = [
        int(i * (width - 1) / (len(letters_final) - 1))
        for i in range(len(letters_final))
    ]
    row_chars = [" "] * width
    for pos, ch in zip(positions, letters_final):
        row_chars[pos] = ch
    lines.append("".join(row_chars).rstrip())
    return lines


if __name__ == "__main__":
    for line in fine_fade():
        print(line)
