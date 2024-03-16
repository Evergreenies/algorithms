def merge_array(arr: list[int], left: list[int], right: list[int]) -> None:
    left_length = len(left)
    right_length = len(right)
    left_index, right_index = 0, 0
    current_index = 0

    while left_index < left_length and right_index < right_length:
        if left[left_index] <= right[right_index]:
            arr[current_index] = left[left_index]
            left_index += 1
        else:
            arr[current_index] = right[right_index]
            right_index += 1

        current_index += 1

    while left_index < left_length:
        arr[current_index] = left[left_index]
        left_index += 1
        current_index += 1

    while right_index < right_length:
        arr[current_index] = right[right_index]
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

    merge_array(arr, left, right)


def three_sum_hash(arr: list[int], target: int) -> bool:
    if not arr or len(arr) < 3:
        return False

    if len(arr) == 3:
        return sum(arr) == target

    merge_sort(arr)
    for index in range(len(arr) - 2):
        left = index + 1
        right = len(arr) - 1

        while left < right:
            if (arr[index] + arr[left] + arr[right]) == target:
                return True
            elif (arr[index] + arr[left] + arr[right]) < target:
                left += 1
            else:
                right -= 1

    return False


if __name__ == "__main__":
    assert three_sum_hash([10, 303, 3, 4, 25], 49) is False
    assert three_sum_hash([10, 303, 3, 4, 25], 39) is True
    assert three_sum_hash([10, 303, 3, 4, 25], 9) is False
    assert three_sum_hash([], 0) is False
    assert three_sum_hash([1], 1) is False
    assert three_sum_hash([1, 2, 3], 6) is True
    assert three_sum_hash([-3, -3, -3], -9) is True
    assert three_sum_hash([-3, 0, 3], 0) is True
