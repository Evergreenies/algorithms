"""
Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].
"""


def bubble_sort(intervals: list[list | tuple]) -> list[list | tuple]:
    length = len(intervals)

    swapped = True
    while swapped:
        swapped = False
        for index in range(length - 1):
            if intervals[index][0] > intervals[index + 1][0]:
                intervals[index], intervals[index + 1] = (
                    intervals[index + 1],
                    intervals[index],
                )
                swapped = True

        if not swapped:
            break

    return intervals


def merge_intervals(intervals: list[list | tuple]) -> list[list | tuple]:
    intervals = bubble_sort(intervals)
    merged_intervals: list[list | tuple] = [intervals[0]]

    for start, end in intervals[1:]:
        if merged_intervals[-1][1] >= start:
            merged_intervals[-1] = (
                merged_intervals[-1][0],
                max(merged_intervals[-1][1], end),
            )
        else:
            merged_intervals.append((start, end))

    return merged_intervals


if __name__ == "__main__":
    assert merge_intervals([(1, 3), (5, 8), (4, 10), (20, 25)]) == [
        (1, 3),
        (4, 10),
        (20, 25),
    ]
