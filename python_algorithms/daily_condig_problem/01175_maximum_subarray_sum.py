"""
Given a circular array, compute its maximum subarray sum in O(n) time. 
A subarray can be empty, and in this case the sum is 0.

For example, given [8, -1, 3, 4], return 15 as we choose the numbers 
3, 4, and 8 where the 8 is obtained from wrapping around.

Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1.
"""


def max_sum_subarray(arr: list[int]) -> int:
    max_subarray = arr[0]
    min_subarray = arr[0]
    curr_max_subarray = arr[0]
    curr_min_subarray = arr[0]

    for number in arr[1:]:
        curr_max_subarray = number + max(curr_max_subarray, 0)
        curr_min_subarray = number + min(curr_min_subarray, 0)
        max_subarray = max(max_subarray, curr_max_subarray)
        min_subarray = min(min_subarray, curr_min_subarray)

    return (
        max_subarray
        if max_subarray <= 0
        else max(max_subarray, sum(arr) - min_subarray)
    )


if __name__ == "__main__":
    assert max_sum_subarray([8, -1, 3, 4]) == 15
    assert max_sum_subarray([-4, 5, 1, 0]) == 6
