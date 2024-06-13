"""
Compute the running median of a sequence of numbers. That is, given a stream of numbers,
print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2
"""

import heapq


class RunningMedian:
    def __init__(self) -> None:
        self.lower = []  # max-heap
        self.upper = []  # mean-heap

    def add_number(self, num: int):
        # add to max heap
        heapq.heappush(self.lower, -num)

        # ensure evey element in max-heap is less than every element in min-heap
        if self.lower and self.upper and (-self.lower[0] > self.upper[0]):
            value = -heapq.heappop(self.lower)
            heapq.heappush(self.upper, value)

        # balance the heaps so that difference in sizez is at most 1
        if len(self.lower) > len(self.upper) + 1:
            value = -heapq.heappop(self.lower)
            heapq.heappush(self.upper, value)
        elif len(self.upper) > len(self.lower):
            value = heapq.heappop(self.upper)
            heapq.heappush(self.lower, -value)

    def get_median(self) -> float:
        if len(self.lower) > len(self.upper):
            return -self.lower[0]
        elif len(self.upper) > len(self.lower):
            return self.upper[0]
        else:
            return (-self.lower[0] + self.upper[0]) / 2.0


def running_median(arr: list[int]) -> None:
    rm = RunningMedian()

    for number in arr:
        rm.add_number(number)
        print(rm.get_median())


if __name__ == "__main__":
    running_median([2, 1, 5, 7, 2, 0, 5])
