from typing import Any


class Array:
    def __init__(self, size: int = 10):
        self.array = [None] * size
        self.length = 0
        self.size = size

    def display(self) -> None:
        print(f"PRINTING ARRAY: {self.array}")

    def append(self, item: Any) -> None:
        if self.length > (self.size - 1):
            raise Exception("array is full")

        self.array[self.length] = item
        self.length += 1

    def insert(self, index: int, item: Any) -> None:
        if self.length > self.size - 1:
            raise Exception("array is full")

        idx = self.length
        while idx > index:
            self.array[idx] = self.array[idx - 1]
            idx -= 1

        self.array[idx] = item
        self.length += 1

    def delete(self, index: int) -> Any:
        if index < 0 or index > self.length:
            raise IndexError("index out of range")

        index -= 1
        item = self.array[index]
        while index < self.length:
            self.array[index] = self.array[index + 1]
            index += 1

        self.array[index + 1] = None
        self.length -= 1

        return item

    def search_transpose(self, item: Any) -> int:
        """
        searches for item in array and returning index of an array i found
        else returns -1

        Transpose is a technique used to optimized search when there are most
        frequent element to search in an array. This technique just swap searched
        element with previous index position

        :param item: element to search
        :return: index
        """
        for index in range(self.length):
            if item == self.array[index]:
                self._swap(index, index - 1)

                return index

        return -1

    def search_move_to_front(self, item: Any) -> int:
        """
        Searches item in array
        Moves target position to the first position in order to optimize search

        :param item: item to search
        :return: index
        """
        for index in range(self.length):
            if item == self.array[index]:
                self._swap(0, index)

                return index

        return -1

    def binary_search(self, item: Any) -> int:
        _arr = [itm for itm in self.array if itm]
        print(f"SORTED ARR: {_arr}")

        low, high = 0, len(_arr)-1
        while low <= high:
            middle = (low + high) // 2
            if _arr[middle] == item:
                return middle
            elif item > _arr[middle]:
                low = middle + 1
            else:
                high = middle - 1

        return -1

    def _swap(self, from_idx: int, to_idx: int) -> None:
        self.array[to_idx], self.array[from_idx] = self.array[from_idx], self.array[to_idx]


arr = Array(6)
arr.append(1)
arr.insert(1, 2)
print(arr.delete(2))
arr.append(3)
arr.display()
print(arr.search_transpose(3))
print(arr.search_transpose(4))
arr.display()
print(arr.search_move_to_front(1))
arr.display()
print(arr.binary_search(3))
print(arr.binary_search(4))
