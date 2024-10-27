"""
Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure
with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.
"""

from typing import Any


class QueueUsingStacks:
    def __init__(self) -> None:
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, item: Any) -> None:
        self.stack_in.append(item)

    def dequeue(self) -> Any:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        if not self.stack_out:
            raise IndexError("cant dequeue from emty queue")

        return self.stack_out.pop()

    def is_empty(self) -> bool:
        return not self.stack_out and not self.stack_in

    def peek(self) -> Any:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        if not self.stack_out:
            raise IndexError("cont dequeue from empty queue")

        return self.stack_out[-1]


queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Output: 1
print(queue.peek())  # Output: 2
print(queue.dequeue())  # Output: 2
print(queue.is_empty())  # Output: False
print(queue.dequeue())  # Output: 3
print(queue.is_empty())  # Output: True
