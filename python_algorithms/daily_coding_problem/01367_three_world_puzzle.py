"""
A cryptarithmetic puzzle is a mathematical game where the digits of some numbers are represented by letters.
Each letter represents a unique digit.

For example, a puzzle of the form:

  SEND
+ MORE
--------
 MONEY
may have the solution:

{'S': 9, 'E': 5, 'N': 6, 'D': 7, 'M': 1, 'O', 0, 'R': 8, 'Y': 2}
Given a three-word puzzle like the one above, create an algorithm that finds a solution.
"""

from itertools import permutations


# Helper function to convert a word to a number using a mapping of letter -> digit
def word_to_num(word, letter_to_digit):
    return int("".join(str(letter_to_digit[letter]) for letter in word))


def solve_cryptarithmetic(send, more, money):
    # Extract all unique letters from the words
    letters = set(send + more + money)

    # Ensure we only have unique letters
    if len(letters) > 10:
        raise ValueError("Too many unique letters for digits 0-9")

    # Create a list of all permutations of digits (0-9) for these letters
    letter_list = list(letters)

    # Try every permutation of digits for the letters
    for perm in permutations(range(10), len(letters)):
        # Create a mapping from letters to digits
        letter_to_digit = dict(zip(letter_list, perm))

        # Ensure that the leading letters are not zero
        if (
            letter_to_digit[send[0]] == 0
            or letter_to_digit[more[0]] == 0
            or letter_to_digit[money[0]] == 0
        ):
            continue

        # Convert the words to numbers based on the current letter->digit mapping
        send_value = word_to_num(send, letter_to_digit)
        more_value = word_to_num(more, letter_to_digit)
        money_value = word_to_num(money, letter_to_digit)

        # Check if the sum holds true
        if send_value + more_value == money_value:
            return letter_to_digit

    # If no solution is found, return None
    return None


# Example usage
send = "SEND"
more = "MORE"
money = "MONEY"
solution = solve_cryptarithmetic(send, more, money)

if solution:
    print("Solution found:", solution)
else:
    print("No solution exists")
