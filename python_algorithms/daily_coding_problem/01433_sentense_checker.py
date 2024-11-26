"""
Create a basic sentence checker that takes in a stream of characters and determines whether they 
form valid sentences. If a sentence is valid, the program should print it out.

We can consider a sentence valid if it conforms to the following rules:

The sentence must start with a capital letter, followed by a lowercase letter or a space.
All other characters must be lowercase letters, separators (,,;,:) or terminal marks (.,?,!,‽).
There must be a single space between each word.
The sentence must end with a terminal mark immediately following a word.
"""

import re


class SentenseChecker(object):
    def __init__(self) -> None:
        self.buffer = ""
        self.terminal_marks = {".", "?", "!", "!?"}
        self.separator_marks = {",", ";", ":"}

    def is_valid_sentence(self, sentence: str) -> bool:
        if not sentence: 
            return False

        if not sentence[0].isupper():
            return False

        if len(sentence) < 2 or sentence[-1] not in self.terminal_marks:
            return False

        if sentence[-2] == " ": 
            return False

        if not re.fullmatch(r"[A-Z][a-z ,;:]*[.?!‽]", sentence):
            return False

        return True

    def add_character(self, char: str):
        self.buffer += char
        if char in self.terminal_marks:
            if self.is_valid_sentence(self.buffer.strip()):
                print(f"valid sentence: {self.buffer.strip()}")
            else:
                print(f"in-valid sentence: {self.buffer.strip()}")

            self.buffer = ""

checker = SentenseChecker()
stream = "Hello, world! This is a test. Invalid sentence Without ending"

for char in stream:
    checker.add_character(char)

