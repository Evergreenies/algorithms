"""
Find the pairs that sums up to the k in sorted arr.
"""


def find_pairs(arr: list[int], target: int) -> tuple | None:
    if not arr: return

    left, right = 0, len(arr) - 1
    while left < right:
        _sum = arr[left] + arr[right]

        if _sum == target:
            # return arr[left], arr[right]
            print(f"Pair tat sums to K: {target} => {arr[left], arr[right]}")

        if _sum > target:
            right -= 1
            continue

        if _sum < target:
            left += 1
            continue

        left += 1
        right += 1


print(
    find_pairs([2, 3, 4, 5, 6, 7, 8, 10, 14, 16], 10)
)
