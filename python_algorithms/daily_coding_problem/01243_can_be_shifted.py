"""
Given two strings A and B, return whether or not A can be shifted some number of times to get B.

For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.
"""


def can_be_shifted(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False

    return str2 in (str1 + str1)


if __name__ == "__main__":
    assert can_be_shifted("abcde", "cdeab") is True
    assert can_be_shifted("abc", "acb") is False
