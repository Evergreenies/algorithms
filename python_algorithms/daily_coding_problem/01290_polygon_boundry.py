"""
You are given a list of N points (x1, y1), (x2, y2), ..., (xN, yN) representing a polygon. You can assume these points
are given in order; that is, you can construct the polygon by connecting point 1 to point 2, point 2 to point 3, and so
on, finally looping around to connect point N to point 1.

Determine if a new point p lies inside this polygon. (If p is on the boundary of the polygon, you should return False).
"""


def is_point_inside_polygon(polygon: list[tuple], point: tuple) -> bool:
    count = 0
    for index in range(len(polygon)):
        next_index = (index + 1) % len(polygon)

        p1x, p1y = polygon[index]
        p2x, p2y = polygon[next_index]

        if (p1y <= point[1] < p2y or p2y <= point[1] < p1y) and (
            point[0] < (p2x - p1x) * (point[1] - p1y) / (p2y - p1y) + p1x
        ):
            count += 1

    return count % 2 != 0


polygon = [(1, 1), (5, 1), (5, 4), (1, 4)]
point1 = (2, 2)
point2 = (4, 3)
point3 = (5, 1)

print(is_point_inside_polygon(polygon, point1))
print(is_point_inside_polygon(polygon, point2))
print(is_point_inside_polygon(polygon, point3))
