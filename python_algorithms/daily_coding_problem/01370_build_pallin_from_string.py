"""
Given a string which we can delete at most k, return whether you can make a palindrome.

For example, given 'waterrfetawx' and a k of 2, you could delete f and x to get 'waterretaw'.
"""


def can_make_palindrome(s, k):
    def is_palindrome_with_deletions(left, right, k):
        if k < 0:  # Too many deletions
            return False
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # Try deleting one character from either end
                return is_palindrome_with_deletions(
                    left + 1, right, k - 1
                ) or is_palindrome_with_deletions(left, right - 1, k - 1)
        return True

    return is_palindrome_with_deletions(0, len(s) - 1, k)


# Example usage:
s = "waterrfetawx"
k = 2
print(can_make_palindrome(s, k))  # Output: True
