"""
Given a string, find the length of the smallest window that contains every distinct character.
Characters may appear more than once in the window.

For example, given "jiujitsu", you should return 5, corresponding to the final five letters.
"""


def smallest_window(string: str) -> int:
    char_count, distinct_char = {}, len(set(string))
    start, end, min_window = 0, 0, float("inf")

    while end < len(string):
        char = string[end]
        char_count[char] = char_count.get(char, 0) + 1

        while len(char_count) == distinct_char:
            min_window = min(min_window, end - start + 1)
            char = string[start]
            char_count[char] -= 1

            if char_count[char] == 0:
                del char_count[char]

            start += 1

        end += 1

    return int(min_window)


if __name__ == "__main__":
    assert smallest_window("jiujitsu") == 5
