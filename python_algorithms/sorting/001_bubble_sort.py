"""
# Bubble sort

**1. Setup:**
* Unsorted array `arr` of length `n`.
* `swapped` flag = `False`.

**2. Loop:**
* For each element `i` in `arr` (except the last):
    * For elements `j` from 0 to `n-i-2`:
        * If `arr[j] > arr[j+1]`:
            * Swap `arr[j]` and `arr[j+1]`.
            * Set `swapped` to `True`.
    * If `swapped` is `False`:
        * Break (array is sorted).
* Set `swapped` back to `False` for next iteration.

**Repeat** steps 2-3 until the loop completes.
"""


def bubble_sort(arr: list[int]) -> list[int]:
    if not arr:
        return []

    length = len(arr) - 1
    for index_i in range(length):
        swapped = False
        for index_j in range(length - index_i):
            if arr[index_j] > arr[index_j + 1]:
                arr[index_j], arr[index_j + 1] = arr[index_j + 1], arr[index_j]
                swapped = True

        if not swapped:
            break
    return arr


if __name__ == "__main__":
    assert bubble_sort([5, 9, 2, 1, 67, 34, 88, 34]) == [1, 2, 5, 9, 34, 34, 67, 88]
    assert bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
