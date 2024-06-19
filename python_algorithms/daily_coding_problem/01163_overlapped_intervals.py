"""
Given a collection of intervals, find the minimum number of intervals you need to remove to make the
rest of the intervals non-overlapping.

Intervals can "touch", such as [0, 1] and [1, 2], but they won't be considered overlapping.

For example, given the intervals (7, 9), (2, 4), (5, 8), return 1 as the last interval can be removed
and the first two won't overlap.

The intervals are not necessarily sorted in any order.
"""


def erase_overlapped_intervals(intervals: list[tuple]) -> int:
    if not intervals:
        return 0

    intervals.sort(key=lambda x: x[1])
    non_overlapped_count = 0
    end_time = float("-inf")

    for interval in intervals:
        if interval[0] >= end_time:
            non_overlapped_count += 1
            end_time = interval[1]

    return len(intervals) - non_overlapped_count


assert erase_overlapped_intervals([(7, 9), (2, 4), (5, 8)]) == 1
