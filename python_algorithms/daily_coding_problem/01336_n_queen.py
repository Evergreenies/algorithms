"""
You have an N by N board. Write a function that, given N, returns the number of possible arrangements
of the board where N queens can be placed on the board without threatening each other, i.e. no two queens
share the same row, column, or diagonal.
"""


def backtrack(n: int, row: int, cols: set, left_dig: set, right_dig: set) -> int:
    if row == n:
        return 1

    solutions = 0
    for col in range(n):
        if col in cols or (row - col) in left_dig or (row + col) in right_dig:
            continue

        cols.add(col)
        left_dig.add(row - col)
        right_dig.add(row + col)

        solutions += backtrack(n, row + 1, cols, left_dig, right_dig)

        cols.remove(col)
        left_dig.remove(row - col)
        right_dig.remove(row + col)

    return solutions


def count_possibilities(n: int) -> int:
    return backtrack(n, 0, set(), set(), set())


print(count_possibilities(4))
