"""
Write an algorithm that finds the total number of set bits in all integers between 1 and N.
"""


def count_set_bits(n: int) -> int:
    total_set_bits = 0
    for num in range(1, n + 1):
        count = 0
        # Brian Kerninghans algorithm
        while num:
            count += num & 1
            num >>= 1

        total_set_bits += count

    return total_set_bits


if __name__ == "__main__":
    assert count_set_bits(5) == 7
    assert count_set_bits(0) == 0
    assert count_set_bits(7) == 12
