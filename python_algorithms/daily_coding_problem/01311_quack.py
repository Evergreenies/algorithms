"""
A quack is a data structure combining properties of both stacks and queues. It can be viewed as a list
of elements written left to right such that three operations are possible:

push(x): add a new item x to the left end of the list
pop(): remove and return the item on the left end of the list
pull(): remove the item on the right end of the list.

Implement a quack using three stacks and O(1) additional memory, so that the amortized time for any
push, pop, or pull operation is O(1).
"""


class Quack:
    def __init__(self) -> None:
        self.stack1 = []
        self.stack2 = []
        self.stack3 = []

    def push(self, item):
        self.stack1.append(item)

    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop() if self.stack2 else None

    def pull(self):
        if not self.stack1:
            while self.stack2:
                self.stack1.append(self.stack2.pop())

        return self.stack1.pop() if self.stack1 else None


quack = Quack()
quack.push(1)
quack.push(2)
quack.push(3)
print(quack.pop())  # Output: 3 (left end of the list)
print(quack.pull())  # Output: 1 (right end of the list)
quack.push(4)
print(quack.pop())  # Output: 2 (left end of the list)
print(quack.pop())
