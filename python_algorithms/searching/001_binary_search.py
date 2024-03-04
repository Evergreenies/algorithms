def binary_search(arr: list[int], target: int) -> int:
    if not arr:
        return -1

    arr.sort()
    left, right = 0, len(arr) - 1

    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


if __name__ == "__main__":
    assert binary_search([1, 2, 3, 4, 5], 5) == 4
