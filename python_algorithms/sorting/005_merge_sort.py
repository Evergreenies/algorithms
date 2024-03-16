def merge_arr(arr: list[int], left_arr: list[int], right_arr: list[int]) -> None:
    left_length = len(left_arr)
    right_length = len(right_arr)
    current_index, left_index, right_index = 0, 0, 0

    while left_index < left_length and right_index < right_length:
        if left_arr[left_index] <= right_arr[right_index]:
            arr[current_index] = left_arr[left_index]
            left_index += 1
        else:
            arr[current_index] = right_arr[right_index]
            right_index += 1

        current_index += 1

    while left_index < left_length:
        arr[current_index] = left_arr[left_index]
        left_index += 1
        current_index += 1

    while right_index < right_length:
        arr[current_index] = right_arr[right_index]
        right_index += 1
        current_index += 1


def merge_sort(arr: list[int]) -> list[int]:
    if not arr:
        return []

    if len(arr) < 2:
        return arr

    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    merge_sort(left)
    merge_sort(right)
    merge_arr(arr, left, right)

    return arr


if __name__ == "__main__":
    assert merge_sort([]) == []
    assert merge_sort([-1]) == [-1]
    assert merge_sort([10, 3, 15, 7, 8, 23, 98, 29]) == [3, 7, 8, 10, 15, 23, 29, 98]
    assert merge_sort([2, 3]) == [2, 3]
    assert merge_sort([3, 2]) == [2, 3]
    assert merge_sort([5, 6, 3, 1]) == [1, 3, 5, 6]
    assert merge_sort([7, 5, 6, 3, 1]) == [1, 3, 5, 6, 7]
    assert merge_sort([23, 14, 90, 6, 45, 45, 34, 24, 19]) == [
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
