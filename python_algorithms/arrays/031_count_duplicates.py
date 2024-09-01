"""
Print the count of duplicate elements
"""


def duplicate_count(arr: list[int]) -> None:
    if not arr:
        return

    index = 0
    while index < len(arr) - 1:
        if arr[index] == arr[index + 1]:
            index_j = index + 1
            while arr[index_j] == arr[index]:
                index_j += 1

            print(f"{arr[index]} repeated {index_j - index} times.")
            index = index_j - 2

        index += 1


duplicate_count([3, 6, 8, 8, 10, 12, 15, 15, 15, 20])
