"""
Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".
"""


def longest_pallindrom(string: str) -> str:
    length = len(string)
    dp = [[False for _ in range(length)] for _ in range(length)]

    for index in range(length):
        dp[index][index] = True

    max_length, start = 1, 0
    for index_i in range(1, length):
        for index_j in range(index_i - 1, -1, -1):
            if string[index_i] == string[index_j] and (
                index_i - index_j == 1 or dp[index_j + 1][index_i - 1]
            ):
                dp[index_j][index_i] = True

                if index_i - index_j + 1 > max_length:
                    max_length = index_i - index_j + 1
                    start = index_j

    return string[start : start + max_length]


if __name__ == "__main__":
    print(longest_pallindrom("aabcdcb"))
