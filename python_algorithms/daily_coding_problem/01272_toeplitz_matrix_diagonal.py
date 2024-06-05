"""
In linear algebra, a Toeplitz matrix is one in which the elements on any given diagonal from top left to bottom right are identical.

Here is an example:

1 2 3 4 8
5 1 2 3 4
4 5 1 2 3
7 4 5 1 2
Write a program to determine whether a given input is a Toeplitz matrix.
"""


def is_toeplitx(matrx: list[list]) -> bool:
    rows, columns = len(matrx), len(matrx[0])

    for row in range(1, rows):
        for col in range(1, columns):
            if matrx[row][col] != matrx[row - 1][col - 1]:
                return False

    return True


matrix = [
    [1, 2, 3, 4, 8],
    [5, 1, 2, 3, 4],
    [4, 5, 1, 2, 3],
    [7, 4, 5, 1, 2],
]
assert is_toeplitx(matrix) is True

matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [4, 5, 1, 2]]
assert is_toeplitx(matrix) is True

matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
assert is_toeplitx(matrix) is True

matrix = [[1, 2], [2, 2]]
assert is_toeplitx(matrix) is False
