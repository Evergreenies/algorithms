"""
Given an integer n, find the next biggest integer with the same number of 1-bits on.
For example, given the number 6 (0110 in binary), return 9 (1001).
"""


def next_biggest_with_same_bits(n):
    # Step 1: Identify the rightmost '0' with '1' to its right
    c = n
    c0 = c1 = 0

    # Count the number of trailing zeros (c0) and ones (c1) in n
    while ((c & 1) == 0) and (c != 0):
        c0 += 1
        c >>= 1

    while (c & 1) == 1:
        c1 += 1
        c >>= 1

    # If there are no zeros to the right of the ones, there is no bigger number with same number of 1-bits
    if c0 + c1 == 31 or c0 + c1 == 0:
        return -1

    # Position of rightmost non-trailing zero (rightmost '0' with '1' to its right)
    p = c0 + c1

    # Step 2: Swap this '0' with the '1'
    n |= 1 << p  # Flip the zero at position p
    n &= ~((1 << p) - 1)  # Clear all bits to the right of p
    n |= (1 << (c1 - 1)) - 1  # Insert (c1-1) ones on the right

    return n


print(next_biggest_with_same_bits(6))
print(next_biggest_with_same_bits(8))
