"""
Given an array and a number k that's smaller than the length of the array,
rotate the array to the right k elements in-place.
"""


def rotate_right_in_place(arr: list[int], k: int) -> list:
    length, k = len(arr), k % len(arr)

    # reverse entire array
    reverse(arr, 0, length - 1)

    # reverse the first k elements
    reverse(arr, 0, k - 1)

    # reverse the remaining elements
    reverse(arr, k, length - 1)

    return arr


def reverse(arr: list[int], start: int, end: int) -> None:
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


print(rotate_right_in_place([1, 2, 3, 4, 5, 6, 7], 3))
