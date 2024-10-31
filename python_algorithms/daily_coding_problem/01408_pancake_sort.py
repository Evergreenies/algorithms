"""
Given a list, sort it using this method: reverse(lst, i, j), which reverses lst from i to j.
"""


def reverse(arr: list, index_i: int, index_j: int) -> None:
    while index_i < index_j:
        arr[index_i], arr[index_j] = arr[index_j], arr[index_i]
        index_i += 1
        index_j -= 1


def pancake_sort(arr: list) -> list:
    length = len(arr)
    for index_i in range(length - 1, 0, -1):
        man_index = 0
        for index_j in range(0, index_i + 1):
            if arr[index_j] > arr[man_index]:
                man_index = index_j

        if man_index != index_i:
            if man_index != 0:
                reverse(arr, 0, man_index)

            reverse(arr, 0, index_i)

    return arr


print(pancake_sort([3, 2, 4, 1]))
