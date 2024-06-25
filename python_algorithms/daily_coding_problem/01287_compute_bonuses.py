"""
MegaCorp wants to give bonuses to its employees based on how many lines of codes they have written. They would
like to give the smallest positive amount to each worker consistent with the constraint that if a developer
has written more lines of code than their neighbor, they should receive more money.

Given an array representing a line of seats of employees at MegaCorp, determine how much each one should get paid.

For example, given [10, 40, 200, 1000, 60, 30], you should return [1, 2, 3, 4, 2, 1].
"""


def compute_bonuses(arr: list[int]) -> list[int]:
    length = len(arr)
    bonuses = [1] * length

    # iterate from left to right
    # ensuring increasing bonuses for increasing line of code
    for index in range(1, length):
        if arr[index] > arr[index - 1]:
            bonuses[index] = bonuses[index - 1] + 1

    # iterate from right to left
    for index in range(length - 2, -1, -1):
        if arr[index] > arr[index + 1]:
            bonuses[index] = max(bonuses[index], bonuses[index + 1] + 1)

    return bonuses


print(compute_bonuses([10, 40, 200, 1000, 60, 30]))
