import re


def is_valid(isbn: str) -> bool:
    if "-" in isbn and not re.match(r"^\d-\d{3}-\d{5}-[\dX]$", isbn):
        return False

    isbn_clean: str = isbn.replace("-", "")

    if len(isbn_clean) != 10:
        return False

    digits: list[int] = []
    for i, char in enumerate(isbn_clean):
        if i < 9:
            if not char.isdigit():
                return False
            digits.append(int(char))
        else:
            if char == "X":
                digits.append(10)
            elif char.isdigit():
                digits.append(int(char))
            else:
                return False

    isbn_sum: int = sum(coef * digit for digit, coef in zip(digits, range(10, 0, -1)))

    return isbn_sum % 11 == 0
