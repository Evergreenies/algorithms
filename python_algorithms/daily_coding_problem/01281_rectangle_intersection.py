"""
Given two rectangles on a 2D graph, return the area of their intersection. If the rectangles don't intersect, return 0.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}
and

{
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
}
return 6.
"""


def intersection_area(rect1: dict, rect2: dict) -> int:
    x1, y1 = rect1.get("top_left", ())
    w1, h1 = rect1.get("dimensions", ())
    x2, y2 = rect2.get("top_left", ())
    w2, h2 = rect2.get("dimensions", ())

    # determine bottom-right corners
    x1_br, y1_br = x1 + w1, y1 - h1
    x2_br, y2_br = x2 + w2, y2 - h2

    # calculate the coordinates of intersection rectangle
    left = max(x1, x2)
    right = min(x1_br, x2_br)
    top = min(y1, y2)
    bottom = max(y1_br, y2_br)

    width = right - left
    height = top - bottom

    if width <= 0 or height <= 0:
        return 0

    return width * height


rect1 = {
    "top_left": (1, 4),
    "dimensions": (3, 3),  # width, height
}
rect2 = {
    "top_left": (0, 5),
    "dimensions": (4, 3),  # width, height
}

assert intersection_area(rect1, rect2) == 6
