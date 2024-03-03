def binary_search(arr: list[int], target: int, left: int, right: int) -> int:
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


def find_pivot(arr: list[int]) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] > arr[right]:
            left = middle + 1
        else:
            right = middle - 1
    return left


def search_in_rotated_array(arr: list[int], target: int) -> int:
    pivot = find_pivot(arr)
    if arr[pivot] == target:
        return pivot

    if arr[0] <= target <= arr[pivot - 1]:
        return binary_search(arr, target, 0, pivot)
    return binary_search(arr, target, pivot + 1, len(arr) - 1)


if __name__ == "__main__":
    assert search_in_rotated_array([5, 6, 7, 1, 2, 3, 4], 2) == 4
