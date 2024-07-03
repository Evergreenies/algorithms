"""
You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure
to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
"""


class OrderLog:
    def __init__(self, max_size: int) -> None:
        self.max_size = max_size
        self.data = [-1] * max_size
        self.head = 0

    def record(self, order_id: int) -> None:
        self.data[self.head] = order_id
        self.head = (self.head + 1) % self.max_size

    def get_last(self, index: int) -> int | None:
        if index >= self.max_size:
            return None

        idx = (self.head - 1 - index) % self.max_size
        return self.data[idx]


log = OrderLog(3)
log.record(1)
log.record(2)
log.record(3)
log.record(4)

print(log.get_last(0))
print(log.get_last(1))
