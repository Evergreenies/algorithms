"""
Determine whether there exists a one-to-one character mapping from one string s1 to another s2.

For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.

Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.
"""


def char_mapping(string1: str, string2: str) -> bool:
    if len(string1) != len(string2):
        return False

    s1_to_s2, s2_to_s1 = {}, {}
    for char1, char2 in zip(string1, string2):
        if char1 in s1_to_s2:
            if s1_to_s2[char1] != char2:
                return False
        else:
            s1_to_s2[char1] = char2

        if char2 in s2_to_s1:
            if s2_to_s1[char2] != char1:
                return False
        else:
            s2_to_s1[char2] = char1

    return True


assert char_mapping("abc", "bcd") is True
assert char_mapping("foo", "bar") is False
