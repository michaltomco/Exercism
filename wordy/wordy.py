from typing import Final


OPERATORS: Final[dict[str, str]] = {
    "plus": "+",
    "minus": "-",
    "multiplied": "*",
    "divided": "/",
}
SYNTAX_ERROR_MSG: Final[str] = "syntax error"
UNKNOWN_OPERATION_ERROR_MSG: Final[str] = "unknown operation"


def _is_number(token: str) -> bool:
    return token.count("-") <= 1 and token.lstrip("-").isnumeric()


def answer(question: str) -> int:
    expected_operator: bool = False
    expected_number: bool = True
    equation: str = str()
    question = question[:-1]

    for word in question.split():
        if word in OPERATORS and expected_number:
            raise ValueError(SYNTAX_ERROR_MSG)
        elif expected_number & _is_number(woexercism rd):
            equation = "".join([equation, word])
            expected_number = False
            expected_operator = True
        elif word in OPERATORS and expected_operator:
            equation = "".join([equation, OPERATORS[word]])
            expected_number = True
            expected_operator = False
        elif expected_operator:
            if word.lstrip('-').isnumeric():
                raise ValueError(SYNTAX_ERROR_MSG)
            raise ValueError(UNKNOWN_OPERATION_ERROR_MSG)
    try:
        return int(eval(equation))
    except Exception:
        raise ValueError(SYNTAX_ERROR_MSG)
