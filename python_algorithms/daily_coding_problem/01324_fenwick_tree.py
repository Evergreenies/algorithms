"""
You are given an array of length 24, where each element represents the number of new subscribers
during the corresponding hour. Implement a data structure that efficiently supports the following:

update(hour: int, value: int): Increment the element at index hour by value.
query(start: int, end: int): Retrieve the number of subscribers that have signed up between start
and end (inclusive).
You can assume that all values get cleared at the end of the day, and that you will not be asked
for start and end values that wrap around midnight.
"""


class FenwickTree:
    def __init__(self, size: int) -> None:
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index: int, delta: int):
        index += 1
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def prefix_sum(self, index: int) -> int | float:
        index += 1
        result = 0

        while index > 0:
            result += self.tree[index]
            index -= index & -index

        return result

    def range_sum(self, start: int, end: int) -> int | float:
        return self.prefix_sum(end) - self.prefix_sum(start - 1)


class SubscriberCounter:
    def __init__(self):
        self.fenwick_tree = FenwickTree(24)
        self.subscribers = [0] * 24

    def update(self, hour: int, value: int) -> None:
        self.subscribers[hour] += value
        self.fenwick_tree.update(hour, value)

    def query(self, start: int, end: int) -> int | float:
        return self.fenwick_tree.range_sum(start, end)


counter = SubscriberCounter()
counter.update(5, 10)
counter.update(5, 5)
counter.update(10, 20)
print(counter.query(5, 10))
print(counter.query(0, 23))
