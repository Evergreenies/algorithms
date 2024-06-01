"""
Given three 32-bit integers x, y, and b, return x if b is 1 and y if b is 0, using only mathematical or bit operations. 
You can assume b can only be 1 or 0.
"""


def select_from_math(x: int, y: int, b: int) -> int:
    multi = (x - y) * b
    return y + multi


if __name__ == "__main__":
    assert select_from_math(5, 10, 0) == 10
    assert select_from_math(5, 10, 1) == 5
    assert select_from_math(5, 9, 1) == 5
    assert select_from_math(9, 5, 1) == 9
