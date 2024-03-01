"""
**Challenge:** You are given a list of numbers (`lst`) and a maximum number of
occurrences (`N`) for each number. Your task is to create a new list that contains
each unique number in the original list **at most N times**, while preserving
the original order.

**Example:**
* **Input:** `lst = [1, 2, 3, 1, 2, 1, 2, 3]`, `N = 2`
* **Output:** `[1, 2, 3, 1, 2]`

**Explanation:**
1. The number `1` appears three times in the original list, but we can only include
it twice in the new list.
2. Similarly, the number `2` appears three times, but we can only include it twice
in the new list.
3. Both `1` and `2` have reached their maximum allowed occurrences (twice), so we
include the next unique number, `3`.

This process continues until all unique numbers in the original list have been
processed, ensuring no number appears more than `N` times in the final list.
"""


def nth_occurrences(arr: list[int], nth: int) -> list[int]:
    counts = dict()
    result_list = []

    for element in arr:
        counts[element] = counts.get(element, 0)
        if counts.get(element) < nth:
            result_list.append(element)
            counts[element] += 1

    return result_list


if __name__ == '__main__':
    assert nth_occurrences([1, 2, 3, 1, 2, 1, 2, 3], 2) == [1, 2, 3, 1, 2, 3]
    assert nth_occurrences([1, 2, 3, 1, 2, 1, 2, 3], 3) == [1, 2, 3, 1, 2, 1, 2, 3]
    assert nth_occurrences([], 2) == []
    assert nth_occurrences([1], 1) == [1]
