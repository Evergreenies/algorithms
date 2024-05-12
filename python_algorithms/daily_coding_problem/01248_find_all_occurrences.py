"""
Given a string s and a list of words words, where each word is the same length, find all starting 
indices of substrings in s that is a concatenation of every word in words exactly once.

For example, given s = "dogcatcatcodecatdog" and words = ["cat", "dog"], return [0, 13], 
since "dogcat" starts at index 0 and "catdog" starts at index 13.

Given s = "barfoobazbitbyte" and words = ["dog", "cat"], return [] since there are no substrings 
composed of "dog" and "cat" in s.

The order of the indices does not matter.
"""

from collections import defaultdict


def find_all_concatinations(strings: str, words: list[str]) -> list[int]:
    word_length, all_indices, word_dict = len(words[0]), [], defaultdict(int)

    for word in words:
        word_dict[word] += 1

    for index in range(len(strings) - word_length * len(words) + 1):
        current_window = strings[index : index + word_length * len(words)]
        window_words = [
            current_window[j : j + word_length]
            for j in range(0, len(current_window), word_length)
        ]

        if all(word in word_dict and word_dict[word] > 0 for word in window_words):
            for word in window_words:
                word_dict[word] -= 1

            all_indices.append(index)
            for word in window_words:
                word_dict[word] += 1

    return all_indices


if __name__ == "__main__":
    # Example usage
    s = "dogcatcatcodecatdog"
    words = ["cat", "dog"]
    indices = find_all_concatinations(s, words)
    print(indices)  # Output: [0, 13]

    s = "barfoobazbitbyte"
    words = ["dog", "cat"]
    indices = find_all_concatinations(s, words)
    print(indices)  # Output: []
