import random
from typing import List

def fine_fade(phrase: str = "EVERYTHING IS FINE", rows: int = 6, width: int = 40, seed: int | None = None) -> List[str]:
    """Return rows of text fading to a spaced "F I N E".

    Characters from the start of the phrase disappear row by row while the
    gaps between remaining characters become increasingly random. The final
    row spreads the letters ``F`` ``I`` ``N`` ``E`` evenly across ``width``.
    """
    rng = random.Random(seed)
    letters = list(phrase.replace(" ", ""))
    lines: List[str] = []

    for row in range(rows - 1):
        start = min(row, len(letters) - 4)
        remain = letters[start:]
        max_gap = row + 1
        parts = []
        for i, ch in enumerate(remain):
            parts.append(ch)
            if i < len(remain) - 1:
                parts.append(" " * rng.randint(0, max_gap))
        lines.append("".join(parts))

    # Final row: letters F I N E evenly spaced across the width
    letters_final = list("FINE")
    positions = [int(i * (width - 1) / (len(letters_final) - 1)) for i in range(len(letters_final))]
    row_chars = [" "] * width
    for pos, ch in zip(positions, letters_final):
        row_chars[pos] = ch
    lines.append("".join(row_chars).rstrip())
    return lines


if __name__ == "__main__":
    for line in fine_fade():
        print(line)
