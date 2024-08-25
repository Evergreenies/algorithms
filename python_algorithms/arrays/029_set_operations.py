"""
Perform set operations

Union
Intersection
Difference

Note: The provided input arrays would be in sorted order
"""


def union(arr1: list[int], arr2: list[int]) -> list[int]:
    if not arr1:
        return arr2
    if not arr2:
        return arr1

    result = []
    index_i, index_j = 0, 0
    while index_i < len(arr1) and index_j < len(arr2):
        if arr1[index_i] == arr2[index_j]:
            result.append(arr1[index_i])
            index_i += 1
            index_j += 1
        elif arr1[index_i] < arr2[index_j]:
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


def intersection(arr1: list[int], arr2: list[int]) -> list[int]:
    if not arr1:
        return arr2
    if not arr2:
        return arr1

    result = []
    index_i, index_j = 0, 0
    while index_i < len(arr1) and index_j < len(arr2):
        if arr1[index_i] == arr2[index_j]:
            result.append(arr1[index_i])
            index_i += 1
            index_j += 1
        elif arr1[index_i] < arr2[index_j]:
            index_i += 1
        else:
            index_j += 1

    return result


def difference(arr1: list[int], arr2: list[int]) -> list[int]:
    if not arr1:
        return arr2
    if not arr2:
        return arr1

    result = []
    index_i, index_j = 0, 0
    while index_i < len(arr1) and index_j < len(arr2):
        if arr1[index_i] == arr2[index_j]:
            index_i += 1
            index_j += 1
        elif arr1[index_i] < arr2[index_j]:
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


print(union([0, 1, 4, 5, 6], [2, 7, 9, 10]))
print(intersection([0, 1, 4, 5, 6, 7], [2, 7, 9, 10]))
print(difference([0, 1, 4, 5, 6, 7], [2, 7, 9, 10]))
