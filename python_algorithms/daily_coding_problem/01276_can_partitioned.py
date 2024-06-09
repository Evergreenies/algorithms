"""
Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can
split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets
that add up to the same sum.
"""


def can_partitioned(arr: list[int]) -> bool:
    total_sum = sum(arr)
    if total_sum % 2 != 0:
        return False

    targeted_sum = total_sum // 2
    dp = [[False for _ in range(total_sum + 1)] for _ in range(len(arr) + 1)]

    for index in range(len(dp)):
        dp[index][0] = True

    for index_i in range(1, len(arr) + 1):
        for index_j in range(1, targeted_sum + 1):
            if arr[index_i - 1] <= index_j:
                dp[index_i][index_j] = (
                    dp[index_i - 1][index_j]
                    or dp[index_i - 1][index_j - arr[index_i - 1]]
                )
            else:
                dp[index_i][index_j] = dp[index_i - 1][index_j]

    return dp[len(arr)][targeted_sum]


if __name__ == "__main__":
    assert can_partitioned([15, 5, 20, 10, 35, 15, 10]) is True
    assert can_partitioned([15, 5, 20, 10, 35]) is False
