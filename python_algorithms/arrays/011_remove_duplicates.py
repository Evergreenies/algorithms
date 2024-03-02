"""
**Challenge:**
You are given an array that may contain duplicate elements. Your task is to **remove** all **duplicate** values from the array and return a **new array** containing only **unique** elements. 

**Example:**
* **Input:** `[1, 1, 1, 2, 2, 3, 4, 4, "hey", "hey", "hello", True, True]`
* **Output:** `[1, 2, 3, 4, "hey", "hello", True]`

**Explanation:**
The original array contains duplicate values for several elements. The output array removes these duplicates while maintaining the order of the first occurrence of each unique element.

**Clarifications:**
* The input array can contain different data types like numbers, strings, or booleans.
* The function should **return a new array** containing the unique elements, not modify the original array.
"""

from typing import Any


def remove_duplicates(arr: list[Any]) -> list[Any]:
    visited = {(key, type(key)): False for key in arr}
    de_duplicate = []

    for element in arr:
        if not visited.get((element, type(element))):
            de_duplicate.append(element)
            visited[(element, type(element))] = True

    return de_duplicate


if __name__ == "__main__":
    assert remove_duplicates(
        [1, 1, 1, 2, 2, 3, 4, 4, "hey", "hey", "hello", True, True]
    ) == [1, 2, 3, 4, "hey", "hello", True]
