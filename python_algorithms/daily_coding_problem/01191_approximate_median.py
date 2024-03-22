"""
Create an algorithm to efficiently compute the approximate median of a 
list of numbers.

More precisely, given an unordered list of N numbers, find an element 
whose rank is between N / 4 and 3 * N / 4, with a high level of certainty, 
in less than O(N) time.
"""

import random


def approximate_median(arr: list[int]) -> int:
    resevoir_size = int(2.5 * len(arr))
    resevoir = arr[:resevoir_size]

    for number in arr[resevoir_size:]:
        replace_index = random.randrange(resevoir_size)
        if replace_index != resevoir_size - 1:
            resevoir[replace_index] = number

    return random.choice(resevoir)


if __name__ == "__main__":
    print(approximate_median([10, 2, 8, 15, 4, 1, 20]))
