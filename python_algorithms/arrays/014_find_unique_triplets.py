"""
**Challenge:**
You are given an array of integers. Your task is to find all **unique triplets** within 
the array that **add up to zero**. A triplet is a combination of three distinct elements.

**Example:**
* **Input:** `[-1, 0, 1, 2, -1, -4]`
* **Output:** `[(-1, 0, 1), (-1, -1, 2)]` (Set representation emphasizes unique combinations)

**Clarifications:**
* The output should contain **unique triplets** only, meaning the same combination of 
elements shouldn't appear multiple times.
* The order of elements within a triplet doesn't matter.
"""


def find_triplet_sum_zero(arr: list[int]) -> set[tuple]:
    triplets = set()
    arr.sort()

    for index in range(len(arr) - 2):
        left, right = index + 1, len(arr) - 1

        while left < right:
            current_sum = arr[index] + arr[left] + arr[right]
            if current_sum == 0:
                triplets.add((arr[index], arr[left], arr[right]))

                left += 1
                right -= 1
            else:
                if abs(current_sum) < abs(current_sum + arr[left]):
                    left += 1
                else:
                    right -= 1

    return triplets


if __name__ == "__main__":
    assert find_triplet_sum_zero([-1, 0, 1, 2, -1, -4]) == {(-1, 0, 1), (-1, -1, 2)}
    assert find_triplet_sum_zero([-1, 3, 1, 2, -1, -4, -2]) == {
        (-4, 1, 3),
        (-2, -1, 3),
        (-1, -1, 2),
    }
