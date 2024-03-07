"""
Here's a clear and concise problem statement for checking if two strings are anagrams:

**Problem:**
Given two strings, S1 and S2, determine if S2 is an anagram of S1. An anagram is a word 
or phrase formed by rearranging the letters of another word or phrase.

**Example:**
- S1 = "silent" and S2 = "listen" are anagrams because you can rearrange the letters 
  in "silent" to form "listen".
- S1 = "cinema" and S2 = "iceman" are anagrams.
- S1 = "bottle" and S2 = "bobble" are not anagrams.

**Constraints:**
- Strings can contain only lowercase letters (a-z).
"""

from collections import defaultdict


def counter(string: str) -> dict:
    _dict = defaultdict(int)
    for character in string:
        _dict[character] += 1

    return _dict


def is_anagram(string1: str, string2: str) -> bool:
    return counter(string1) == counter(string2)


if __name__ == "__main__":
    test_case = [
        ("paper", "reapa", False),
        ("restful", "fluster", True),
        ("cats", "tocs", False),
        ("monkeyswrite", "newyorktimes", True),
        ("elbow", "below", True),
        ("tax", "taxi", False),
        ("taxi", "tax", False),
        ("night", "thing", True),
        ("abbc", "aabc", False),
        ("po", "popp", False),
        ("pp", "oo", False),
    ]

    def test_anagrams():
        for item in test_case:
            assert is_anagram(item[0], item[1]) == item[2]
