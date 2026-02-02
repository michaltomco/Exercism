from typing import Final

OPENING_BRACKETS: Final[dict[str, str]] = {"[": "]", "(": ")", "{": "}"}
CLOSING_BRACKETS: Final[frozenset[str]] = frozenset(OPENING_BRACKETS.values())


def is_paired(input_string: str) -> bool:
    opened_bracket_stack: list[str] = []

    for char in input_string:
        if char in OPENING_BRACKETS:
            opened_bracket_stack.append(OPENING_BRACKETS[char])
        elif char in CLOSING_BRACKETS:
            if not opened_bracket_stack or opened_bracket_stack[-1] != char:
                return False
            opened_bracket_stack.pop()

    return not opened_bracket_stack
