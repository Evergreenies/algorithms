"""
You are given a string formed by concatenating several words corresponding to the integers
zero through nine and then anagramming.

For example, the input could be 'niesevehrtfeev', which is an anagram of 'threefiveseven'.
Note that there can be multiple instances of each integer.

Given this string, return the original integers in sorted order. In the example above,
this would be 357.
"""

from collections import Counter


def original_integers_from_anagram(string: str) -> str:
    count = Counter(string)

    out = [0] * 10

    # identify and assign unique charecter of each digit and assign to respective position
    out[0] = count["z"]
    out[2] = count["w"]
    out[4] = count["u"]
    out[6] = count["x"]
    out[8] = count["g"]

    out[3] = count["h"] - out[8]
    out[5] = count["f"] - out[4]
    out[7] = count["s"] - out[6]
    out[1] = count["o"] - out[0] - out[2] - out[4]
    out[9] = count["i"] - out[5] - out[6] - out[8]

    result = []
    for index in range(10):
        result.extend([str(index)] * out[index])

    return "".join(result)


assert original_integers_from_anagram("niesevehrtfeev") == "357"
assert original_integers_from_anagram("owoztneoer") == "012"
