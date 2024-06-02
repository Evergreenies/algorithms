"""
Given an N by N matrix, rotate it by 90 degrees clockwise.

For example, given the following matrix:

[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
you should return:

[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
Follow-up: What if you couldn't use any extra space?
"""


def rotate_matrix(matrix: list[list]) -> list[list]:
    length = len(matrix)
    rotated_matrix = [[0] * length for _ in range(length)]

    for i in range(length):
        for j in range(length):
            rotated_matrix[j][length - 1 - i] = matrix[i][j]

    return rotated_matrix


if __name__ == "__main__":
    assert rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]
