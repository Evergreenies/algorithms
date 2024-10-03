"""
Describe an algorithm to compute the longest increasing subsequence of an array of numbers in O(n log n) time.
"""


def binary_search(arr: list, target: int) -> int:
    left, right = 0, len(arr) - 1

    while left <= right:
        middle = (left + right) // 2
        if arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return left


def length_of_lis(arr: list) -> tuple[int, list]:
    if not arr:
        return 0, []

    tails = []
    for item in arr:
        pos = binary_search(tails, item)
        if pos < len(tails):
            tails[pos] = item
        else:
            tails.append(item)

    return len(tails), tails


ar = [10, 9, 2, 5, 3, 7, 101, 18]
pos, tails = length_of_lis(ar)
print(tails)
assert pos == 4, f"expected 2, got {pos}"
