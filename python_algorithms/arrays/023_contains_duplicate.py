"""
Given an array nums and an integer k, return true if there are two distinct indices i and j in the array
such that nums[i] == nums[j] and abs(i - j) <= k.
"""


def contains_duplication(arr: list[int], k: int) -> bool:
    visited = dict()
    for index in range(len(arr)):
        if visited.get(arr[index]) is not None:
            return True

        visited[arr[index]] = index
        if len(visited) > k:
            visited.pop(arr[index - k])

    return False


assert contains_duplication([1, 2, 3, 1], 3) is True
assert contains_duplication([1, 0, 1, 1], 1) is True
assert contains_duplication([1, 2, 3, 1, 2, 3], 2) is False
