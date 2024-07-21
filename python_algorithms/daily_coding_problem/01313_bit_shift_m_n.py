"""
Write a function that returns the bitwise AND of all integers between M and N, inclusive.
"""


def range_bitwise_and(m: int, n: int) -> int:
    shift = 0

    while m < n:
        m >>= 1
        n >>= 1
        shift += 1

    return m << shift


print(range_bitwise_and(5, 7))
print(range_bitwise_and(0, 1))
print(range_bitwise_and(10, 15))
