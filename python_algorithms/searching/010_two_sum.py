"""
**Challenge:**
Given a **sorted array of integers** (ascending order) and a specific **target sum**, 
your task is to identify the **indices** of the **two numbers** within the array that 
**add up to the target sum**.

**Key Points:**
* The input array (`numbers`) contains **unique** integers sorted in **ascending order**.
* You need to find **two distinct** elements whose sum equals the **target number**.
* The function should return a list containing the **indices** (1-based) of these two 
elements, where the **first number's index must be less than the second number's index**.
* Each input is guaranteed to have **exactly one unique solution**.

**Examples:**
* **Input:** `numbers = [2, 7, 11, 15]`, `target = 9`
* **Output:** `[1, 2]` (Explanation: `numbers[0] + numbers[1] = 2 + 7 = 9`)

**Clarifications:**
* The rephrased question avoids mentioning specific solution approaches ("binary search", 
"dictionary", "two pointers") and focuses on the problem itself.
* It clarifies that the solution should provide 1-based indices and emphasizes the 
uniqueness requirement of the two elements.
"""


def two_sum(arr: list[int], target: int) -> list:
    if not arr:
        return []

    left, right = 0, len(arr) - 1
    while left <= right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [1, 2]
