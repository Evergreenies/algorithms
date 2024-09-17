"""
Given a string of digits, generate all possible valid IP address combinations.

IP addresses must follow the format A.B.C.D, where A, B, C, and D are numbers between 0 and 255.
Zero-prefixed numbers, such as 01 and 065, are not allowed, except for 0 itself.

For example, given "2542540123", you should return ['254.25.40.123', '254.254.0.123'].
"""


def is_valid_part(s):
    # Check if the string is a valid segment
    if len(s) > 1 and s[0] == "0":  # No leading zeros allowed except '0'
        return False
    if 0 <= int(s) <= 255:
        return True
    return False


def restore_ip_addresses(s):
    result = []
    n = len(s)

    # Loop through each possible partition of the string into four parts
    for i in range(1, min(4, n)):  # First part A
        for j in range(i + 1, min(i + 4, n)):  # Second part B
            for k in range(j + 1, min(j + 4, n)):  # Third part C
                A = s[:i]
                B = s[i:j]
                C = s[j:k]
                D = s[k:]

                # Check if all parts are valid
                if (
                    is_valid_part(A)
                    and is_valid_part(B)
                    and is_valid_part(C)
                    and is_valid_part(D)
                ):
                    result.append(f"{A}.{B}.{C}.{D}")

    return result


# Example usage:
s = "2542540123"
print(restore_ip_addresses(s))  # Output: ['254.25.40.123', '254.254.0.123']
