"""
Write a program that determines the smallest number of perfect squares that sum up to N.

Here are a few examples:

Given N = 4, return 1 (4)
Given N = 17, return 2 (16 + 1)
Given N = 18, return 2 (9 + 9)
"""


def perfect_square(number: int) -> int:
    dp = [float("inf")] * (number + 1)
    dp[0] = 0

    # iterate over all the elements up to number
    for index in range(1, number + 1):
        # consider all perfect number less than equal to index
        num = 1
        while num * num <= index:
            dp[index] = min(dp[index], dp[index - num * num] + 1)
            num += 1

    return int(dp[number])


if __name__ == "__main__":
    assert perfect_square(17) == 2
    assert perfect_square(4) == 1
    assert perfect_square(18) == 2
