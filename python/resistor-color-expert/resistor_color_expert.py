RESISTORS: dict[str, dict[str, int | str]] = {
    "black": {"resistance": 0},
    "brown": {"resistance": 1, "tolerance": "±1%"},
    "red": {"resistance": 2, "tolerance": "±2%"},
    "orange": {"resistance": 3},
    "yellow": {"resistance": 4},
    "green": {"resistance": 5, "tolerance": "±0.5%"},
    "blue": {"resistance": 6, "tolerance": "±0.25%"},
    "violet": {"resistance": 7, "tolerance": "±0.1%"},
    "grey": {"resistance": 8, "tolerance": "±0.05%"},
    "white": {"resistance": 9},
    "gold": {"tolerance": "±5%"},
    "silver": {"tolerance": "±10%"},
}


RESISTOR_RESISTANCE: dict[str, int] = {
    color: int(data["resistance"])
    for color, data in RESISTORS.items()
    if "resistance" in data
}

RESISTOR_TOLERANCE: dict[str, str] = {
    color: str(data["tolerance"])
    for color, data in RESISTORS.items()
    if "tolerance" in data
}

UNITS: dict[int, str] = {
    1_000_000_000: "gigaohms",
    1_000_000: "megaohms",
    1000: "kiloohms",
    1: "ohms",
}


def _validate_color_bands(colors: list[str]) -> None:

    if not colors:
        raise ValueError("Colors list cannot be empty")

    if len(colors) == 1:
        if colors[0] != "black":
            raise ValueError(f"Invalid digit color: {colors[0]}")
    else:
        for color in colors[:-1]:
            if color not in RESISTOR_RESISTANCE:
                raise ValueError(f"Invalid digit color: {color}")

        tolerance_color: str = colors[-1]
        if tolerance_color not in RESISTOR_TOLERANCE:
            raise ValueError(f"Invalid tolerance color: {tolerance_color}")


def resistor_label(colors: list[str]) -> str:

    _validate_color_bands(colors)

    if len(colors) == 1:
        return f"0 {UNITS[1]}".strip()

    digits: list[int] = [RESISTOR_RESISTANCE[color] for color in colors[:-2]]
    multiplier: int = 10 ** RESISTOR_RESISTANCE[colors[-2]]
    tolerance: str = RESISTOR_TOLERANCE.get(colors[-1], "")

    value: int = int("".join(map(str, digits))) * multiplier if digits else 0

    if value == 0:
        return f"0 {UNITS[1]} {tolerance}".strip()

    for divisor in UNITS.keys():
        if value >= divisor:
            result: str = f"{value / divisor:g} {UNITS[divisor]}"
            return f"{result} {tolerance}".strip()

    # Fallback (should never reach here given UNITS contains 1)
    return f"{value} {UNITS[1]} {tolerance}".strip()
