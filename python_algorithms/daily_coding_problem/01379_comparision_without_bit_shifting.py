"""
Find the maximum of two numbers without using any if-else statements, branching, or direct comparisons.
"""


def comparisons(a: int, b: int) -> int:
    # find the difference, if +ve then a is greater than b else b is greater
    diff = a - b

    # find the sign of the diff by bit shifting, 1 if -ve else 0 on +ve
    # used 31 bit shift by considering 32bit integer
    sign = (diff >> 31) & 1
    # right shift helps to determine MSB.
    # MSB 0 for non-negative numbers, 1 for positive numbers

    # return grater number, a if sign is 0 else b on 1 sign
    return a * (1 - sign) + b * sign


print(comparisons(10, 10))
print(comparisons(10, 100))
