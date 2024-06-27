"""
Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.
"""


def power(x, y):
    if y == 0:
        return 1

    if y < 0:
        x = 1 / x
        y = -y

    result = 1
    while y > 0:
        if y % 2 == 1:
            result *= x

        x *= x
        y //= 2

    return result


assert power(2, 10) == 1024
assert power(3, 5) == 243
