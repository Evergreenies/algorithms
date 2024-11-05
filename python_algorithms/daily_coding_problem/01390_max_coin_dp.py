"""
You are given a 2-d matrix where each cell represents number of coins in that cell.
Assuming we start at matrix[0][0], and can only move right or down, find the maximum
number of coins you can collect by the bottom right corner.

For example, in this matrix

0 3 1 1
2 0 0 4
1 5 3 1
The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.
"""


def max_coins(matrix: list[list]) -> int:
    if not matrix:
        return 0

    rows = len(matrix)
    if rows == 0:
        return 0

    cols = len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]
    dp[0][0] = matrix[0][0]

    for index_j in range(1, cols):
        dp[0][index_j] = dp[0][index_j - 1] + matrix[0][index_j]

    for index_i in range(1, rows):
        dp[index_i][0] = dp[index_i - 1][0] + matrix[index_i][0]

    for index_i in range(1, rows):
        for index_j in range(1, cols):
            dp[index_i][index_j] = (
                max(dp[index_i - 1][index_j], dp[index_i][index_j - 1])
                + matrix[index_i][index_j]
            )

    return dp[-1][-1]


matrix = [[0, 3, 1, 1], [2, 0, 0, 4], [1, 5, 3, 1]]

print(max_coins(matrix))
