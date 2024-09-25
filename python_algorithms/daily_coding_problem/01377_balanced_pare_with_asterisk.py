"""
You're given a string consisting solely of (, ), and *. * can represent either a (, ), or an empty string.
Determine whether the parentheses are balanced.

For example, (()* and (*) are balanced. )*( is not balanced.
"""


def check_valid_string(string: str) -> bool:
    low = 0  # min possible open parentheses count
    high = 0  # max possible open parentheses count

    for char in string:
        if char == "(":
            low += 1
            high += 1
        elif char == ")":
            low -= 1
            high -= 1
        else:
            low -= 1  # treated as )
            high += 1  # treated as (

        if high < 0:
            return False

        low = max(low, 0)

    return low == 0


assert check_valid_string("(()*") is True
assert check_valid_string("(*)") is True
assert check_valid_string(")*(") is False
