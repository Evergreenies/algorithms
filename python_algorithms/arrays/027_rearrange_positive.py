"""
Rearrange an array such that all -ve numbers should be at left and +ve numbers should be at right
"""


def rearrange(arr: list[int]) -> list[int]:
    if not arr:
        return []

    length = len(arr)
    if length == 1:
        return arr

    left, right = 0, length - 1
    while left <= right:
        while arr[left] < 0:
            left += 1
        while arr[right] >= 0:
            right -= 1

        arr[left], arr[right] = arr[right], arr[left]
    arr[left], arr[right] = arr[right], arr[left]

    return arr


print(rearrange([-6, 3, -8, 10, 5, -7, -9, 12, -4, 2]))
