"""
You are given a string consisting of the letters x and y, such as xyxxxyxyy. In addition, 
you have an operation called flip, which changes a single x to y or vice versa.

Determine how many times you would need to apply this operation to ensure that all x's come 
before all y's. In the preceding example, it suffices to flip the second and sixth characters, 
so you should return 2.
"""


def min_flips(string: str) -> int:
    length = len(string)
    left, right = [0 for _ in range(length)], [0 for _ in range(length)]

    left[0] = 0
    right[-1] = 0

    for index in range(1, length):
        left[index] = left[index - 1] + (1 if string[index - 1] == "y" else 0)

    index = length - 2
    while index >= 0:
        right[index] = right[index + 1] + (1 if string[index + 1] == "x" else 0)
        index -= 1

    result = length
    for idx in range(length):
        result = min(result, left[idx] + right[idx])

    return result


if __name__ == "__main__":
    assert min_flips("xyxxxyxyy") == 2
