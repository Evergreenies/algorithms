"""
Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.

For example, given 156, you should return 3.
"""


def longest_consecutive_ones(n):
    # Convert n to its binary representation and remove the '0b' prefix
    binary_representation = bin(n)[2:]

    # Split the binary representation by '0' to find sequences of '1's
    ones_sequences = binary_representation.split("0")

    # Find the length of the longest sequence of '1's
    longest_run = max(len(seq) for seq in ones_sequences)

    return longest_run


# Example usage:
n = 156
print(longest_consecutive_ones(n))  # Output should be 3
