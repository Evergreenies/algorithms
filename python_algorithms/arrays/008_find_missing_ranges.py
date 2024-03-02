"""
**Challenge:**
You are given a sorted array of **unique** integers, a **lower bound** (`low`), and an **upper bound** (`high`). 
Your task is to find all the **missing ranges** between `low` and `high` that are **not** present in the array.

**Missing Range:**
A missing range refers to a **consecutive sequence of integers** that is **not included** in the given array, 
but falls within the specified **inclusive** range of `low` and `high`.

**Example:**
* **Input:** Array = [3, 5, 7, 9, 11], `low` = 1, `high` = 10
* **Output:** [(1, 2), (4, 4), (6, 8), (10, 10)]

**Explanation:**
* The missing ranges are:
    * **(1, 2):** Numbers 1 and 2 are not present in the array, but they fall within the range (1, 10).
    * **(4, 4):** Number 4 is present only once in the array, but the range specifies it should appear consecutively.
    * **(6, 8):** Numbers 6, 7, and 8 are not present in the array.
    * **(10, 10):** Although 10 is present in the array, the range specifies it should appear once.
"""


def find_missing_ranges(arr: list[int], low: int, high: int) -> list[tuple[int, int]]:
    result = []
    start = low

    for element in arr:
        if element == start:
            start += 1
        elif element > start:
            result.append((start, element - 1))
            start = element + 1

    if start < high:
        result.append((start, high))

    return result


if __name__ == "__main__":
    assert find_missing_ranges([3, 5], 1, 10) == [(1, 2), (4, 4), (6, 10)]
