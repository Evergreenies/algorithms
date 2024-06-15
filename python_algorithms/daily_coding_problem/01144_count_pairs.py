"""
Given integers M and N, write a program that counts how many positive integer pairs (a, b) satisfy the following conditions:

a + b = M
a XOR b = N
"""


def count_pairs(m, n):
    if m < n or (m - n) % 2 != 0:
        return 0

    a_and_b = (m - n) // 2
    count = 0

    for a in range(1, m):
        b = m - a
        if a > b:
            break

        if a ^ b == n and (a & b) == a_and_b:
            count += 1

    return count


M = 10
N = 4
print(f"The number of pairs (a, b) for M={M} and N={N} is: {count_pairs(M, N)}")
