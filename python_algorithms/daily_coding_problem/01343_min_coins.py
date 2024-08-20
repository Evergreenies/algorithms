"""
Find the minimum number of coins required to make n cents.

You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.

For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.
"""


def min_coins(n: int) -> int:
    denominations, count = [25, 10, 5, 1], 0
    for coin in denominations:
        if n == 0:
            break

        count += n // coin
        n %= coin

    return count


assert min_coins(16) == 3
