"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""


def num_decoding(string: str) -> int:
    if not string or string[0] == "0":
        return 0

    length = len(string)
    dp = [0] * (length + 1)
    dp[0] = 1
    dp[1] = 1

    for index in range(2, length + 1):
        if 1 <= int(string[index - 1 : index]) <= 9:
            dp[index] += dp[index - 1]

        if 10 <= int(string[index - 2 : index]) <= 26:
            dp[index] += dp[index - 2]

    return dp[length]


print(num_decoding("111"))
print(num_decoding("0111"))
