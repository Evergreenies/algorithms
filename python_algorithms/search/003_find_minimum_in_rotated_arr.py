def find_minimum(arr: list[int]) -> int:
    left, right = 0, len(arr) - 1
    while left < right:
        middle = (left + right) // 2
        if arr[middle] > arr[right]:
            left = middle + 1
        else:
            right = middle
    return arr[left]


if __name__ == "__main__":
    assert find_minimum([5, 6, 7, 1, 2, 3, 4]) == 1
