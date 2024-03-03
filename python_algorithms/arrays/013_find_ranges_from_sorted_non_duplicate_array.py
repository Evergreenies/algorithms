"""
**Challenge:**
You are given a sorted array of **unique integers**. Your task is to **summarize 
the ranges** of consecutive numbers within the array. This summary should be 
represented as a list of **tuples**, where each tuple represents the **starting 
and ending values** of a specific range.

**Example:**
* **Input:** `[0, 1, 2, 4, 5, 7]` (sorted and without duplicates)
* **Output:** `[(0, 2), (4, 5), (7, 7)]`

**Explanation:**
The output list contains three tuples:
* `(0, 2)`: Represents the range from 0 (inclusive) to 2 (inclusive) as these three 
numbers appear consecutively in the input array.
* `(4, 5)`: Represents the range from 4 (inclusive) to 5 (inclusive) as they also 
appear consecutively.
* `(7, 7)`: Represents the single element 7 (appearing only once) as a separate range.

**Clarifications:**
* The input array is sorted and contains **unique** integer values.
* The output list should be a list of tuples, where each tuple contains two integers 
representing the starting and ending positions of a consecutive range.
"""


def find_array_of_ranges(arr: list[int]) -> list[tuple[int, int]] | list:
    if not arr:
        return []
    ranges = []
    start = arr[0]

    for index in range(1, len(arr)):
        if arr[index] != arr[index - 1] + 1:
            ranges.append((start, arr[index - 1]))
            start = arr[index]

    ranges.append((start, arr[-1]))
    return ranges


if __name__ == "__main__":
    assert find_array_of_ranges([0, 1, 2, 4, 5, 7]) == [(0, 2), (4, 5), (7, 7)]
    assert find_array_of_ranges([-5, -4, -3, 1, 2, 4, 5, 6]) == [
        (-5, -3),
        (1, 2),
        (4, 6),
    ]
    assert find_array_of_ranges([-2, -1, 0, 1, 2]) == [(-2, 2)]
