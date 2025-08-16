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
    Instead of squeezing remaining letters together, characters are replaced
    with blanks so each line keeps the original layout. The number of removed
    characters increases on each row. The final row spreads the letters ``F``
    ``I`` ``N`` ``E`` evenly across ``width``.
    """

    rng = random.Random(seed)
    chars = list(phrase)
    lines: List[str] = []

    for row in range(rows - 1):
        lines.append("".join(chars))

        # Remove more letters as we progress downwards, but ensure at least
        # four characters remain for the final "FINE" line.
        remaining_indices = [i for i, ch in enumerate(chars) if ch != " "]
        remove_count = min(row + 1, max(0, len(remaining_indices) - 4))
        for idx in rng.sample(remaining_indices, remove_count):
            chars[idx] = " "

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
