"""
Given a word W and a string S, find all starting indices in S which are anagrams of W.

For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.
"""


def find_anagram_indices(W: str, S: str) -> list[int]:
    w_chars = set(W)
    result, length = [], len(W)

    for index in range(len(S)):
        s_char = set(S[index : index + length])
        if s_char == w_chars:
            result.append(index)

    return result


if __name__ == "__main__":
    print(find_anagram_indices("ab", "abxaba"))
