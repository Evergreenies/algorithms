"""
An imminent hurricane threatens the coastal town of Codeville. If at most two people can 
fit in a rescue boat, and the maximum weight limit for a given boat is k, determine how 
many boats will be needed to save everyone.

For example, given a population with weights [100, 200, 150, 80] and a boat limit of 200, 
the smallest number of boats required will be three.
"""


def bubble_sort(arr: list[int]) -> list[int]:
    swap = True
    while swap:
        swap = False
        for index in range(0, len(arr) - 1):
            if arr[index] < arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
                swap = True

    return arr


def num_of_boats_needed(weights: list[int], limit: int) -> int:
    boats, left, right = 0, 0, len(weights) - 1
    weights = bubble_sort(weights)

    while left < right:
        if (weights[left] + weights[right]) <= limit:
            left += 1

        boats += 1
        right -= 1

    return boats


if __name__ == "__main__":
    assert bubble_sort([5, 6, 3, 2, 7, 4, 0]) == [7, 6, 5, 4, 3, 2, 0]
    print(num_of_boats_needed([100, 200, 150, 80], 200))
    assert num_of_boats_needed([100, 200, 150, 80], 200) == 3
