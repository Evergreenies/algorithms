"""
Assume you have access to a function toss_biased() which returns 0 or 1 with a probability
that's not 50-50 (but also not 0-100 or 100-0). You do not know the bias of the coin.

Write a function to simulate an unbiased coin toss.
"""

import random


def toss_biased() -> int:
    return 1 if random.random() < 0.7 else 0


def toss_unbiased() -> int:
    while True:
        toss1 = toss_biased()
        toss2 = toss_biased()

        if toss1 != toss2:
            return toss1


def simulate_unbiased_tosses(iterations=100000) -> float:
    result = [toss_unbiased() for _ in range(iterations)]
    return sum(result) / len(result)


print(simulate_unbiased_tosses())
