"""
Merge two sorted array
"""


def merge(arr1: list[int], arr2: list[int]) -> list[int]:
    if not arr1:
        return arr2

    if not arr2:
        return arr1

    result = []
    index_i, index_j = 0, 0
    while index_i < len(arr1) and index_j < len(arr2):
        if arr1[index_i] < arr2[index_j]:
            result.append(arr1[index_i])
            index_i += 1
        else:
            result.append(arr2[index_j])
            index_j += 1

    while index_i < len(arr1):
        result.append(arr1[index_i])
        index_i += 1

    while index_j < len(arr2):
        result.append(arr2[index_j])
        index_j += 1

    return result


print(merge([0, 1, 4, 5, 6], [2, 7, 9, 10]))
