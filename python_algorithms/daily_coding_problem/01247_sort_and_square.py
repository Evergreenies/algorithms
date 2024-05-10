"""
Given a sorted list of integers, square the elements and give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
"""


def square_with_bubble_sort(arr: list[int]) -> list[int]:
    if not arr:
        return []

    arr = [x**2 for x in arr]
    swapped = True
    while swapped:
        swapped = False
        for index in range(len(arr) - 1):
            if arr[index] > arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
                swapped = True

    return arr


def square_with_bubble_sort1(arr: list[int]) -> list[int]:
    if not arr:
        return []

    if len(arr) == 1:
        return [x**2 for x in arr]

    arr = [x**2 for x in arr]
    for index_i in range(len(arr) - 1):
        swapped = True
        for index_j in range(len(arr) - index_i - 1):
            if arr[index_j] > arr[index_j + 1]:
                arr[index_j], arr[index_j + 1] = arr[index_j + 1], arr[index_j]
                swapped = True

        if not swapped:
            break

    return arr


if __name__ == "__main__":
    assert square_with_bubble_sort([-9, -2, 0, 2, 3]) == [0, 4, 4, 9, 81]
    assert square_with_bubble_sort1([-9, -2, 0, 2, 3]) == [0, 4, 4, 9, 81]
