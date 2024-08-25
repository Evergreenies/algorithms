"""
Find first missing element from given array
"""


def find_first_missing(arr: list[int]) -> None:
    if not arr:
        return

    # sort array to ease the search
    arr.sort()
    low, high, length = arr[0], arr[-1], len(arr)
    diff = low
    for index in range(length):
        if arr[index] - index != diff:
            print(f"first missing element: {index + diff}")
            break


def find_all_missing_elements(arr: list[int]) -> None:
    if not arr: return

    arr.sort()
    low, high, length = arr[0], arr[-1], len(arr)
    diff = low
    for index in range(length):
        if arr[index] - index != diff:
            while diff < arr[index] - index:
                print(f"missing element: {index + diff}")
                diff += 1


def max_min(arr: list[int]) -> tuple[int, int]:
    _max, _min = float("-inf"), float("inf")
    for item in arr:
        if item < _min:
            _min = item
        if item > _max:
            _max = item

    return _min, _max


def find_missing_optimized(arr: list[int]) -> None:
    if not arr:
        return

    _min, _max = max_min(arr)
    _map = dict()
    for item in arr:
        _map[item] = _map.get(item, 0) + 1

    for item in range(_min, _max):
        if _map.get(item) is None:
            print(f"missing element: {item}")


find_first_missing([6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 29])
find_all_missing_elements([6, 7, 8, 9, 11, 12, 15, 16, 17, 18, 19])
find_missing_optimized([6, 7, 8, 9, 11, 12, 15, 16, 17, 18, 19])
