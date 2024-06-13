"""
Write a function that rotates a list by k elements. For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2].
Try solving this without creating a copy of the list. How many swap or move operations do you need?
"""


def rotate_by_k_pythonic(arr: list[int], rotations: int) -> list[int]:
    if not arr:
        return []

    if len(arr) == 1:
        return arr

    rotations = rotations % len(arr)

    while rotations > 0:
        arr.append(arr.pop(0))
        rotations -= 1

    return arr


def reverse(arr: list[int], start: int, end: int) -> list[int]:
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr


def rotate_by_k(arr: list[int], rotations: int) -> list[int]:
    length = len(arr)
    rotations = rotations % length

    if rotations == 0:
        return arr

    # reverse first k elements
    reverse(arr, 0, rotations - 1)

    # reverse the remaining length - k elements
    reverse(arr, rotations, length - 1)

    # reverse entire list
    reverse(arr, 0, length - 1)

    return arr


if __name__ == "__main__":
    assert rotate_by_k_pythonic([1, 2, 3, 4, 5, 6], 2) == [3, 4, 5, 6, 1, 2]
    assert rotate_by_k([1, 2, 3, 4, 5, 6], 2) == [3, 4, 5, 6, 1, 2]
