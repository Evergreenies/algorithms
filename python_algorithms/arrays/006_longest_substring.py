"""
**Challenge:**
You are given a string. Your task is to find the **length of the longest substring** within 
that string that does not contain any **repeated characters**.

**Definition:**
* A substring is a contiguous sequence of characters within a string.
* A character is considered "repeated" if it appears more than once within the substring.

**Examples:**
* **Input:** "abcabcbb"
* **Output:** 3 (The longest substring without repeating characters is "abc")
* **Explanation:** Other substrings in the string also meet the criteria (e.g., "bc"), but 
"abc" has the maximum length.

* **Input:** "bbbbb"
* **Output:** 1 (The longest substring without repeating characters is "b")
* **Explanation:** All characters in the string are repeated, so the longest valid substring 
is just a single character.

* **Input:** "pwwkew"
* **Output:** 3 (The longest substring without repeating characters is "wke")
* **Explanation:** While "pwke" might not be the first unique substring you encounter, it is 
the longest one.

**Important Note:**
The answer must be a **substring**, meaning the characters must appear consecutively in the 
original string. For example, in the input "pwwkew", "pwke" is the correct answer, even though 
"pwkew" itself contains repeated characters. "pwkew" is considered a **subsequence** (a sequence 
of characters that may not appear consecutively) and not a substring.
"""


def longest_substring_without_repeating_char_sliding_window(string: str) -> int:
    """
    - The left and right pointers mark the current window boundaries.
    - The visited set stores characters currently present within the window.
    - The loop iterates, expanding the window to the right until a repeated character is encountered.
    - If a repeated character is found (checked in the visited set), the left pointer is moved,
      shrinking the window and removing the character from the visited set.
    - The maximum length of unique substring visited so far is kept track of and updated if the current
      window length exceeds it.
    """
    visited = set()
    left, right, max_length = 0, 0, 0

    while right < len(string):
        char = string[right]
        right += 1

        while char in visited:
            visited.remove(string[left])
            left += 1

        visited.add(char)
        max_length = max(max_length, right - left)

    return max_length


def longest_substring_without_repeating_char_hash_tables(string: str) -> int:
    left, max_length = 0, 0
    char_index = {}

    for right in range(len(string)):
        char = string[right]

        if char in char_index and char_index[char] >= left:
            left = max(left, char_index[char] + 1)

        char_index[char] = right
        max_length = max(max_length, right - left + 1)

    return max_length


def longest_substring_without_repeating_char_substring_v1(
    string: str,
) -> tuple[int, str]:
    substring = ""
    visited = {}
    current, max_length = 0, 0

    for index, char in enumerate(string):
        if char in visited and current <= visited[char]:
            current = visited[char] + 1
        elif (index - current + 1) > max_length:
            max_length = index - current + 1
            substring = string[current : index + 1]

        visited[char] = index

    return max_length, substring


def longest_substring_without_repeating_char_substring_v2(
    string: str,
) -> tuple[int, str]:
    substring, current = "", 0
    visited = set()

    for index in range(len(string)):
        while string[index] in visited:
            visited.remove(string[current])
            current += 1
        visited.add(string[index])
        substring = max(substring, string[current : index + 1], key=len)

    return len(substring), substring


if __name__ == "__main__":
    assert longest_substring_without_repeating_char_sliding_window("abcabcbb") == 3
    assert longest_substring_without_repeating_char_sliding_window("bbbbb") == 1
    assert longest_substring_without_repeating_char_sliding_window("pwwkew") == 3

    assert longest_substring_without_repeating_char_hash_tables("abcabcbb") == 3
    assert longest_substring_without_repeating_char_hash_tables("bbbbb") == 1
    assert longest_substring_without_repeating_char_hash_tables("pwwkew") == 3

    assert longest_substring_without_repeating_char_substring_v1("abcabcbb") == (
        3,
        "abc",
    )
    assert longest_substring_without_repeating_char_substring_v1("bbbbb") == (1, "b")
    assert longest_substring_without_repeating_char_substring_v1("pwwkew") == (3, "wke")

    assert longest_substring_without_repeating_char_substring_v2("abcabcbb") == (
        3,
        "abc",
    )
    assert longest_substring_without_repeating_char_substring_v2("bbbbb") == (1, "b")
    assert longest_substring_without_repeating_char_substring_v2("pwwkew") == (3, "wke")
