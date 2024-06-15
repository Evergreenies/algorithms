"""
Let's define a "sevenish" number to be one which is either a power of 7, or the sum of unique powers of 7.
The first few sevenish numbers are 1, 7, 8, 49, and so on. Create an algorithm to find the nth sevenish number.
"""


def nth_sevenish_number(nth: int) -> int:
    result, power = 0, 0

    while nth > 0:
        if nth & 1:
            result += 7**power

        nth >>= 1  # right shift to process next bit
        power += 1

    return result


if __name__ == "__main__":
    assert nth_sevenish_number(5) == 50
