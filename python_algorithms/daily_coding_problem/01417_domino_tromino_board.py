"""
ou are given a 2 x N board, and instructed to completely cover the board with the following shapes:

Dominoes, or 2 x 1 rectangles.
Trominoes, or L-shapes.
For example, if N = 4, here is one possible configuration, where A is a domino, and B and C are trominoes.

A B B C
A B C C
Given an integer N, determine in how many ways this task is possible.
"""


def number_of_ways_to_cover_board(num: int) -> int:
    if num < 0:
        return 0

    if num in [1, 2, 0]:
        return num

    dp = [0] * (num + 1)
    dp[1] = 1
    dp[2] = 2

    for position in range(3, num + 1):
        dp[position] = dp[position - 1] + 2 * dp[position - 2]

    return dp[num]


# assert number_of_ways_to_cover_board(4) == 11
print(number_of_ways_to_cover_board(4))
