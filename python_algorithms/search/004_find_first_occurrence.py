"""
**Challenge:**
Given a **sorted array** (increasing order) and a specific **target number**, your 
task is to find the **index** of the **first occurrence** of the target number 
within the array. 

**Key Points:**
* The input array is **sorted** in **ascending order**.
* You need to find the **index** of the first occurrence of the target number, not 
the number itself.
* If the target number doesn't exist in the array, you should return **-1**.

**Example:**
* **Input:** `[1, 3, 5, 7, 7, 9]`, `target = 7`
* **Output:** `3` (Explanation: The target number 7 first appears at index 3)

**Efficiency:**
* This approach utilizes **binary search**, resulting in a time complexity of 
**O(log n)**, where n is the length of the array. This signifies that the search 
time grows logarithmically with the array size, making it efficient for large datasets.
"""


def first_occurrence(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        middle = (left + right) // 2
        if left == right:
            break
        if arr[middle] < target:
            left = middle + 1
        else:
            right = middle

    if arr[left] == target:
        return left
    return -1


if __name__ == "__main__":
    assert first_occurrence([1, 3, 5, 7, 7, 9], 7) == 3
