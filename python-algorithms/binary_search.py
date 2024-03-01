def binary_search(arr: list, target: int) -> int:
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


print(binary_search([1, 3, 5, 7, 9, 11, 13, 15, 17], 13))
print(binary_search([1, 3, 5, 7, 9, 11, 13, 15, 17], 1))
print(binary_search([1, 3, 5, 7, 9, 11, 13, 15, 17], 0))
