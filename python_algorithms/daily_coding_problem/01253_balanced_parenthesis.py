"""
Given a string of round, curly, and square open and closing brackets, return whether the 
brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""


def is_balanced(string: str) -> bool:
    stack = []
    opening_barckets = {"(": ")", "{": "}", "[": "]"}
    closing_brackets = set(opening_barckets.values())

    for char in string:
        if char in opening_barckets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or opening_barckets[stack.pop()] != char:
                return False

    return not stack


if __name__ == "__main__":
    assert is_balanced("[](){}([])") is True
    assert is_balanced("{)") is False
