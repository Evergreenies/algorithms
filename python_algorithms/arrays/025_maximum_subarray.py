"""
Given an integer array nums, find the contiguous subarray (containing at least one number which has the
largest sum and return its sum.

A subarray is a contiguous part of an array.
"""


def max_subarray(arr: list[int]) -> int:
    if not arr:
        return 0

    max_sum, current_sum = arr[0], 0
    for item in arr:
        if current_sum < 0:
            current_sum = 0

        current_sum += item
        max_sum = max(max_sum, current_sum)

    return max_sum


print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
