"""
You are in an infinite 2D grid where you can move in any of the 8 directions:

(x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)

You are given a sequence of points and the order in which you need to cover the points. Give the minimum
number of steps in which you can achieve it. You start from the first point.

Example:
Input: [(0, 0), (1, 1), (1, 2)]
Output: 2

It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).
"""


def steps_between(p1: tuple, p2: tuple) -> int:
    return max(abs(p2[0] - p1[0]), abs(p2[1] - p1[1]))


def min_steps(points: list[tuple]) -> int:
    total_steps = 0
    for index in range(1, len(points)):
        total_steps += steps_between(points[index - 1], points[index])

    return total_steps


if __name__ == "__main__":
    assert min_steps([(0, 0), (1, 1), (2, 2)]) == 2
