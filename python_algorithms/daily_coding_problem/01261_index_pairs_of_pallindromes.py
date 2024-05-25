"""
Given a list of words, find all pairs of unique indices such that the concatenation of the two words is a palindrome.

For example, given the list ["code", "edoc", "da", "d"], return [(0, 1), (1, 0), (2, 3)].
"""


def is_pallindrome(string: str) -> bool:
    return string == string[::-1]


def indices_pairs_of_pallindromes(arr: list[str]) -> list[tuple[int, int]]:
    indices = []
    for index1, word1 in enumerate(arr):
        for index2, word2 in enumerate(arr):
            if index1 != index2:
                if is_pallindrome(word1 + word2):
                    indices.append((index1, index2))

    return indices


if __name__ == "__main__":
    assert indices_pairs_of_pallindromes(["code", "edoc", "da", "d"]) == [
        (0, 1),
        (1, 0),
        (2, 3),
    ]
