def shell_sort(arr: list[int]) -> list[int]:
    if not arr:
        return []

    length = len(arr)
    if length <= 1:
        return arr

    gap = length // 2
    while gap > 0:
        for current_index in range(gap, length):
            current_element = arr[current_index]
            shift_index = current_index

            while shift_index >= gap and current_element < arr[shift_index - gap]:
                arr[shift_index] = arr[shift_index - gap]
                shift_index -= gap

            arr[shift_index] = current_element
        gap //= 2

    return arr


if __name__ == "__main__":
    assert shell_sort([]) == []
    assert shell_sort([-1]) == [-1]
    assert shell_sort([10, 3, 15, 7, 8, 23, 98, 29]) == [3, 7, 8, 10, 15, 23, 29, 98]
    assert shell_sort([2, 3]) == [2, 3]
    assert shell_sort([3, 2]) == [2, 3]
    assert shell_sort([5, 6, 3, 1]) == [1, 3, 5, 6]
    assert shell_sort([7, 5, 6, 3, 1]) == [1, 3, 5, 6, 7]
    assert shell_sort([23, 14, 90, 6, 45, 45, 34, 24, 19]) == [
        6,
        14,
        19,
        23,
        24,
        34,
        45,
        45,
        90,
    ]
