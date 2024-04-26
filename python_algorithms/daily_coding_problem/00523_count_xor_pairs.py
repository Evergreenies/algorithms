"""
Given intergers M and N, write a program that counts how many positive interger pairs (a, b) satisfy following conditions:

a + b = M
a XOR b = N
"""


def count_xor_pairs(m: int, n: int) -> int:
    count = 0
    for index in range(1, m):
        if (index ^ (m - index)) == n:
            count += 1

    return count


if __name__ == "__main__":
    assert count_xor_pairs(100, 4) == 2
    assert count_xor_pairs(5, 2) == 0
