"""
Given an array of numbers and an index i, return the index of the nearest larger number of the number at index i,
where distance is measured in array indices.

For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.

If two distances to larger numbers are the equal, then return any one of them. If the array at i doesn't have a
nearest larger integer, then return null.

Follow-up: If you can preprocess the array, can you do this in constant time?
"""


def brute_force_nearest_largest_index(arr: list[int], index: int) -> int | None:
    if not arr or len(arr) < 2:
        return None

    length = len(arr)
    left, right = index - 1, index + 1

    while left >= 0 or right < length:
        if left >= 0 and arr[left] > arr[index]:
            return left
        if right < length and arr[right] > arr[index]:
            return right

        left -= 1
        right += 1

    return None


def pre_process_array(arr: list[int]) -> tuple:
    length, stack = len(arr), []
    nearest_left, nearest_right = [-1] * length, [-1] * length

    for index in range(length):
        while stack and arr[stack[-1]] <= arr[index]:
            stack.pop()

        if stack:
            nearest_left[index] = stack[-1]

        stack.append(index)

    stack.clear()

    for index in range(length - 1, -1, -1):
        while stack and arr[stack[-1]] <= arr[index]:
            stack.pop()

        if stack:
            nearest_right[index] = stack[-1]

        stack.append(index)

    return nearest_left, nearest_right


def query_nearest_largest(
    index: int, nearest_left: list, nearest_right: list
) -> int | None:
    left_index = nearest_left[index]
    right_index = nearest_right[index]

    if left_index == -1 and right_index == -1:
        return None

    if left_index == -1:
        return right_index

    if right_index == -1:
        return left_index

    return (
        left_index
        if abs(index - left_index) <= abs(index - right_index)
        else right_index
    )


print(brute_force_nearest_largest_index([4, 1, 3, 5, 6], 0))
print(query_nearest_largest(0, *pre_process_array([4, 1, 3, 5, 6])))
