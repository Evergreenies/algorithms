"""
**Challenge:**
Given an **array of integers**, sorted in **ascending order**, you need to find 
the **starting and ending indices** of a specific **target value**.

**Important Points:**
* The input array (`nums`) contains **integers** arranged in **increasing order**.
* You're searching for a specific **target value**.
* The function should return a list containing two integers:
    * The **first index** at which the target value appears (or -1 if not found).
    * The **last index** at which the target value appears (or -1 if not found).

**Examples:**
* **Input:** `nums = [5, 7, 7, 8, 8, 8, 10]`, `target = 8`
* **Output:** `[3, 5]` (Explanation: The target "8" starts at index 3 and ends at index 5)
* **Input:** `nums = [5, 7, 7, 8, 8, 8, 10]`, `target = 11`
* **Output:** `[-1, -1]` (Explanation: The target "11" is not present in the array)
"""


def search_range_of_target(arr: list[int], target: int) -> list[int]:
    if not arr:
        return [-1, -1]

    left, right = 0, len(arr) - 1
    while left < right:
        middle = left + (right - left) // 2
        if arr[middle] < target:
            left = middle + 1
        else:
            right = middle

    for index in range(len(arr) - 1, -1, -1):
        if arr[index] == target:
            return [left, index]

    return [-1, -1]


if __name__ == "__main__":
    assert search_range_of_target([5, 7, 7, 8, 8, 8, 10], 8) == [3, 5]
    assert search_range_of_target([5, 7, 7, 8, 8, 8, 10], 11) == [-1, -1]
