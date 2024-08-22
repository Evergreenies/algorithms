"""
Given an array of integers out of order, determine the bounds of the smallest window that must be sorted
in order for the entire array to be sorted. For example, given [3, 7, 5, 6, 9], you should return (1, 3).
"""


def find_sorted_window(arr: list[int]) -> tuple:
    length = len(arr)
    start, end = 0, length - 1

    # find the first element out of order from left
    while start < end and arr[start] < arr[start + 1]:
        start += 1

    # return if array is already sorted
    if start == end:
        return 0, 0

    # find the first element out of order from right
    while end > 0 and arr[end] > arr[end - 1]:
        end -= 1

    # find min and max element of the subarray
    subarray_min = min(arr[start : end + 1])
    subarray_max = max(arr[start : end + 1])

    # extend the left half
    while start > 0 and arr[start - 1] > subarray_min:
        start -= 1

    # expand the right half
    while end < length - 1 and arr[end + 1] < subarray_max:
        end += 1

    return start, end


print(find_sorted_window([3, 7, 5, 6, 9]))
