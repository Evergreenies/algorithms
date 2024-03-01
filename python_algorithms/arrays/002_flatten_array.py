"""
**Challenge:** You are given an array (`arr`) that may contain other arrays 
(nested arrays) of varying depths. Your task is to **flatten** this array 
into a single, one-dimensional array containing all the original elements, 
removing any nested structures.

**Example:**
* **Input:** `arr = [1, [2, [3, 4]], 5]`
* **Output:** `[1, 2, 3, 4, 5]`

**Explanation:**
1. We start with the first element, `1`, and add it directly to the resulting 
flattened array.
2. We encounter a nested array, `[2, [3, 4]]`. Instead of adding the entire 
array, we need to extract its individual elements (`2`, `3`, and `4`) and add 
them to the flattened array.
3. Finally, we add the remaining element, `5`, to the flattened array.

The resulting flattened array contains all the original elements from the nested 
structure in a single, linear order.
"""

from collections.abc import Iterable
from typing import Any


def flatten_brute(arr: list[Any], output_arr: list[Any]) -> list[Any]:
    if not output_arr:
        output_arr = []

    for element in arr:
        if isinstance(element, Iterable) and not isinstance(element, str):
            flatten_brute(element, output_arr)
        else:
            output_arr.append(element)

    return output_arr


def flatten_stack(arr: list[Any] | tuple[Any]) -> list[Any]:
    if len(arr) == 0:
        return arr

    flatten_list, stack = [], [arr]
    while stack:
        current = stack.pop()

        for element in current:
            if isinstance(element, Iterable) and not isinstance(element, str):
                stack.append(element)
            else:
                flatten_list.append(element)

    return flatten_list


def is_flattened(arr: list[Any]) -> bool:
    for element in arr:
        if isinstance(element, Iterable) and not isinstance(element, str):
            return False
    return True


if __name__ == "__main__":
    assert flatten_brute([1, [2, 3, [4, [5]]], 6], []) == [1, 2, 3, 4, 5, 6]
    assert flatten_brute([], []) == []
    assert flatten_brute([1, (2, 3, [4, 5]), 6], []) == [1, 2, 3, 4, 5, 6]

    assert is_flattened(flatten_stack([1, [2, 3, [4, [5]]], 6])) is True
    assert flatten_stack([]) == []
    assert is_flattened(flatten_stack([1, (2, 3, [4, 5]), 6])) is True
    assert flatten_stack((1, 2)) == [1, 2]
    assert flatten_stack([1]) == [1]
