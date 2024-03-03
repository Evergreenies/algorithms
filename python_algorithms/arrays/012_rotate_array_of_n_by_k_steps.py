"""
**Challenge:**
You are given an array of integers and two numbers: `n` (the number of elements
in the array)and `k` (the number of positions to rotate the array to the right).
Your task is to **modify the original array in-place** to achieve the right rotation.

**Example:**
* **Input:** Array = [1, 2, 3, 4, 5, 6, 7], `n` = 7, `k` = 3
* **Output:** The original array is modified to [5, 6, 7, 1, 2, 3, 4] (rotated to
the right by 3 positions)

**Clarifications:**
* The rotation happens **to the right**, meaning elements are shifted towards the
beginning of the array.
* The function should **modify the original array in-place** and not return a new array.
"""

from typing import Any


def rotate_array_of_n_by_k_steps(arr: list[Any], k: int) -> list[Any] | None:
    if not arr:
        return

    length = len(arr)
    k = k % length
    return arr[length - k :] + arr[: length - k]


def rotate_array_of_n_by_k_steps_reverse(arr: list[Any], k: int) -> list[Any]:
    if k <= 0:
        return arr

    def reverse(arr: list[Any], start: int, end: int) -> None:
        while start <= end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    length = len(arr)
    k = k % length

    reverse(arr, length - k, length - 1)
    reverse(arr, 0, length - k - 1)
    reverse(arr, 0, length - 1)

    return arr


if __name__ == "__main__":
    assert rotate_array_of_n_by_k_steps([1, 2, 3, 4, 5, 6, 7], 3) == [
        5,
        6,
        7,
        1,
        2,
        3,
        4,
    ]
    assert rotate_array_of_n_by_k_steps([1, 2, 3, 4, 5, 6], 3) == [4, 5, 6, 1, 2, 3]
    assert rotate_array_of_n_by_k_steps([1, 2, 3, 4, 5, 6], 0) == [1, 2, 3, 4, 5, 6]
    assert rotate_array_of_n_by_k_steps([1, 2, 3, 4, 5, 6], 1) == [6, 1, 2, 3, 4, 5]
    assert rotate_array_of_n_by_k_steps([1, 2, 3, 4, 5, 6], 7) == [6, 1, 2, 3, 4, 5]
    assert rotate_array_of_n_by_k_steps([1, 2, 3, 4, 5, 6], 6) == [1, 2, 3, 4, 5, 6]

    assert rotate_array_of_n_by_k_steps_reverse([1, 2, 3, 4, 5, 6, 7], 3) == [
        5,
        6,
        7,
        1,
        2,
        3,
        4,
    ]
    assert rotate_array_of_n_by_k_steps_reverse([1, 2, 3, 4, 5, 6], 3) == [
        4,
        5,
        6,
        1,
        2,
        3,
    ]
    assert rotate_array_of_n_by_k_steps_reverse([1, 2, 3, 4, 5, 6], 0) == [
        1,
        2,
        3,
        4,
        5,
        6,
    ]
    assert rotate_array_of_n_by_k_steps_reverse([1, 2, 3, 4, 5, 6], 1) == [
        6,
        1,
        2,
        3,
        4,
        5,
    ]
    assert rotate_array_of_n_by_k_steps_reverse([1, 2, 3, 4, 5, 6], 7) == [
        6,
        1,
        2,
        3,
        4,
        5,
    ]
    assert rotate_array_of_n_by_k_steps_reverse([1, 2, 3, 4, 5, 6], 6) == [
        1,
        2,
        3,
        4,
        5,
        6,
    ]
