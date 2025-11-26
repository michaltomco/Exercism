def score(x: float, y: float) -> int:
    distance = (x**2 + y**2) ** 0.5
    match distance:
        case d if d <= 1:
            return 10
        case d if d <= 5:
            return 5
        case d if d <= 10:
            return 1
        case _:
            return 0
