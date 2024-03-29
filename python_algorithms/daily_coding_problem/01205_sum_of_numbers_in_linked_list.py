"""
Let's represent an integer in a linked list format by having each node 
represent a digit in the number. The nodes make up the number in reversed order.

For example, the following linked list:

1 -> 2 -> 3 -> 4 -> 5
is the number 54321.

Given two linked lists in this format, return their sum in the same 
linked list format.

For example, given

9 -> 9
5 -> 2
return 124 (99 + 25) as:

4 -> 2 -> 1
"""
import math


class Stack:
    def __init__(self, capacity: int = 0) -> None:
        self.arr: list[int | None] = [None for _ in range(capacity)]
        self.top = -1
        self.capacity = capacity

    def is_empty(self) -> bool:
        return self.top == -1

    def is_full(self) -> bool:
        return (self.capacity - 1) == self.top

    def push(self, element: int) -> None:
        if self.is_full():
            raise Exception("stack is full")

        self.top += 1
        self.arr[self.top] = element

    def pop(self) -> int | None:
        if self.is_empty():
            raise Exception("stack is empty")

        top = self.arr[self.top]
        self.arr[self.top] = None
        self.top -= 1
        return top

    def size(self) -> int:
        return self.top + 1

    def darin(self) -> None:
        self.arr = []
        self.top = -1


def prepare_num(num: int | None, decimal: int) -> int:
    if num is None:
        return 0

    for _ in range(decimal):
        num *= 10

    return num


def get_number_from_linked_list(arr: list[int]) -> int:
    stack = Stack(len(arr))
    for integer in arr:
        stack.push(integer)

    _sum = 0
    while stack.size() - 1 >= 0:
        _sum += prepare_num(stack.pop(), stack.size())

    return _sum


def get_first_digit_with_reminder(number: int) -> tuple[int, int]:
    divisor = 10 ** (int(math.log10(number)))
    return number // divisor, number % divisor


def sum_of_two_linked_list(
    linked_list1: list[int], linked_list2: list[int]
) -> list[int]:
    _sum = get_number_from_linked_list(linked_list1) + get_number_from_linked_list(
        linked_list2
    )

    capacity = int(math.log10(_sum) + 1)
    stack = Stack(capacity)
    while _sum >= 0 and capacity > 0:
        digit, _sum = get_first_digit_with_reminder(_sum)
        capacity -= 1
        stack.push(digit)

    result = []
    while stack.size() > 0:
        result.append(stack.pop())

    return result


if __name__ == "__main__":
    stack = Stack(5)
    assert stack.is_empty() is True
    assert stack.top == -1
    stack.push(1)
    stack.push(2)
    assert stack.size() == 2
    assert stack.pop()
    assert stack.pop()
    assert stack.size() == 0
    assert stack.top == -1

    assert get_number_from_linked_list([1, 2, 3, 4, 5]) == 54321
    assert sum_of_two_linked_list([9, 9], [5, 2]) == [4, 2, 1]
