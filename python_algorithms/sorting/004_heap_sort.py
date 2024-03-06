# Heap Sort


def swap(arr: list[int], index_i: int, index_j: int) -> list[int]:
    arr[index_i], arr[index_j] = arr[index_j], arr[index_i]
    return arr


def shift_down(arr: list[int], parent: int, upper: int) -> list[int]:
    while True:
        left_child, right_child = parent * 2 + 1, parent * 2 + 2
        if max(left_child, right_child) < upper:
            if arr[parent] >= max(arr[left_child], arr[right_child]):
                break
            elif arr[left_child] > arr[right_child]:
                swap(arr, parent, left_child)
                parent = left_child
            else:
                swap(arr, parent, right_child)
                parent = right_child
        elif left_child < upper:
            if arr[left_child] > arr[parent]:
                swap(arr, parent, left_child)
                parent = left_child
            else:
                break
        elif right_child < upper:
            if arr[right_child] > arr[parent]:
                swap(arr, parent, right_child)
                parent = right_child
            else:
                break
        else:
            break

    return arr


def heap_sort(arr: list[int]) -> list[int]:
    for index in range((len(arr) - 2) // 2, -1, -1):
        arr = shift_down(arr, index, len(arr))

    for index in range(len(arr) - 1, 0, -1):
        arr = swap(arr, 0, index)
        arr = shift_down(arr, 0, index)

    return arr


if __name__ == "__main__":
    assert heap_sort([5, 16, 8, 14, 20, 1, 26]) == [1, 5, 8, 14, 16, 20, 26]
