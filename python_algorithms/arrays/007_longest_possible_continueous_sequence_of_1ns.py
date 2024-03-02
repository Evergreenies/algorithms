"""
**Challenge:**
Imagine you have a binary array containing only 0s and 1s. You want to find the **index of a 
single 0** that can be replaced with a 1 to create the **longest possible continuous sequence 
of 1s** in the array.

**Clarifications:**
* You are allowed to **replace only one 0** with a 1.
* The goal is to maximize the **length of the continuous sequence of 1s** after the replacement.
* If there are **no zeros** in the array, the function should return **-1**.

**Example:**
* **Input:** `[1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1]`
* **Output:** `3` (Replacing the 0 at index 3 with a 1 creates the longest continuous sequence 
of 1s with length 6)
"""


def longest_possible_continuous_sequence(arr: list[int]) -> int:
    max_count, max_index = 0, 0
    prev_zero, prev_prev_zero = -1, -1

    if not arr or all(arr):
        return -1

    for index in range(len(arr)):
        if arr[index] == 0:
            if index - prev_prev_zero > max_count:
                max_count = index - prev_prev_zero
                max_index = prev_zero

            prev_prev_zero = prev_zero
            prev_zero = index

        if len(arr) - prev_prev_zero > max_count:
            max_index = prev_zero

    return max_index


if __name__ == "__main__":
    assert (
        longest_possible_continuous_sequence([1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1])
        == 3
    )
