"""
Implement a bit array.

A bit array is a space efficient array that holds a value of 1 or 0 at each index.

init(size): initialize the array with size
set(i, val): updates index at i with val where val is either 1 or 0.
get(i): gets the value at index i.
"""

from typing import Any


class Bit:
    __bits = [0, 1]
    __value = None

    def __get__(self, obj: Any, typ: Any = None) -> int | None:
        return self.__value

    def __set__(self, obj: Any, value: int):
        if value in self.__bits:
            self.__value = value
        else:
            raise ValueError("value must be either `0` or `1`")


class BitArray:
    __value = Bit()

    def __init__(self, size: int) -> None:
        self.size = size
        self.arr: list[Bit | None] = [None for _ in range(size)]

    def set(self, index: int, value: int) -> None:
        if isinstance(index, int) or index <= self.size:
            if not isinstance(value, int):
                raise ValueError("value must be integer value")

            self.__value = value
            self.arr[index - 1] = self.__value
        else:
            raise IndexError("invalid index")

    def get(self, index: int) -> Bit | None:
        if isinstance(index, int) or index < self.size:
            return self.arr[index - 1]
        else:
            raise IndexError("invalid index")


if __name__ == "__main__":
    arr = BitArray(5)
    arr.set(1, 0)
    print(arr.get(1))

    arr.set(2, 1)
    arr.set(5, 0)
