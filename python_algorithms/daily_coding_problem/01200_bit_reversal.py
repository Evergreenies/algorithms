"""
Given a 32-bit integer, return the number with its bits reversed.

For example, given the binary number 
1111 0000 1111 0000 1111 0000 1111 0000, 
return 0000 1111 0000 1111 0000 1111 0000 1111.
"""


def reverse_bits(bits: int) -> int:
    return int("".join(reversed(format(bits, "b").zfill(32))), 2)


if __name__ == "__main__":
    assert (
        reverse_bits(0b11110000111100001111000011110000)
        == 0b00001111000011110000111100001111
    )
