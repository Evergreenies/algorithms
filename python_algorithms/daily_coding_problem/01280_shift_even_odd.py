"""
Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and 2nd bit should be swapped,
the 3rd and 4th bit should be swapped, and so on.

For example, 10101010 should be 01010101. 11100010 should be 11010001.

Bonus: Can you do this in one line?
"""


def swap_even_odd_bits(digit):
    """
    The hexadecimal numbers 0xAA and 0x55 are used as bit masks to isolate the even and odd bits of an 8-bit integer.

    0xAA in binary is 10101010.
    0x55 in binary is 01010101.
    """
    return ((digit & 0xAA) >> 1) | ((digit & 0x55) << 1)


print(bin(swap_even_odd_bits(0b10101010)))
print(bin(swap_even_odd_bits(0b11100010)))
