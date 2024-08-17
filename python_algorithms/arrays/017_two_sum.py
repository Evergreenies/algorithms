"""
**Challenge:**
You are given an array of **unique integers** and a **specific target sum**. 
Your task is to find the **indices** of the **two** elements within the array 
that **add up to the target sum**. It's important to note that:

* Each input will have **exactly one valid solution**.
* You cannot use the same element **twice**.

**Example:**
* **Input:** `[2, 7, 11, 15]`, `target = 9`
* **Output:** `(0, 1)` (Explanation: `nums[0] + nums[1] = 2 + 7 = 9`)

**Clarifications:**
* The input array contains **unique** integers.
* The output is a tuple containing the **indices** of the two elements, not 
the elements themselves.
"""


def two_sum(arr: list[int], target: int) -> tuple[int, int] | None:
    if not arr:
        return

    visited = {}
    for index, num in enumerate(arr):
        complement = target - num

        if visited.get(complement) is not None:
            return visited[complement], index

        visited[num] = index

    return


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == (0, 1)
