"""
A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing
cost while ensuring that no two neighboring houses are of the same color.

Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color,
return the minimum cost which achieves this goal.
"""


def min_cost_paint_house(costs: list[list]) -> int:
    if not costs:
        return 0

    n, k = len(costs), len(costs[0])  # houses and colors respectivelly
    dp = costs[0][:]
    for idx_i in range(1, n):
        new_dp = [0] * k
        for idx_j in range(k):
            new_dp[idx_j] = costs[idx_i][idx_j] + min(
                dp[c] for c in range(k) if c != idx_j
            )

        dp = new_dp

    return min(dp)


costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
assert min_cost_paint_house(costs) == 10
