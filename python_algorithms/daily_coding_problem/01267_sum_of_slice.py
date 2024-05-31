"""
Given a list of numbers L, implement a method sum(i, j) which returns the sum from the sublist L[i:j] (including i, excluding j).

For example, given L = [1, 2, 3, 4, 5], sum(1, 3) should return sum([2, 3]), which is 5.

You can assume that you can do some pre-processing. sum() should be optimized over the pre-processing step.
"""


class SumOfSlice:
    def __init__(self, arr: list[int]) -> None:
        self.accumulated_sum = [0 for _ in range(len(arr) + 1)]

        for index in range(len(arr)):
            self.accumulated_sum[index + 1] = self.accumulated_sum[index] + arr[index]

    def sum(self, start: int, end: int) -> int:
        return self.accumulated_sum[end] - self.accumulated_sum[start]


def sum_of_slice(arr: list[int], start: int, end: int) -> int:
    _sum = 0
    for index in range(start, end):
        _sum += arr[index]

    return _sum


if __name__ == "__main__":
    assert sum_of_slice([1, 2, 3, 4, 5], 1, 3) == 5

    acc_sum = SumOfSlice([1, 2, 3, 4, 5])
    assert acc_sum.sum(1, 3) == 5
