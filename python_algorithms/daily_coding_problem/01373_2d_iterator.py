"""
Implement a 2D iterator class. It will be initialized with an array of arrays, and should implement the
following methods:

next(): returns the next element in the array of arrays. If there are no more elements, raise an exception.
has_next(): returns whether or not the iterator still has elements left.
For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next() repeatedly should output 1, 2, 3, 4, 5, 6.

Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty.
"""

from typing import Any


class Iterator2D:
    def __init__(self, arr: list[list]) -> None:
        self.arr = arr
        self.row, self.col = 0, 0

    def has_nxt(self) -> bool:
        while self.row < len(self.arr) and self.col >= len(self.arr[self.row]):
            self.row += 1
            self.col = 0

        return self.row < len(self.arr)

    def nxt(self) -> Any:
        if not self.has_nxt():
            raise StopIteration("no more elememnts")

        result = self.arr[self.row][self.col]
        self.col += 1

        return result


vec2d = [[1, 2], [3], [], [4, 5, 6]]
iterator = Iterator2D(vec2d)

while iterator.has_nxt():
    print(iterator.nxt())
