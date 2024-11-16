"""
You are given an array of nonnegative integers. Let's say you start at the beginning of the
array and are trying to advance to the end. You can advance at most, the number of steps that
you're currently on. Determine whether you can get to the end of the array.

For example, given the array [1, 3, 1, 2, 0, 1], we can go from indices 0 -> 1 -> 3 -> 5,
so return true.

Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.
"""


def can_reach_end(arr: list[int]) -> bool:
    max_reach, target = 0, len(arr) - 1

    for index, steps in enumerate(arr):
        if index > max_reach:
            return False

        max_reach = max(max_reach, index + steps)
        if max_reach >= target:
            return True

    return False


print(can_reach_end([1, 3, 1, 2, 0, 1]))  # Output: True
print(can_reach_end([1, 2, 1, 0, 0]))
