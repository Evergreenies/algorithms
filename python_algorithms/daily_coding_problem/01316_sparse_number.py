"""
We say a number is sparse if there are no adjacent ones in its binary representation.

For example, 21 (10101) is sparse, but 22 (10110) is not. For a given input N,
find the smallest sparse number greater than or equal to N.

Do this in faster than O(N log N) time.
"""


def next_parse_number(num: int) -> int:
    bits = list(bin(num)[2:])
    bits = [0] + [int(b) for b in bits]

    length = len(bits)
    index = 1
    while index < length - 1:
        if index + 1 < length and bits[index] == 1 and bits[index + 1] == 1:
            index_j = index

            while index_j >= 0 and bits[index_j] != 0:
                bits[index_j] = 0
                index_j -= 1

            bits[index_j] = 1
            for k in range(index_j + 1, length):
                bits[k] = 0

            index = index_j
        else:
            index += 1

    result = 0
    for b in bits:
        result = (result << 1) | b

    return result


print(next_parse_number(22))
