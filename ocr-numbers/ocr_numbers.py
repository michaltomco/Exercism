from typing import Final

ROWS_PER_DIGIT: Final[int] = 4
COLS_PER_DIGIT: Final[int] = 3
VALID_CHARS: Final[set[str]] = {" ", "|", "_"}
OCR_DIGITS: Final[dict[tuple[str, str, str, str], str]] = {
    (" _ ", "| |", "|_|", "   "): "0",
    ("   ", "  |", "  |", "   "): "1",
    (" _ ", " _|", "|_ ", "   "): "2",
    (" _ ", " _|", " _|", "   "): "3",
    ("   ", "|_|", "  |", "   "): "4",
    (" _ ", "|_ ", " _|", "   "): "5",
    (" _ ", "|_ ", "|_|", "   "): "6",
    (" _ ", "  |", "  |", "   "): "7",
    (" _ ", "|_|", "|_|", "   "): "8",
    (" _ ", "|_|", " _|", "   "): "9",
}


def convert(input_grid: list[str]) -> str:
    _validate_input(input_grid)

    digit_rows: int = len(input_grid) // ROWS_PER_DIGIT
    digit_cols: int = len(input_grid[0]) // COLS_PER_DIGIT

    result_numbers: list[str] = []
    for digit_row in range(digit_rows):
        result_number: list[str] = []
        for digit_col in range(digit_cols):
            digit: list[str] = _get_digit(input_grid, digit_row * ROWS_PER_DIGIT, digit_col * COLS_PER_DIGIT)
            result_number.append(_parse_digit(digit))
        result_numbers.append("".join(result_number))

    return ",".join(result_numbers)

def _get_digit(input_grid: list[str], start_row: int, start_col: int) -> list[str]:
    return [
        input_grid[start_row + row_in_digit][start_col : start_col + COLS_PER_DIGIT]
        for row_in_digit in range(ROWS_PER_DIGIT)
    ]

def _parse_digit(digit_slice: list[str]) -> str:
    return OCR_DIGITS.get(tuple(digit_slice), "?")  # type: ignore

def _validate_input(input_grid: list[str]) -> None:
    row_count: int = len(input_grid)
    if row_count % ROWS_PER_DIGIT != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    column_count: int = len(input_grid[0])
    if column_count % COLS_PER_DIGIT != 0:
        raise ValueError("Number of input columns is not a multiple of three")

    for row in input_grid:
        if len(row) != column_count:
            raise ValueError("Number of input columns is not a multiple of three")
        if not all(char in VALID_CHARS for char in row):
            raise ValueError("Invalid input characters")
