"""
Design and implement a HitCounter class that keeps track of requests (or hits). It should
support the following operations:

- record(timestamp): records a hit that happened at timestamp
- total(): returns the total number of hits recorded
- range(lower, upper): returns the number of hits that occurred between timestamps lower and
upper (inclusive)

Follow-up: What if our system has limited memory?
"""

from collections import deque


class HitCounter:
    def __init__(self) -> None:
        self.hits = deque()

    def record(self, timestamp: int) -> None:
        if self.hits and self.hits[-1][0] == timestamp:
            self.hits[-1] = (timestamp, self.hits[-1][1] + 1)
        else:
            self.hits.append((timestamp, 1))

    def total(self) -> int:
        return sum(count for _, count in self.hits)

    def range(self, lower: int, upper: int) -> int:
        _total = 0
        for timestamp, count in self.hits:
            if lower <= timestamp <= upper:
                _total += count

        return _total

    def clean(self, current_time: int, time_window: int) -> None:
        while self.hits and self.hits[0][0] < current_time - time_window:
            self.hits.popleft()


counter = HitCounter()
counter.record(1)
counter.record(2)
counter.record(2)
counter.record(5)

print(f"Total hits: {counter.total()}")
print(f"Hits between 1 and 3: {counter.range(1, 3)}")
print(f"Hits between 3 and 5: {counter.range(3, 5)}")

counter.clean(current_time=6, time_window=3)
print(f"Total hits after cloan-up: {counter.total()}")
