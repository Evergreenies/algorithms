"""
Given a string, split it into as few strings as possible such that each string is a palindrome.

For example, given the input string racecarannakayak, return ["racecar", "anna", "kayak"].

Given the input string abc, return ["a", "b", "c"].
"""

from typing import Any


def is_pallindrome(string: str) -> bool:
    return string == string[::-1]


def min_pallindrome_partition(string: str) -> list[Any]:
    result = []
    while len(string) != 0:
        if is_pallindrome(string):
            result.append(string)
            string = ""

            return result
        else:
            index = -1
            while not is_pallindrome(string[:index]):
                index -= 1

            result.append(string[:index])
            string = string[index:]

    return result


print(min_pallindrome_partition("racecarannakayak"))
print(min_pallindrome_partition("abc"))
