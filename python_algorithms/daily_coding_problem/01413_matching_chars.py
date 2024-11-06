"""
Given a string and a set of characters, return the shortest substring containing all
the characters in the set.

For example, given the string "figehaeci" and the set of characters {a, e, i}, you
should return "aeci".

If there is no substring containing all the characters in the set, return null.
"""

from collections import Counter


def shortest_substring(s, chars):
    # Edge case
    if not s or not chars:
        return None

    # Create a frequency map for the characters in the set
    required_chars = Counter(chars)
    # Total unique characters needed in the substring
    required_length = len(required_chars)

    # Pointers for the sliding window
    start, end = 0, 0
    # Track the count of unique characters matched
    formed = 0
    # Dictionary to keep track of the count of characters in the current window
    window_counts = {}

    # Variables to store the result
    min_len = float("inf")
    min_window = ""

    # Expand the window with `end`
    while end < len(s):
        char = s[end]
        window_counts[char] = window_counts.get(char, 0) + 1

        # Check if the current character's frequency matches that in `required_chars`
        if char in required_chars and window_counts[char] == required_chars[char]:
            formed += 1

        # Try to shrink the window with `start`
        while start <= end and formed == required_length:
            # Update the minimum window
            if end - start + 1 < min_len:
                min_len = end - start + 1
                min_window = s[start : end + 1]

            # Remove the character at `start` from the window
            start_char = s[start]
            window_counts[start_char] -= 1
            if (
                start_char in required_chars
                and window_counts[start_char] < required_chars[start_char]
            ):
                formed -= 1

            # Move `start` pointer to the right
            start += 1

        # Move `end` pointer to the right
        end += 1

    return min_window if min_len != float("inf") else None


# Example usage
s = "figehaeci"
chars = {"a", "e", "i"}
print(shortest_substring(s, chars))  # Output should be "aeci"
