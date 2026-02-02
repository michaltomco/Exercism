RESISTORS: dict[str, int] = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}

UNITS: list[tuple[int, str]] = [
    (10**0, "ohms"),
    (10**3, "kiloohms"),
    (10**6, "megaohms"),
    (10**9, "gigaohms"),
]


def label(colors: list[str]) -> str:
    """Calculate the resistance value and return it with appropriate unit."""
    first, second, third = (RESISTORS[color] for color in colors[:3])
    value: int = (first * 10 + second) * 10**third

    if value == 0:
        return "0 ohms"

    for divisor, unit in reversed(UNITS):
        if value % divisor == 0:
            return f"{value // divisor} {unit}"

    return f"{value} ohms"
