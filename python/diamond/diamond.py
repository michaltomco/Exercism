from string import ascii_uppercase
from typing import Final


SPACE: Final[str] = " "

def rows(letter: str) -> list[str]:
    if letter == "A":
        return ["A"]
    
    result: list[str] = []

    n = ascii_uppercase.index(letter)
    result = []

    for i in range(-n, n + 1):
        letter_index = n - abs(i)
        current_letter = ascii_uppercase[letter_index]
        outer_spaces = abs(i)
        inner_spaces = letter_index * 2 - 1

        if letter_index == 0:
            result.append(f"{SPACE * outer_spaces}A{SPACE * outer_spaces}")
        else:
            result.append(
                f"{SPACE * outer_spaces}{current_letter}{SPACE * inner_spaces}{current_letter}{SPACE * outer_spaces}"
            )

    return result
