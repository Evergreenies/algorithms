"""
One way to unlock an Android phone is through a pattern of swipes across a 1-9 keypad.

For a pattern to be valid, it must satisfy the following:

All of its keys must be distinct.
It must not connect two keys by jumping over a third key, unless that key has already been used.
For example, 4 - 2 - 1 - 7 is a valid pattern, whereas 2 - 1 - 7 is not.

Find the total number of valid unlock patterns of length N, where 1 <= N <= 9.
"""


def is_valid_move(used: list, current: int, nxt: int, jump: list) -> bool:
    if used[nxt]:
        return False

    if jump[current][nxt] == 0:
        return True

    return used[jump[current][nxt]]


def total_patterns(n: int) -> int:
    jump = [[0] * 10 for _ in range(10)]

    jump[1][3] = jump[3][1] = 2
    jump[1][7] = jump[7][1] = 4
    jump[3][9] = jump[9][3] = 6
    jump[7][9] = jump[9][7] = 8

    jump[1][9] = jump[9][1] = jump[3][7] = jump[7][3] = 5
    jump[2][8] = jump[8][2] = jump[4][6] = jump[6][4] = 5

    total_patterns_count = 0
    used = [False] * 10

    for length in range(1, n + 1):
        total_patterns_count += dfs(1, 1, used, jump, length) * 4
        total_patterns_count += dfs(2, 1, used, jump, length) * 4
        total_patterns_count += dfs(5, 1, used, jump, length)

    return total_patterns_count


def dfs(current: int, length: int, used: list, jump: list, n: int) -> int:
    if length == n:
        return 1

    used[current] = True
    total_patterns_count = 0

    for nxt in range(1, 10):
        if is_valid_move(used, current, nxt, jump):
            total_patterns_count += dfs(nxt, length + 1, used, jump, n)

    used[current] = False
    return total_patterns_count


print(total_patterns(4))
