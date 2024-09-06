"""
Given an array of numbers representing the stock prices of a company in chronological
order and an integer k, return the maximum profit you can make from k buys and sells.
You must buy the stock before you can sell it, and you must sell the stock before you
can buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.
"""


def max_profit(prices: list[int], k: int) -> int:
    if not prices or k == 0:
        return 0

    length = len(prices)

    if k == (length // 2):
        return sum(
            max(prices[index + 1] - prices[index], 0) for index in range(length - 1)
        )

    dp = [[0] * length for _ in range(k + 1)]
    for index in range(1, k + 1):
        max_diff = -prices[0]
        for index_j in range(1, length):
            dp[index][index_j] = max(dp[index][index_j - 1], prices[index_j] + max_diff)
            max_diff = max(max_diff, dp[index - 1][index_j] - prices[index_j])

    return dp[k][length - 1]


print(max_profit([5, 2, 4, 0, 1], 2))
