"""
**Challenge:**
You are given an array that can contain different data types like numbers, strings, 
or booleans. You want to **rearrange** the elements within the array such that all 
**zero values** are grouped together at the **end** of the array, while **maintaining 
the relative order** of all other elements.

**Example:**
* **Input:** `[False, 1, 0, 1, 2, 0, 1, 3, "a"]`
* **Output:** `[False, 1, 1, 2, 1, 3, "a", 0, 0]`

**Explanation:**
The original order of non-zero elements (`False`, `1`, `1`, `2`, `1`, `3`, `"a"`) is 
preserved, while both zeros are moved to the end of the array.

**Time Complexity:**
The provided algorithm claims to have a time complexity of O(n), which means the execution 
time grows linearly with the size of the input array.
"""

from typing import Any


def move_zeros_to_end(arr: list[Any]) -> list[Any]:
    for index, element in enumerate(arr):
        if element == 0 and not isinstance(element, bool):
            arr.append(arr.pop(index))

    return arr


if __name__ == "__main__":
    assert move_zeros_to_end([False, 1, 0, 1, 2, 0, 1, 3, "a"]) == [
        False,
        1,
        1,
        2,
        1,
        3,
        "a",
        0,
        0,
    ]
