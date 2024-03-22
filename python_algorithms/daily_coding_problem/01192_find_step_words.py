"""
A step word is formed by taking a given word, adding a letter, and anagramming 
the result. For example, starting with the word "APPLE", you can add an "A" 
and anagram to get "APPEAL".

Given a dictionary of words and an input word, create a function that returns 
all valid step words.
"""
import string


# TODO: incomplete solution
def find_step_words(word: str, dictionary: set | list) -> list[str]:
    if not word:
        return []

    step_words = []
    for wrd in dictionary:
        if len(word) - len(wrd) != 1:
            continue

        word_freq = letter_frequency(word)
        curr_freq = letter_frequency(wrd)
        difference = 0

        for char in word_freq.keys():
            difference += abs(word_freq[char] - curr_freq[char])

        if difference == 1:
            step_words.append(wrd)

    return step_words


def letter_frequency(word: str) -> dict[str, int]:
    letter_freq = {char: 0 for char in string.ascii_lowercase}
    for char in word:
        letter_freq[char] += 1

    return letter_freq


if __name__ == "__main__":
    print(find_step_words("appeal", ["apple", "pear", "lemon", "paple"]))
