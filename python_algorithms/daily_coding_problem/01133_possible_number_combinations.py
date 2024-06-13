"""
Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible
letters the number could represent. You can assume each valid number in the mapping is a single digit.

For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23”
should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].
"""


def backetrack(
    index: int,
    path: list[str],
    combinations: list[str],
    digits_to_latters: dict,
    digits: str,
) -> None:
    if index == len(digits):
        combinations.append("".join(path))
        return

    possible_letters = digits_to_latters[digits[index]]

    for letter in possible_letters:
        path.append(letter)
        backetrack(index + 1, path, combinations, digits_to_latters, digits)
        path.pop()


def letter_combinations(digits: str, digits_to_latters: dict) -> list[str]:
    combinations = []

    if not digits:
        return combinations

    backetrack(0, [], combinations, digits_to_latters, digits)

    return combinations


if __name__ == "__main__":
    mapping = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }
    print(letter_combinations("23", mapping))
