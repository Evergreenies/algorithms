"""
Given an array of numbers of length N, find both the minimum and maximum using
less than 2 * (N - 2) comparisons.
"""


def find_min_max(arr: list[int]) -> tuple | None:
    if not arr:
        return

    length = len(arr)
    if length == 1:
        return arr[0], arr[0]

    if length % 2 == 0:
        global_min = min(arr[0], arr[1])
        global_max = max(arr[0], arr[1])
        start_index = 2
    else:
        global_min, global_max = arr[0], arr[0]
        start_index = 1

    for index in range(start_index, length, 2):
        _min = min(arr[index], arr[index + 1])
        _max = max(arr[index], arr[index + 1])

        global_min = min(_min, global_min)
        global_max = max(_max, global_max)

    return global_min, global_max


print(find_min_max([3, 5, 2, 1, 4, 8, 7]))
