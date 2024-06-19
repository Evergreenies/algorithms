"""
Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.

A solution will always exist. See Goldbach’s conjecture.

Example:

Input: 4
Output: 2 + 2 = 4
If there are more than one solution possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then

[a, b] < [c, d]
If a < c OR a==c AND b < d.
"""


def sieve_of_eratosthenes(limit: int) -> list[int]:
    is_prime = [True] * (limit + 1)
    index = 2

    while (index * index) <= limit:
        if is_prime[index]:
            for i in range(index * index, limit + 1, index):
                is_prime[i] = False

        index += 1

    primes = []
    for num in range(2, limit + 1):
        if is_prime[num]:
            primes.append(num)

    return primes


def find_goldbach_pair(number: int) -> tuple:
    primes = sieve_of_eratosthenes(number)
    primes_set = set(primes)

    for prime in primes:
        if (number - prime) in primes_set:
            return prime, number - prime

    return None, None


# Example usage
even_number = 4
prime1, prime2 = find_goldbach_pair(even_number)
print(f"{prime1} + {prime2} = {even_number}")

# Another example usage
even_number = 28
prime1, prime2 = find_goldbach_pair(even_number)
print(f"{prime1} + {prime2} = {even_number}")
