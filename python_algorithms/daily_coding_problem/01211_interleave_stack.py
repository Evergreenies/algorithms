"""
Given a stack of N elements, interleave the first half of the stack with the 
second half reversed using only one other queue. This should be done in-place.

Recall that you can only push or pop from a stack, and enqueue or dequeue 
from a queue.

For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3]. 
If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].

Hint: Try working backwards from the end state.
"""


from collections import deque
from typing import Any


def interleaved_stack_buildin(stack: list[Any]) -> list[Any]:
    start, stop = 1, len(stack)
    queue = deque()

    while start != stop:
        while len(stack) > start:
            queue.append(stack.pop())

        while len(queue) > 0:
            stack.append(queue.popleft())

        start += 1

    return stack


if __name__ == "__main__":
    assert interleaved_stack_buildin([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
    assert interleaved_stack_buildin([1, 2, 3, 4]) == [1, 4, 2, 3]
