"""
Given a 32-bit positive integer N, determine whether it is a power of four in faster than O(log N) time
"""


def is_power_of_four(n: int) -> bool:
    # check if bit representation has only one bit as `1`
    if n > 0 and (n & (n - 1)) == 0:
        # check if `1` bit is in odd position
        return (n & 0x55555555) != 0

    return False


assert is_power_of_four(16) is True
assert is_power_of_four(64) is True
assert is_power_of_four(256) is True
assert is_power_of_four(1024) is True
assert is_power_of_four(1022) is False
