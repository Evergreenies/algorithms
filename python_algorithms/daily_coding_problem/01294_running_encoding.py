"""
Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent
repeated successive characters as a single count and character. For example,
the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits
and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
"""


def encode(string: str) -> str:
    encoded, count = "", 1
    for index in range(1, len(string)):
        if string[index] == string[index - 1]:
            count += 1
        else:
            encoded += str(count) + string[index - 1]
            count = 1

    encoded += str(count) + string[-1]

    return encoded


def decode(string: str) -> str:
    decoded, index = "", 0

    while index < len(string):
        count = int(string[index])

        index += 1
        char = string[index]
        decoded += char * count

        index += 1

    return decoded


print(encode("AAAABBBCCDAA"))
print(decode(encode("AAAABBBCCDAA")))
