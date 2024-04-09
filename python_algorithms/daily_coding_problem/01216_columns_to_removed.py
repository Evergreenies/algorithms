"""
You are given an N by M 2D matrix of lowercase letters. Determine the minimum number of columns that can 
be removed to ensure that each row is ordered from top to bottom lexicographically. That is, the letter 
at each column is lexicographically later as you go down each row. It does not matter whether each row 
itself is ordered lexicographically.

For example, given the following table:

cba
daf
ghi
This is not ordered because of the a in the center. We can remove the second column to make it ordered:

ca
df
gi
So your function should return 1, since we only needed to remove 1 column.

As another example, given the following table:

abcdef
Your function should return 0, since the rows are already ordered (there's only one row).

As another example, given the following table:

zyx
wvu
tsr
Your function should return 3, since we would need to remove all the columns to order it.
"""


from typing import Any


def min_columns(matrix: list[Any]) -> int:
    if not matrix:
        return 0

    if len(matrix) == 1:
        return 0

    n_rows, n_cols = len(matrix), len(matrix[0])
    keep_cols = set(range(n_cols))

    for col in range(n_cols):
        for row in range(n_rows - 1):
            if matrix[row][col] > matrix[row + 1][col]:
                keep_cols.discard(col)
                break

    return n_cols - len(keep_cols)


if __name__ == "__main__":
    assert min_columns([["c", "b", "a"], ["d", "a", "f"], ["g", "h", "i"]]) == 1
    assert min_columns([["a", "b", "c", "d", "e", "f"]]) == 0
    assert min_columns([["z", "y", "x"], ["w", "v", "u"], ["t", "s", "r"]]) == 3
