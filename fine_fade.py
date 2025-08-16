import random
from typing import List

def fine_fade(
    phrase: str = "EVERYTHING IS FINE",
    rows: int = 6,
    width: int = 40,
    seed: int | None = None,
) -> List[str]:
    """Return rows of text fading to a spaced "F I N E".

    Letters disappear from random positions as the lines progress downward.
    Each line shows the remaining characters separated by single spaces and
    removes an increasing number of letters so that text contracts rather than
    leaving growing gaps. The final row spreads the letters ``F`` ``I`` ``N``
    ``E`` evenly across ``width``.
    """

    rng = random.Random(seed)
    remaining = list(phrase.replace(" ", ""))
    lines: List[str] = []

    for row in range(rows - 1):
        lines.append(" ".join(remaining))

        # Remove more letters as we progress downwards, but ensure at least
        # four characters remain for the final "FINE" line.
        remove_count = min(row + 1, len(remaining) - 4)
        for _ in range(remove_count):
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
