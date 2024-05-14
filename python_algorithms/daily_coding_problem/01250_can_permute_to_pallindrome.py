"""
Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form racecar, 
which is a palindrome. daily should return false, since there's no rearrangement that 
can form a palindrome.
"""

from collections import defaultdict


def can_premute_pallindrome(string: str) -> bool:
    char_count = defaultdict(int)
    for char in string:
        char_count[char] += 1

    odd_count = 0
    for count in char_count.values():
        odd_count += count % 2

    return odd_count <= 1


if __name__ == "__main__":
    assert can_premute_pallindrome("carrace") is True
    assert can_premute_pallindrome("daily") is False
