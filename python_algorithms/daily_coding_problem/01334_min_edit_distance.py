"""
The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions
required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three:
substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""


def edit_distance(str1: str, str2: str) -> int:
    len1, len2 = len(str1), len(str2)
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    # fill the first column
    for index in range(len1 + 1):
        dp[index][0] = index

    # fill the first row
    for index in range(len2 + 1):
        dp[0][index] = index

    for row in range(1, len1 + 1):
        for col in range(1, len2 + 1):
            if str1[row - 1] == str2[col - 1]:
                dp[row][col] = dp[row - 1][col - 1]
            else:
                dp[row][col] = 1 + min(
                    dp[row - 1][col],  # deletions
                    dp[row][col - 1],  # insertions
                    dp[row - 1][col - 1],  # substitutions
                )

    return dp[len1][len2]


print(edit_distance("kitten", "sitting"))
print(edit_distance("kitten", "setting"))
