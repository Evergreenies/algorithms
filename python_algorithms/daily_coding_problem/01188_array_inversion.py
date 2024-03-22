"""
We can determine how "out of order" an array A is by counting the 
number of inversions it has. Two elements A[i] and A[j] form an 
inversion if A[i] > A[j] but i < j. That is, a smaller element 
appears after a larger element.

Given an array, count the number of inversions it has. Do this 
faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions. The array 
[2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). 
The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair 
forms an inversion.
"""


from typing import Tuple


def merge_array(
    arr: list[int], left: list[int], right: list[int]
) -> Tuple[list[int], int]:
    left_length = len(left)
    right_length = len(right)

    left_index, right_index = 0, 0
    current_index, merged_inversion = 0, 0

    while left_index < left_length and right_index < right_length:
        if left[left_index] <= right[right_index]:
            arr[current_index] = left[left_index]
            left_index += 1
        else:
            arr[current_index] = right[right_index]
            right_index += 1
            merged_inversion += left_length - left_index

        current_index += 1

    while left_index < left_length:
        arr[current_index] = left[left_index]
        left_index += 1
        current_index += 1

    while right_index < right_length:
        arr[current_index] = right[right_index]
        right_index += 1
        current_index += 1

    return arr, merged_inversion


def array_inversion(arr: list[int]) -> Tuple[list[int], int]:
    if len(arr) <= 1:
        return arr, 0

    middle = len(arr) // 2
    left, left_inversion = array_inversion(arr[:middle])
    right, right_inversion = array_inversion(arr[middle:])
    merged_arr, merged_inversion = merge_array(arr, left, right)

    return merged_arr, left_inversion + right_inversion + merged_inversion


if __name__ == "__main__":
    assert array_inversion([2, 4, 1, 3, 5]) == ([1, 2, 3, 4, 5], 3)
