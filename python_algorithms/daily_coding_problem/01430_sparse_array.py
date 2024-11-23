"""
You have a large array with most of the elements as zero.

Use a more space-efficient data structure, SparseArray, that implements the same interface:

init(arr, size): initialize with the original large array and size.
set(i, val): updates index at i with val.
get(i): gets the value at index i.
"""


class SparseArray(object):
    def __init__(self, arr: list[int], size: int) -> None:
        self.arr = {index: value for index, value in enumerate(arr) if value != 0}
        self.size = size

    def set(self, index: int, value: int) -> None:
        if index < 0 or index >= self.size:
            raise IndexError("index out of range")

        if value == 0:
            self.arr.pop(index, None)
        else:
            self.arr[index] = value

    def get(self, index) -> int | None:
        if index < 0 or index >= self.size:
            raise IndexError("index out of range")

        return self.arr.get(index, None)


ar = [0, 0, 3, 0, 0, 4, 0, 5]
sparse_arr = SparseArray(ar, len(ar))

# print(sparse_arr.get(4))  # index out of range error
print(sparse_arr.get(5))
print(sparse_arr.get(2))

sparse_arr.set(4, 12)
print(sparse_arr.get(4))
