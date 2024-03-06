"""
Suppose an array sorted in ascending order is rotated at some pivot unknown 
to you beforehand. Find the minimum element in O(log N) time. You may assume 
the array does not contain duplicates.

For example, given [5, 7, 10, 3, 4], return 3.
"""


def find_pivot(arr: list[int]) -> int:
    left, right = 0, len(arr) - 1
    while left < right:
        middle = (right + left) // 2
        if arr[middle] > arr[right]:
            left = middle + 1
        else:
            right = middle

    return arr[left]


if __name__ == "__main__":
    assert find_pivot([5, 7, 10, 3, 4]) == 3
