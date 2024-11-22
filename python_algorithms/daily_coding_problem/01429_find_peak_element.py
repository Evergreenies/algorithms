"""
Given a array that's sorted but rotated at some unknown pivot, in which all elements are distinct,
find a "peak" element in O(log N) time.

An element is considered a peak if it is greater than both its left and right neighbors. It is
guaranteed that the first and last elements are lower than all others.
"""


def find_peak_element(arr: list[int]) -> int | None:
    length = len(arr)
    low, high = 0, length - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return arr[mid]

        if mid > 0 and arr[mid - 1] > arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return None


print(find_peak_element([15, 20, 25, 5, 10]))
