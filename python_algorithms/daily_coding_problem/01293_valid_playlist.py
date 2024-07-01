"""
You are going on a road trip, and would like to create a suitable music playlist. The trip will require
N songs, though you only have M songs downloaded, where M < N. A valid playlist should select each song
at least once, and guarantee a buffer of B songs between repeats.

Given N, M, and B, determine the number of valid playlists.
"""


def valid_playlist(required_songs: int, available_songs: int, buffer: int) -> int:
    mod = 10**9 + 7
    dp = [[0] * (available_songs + 1) for _ in range(required_songs + 1)]
    dp[0][0] = 1

    for index_i in range(1, required_songs + 1):
        for index_j in range(1, available_songs + 1):
            dp[index_i][index_j] += (available_songs - (index_j - 1)) * dp[index_i - 1][
                index_j - 1
            ]
            dp[index_i][index_j] %= mod

            if index_j > buffer:
                dp[index_i][index_j] += (index_j - buffer) * dp[index_i - 1][index_j]
                dp[index_i][index_j] %= mod

    return dp[required_songs][available_songs]


print(valid_playlist(5, 3, 2))
