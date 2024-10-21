"""
Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.
"""


def check_possibility(arr: list[int]) -> bool:
    count = 0
    for index in range(1, len(arr)):
        if arr[index] < arr[index - 1]:
            if count > 0:
                return False

            count += 1

            if index == 1 or arr[index] >= arr[index - 2]:
                arr[index - 1] = arr[index]
            else:
                arr[index] = arr[index - 1]

    return True


assert check_possibility([10, 5, 7]) is True
assert check_possibility([10, 5, 1]) is False
