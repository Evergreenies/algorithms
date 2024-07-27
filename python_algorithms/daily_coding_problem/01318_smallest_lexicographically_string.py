"""
You are given a string of length N and a parameter k. The string can be manipulated by taking
one of the first k letters and moving it to the end.

Write a program to determine the lexicographically smallest string that can be created after
an unlimited number of moves.

For example, suppose we are given the string daily and k = 1. The best we can create in this
case is ailyd.
"""


def smallest_lexicographically_string(string: str, k: int) -> str:
    k += 1
    while True:
        index = 0

        while index < k - 1 and string[index] <= string[index + 1]:
            index += 1

        if index == k - 1:
            break

        string = string[index + 1 :] + string[: index + 1]

    return string


print(smallest_lexicographically_string("daily", 1))
print(smallest_lexicographically_string("daily", 2))
