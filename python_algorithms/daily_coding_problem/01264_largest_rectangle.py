"""
Given an N by M matrix consisting only of 1's and 0's, find the largest rectangle containing 
only 1's and return its area.

For example, given the following matrix:

[[1, 0, 0, 0],
 [1, 0, 1, 1],
 [1, 0, 1, 1],
 [0, 1, 0, 0]]
Return 4.
"""


def largest_reactangle_area(matrix: list[list]) -> int:
    rows_length = len(matrix)
    cols_length = len(matrix[0])
    dp = [[0 for _ in range(cols_length)] for _ in range(rows_length)]

    for index_j in range(cols_length):
        dp[0][index_j] = matrix[0][index_j]

    max_area = 0
    for index_i in range(1, rows_length):
        for index_j in range(cols_length):
            if matrix[index_i][index_j] == 0:
                dp[index_i][index_j] = 0
            else:
                dp[index_i][index_j] = dp[index_i - 1][index_j] + 1

            width = min(dp[index_i][index_j], index_j + 1)
            area = width * dp[index_i][index_j]
            max_area = max(max_area, area)

    return max_area


if __name__ == "__main__":
    matrix = [[1, 0, 0, 0], [1, 0, 1, 1], [1, 0, 1, 1], [0, 1, 0, 0]]
    assert largest_reactangle_area(matrix) == 4
