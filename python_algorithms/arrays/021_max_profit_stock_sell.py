"""
You are given an array prices where prices[i] is the price of a given stock on the i^th day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a
different day in future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any
profit return 0.
"""


def max_profit(prices: list[int]) -> int:
    if not prices:
        return 0

    buy, profit = prices[0], 0
    for index in range(len(prices)):
        if prices[index] < buy:
            buy = prices[index]

        profit = max(profit, prices[index] - buy)

    return profit


assert max_profit([7, 1, 5, 3, 6, 4]) == 5
