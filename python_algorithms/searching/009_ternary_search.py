"""
**Challenge:**
**Ternary Search** is a divide-and-conquer algorithm specifically designed for searching 
**sorted arrays**. It aims to find a specific **target element** within the array.

**Key Points:**
* The input array is **sorted** in **ascending order**.
* This algorithm is similar to binary search but divides the array into **three parts** 
instead of two.
* Based on the target value's comparison with elements in the divided sections, the search 
area is efficiently narrowed down until the target is found or determined to be absent.

**Clarifications:**
* The question doesn't mention specific implementation details like "mid1" or "mid2". This 
rephrased version avoids those details and focuses on the high-level concept.
* While the question mentions the time complexity as "O(log3(N))", it also clarifies that 
"log3" refers to the logarithm base 3.
"""


def ternary_search(arr: list[int], target: int) -> int:
    if not arr:
        return -1

    left, right = 0, len(arr) - 1
    while left <= right:
        middle1 = left + (right - left) // 3
        middle2 = right - (right - left) // 3

        if arr[middle1] == target:
            return middle1
        elif arr[middle2] == target:
            return middle2

        if arr[middle2] > target:
            left = middle2 + 1
        elif arr[middle1] < target:
            right = middle1 - 1
        else:
            return -1
    return -1


if __name__ == "__main__":
    assert ternary_search([1, 3, 5, 7, 9, 11, 13], 9) == 4
