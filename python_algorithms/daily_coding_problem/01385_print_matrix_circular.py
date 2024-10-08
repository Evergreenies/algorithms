"""
Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
 [6,  7,  8,  9,  10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]
You should print out the following:

1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12
"""


def sprial_order(matrix: list[list]) -> None:
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    result = []

    while top <= bottom and left <= right:
        # traverse from left to right
        for col in range(left, right + 1):
            result.append(matrix[top][col])

        # increate top just in order to manager visited rows
        top += 1

        # taverse from top to bottom
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])

        # decrease the columns count from right as reset the boundry
        right -= 1

        if top <= bottom:
            # traveser last row from right to the left
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])

            bottom -= 1  # reset boundry

        if left <= right:
            # traverse first columns (boundry) from bottom to up
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])

            left += 1  # reset boundry

    for num in result:
        print(num)


matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
sprial_order(matrix)
