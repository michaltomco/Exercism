def square_root(number: int) -> int:
    if number == 0:
        return 0
    pivot: int = number
    while True:
        next_pivot = (pivot + number // pivot) // 2
        if next_pivot >= pivot:
            return pivot
        pivot = next_pivot