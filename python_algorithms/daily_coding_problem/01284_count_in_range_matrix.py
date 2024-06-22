"""
Let A be an N by M matrix in which every row and every column is sorted.

Given i1, j1, i2, and j2, compute the number of elements of M smaller than M[i1, j1] and larger than M[i2, j2].

For example, given the following matrix:

[[1, 3, 7, 10, 15, 20],
 [2, 6, 9, 14, 22, 25],
 [3, 8, 10, 15, 25, 30],
 [10, 11, 12, 23, 30, 35],
 [20, 25, 30, 35, 40, 45]]
And i1 = 1, j1 = 1, i2 = 3, j2 = 3, return 15 as there are 15 numbers in the matrix smaller than 6 or greater than 23.
"""


def count_elements(matrix, i1, j1, i2, j2):
    rows, cols = len(matrix), len(matrix[0])
    count = 0

    for index_i in range(rows):
        for index_j in range(cols):
            if index_i < i1 or (index_i == i1 and index_j < j1):
                count += 1

    for index_i in range(rows):
        for index_j in range(cols):
            if index_i > i2 or (index_i == i1 and index_j > j2):
                count += 1

    count -= rows * cols

    return abs(count)


# Example usage
matrix = [
    [1, 3, 7, 10, 15, 20],
    [2, 6, 9, 14, 22, 25],
    [3, 8, 10, 15, 25, 30],
    [10, 11, 12, 23, 30, 35],
    [20, 25, 30, 35, 40, 45],
]
i1, j1 = 1, 1
i2, j2 = 3, 3

count = count_elements(matrix, i1, j1, i2, j2)
print(f"Number of elements: {count}")
