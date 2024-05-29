"""
Given a dictionary of words and a string made up of those words (no spaces), return the original 
sentence in a list. If there is more than one possible reconstruction, return any of them. If 
there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", 
you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", 
return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""


def word_break(word_dict: set, string: str) -> list:
    dp = [False for _ in range(len(string) + 1)]
    dp[0] = True
    results = []

    for index_i in range(1, len(string) + 1):
        for index_j in range(index_i):
            if string[index_j:index_i] in word_dict and dp[index_j]:
                dp[index_i] = True
                results.append(string[index_j:index_i])

    return results


if __name__ == "__main__":
    word_dict = set(["bed", "bath", "bedbath", "and", "beyond"])
    s = "bedbathandbeyond"

    assert word_break(word_dict, s) == ["bed", "bedbath", "bath", "and", "beyond"]
