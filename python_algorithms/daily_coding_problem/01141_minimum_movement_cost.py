"""
There are M people sitting in a row of N seats, where M < N. Your task is to redistribute people such that
there are no gaps between any of them, while keeping overall movement to a minimum.

For example, suppose you are faced with an input of [0, 1, 1, 0, 1, 0, 0, 0, 1], where 0 represents an empty
seat and 1 represents a person. In this case, one solution would be to place the person on the right in the
fourth seat. We can consider the cost of a solution to be the sum of the absolute distance each person must
move, so that the cost here would be five.

Given an input such as the one above, return the lowest possible cost of moving people to remove all gaps.
"""


def minimum_movement_cost(arr: list[int]) -> int:
    positions = [index for index, seat in enumerate(arr) if seat == 1]
    length = len(positions)

    median_index = length // 2
    median_position = positions[median_index]
    target_position = list(
        range(median_position - median_index, median_position - median_index + length)
    )

    return sum(abs(p - t) for p, t in zip(positions, target_position))


if __name__ == "__main__":
    assert minimum_movement_cost([0, 1, 1, 0, 1, 0, 0, 0, 1]) == 5
