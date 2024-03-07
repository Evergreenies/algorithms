"""
**Problem:**
Given a string `s`, design a function that compresses the string by **replacing consecutive occurrences of characters** with a single character followed by the count of those occurrences.

**Rules:**
- The compressed string should only contain characters and their corresponding counts. 
- The count should be represented using digits (0-9).
- If a character appears only once, it should remain the same in the compressed string without a count.

**Example:**
- Input: `ssssbbz`
- Output: `4s2bz` (Explanation: "4" represents four 's', "2" represents two 'b')

**Constraints:**
- The input string `s` consists of lowercase English letters only (a-z).
- The compressed string length should be less than or equal to the original string length.
"""


def compress(string: str) -> str:
    string = f"{string} "
    result, length = "", len(string)
    start, end = 0, 0

    while end < length:
        if string[start] == string[end]:
            end += 1
        else:
            sequence_length = end - start
            if sequence_length == 1:
                result = f"{result}{string[start]}"
            else:
                result = f"{result}{sequence_length}{string[start]}"

            start = end

    return result


if __name__ == "__main__":
    assert compress("") == ""
    assert compress("a") == "a"
    assert compress("ab") == "ab"
    assert compress("eeeesyy") == "4es2y"
