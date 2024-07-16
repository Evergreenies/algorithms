"""
Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).
"""

from random import randrange


def random_number_not_in_list(num, arr) -> None | int:
    excluded_count = len(arr)
    available_count = num - excluded_count

    while True:
        candidate = randrange(num)

        if candidate not in arr:
            return candidate

        excluded_count += 1
        available_count -= 1

        if available_count <= 0:
            return None


print(random_number_not_in_list(10, [2, 4, 6]))
