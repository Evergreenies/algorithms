"""
An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time.
If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.
"""


def search_rotated_array(arr: list[int], target: int) -> int | None:
    left, right = 0, len(arr) - 1

    while left <= right:
        # find middle index
        middle = (left + right) // 2

        # check if current element is target
        if target == arr[middle]:
            return middle

        # check the sorted array (left or right)
        if arr[left] <= arr[middle]:
            if arr[left] <= target < arr[middle]:
                right = middle - 1
            else:
                left = middle + 1
        else:
            if arr[middle] < target <= arr[middle]:
                left = middle + 1
            else:
                right = middle - 1

    return


if __name__ == "__main__":
    assert search_rotated_array([13, 18, 25, 2, 8, 10], 8) == 4
