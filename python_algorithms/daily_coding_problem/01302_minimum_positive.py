"""
Given an array of integers, find the first missing positive integer in linear time and constant space.
In other words, find the lowest positive integer that does not exist in the array. The array can contain
duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""


def first_missing_positive(arr: list[int]) -> int:
    length = len(arr)
    for index_i in range(length):
        while (
            1 <= arr[index_i] <= length
            and arr[index_i] != index_i + 1
            and arr[index_i] != arr[arr[index_i] - 1]
        ):
            index_j = arr[index_i] - 1
            arr[index_i], arr[index_j] = arr[index_j], arr[index_i]

    for index in range(length):
        if arr[index] != index + 1:
            return index + 1

    return length + 1


print(first_missing_positive([3, 4, -1, 1]))
print(first_missing_positive([1, 2, 0]))
