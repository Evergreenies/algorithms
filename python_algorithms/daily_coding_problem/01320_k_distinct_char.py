"""
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""


def k_distinct_substring(string: str, k: int) -> int:
    if k == 0 or not string:
        return 0

    left, right = 0, 0
    max_length, char_count = 0, {}
    while right < len(string):
        if string[right] in char_count:
            char_count[string[right]] += 1
        else:
            char_count[string[right]] = 1

        while len(char_count) > k:
            char_count[string[left]] -= 1
            if char_count[string[left]] == 0:
                del char_count[string[left]]

            left += 1

        max_length = max(max_length, right - left + 1)
        right += 1

    return max_length


print(k_distinct_substring("abcba", 2))
