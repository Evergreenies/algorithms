"""
Implement 3 stacks using a single list
"""

from typing import Any


class Stack:
    def __init__(self, number_of_stacks: int = 1) -> None:
        self.list: list[list[Any]] = [[] for _ in range(number_of_stacks)]
        self.number_of_stacks = number_of_stacks

    def is_stack_exceed(self, stack_number: int) -> bool:
        return not (stack_number <= self.number_of_stacks)

    def size(self, stack_number: int = 1):
        if self.is_stack_exceed(stack_number):
            raise ValueError(
                f"we have just {self.number_of_stacks} stacks in our list, but got {stack_number}"
            )

        return len(self.list[stack_number - 1])

    def is_empty(self, stack_number: int) -> bool:
        if self.is_stack_exceed(stack_number):
            raise ValueError(
                f"we have just {self.number_of_stacks} stacks in our list, but got {stack_number}"
            )

        return len(self.list[stack_number - 1]) == 0

    def push(self, stack_number: int, element: Any) -> None:
        if self.is_stack_exceed(stack_number):
            raise ValueError(
                f"we have just {self.number_of_stacks} stacks in our list, but got {stack_number}"
            )

        self.list[stack_number - 1].append(element)

    def pop(self, stack_number: int) -> Any:
        if self.is_stack_exceed(stack_number):
            raise ValueError(
                f"we have just {self.number_of_stacks} stacks in our list, but got {stack_number}"
            )

        if self.size(stack_number) == 0:
            raise ValueError("stack is empty")

        return self.list[stack_number - 1].pop()

    def peek(self, stack_number: int) -> Any:
        if self.is_stack_exceed(stack_number):
            raise ValueError(
                f"we have just {self.number_of_stacks} stacks in our list, but got {stack_number}"
            )

        if self.size(stack_number) == 0:
            raise ValueError("stack is empty")

        return self.list[stack_number - 1][-1]


if __name__ == "__main__":
    stack = Stack(3)

    stack.push(1, 10)
    stack.push(1, 20)
    stack.push(2, 30)
    stack.push(3, 40)

    assert stack.peek(1) == 20
    assert stack.pop(3) == 40
    assert stack.size(1) == 2
