"""
A strobogrammatic number is a positive number that appears the same after 
being rotated 180 degrees. For example, 16891 is strobogrammatic.

Create a program that finds all strobogrammatic numbers with N digits.
"""

from typing import Iterator


STROBO_MAP = {"0": "0", "1": "1", "8": "8", "6": "9", "9": "6"}


def is_strobogrammatic_number(num: str) -> bool:
    if len(num) == 1:
        return num in ["0", "1", "8"]
    else:
        start, end = 0, len(num) - 1
        while start <= end:
            if num[start] in STROBO_MAP and STROBO_MAP[num[start]] == num[end]:
                start += 1
                end -= 1
            else:
                return False

        return True


def find_strobogrammatic_in_range(digit: int) -> Iterator:
    if digit == 0:
        return []

    start = 10 ** (digit - 1)
    end = (10**digit) - 1

    while start <= end:
        if is_strobogrammatic_number(str(start)):
            yield start
        start += 1


def collect_strabogrammatics(digit: int) -> list:
    refined_stobogrammatic = []
    for number in find_strobogrammatic_in_range(digit):
        refined_stobogrammatic.append(number)

    return refined_stobogrammatic


if __name__ == "__main__":
    assert is_strobogrammatic_number("16891") is True
    assert is_strobogrammatic_number("1689") is False
    assert collect_strabogrammatics(3) == [
        101,
        111,
        181,
        609,
        619,
        689,
        808,
        818,
        888,
        906,
        916,
        986,
    ]
    assert collect_strabogrammatics(2) == [11, 69, 88, 96]
