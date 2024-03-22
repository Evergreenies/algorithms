"""
Given a list of points, a central point, and an integer k, find the nearest 
k points from the central point.

For example, given the list of points [(0, 0), (5, 4), (3, 1)], the central 
point (1, 2), and k = 2, return [(0, 0), (3, 1)].
"""

import math


def euclidian_distance(point1: tuple, point2: tuple) -> float:
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def nearest_k_points(points: list[tuple], central_point: tuple, k: int) -> list[tuple]:
    distance = [(euclidian_distance(point, central_point), point) for point in points]
    distance.sort()

    return [point for _, point in distance[:k]]


if __name__ == "__main__":
    points = [(0, 0), (5, 4), (3, 1), (1, 6), (2, 7)]
    central_point = (1, 2)
    k = 3
    assert nearest_k_points(points, central_point, k) == [(0, 0), (3, 1), (1, 6)]
    assert nearest_k_points([(0, 0), (5, 4), (3, 1)], central_point, 2) == [
        (0, 0),
        (3, 1),
    ]
