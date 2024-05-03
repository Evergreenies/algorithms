"""
Implement division of two positive integers without using the division, multiplication, or
modulus operators. Return the quotient as an integer, ignoring the remainder.
"""


def divide(dividend: int, divisor: int) -> int:
    if divisor == 0:
        raise ZeroDivisionError("Divide by zero.")

    if (dividend <= 0) or (divisor < 0):
        return 0

    # need a sign in case of negative values
    # sign = -1 if (dividend < 0) != (divisor < 0) else 1

    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = 0
    while dividend >= divisor:
        dividend -= divisor
        quotient += 1

    # return sign * quotient  # works in case of negative sign
    return quotient


if __name__ == "__main__":
    assert divide(10, 3) == 3
    assert divide(17, 5) == 3
    assert divide(15, 5) == 3
    assert divide(5, 5) == 1
    assert divide(4, 5) == 0
