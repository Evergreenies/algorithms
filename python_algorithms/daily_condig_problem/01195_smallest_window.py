def smallest_window(string: str) -> int:
    char_count = {}  # Hash table to store character frequencies within the window
    unique_chars = len(set(string))  # Number of distinct characters
    left, right = 0, 0
    min_len = float("inf")

    # Sliding window approach
    while right < len(string):
        # Add the current character to the window and its count
        current_char = string[right]
        char_count[current_char] = char_count.get(current_char, 0) + 1

        # Expand the window until we have all distinct characters with sufficient frequency
        while len(char_count) == unique_chars and all(
            val > 0 for val in char_count.values()
        ):
            # Update minimum window length
            min_len = min(min_len, right - left + 1)

            # Remove the leftmost character from the window and its count
            left_char = string[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]  # Remove character if its count becomes 0

            # Move left pointer to shrink the window
            left += 1

        # Move right pointer to expand the window
        right += 1

    return int(min_len) if min_len != float("inf") else 0


if __name__ == "__main__":
    assert smallest_window("jiujitsu") == 5
    assert smallest_window("") == 0
    assert smallest_window("a") == 1
    assert smallest_window("aabbccabaabbccc") == 3
