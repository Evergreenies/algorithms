"""
Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that
all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'],
it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""


def segeregate_colors(arr: list[str]) -> list[str]:
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == "R":
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == "B":
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
        else:
            mid += 1

    return arr


if __name__ == "__main__":
    assert segeregate_colors(["G", "B", "R", "R", "B", "R", "G"]) == [
        "R",
        "R",
        "R",
        "G",
        "G",
        "B",
        "B",
    ]
