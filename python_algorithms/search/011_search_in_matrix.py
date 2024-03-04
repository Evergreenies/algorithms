# Program to seach element in 2D matrix


def binary_search(arr: list[int], target: int) -> bool:
    left, right = 0, len(arr) - 1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == target:
            return True
        elif arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return False


def search_matrix(arr: list[list], target: int) -> bool:
    left, right = 0, len(arr) - 1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle][0] <= target <= arr[middle][-1]:
            return binary_search(arr[middle], target)
        elif arr[middle][-1] < target:
            left = middle + 1
        else:
            right = middle - 1

    return False


if __name__ == "__main__":
    assert search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3) is True
    assert (
        search_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13) is False
    )
