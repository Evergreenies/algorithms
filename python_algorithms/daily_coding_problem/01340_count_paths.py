"""
There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at
the top-left corner and getting to the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

Right, then down
Down, then right
Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
"""


def count_paths(rows: int, cols: int) -> int:
    dp = [[0] * cols for _ in range(rows)]
    dp[0][0] = 1

    for index in range(1, rows):
        dp[index][0] = dp[index - 1][0]

    for index in range(1, cols):
        dp[0][index] = dp[0][index - 1]

    for index_i in range(1, rows):
        for index_j in range(1, cols):
            dp[index_i][index_j] += dp[index_i - 1][index_j] + dp[index_i][index_j - 1]

    return dp[rows - 1][cols - 1]


assert count_paths(5, 5) == 70
