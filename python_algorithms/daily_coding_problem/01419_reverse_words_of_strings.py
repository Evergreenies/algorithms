"""
Given a string of words delimited by spaces, reverse the words in string. For example,
given "hello world here", return "here world hello"

Follow-up: given a mutable string representation, can you perform this operation in-place?
"""


def reverse(lst: list, start: int, end: int) -> list:
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1

    return lst


def reverse_string(string: str) -> str:
    length = len(string)
    lst = list(string)
    lst = reverse(lst, 0, length - 1)

    start = 0
    for index in range(0, length + 1):
        if index == length or lst[index] == " ":
            lst = reverse(lst, start, index - 1)
            start = index + 1

    return "".join(lst)


print(reverse_string("hello world here"))
