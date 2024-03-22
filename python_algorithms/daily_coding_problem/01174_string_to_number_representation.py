"""
Given a string, return whether it represents a number. Here are the different kinds of numbers:

"10", a positive integer
"-10", a negative integer
"10.1", a positive real number
"-10.1", a negative real number
"1e5", a number in scientific notation
And here are examples of non-numbers:

"a"
"x 1"
"a -2"
"-"
"""


def check_string_reresent_number(string: str) -> bool:
    try:
        eval(string)
        return True
    except Exception:
        return False


if __name__ == "__main__":
    assert check_string_reresent_number("10") is True
    assert check_string_reresent_number("-10") is True
    assert check_string_reresent_number("10.1") is True
    assert check_string_reresent_number("-10.1") is True
    assert check_string_reresent_number("1e5") is True
    assert check_string_reresent_number("a") is False
    assert check_string_reresent_number("x 1") is False
    assert check_string_reresent_number("a -2") is False
    assert check_string_reresent_number("-") is False
