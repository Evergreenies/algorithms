"""
Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.

For example, for the input [1, 2, 3, 10], you should return 7.

Do this in O(N) time.
"""


def first_missing_positive(arr: list[int]) -> int:
    smallest_missing_sum = 1
    for num in arr:
        if num > smallest_missing_sum:
            break

        smallest_missing_sum += num

    return smallest_missing_sum


assert first_missing_positive([1, 2, 3, 10]) == 7
