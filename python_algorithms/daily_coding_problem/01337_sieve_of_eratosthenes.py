"""
The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N.
The method is to take increasingly larger prime numbers, and mark their multiples as composite.

For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two),
then [6, 9, 12, ...] (multiples of three), and so on. Once we have done this for all primes less than N,
the unmarked numbers that remain will be prime.

Implement this algorithm.

Bonus: Create a generator that produces primes indefinitely (that is, without taking N as an input).
"""

import math
from typing import Iterator


def n_primes(n: int) -> list[int]:
    dp = [True] * (n + 1)

    dp[0] = False
    dp[1] = False

    for index in range(2, int(math.sqrt(n)) + 1):
        if dp[index]:
            index_j = index * index

            while index_j <= n:
                dp[index_j] = False
                index_j += index

    return [index for index, num in enumerate(dp) if num]


def n_primes_generator() -> Iterator:
    num, primes = 2, dict()

    while True:
        if num not in primes:
            yield num
            primes[num * num] = [num]
        else:
            for p in primes[num]:
                primes.setdefault(p + num, []).append(p)

            del primes[num]

        num += 1


print(n_primes(20))
print(n_primes(100))

primes_gen = n_primes_generator()
for _ in range(20):
    print(next(primes_gen), end=", ")

print()
