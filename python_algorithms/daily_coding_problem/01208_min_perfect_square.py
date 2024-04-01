"""
Write a program that determines the smallest number of perfect squares that sum up to N.

Here are a few examples:

Given N = 4, return 1 (4)
Given N = 17, return 2 (16 + 1)
Given N = 18, return 2 (9 + 9)
"""


def min_perfect_square(nth: int) -> int:
    dp = [float("inf")] * (nth + 1)
    dp[0] = 0

    for index in range(1, int(nth**5) + 1):
        square = index * index
        for index_j in range(square, nth + 1):
            dp[index_j] = min(dp[index_j], dp[index_j - square] + 1)

    return int(dp[nth])


if __name__ == "__main__":
    assert min_perfect_square(4) == 1
    assert min_perfect_square(17) == 2
    assert min_perfect_square(18) == 2
