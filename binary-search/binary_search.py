def find(search_list: list[int], value: int) -> int:
    left, right = 0, len(search_list) - 1
    
    while left <= right:
        pivot = (left + right) // 2
        if search_list[pivot] == value:
            return pivot
        elif search_list[pivot] > value:
            right = pivot - 1
        elif search_list[pivot] < value:
            left = pivot + 1
    
    raise ValueError("value not in array")
