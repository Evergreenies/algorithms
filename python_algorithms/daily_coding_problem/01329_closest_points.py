"""
Given a set of points (x, y) on a 2D cartesian plane, find the two closest points.

For example, given the points [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)],
return [(-1, -1), (1, 1)].
"""

import math


def distance(p1: tuple[int, int], p2: tuple[int, int]) -> float:
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def closest_pair(strip: list[tuple], dist: float) -> tuple[tuple, float]:
    min_dist, closest_pr = dist, tuple()

    strip.sort(key=lambda p: p[1])
    for index_i in range(len(strip)):
        for index_j in range(index_i + 1, len(strip)):
            if (strip[index_j][1] - strip[index_i][1]) >= min_dist:
                break

            dist = distance(strip[index_i], strip[index_j])
            if dist < min_dist:
                min_dist = dist
                closest_pr = (strip[index_i], strip[index_j])

    return closest_pr, min_dist


def closest_pairs_recursive(points: list) -> tuple[tuple, float]:
    length = len(points)
    min_dist, closest_pr = float("inf"), tuple()

    if length <= 3:
        for index_i in range(length):
            for index_j in range(index_i + 1, length):
                dist = distance(points[index_i], points[index_j])

                if dist < min_dist:
                    min_dist = dist
                    closest_pr = (points[index_i], points[index_j])

        return closest_pr, min_dist

    middle = length // 2
    middle_point = points[middle]

    left_pair, left_dist = closest_pairs_recursive(points[:middle])
    right_pair, right_dist = closest_pairs_recursive(points[middle:])

    if left_dist < right_dist:
        dist = left_dist
        min_pair = left_pair
    else:
        dist = right_dist
        min_pair = right_pair

    strip = [p for p in points if abs(p[0] - middle_point[0]) < dist]
    strip_pair, strip_dist = closest_pair(strip, dist)

    if strip_dist < dist:
        return strip_pair, strip_dist

    return min_pair, dist


def closest_pairs(points: list[tuple[int, int]]) -> tuple | list:
    if len(points) < 2:
        return points

    points.sort(key=lambda p: p[0])
    return closest_pairs_recursive(points)[0]


print(closest_pairs([(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)]))
