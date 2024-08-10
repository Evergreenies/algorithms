"""
You are given an N by M matrix of 0s and 1s. Starting from the top left corner,
how many ways are there to reach the bottom right corner?

You can only move right and down. 0 represents an empty space while 1 represents
a wall you cannot walk through.

For example, given the following matrix:

[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]
Return two, as there are only two ways to get to the bottom right:

Right, down, down, right
Down, right, down, right
The top left corner and bottom right corner will always be 0.
"""


def traverse_matrix(matrix: list[list]) -> int:
    if len(matrix) == 0:
        return 0

    rows, columns = len(matrix), len(matrix[0])

    # edge case: if start or end is a wall, no paths are possible
    if matrix[0][0] == 1 or matrix[rows - 1][columns - 1] == 1:
        return 0

    # initialize dp tables
    dp = [[0] * columns for _ in range(rows)]

    # start point
    dp[0][0] = 1

    for row in range(rows):
        for column in range(columns):
            if matrix[row][column] == 1:
                dp[row][column] = 0
            else:
                if row > 0:
                    dp[row][column] += dp[row - 1][column]

                if column > 0:
                    dp[row][column] += dp[row][column - 1]

    return dp[rows - 1][columns - 1]


matrix = [[0, 0, 1], [0, 0, 1], [1, 0, 0]]
print(traverse_matrix(matrix))
