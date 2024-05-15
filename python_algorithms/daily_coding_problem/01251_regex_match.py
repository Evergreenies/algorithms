"""
Implement regular expression matching with the following special characters:

. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular expression and returns whether 
or not the string matches the regular expression.

For example, given the regular expression "ra." and the string "ray", your function should return true. 
The same regular expression on the string "raymond" should return false.

Given the regular expression ".*at" and the string "chat", your function should return true. The same 
regular expression on the string "chats" should return false.
"""


def match(text: str, pattern: str) -> bool:
    i, j = 0, 0
    while i < len(text):
        if (j < len(pattern)) and (pattern[j] == text[i] or pattern[j] == "."):
            i += 1
            j += 1
        elif (j < len(pattern)) and (pattern[j] == "*"):
            matching_char = text[i] if i < len(text) else None
            while (i < len(text)) and (
                text[i] == matching_char or matching_char is None
            ):
                i += 1

            j += 1
        elif (j == len(pattern)) or (i < len(text) and pattern[j] != text[i]):
            if (j > 0) and (pattern[j - 1] == "*"):
                j -= 2
            else:
                return False

    return (i == len(text)) and (j == len(pattern))


if __name__ == "__main__":
    # Example usage
    text1 = "ray"
    pattern1 = "ra."
    print(match(text1, pattern1))  # Output: True

    text2 = "raymond"
    pattern2 = "ra."
    print(match(text2, pattern2))  # Output: False

    text3 = "chat"
    pattern3 = ".*at"
    print(match(text3, pattern3))  # Output: True

    text4 = "chats"
    pattern4 = ".*at"
    print(match(text4, pattern4))  # Output: False
