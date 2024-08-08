"""
You are given given a list of rectangles represented by min and max x- and y-coordinates.
Compute whether or not a pair of rectangles overlap each other.
If one rectangle completely covers another, it is considered overlapping.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
},
{
    "top_left": (-1, 3),
    "dimensions": (2, 1)
},
{
    "top_left": (0, 5),
    "dimensions": (4, 3)
}

return true as the first and third rectangle overlap each other.
"""


def is_overlapped(rect1: dict, rect2: dict) -> bool:
    x1, y1 = rect1["top_left"]
    w1, h1 = rect1["dimensions"]

    x2, y2 = rect2["top_left"]
    w2, h2 = rect2["dimensions"]

    # check horizontal overlap
    if x2 > (x1 + w1) or x1 > (x2 + w2):
        return False

    # check for vertical overlap
    if y2 > (y1 + h1) or y1 > (y2 + h2):
        return False

    return True


def check_overlaps(rectangles: list[dict]) -> bool:
    length = len(rectangles)
    for index_i in range(length - 1):
        for index_j in range(index_i + 1, length):
            if is_overlapped(rectangles[index_i], rectangles[index_j]):
                return True

    return False


rectangles = [
    {"top_left": (1, 4), "dimensions": (3, 3)},
    {"top_left": (-1, 3), "dimensions": (2, 1)},
    {"top_left": (0, 5), "dimensions": (4, 3)},
]

print(check_overlaps(rectangles))
