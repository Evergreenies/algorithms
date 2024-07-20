"""
Using a function rand5() that returns an integer from 1 to 5 (inclusive) with uniform probability,
implement a function rand7() that returns an integer from 1 to 7 (inclusive).
"""

import random


def rand5():
    return random.randint(1, 5)


def rand7():
    while True:
        num = (rand5() - 1) * 5 + rand5()

        if num <= 21:
            return (num - 1) % 7 + 1


print([rand7() for _ in range(1000)])
