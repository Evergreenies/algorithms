# Find K'th smallest number in give 2D matrix


def smallest_element(arr: list[list], middle: int, size: int) -> int:
    row, col, result = size - 1, 0, 0
    while row >= 0 and col < size:
        if arr[row][col] > middle:
            row -= 1
        else:
            result += row + 1
            col += 1
    return result


def kth_smallest_element(arr: list[list], kth: int) -> int:
    if not arr:
        return -1

    rows, columns = len(arr), len(arr[0])
    if kth > (rows * columns):
        return -1

    left, right = arr[0][0], arr[-1][-1] + 1
    while left <= right:
        middle = left + (right - left) // 2
        count = smallest_element(arr, middle, rows)
        if count < kth:
            left = middle + 1
        else:
            right = middle - 1
    return left


if __name__ == "__main__":
    assert kth_smallest_element([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8) == 13
    assert kth_smallest_element([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 45) == -1
    assert kth_smallest_element([[-5]], 1) == -5
    assert kth_smallest_element([[1, 2], [1, 3]], 2) == 1
