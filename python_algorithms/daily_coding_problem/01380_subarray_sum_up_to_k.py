"""
Given a list of integers S and a target number k, write a function that returns a subset of S that
adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
"""


def subset_sum(subset: list, k: int) -> list | None:
    def backtrack(
        current_subset: list, start_index: int, current_sum: int
    ) -> list | None:
        if current_sum == k:
            return current_subset
        if current_sum > k or start_index == len(subset):
            return None

        result = backtrack(
            current_subset + [subset[start_index]],
            start_index + 1,
            current_sum + subset[start_index],
        )
        if result:
            return result

        return backtrack(current_subset, start_index + 1, current_sum)

    return backtrack([], 0, 0)


print(subset_sum([12, 1, 61, 5, 9, 2], 24))
