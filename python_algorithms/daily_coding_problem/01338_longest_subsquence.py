"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4].
Return its length: 4.

Your algorithm should run in O(n) complexity.
"""


def longest_subsequence(arr: list[int]) -> int:
    if len(arr) == 0:
        return 0

    unique = set(arr)
    max_length = 0
    for item in arr:
        if item - 1 not in unique:
            current_num = item
            current_length = 1

            while current_num + 1 in unique:
                current_num += 1
                current_length += 1

            max_length = max(current_length, max_length)

    return max_length


print(longest_subsequence([100, 1, 200, 3, 4, 2]))
