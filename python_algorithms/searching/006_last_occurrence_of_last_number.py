"""
**Challenge:**
Given a **sorted array** (increasing order) and a specific **target number**, your 
task is to identify the **index** of the **last occurrence** of the target number 
within the array. 

**Key Points:**
* The input array is **sorted** in **ascending order**.
* You need to find the **index** of the last occurrence of the target number, not 
the number itself.
* If the target number doesn't exist in the array, you should return **-1**.

**Example:**
* **Input:** `[1, 2, 3, 3, 5, 7]`, `target = 3`
* **Output:** `3` (Explanation: The target number 3 last appears at index 3)

**Efficiency:**
* This approach utilizes **binary search**, resulting in a time complexity of 
**O(log n)**, where n is the length of the array. This signifies that the search 
time grows logarithmically with the array size, making it efficient for large datasets.
"""


def last_occurrence(arr: list[int], target: int) -> int:
    length = len(arr) - 1
    left, right = 0, length
    while left <= right:
        middle = (left + right) // 2
        if (arr[middle] == target and middle == length) or (
            arr[middle] == target and arr[middle + 1] > target
        ):
            return middle
        if arr[middle] <= target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


if __name__ == "__main__":
    assert last_occurrence([1, 2, 3, 3, 5, 7], 3) == 3
