"""
Given a list of elements, find the majority element, which appears more than half the time (> floor(len(lst) / 2.0)).

You can assume that such element exists.

For example, given [1, 2, 1, 1, 3, 4, 0], return 1.
"""


def count(arr: list[int], item: int) -> int:
    count = 0
    for num in arr:
        if item == num:
            count += 1

    return count


def boyer_moore_voting_algo(arr: list[int]) -> int | None:
    _count, candidate = 0, arr[0]
    for item in arr:
        if _count == 0:
            candidate = item

        _count += 1 if item == candidate else -1

    if count(arr, candidate) >= (len(arr) // 2):
        return candidate

    return None


print(boyer_moore_voting_algo([1, 2, 1, 1, 3, 4, 0]))
print(boyer_moore_voting_algo([1, 2, 1, 1, 3, 4, 1]))
