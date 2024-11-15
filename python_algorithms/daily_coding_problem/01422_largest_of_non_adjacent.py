"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should
return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""


def largest_non_adjacent_sum(arr: list) -> int:
    if not arr:
        return 0
    elif len(arr) == 1:
        return max(0, arr[0])

    include = max(0, arr[0])
    exclude = 0

    for num in arr[1:]:
        new_exclude = max(include, exclude)
        include = exclude + num
        exclude = new_exclude

    return max(include, exclude)


print(largest_non_adjacent_sum([2, 4, 6, 2, 5]))  # Output: 13
print(largest_non_adjacent_sum([5, 1, 1, 5]))
