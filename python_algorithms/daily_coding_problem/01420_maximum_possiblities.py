"""
Given a string s and an integer k, break up the string into multiple lines such that each line
has a length of k or less. You must break it up so that words don't break across lines. Each
line has to have the maximum possible amount of words. If there's no way to break the text up,
then return null.

You can assume that there are no spaces at the ends of the string and that there is exactly one
space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should
return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a
length of more than 10.
"""


def split_string(string: str, length: int) -> list:
    lines, arr = [], string.split()

    current_line = arr[0]
    for word in arr[1:]:
        if len(current_line) + 1 + len(word) <= length:
            current_line += " " + word
        else:
            lines.append(current_line)
            current_line = word

    lines.append(current_line)

    return lines


print(split_string("the quick brown fox jumps over the lazy dog", 10))
