def annotate(garden: list[str]) -> list[str]:
    if not garden or not garden[0]:
        return garden

    if _is_valid(garden):
        return [
            "".join(
                _count_adjacent(x, y, garden) if cell != "*" else cell
                for x, cell in enumerate(row)
            )
            for y, row in enumerate(garden)
        ]
    else: raise ValueError("The board is invalid with current input.")

def _is_valid(garden: list[str]) -> bool:
    width = len(garden[0])
    return all(len(row) == width and all(c in " *" for c in row) for row in garden)


def _count_adjacent(x: int, y: int, garden: list[str]) -> str:
    count = sum(
        garden[y + dy][x + dx] == "*"
        for dy in (-1, 0, 1)
        for dx in (-1, 0, 1)
        if _is_inbound(y + dy, x + dx, garden) and _is_not_self(dy, dx)
    )
    return str(count) if count else " "

def _is_inbound(y, x, garden):
    return  0 <= y < len(garden) and 0 <= x < len(garden[0])

def _is_not_self(dy, dx):
    return dy or dx
