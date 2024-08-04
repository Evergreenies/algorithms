"""
Implement a queue using a set of fixed-length arrays.

The queue should support enqueue, dequeue, and get_size operations.
"""

from typing import Any


class FixedArrayQueue:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.arr = [None] * capacity
        self.size = 0
        self.head, self.tail = 0, -1

    def get_size(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size == self.capacity

    def enqueue(self, item: Any) -> None:
        if self.is_full():
            raise Exception("queue is full")

        self.tail = (self.tail + 1) % self.capacity
        self.arr[self.tail] = item
        self.size += 1

    def dequeue(self) -> Any:
        if self.is_empty():
            raise Exception("queue is empty")

        item = self.arr[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1

        return item


queue = FixedArrayQueue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Output: 1
print(queue.get_size())  # Output: 2
queue.enqueue(4)
queue.enqueue(5)
print(queue.dequeue())  # Output: 2
print(queue.dequeue())  # Output: 3
