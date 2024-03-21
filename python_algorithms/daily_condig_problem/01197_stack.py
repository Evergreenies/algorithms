"""
Implement a stack that has the following methods:

- push(val), which pushes an element onto the stack
- pop(), which pops off and returns the topmost element of the stack. 
If there are no elements in the stack, then it should throw an error or return null.
- max(), which returns the maximum value in the stack currently. 
If there are no elements in the stack, then it should throw an error or return null.

Each method should run in constant time.
"""
import math


class Stack:
    def __init__(self) -> None:
        self.stack: list[int] = []
        self.max_value = -math.inf
        self.top: int = -1
        self.size: int = 0

    def push(self, element: int) -> int:
        self.stack.append(element)
        self.top = element

        if element > self.max_value:
            self.max_value = element

        self.size += 1

        return self.top

    def pop(self) -> int:
        if self.size == 0:
            raise IndexError("Cannot pop element from empty stack.")

        element = self.stack.pop(-1)
        self.size -= 1

        if self.size == 0:
            self.max_value = -math.inf
            self.top = -1
            return element

        self.top = self.stack[-1]

        if element >= self.max_value:
            for value in self.stack:
                if value > self.max_value:
                    self.max_value = value
                    break

        return element

    def max(self) -> int:
        if self.size == 0:
            raise IndexError("Stack is empty.")

        return int(self.max_value)

    def display(self) -> list:
        return self.stack


if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    assert stack.display() == [1]

    stack.push(2)
    assert stack.push(3) == 3
    assert stack.push(4) == 4
    assert stack.display() == [1, 2, 3, 4]
    assert stack.max() == 4

    assert stack.pop() == 4
    assert stack.pop() == 3
    assert stack.display() == [1, 2]
