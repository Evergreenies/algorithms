"""
The ancient Egyptians used to express fractions as a sum of several terms where each numerator is one.
For example, 4 / 13 can be represented as 1 / 4 + 1 / 18 + 1 / 468.

Create an algorithm to turn an ordinary fraction a / b, where a < b, into an Egyptian fraction.
"""

import math


def egyptiam_fraction(numerator: int, denominator: int) -> list[int]:
    if numerator >= denominator:
        raise ValueError(f"{numerator=} must be less than {denominator=}")

    fractions = []
    while numerator != 0:
        fraction = math.ceil(denominator / numerator)
        fractions.append(f"1/{fraction}")
        numerator, denominator = (
            numerator * fraction - denominator,
            denominator * fraction,
        )

    return fractions


print(egyptiam_fraction(4, 13))
