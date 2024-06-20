"""
You have n fair coins and you flip them all at the same time. Any that come up tails you set aside.
The ones that come up heads you flip again. How many rounds do you expect to play before only one coin remains?

Write a function that, given n, returns the number of rounds you'd expect to play until one coin remains.
"""

import math


def expected_rounds(num: int) -> int:
    if num < 1:
        raise ValueError("num must be atleast 1")

    rounds = 0
    while num > 1:
        num = math.ceil(num // 2)
        rounds += 1

    return rounds


print(expected_rounds(10))
print(expected_rounds(1))
