"""
**Challenge:**
This algorithm aims to find a specific element within a **sorted array** in a 
more efficient manner compared to linear search. It utilizes "jumps" to quickly 
search through the array, reducing the number of comparisons needed.

**Key Points:**
* The input array is **sorted** in **ascending order**.
* The algorithm searches for a specific **target element** within the array.
* It utilizes a technique called **jumping** to search larger portions of the 
array at a time, potentially reaching the target element faster than linear search.

**Clarifications:**
* While the question mentions "Jump Search" in the title, it doesn't provide 
specific details about the algorithm's implementation. This rephrased version 
avoids mentioning the algorithm name and focuses on the problem context and 
functionalities.
"""
import math


def linear_search(arr: list[int], target: int, current: int) -> int:
    index = 0
    while index != len(arr):
        if arr[index] == target:
            return current + index
        index += 1
    return -1


def jump_search(arr: list[int], target) -> int:
    if not arr:
        return -1

    length = len(arr)
    jump_size = int(math.sqrt(length))
    current = 0

    while current != (length - 1) and arr[current] < target:
        _next = current + jump_size - 1
        if arr[_next] == target:
            return _next
        elif arr[_next] > target:
            return linear_search(arr[current:_next], target, current)

        current += jump_size

    return linear_search(arr[current : current + jump_size], target, current)


if __name__ == "__main__":
    assert jump_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 5) == 5
    assert jump_search([1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6], -1) == -1
