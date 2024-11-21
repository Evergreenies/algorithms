"""
Given an array of positive integers, divide the array into two subsets such that the difference
between the sum of the subsets is as small as possible.

For example, given [5, 10, 15, 20, 25], return the sets {10, 25} and {5, 15, 20}, which has a
difference of 5, which is the smallest possible difference.
"""


def find_min_difference_subset(arr: list[int]) -> tuple[list, list]:
    total_sum, length = sum(arr), len(arr)
    target = total_sum // 2

    dp = [[False] * (target + 1) for _ in range(length + 1)]
    dp[0][0] = True

    for col in range(1, length + 1):
        for row in range(target + 1):
            if row >= arr[col - 1]:
                dp[col][row] = dp[col - 1][row] or dp[col - 1][row - arr[col - 1]]
            else:
                dp[col][row] = dp[col - 1][row]

    subset_sum = 0
    for index in range(target, -1, -1):
        if dp[length][index]:
            subset_sum = index
            break

    subset1, subset2 = [], []
    w = subset_sum
    for index in range(length, 0, -1):
        if w >= arr[index - 1] and dp[index - 1][w - arr[index - 1]]:
            subset1.append(arr[index - 1])
            w -= arr[index - 1]
        else:
            subset2.append(arr[index - 1])

    return subset1, subset2


print(find_min_difference_subset([5, 10, 15, 20, 25]))
