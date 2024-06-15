"""
Implement a data structure which carries out the following operations without resizing the underlying array:

add(value): Add a value to the set of values.
check(value): Check whether a value is in the set.
The check method may return occasional false positives (in other words, incorrectly identifying an element as part of the set), but should always correctly identify a true element.
"""

import hashlib


class BloomFilter:
    def __init__(self, size: int, hash_count: int) -> None:
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size

    def _hashed(self, value):
        hash_results = []
        for index in range(self.hash_count):
            hasher = hashlib.md5(value.encode() + str(index).encode())
            hash_results.append(int(hasher.hexdigest(), 16) % self.size)

        return hash_results

    def add(self, value):
        for position in self._hashed(value):
            self.bit_array[position] = 1

    def check(self, value):
        return all(self.bit_array[position] == 1 for position in self._hashed(value))


# Example usage
bloom = BloomFilter(size=100, hash_count=3)

# Adding values
bloom.add("apple")
bloom.add("banana")

# Checking values
print(bloom.check("apple"))  # Output: True
print(bloom.check("banana"))  # Output: True
print(bloom.check("cherry"))  # Output: False (most likely)
