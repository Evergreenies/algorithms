"""
**Challenge:**
Given an array of elements, this algorithm aims to find the **most frequent value(s)**
within the array. These most frequent values, also known as the **mode**, represent 
the elements that appear the most number of times in the array.

**Key Points:**
* The input is an array of any element type.
* The function returns a **list** containing the **most frequent values**.
* If there are multiple elements with the same highest frequency, all of them are 
included in the returned list.

**Example:**
* **Input:** `[1, 1, 2, 2, 3, 4]`
* **Output:** `[1, 2]` (Both 1 and 2 appear twice, which is the highest frequency)

**Additional Information:**
* This approach utilizes a dictionary to store element counts and find the maximum frequency.
* The time complexity of this algorithm is O(n), meaning its execution time grows linearly 
with the size of the input array.
"""
from collections import defaultdict


def find_most_frequent(arr: list[int]) -> list[int]:
    if not arr:
        return []

    most_frequent = defaultdict(int)
    for element in arr:
        most_frequent[element] += 1

    max_occurrences = max(most_frequent.values(), default=0)
    return [key for key, value in most_frequent.items() if value == max_occurrences]


if __name__ == "__main__":
    assert find_most_frequent([1, 1, 2, 2, 3, 4]) == [1, 2]
    assert find_most_frequent([1, 2, 3, 324, 234, 23, 23, 1, 23, 23]) == [23]
